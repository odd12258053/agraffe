import asyncio
from typing import Any, Generic, Iterable, MutableMapping, Tuple, TypeVar

from agraffe.types import ASGIApp, Message, Scope

Req = TypeVar('Req')
Res = TypeVar('Res')


class HttpCycleBase(Generic[Req, Res]):
    def __init__(self, request: Req):
        self.request = request
        self.status_code = 200
        self.headers: Iterable[Tuple[str, str]] = ()
        self.body = b''
        self.state: MutableMapping[str, Any] = {}
        self.event = asyncio.Event()
        self.started = False

    def __call__(self, app: ASGIApp) -> None:
        loop = asyncio.get_event_loop()
        loop.create_task(self.run_for_lifespan(app))
        instance = self.run(app)
        task = loop.create_task(instance)
        loop.run_until_complete(task)

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
        return None

    async def receive_for_lifespan(self) -> Message:
        if self.started:
            await self.event.wait()
        else:
            self.started = True
        return {}

    async def send_for_lifespan(self, message: Message) -> None:
        return None

    async def run_for_lifespan(self, app: ASGIApp) -> None:
        await app(
            {'type': 'lifespan', 'asgi': {'version': '3.0'}, 'state': self.state},
            self.receive_for_lifespan,
            self.send_for_lifespan,
        )

    async def run(self, app: ASGIApp) -> None:
        try:
            await app(self.scope, self.receive, self.send)
        finally:
            self.event.set()

    async def receive(self) -> Message:
        raise NotImplementedError

    @property
    def scope(self) -> Scope:
        raise NotImplementedError
