import asyncio
from typing import Any, Generic, Iterable, MutableMapping, Tuple, TypeVar

from agraffe.types import ASGIApp, Message, Scope

Req = TypeVar('Req')
Res = TypeVar('Res')


class Lifespan:
    def __init__(self, startup_event: asyncio.Event, shutdown_event: asyncio.Event):
        self.state: MutableMapping[str, Any] = {}
        self.should_exit = False
        self.started = False
        self.startup_event = startup_event
        self.shutdown_event = shutdown_event

    async def receive(self) -> Message:
        if self.started:
            await self.shutdown_event.wait()
            return {'type': 'lifespan.shutdown'}
        else:
            self.started = True
            return {'type': 'lifespan.startup'}

    async def send(self, message: Message) -> None:
        if message['type'] == 'lifespan.startup.complete':
            self.startup_event.set()
        elif message['type'] == 'lifespan.shutdown.complete':
            pass
        elif message['type'] == 'lifespan.startup.failed':
            self.shutdown_event.set()
            self.should_exit = True
        elif message['type'] == 'lifespan.shutdown.failed':
            self.shutdown_event.set()
            self.should_exit = True
        return None

    async def run(self, app: ASGIApp) -> None:
        try:
            await app(
                {'type': 'lifespan', 'asgi': {'version': '3.0'}, 'state': self.state},
                self.receive,
                self.send,
            )
        except BaseException as e:
            self.should_exit = True
            self.startup_event.set()
            raise e


class HttpCycleBase(Generic[Req, Res]):
    def __init__(self, request: Req):
        self.request = request
        self.status_code = 200
        self.headers: Iterable[Tuple[str, str]] = ()
        self.body = b''
        self.startup_event = asyncio.Event()
        self.shutdown_event = asyncio.Event()
        self.lifespan = Lifespan(self.startup_event, self.shutdown_event)

    @property
    def state(self) -> MutableMapping[str, Any]:
        return self.lifespan.state

    def __call__(self, app: ASGIApp) -> None:
        loop = asyncio.get_event_loop()
        lifespan_task = loop.create_task(self.lifespan.run(app))
        main_task = loop.create_task(self.run(app))
        loop.run_until_complete(main_task)
        loop.run_until_complete(lifespan_task)
        if self.lifespan.should_exit:
            err = lifespan_task.exception()
            if err:
                raise err

    @property
    def response(self) -> Res:
        raise NotImplementedError

    async def send(self, message: Message) -> None:
        if message['type'] == 'http.response.start':
            self.status_code = message['status']
            self.headers = tuple(
                (key.decode('latin-1'), value.decode('latin-1'))
                for (key, value) in message['headers']
            )
        elif message['type'] == 'http.response.body':
            self.body = message['body']
        return

    async def run(self, app: ASGIApp) -> None:
        try:
            await self.startup_event.wait()
            if self.lifespan.should_exit:
                return
            await app(self.scope, self.receive, self.send)
        finally:
            self.shutdown_event.set()

    async def receive(self) -> Message:
        raise NotImplementedError

    @property
    def scope(self) -> Scope:
        raise NotImplementedError
