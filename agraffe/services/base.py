import asyncio
from typing import Generic, Iterable, Tuple, TypeVar

from agraffe.types import ASGIApp, Message, Response, Scope

T = TypeVar('T')


class HttpCycleBase(Generic[T]):
    def __init__(self, request: T):
        self.request = request
        self.status_code = 200
        self.headers: Iterable[Tuple[str, str]] = ()
        self.body = b''

    def __call__(self, app: ASGIApp) -> None:
        loop = asyncio.get_event_loop()
        instance = self.run(app)
        task = loop.create_task(instance)
        loop.run_until_complete(task)

    @property
    def response(self) -> Response:
        return self.body, self.status_code, self.headers

    async def send(self, message: Message) -> None:
        if message['type'] == 'http.response.start':
            self.status_code = message['status']
            self.headers = tuple(
                (key.decode(), value.decode()) for (key, value) in message['headers']
            )
        elif message['type'] == 'http.response.body':
            self.body = message['body']
        return None

    async def run(self, app: ASGIApp) -> None:
        await app(self.scope, self.receive, self.send)

    async def receive(self) -> Message:
        raise NotImplementedError

    @property
    def scope(self) -> Scope:
        raise NotImplementedError
