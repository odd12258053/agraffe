""" Agraffe, build API with ASGI in Google Cloud Functions."""

__version__ = "0.1.0"

import asyncio
from typing import Callable, Iterable, Tuple

from .types import ASGIApp, Message, Request, Response, Scope


class ASGICycle:
    def __call__(self, app: ASGIApp) -> None:
        loop = asyncio.get_event_loop()
        instance = self.run(app)
        task = loop.create_task(instance)
        loop.run_until_complete(task)

    async def run(self, app: ASGIApp) -> None:
        await app(self.scope, self.receive, self.send)

    async def receive(self) -> Message:
        raise NotImplementedError

    async def send(self, message: Message) -> None:
        raise NotImplementedError

    @property
    def scope(self) -> Scope:
        raise NotImplementedError


class HttpCycle(ASGICycle):
    def __init__(self, request: Request):
        self.request = request
        self.status_code = 200
        self.headers: Iterable[Tuple[str, str]] = ()
        self.body = b''

    @property
    def response(self) -> Response:
        return self.body, self.status_code, self.headers

    @property
    def scope(self) -> Scope:
        return {
            'type': 'http',
            'asgi': {'version': '3.0'},
            'http_version': '1.1',
            'method': self.request.method,
            'scheme': self.request.scheme,
            'path': self.request.path,
            # 'raw_path': ...,
            'query_string': self.request.query_string,
            'root_path': self.request.environ.get('SCRIPT_NAME', ''),
            'headers': tuple((k.encode(), v.encode()) for k, v in self.request.headers),
            'server': (
                self.request.environ.get('SERVER_NAME'),
                self.request.environ.get('SERVER_PORT'),
            ),
            'client': self.request.remote_addr,
        }

    async def receive(self) -> Message:
        return {
            'type': 'http.request',
            'body': self.request.get_data(
                cache=False, as_text=False, parse_form_data=True
            )
            or b'',
            'more_body': False,
        }

    async def send(self, message: Message) -> None:
        if message['type'] == 'http.response.start':
            self.status_code = message['status']
            self.headers = tuple(
                (key.decode(), value.decode()) for (key, value) in message['headers']
            )
        elif message['type'] == 'http.response.body':
            self.body = message['body']
        return None


class Agraffe:
    def __init__(self, app: ASGIApp):
        self.app = app
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    def __call__(self, request: Request) -> Response:
        cycle = HttpCycle(request)
        cycle(app=self.app)
        return cycle.response

    @classmethod
    def entry_point(cls, app: ASGIApp) -> Callable[[Request], Response]:
        def _entry_point(request: Request) -> Response:
            return cls(app)(request=request)

        return _entry_point
