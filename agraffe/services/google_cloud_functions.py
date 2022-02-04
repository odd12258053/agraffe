from asyncio import Protocol
from typing import Iterable, MutableMapping, Tuple

from agraffe.services.base import HttpCycleBase
from agraffe.types import Message, Scope


class Request(Protocol):
    query_string: str
    headers: Iterable[Tuple[str, str]]
    environ: MutableMapping[str, str]
    method: str
    scheme: str
    path: str
    remote_addr: str

    def get_data(self, cache: bool, as_text: bool, parse_form_data: bool) -> bytes:
        ...


Response = Tuple[bytes, int, Iterable[Tuple[str, str]]]


class HttpCycle(HttpCycleBase[Request, Response]):
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
            'headers': tuple(
                (k.lower().encode('latin-1'), v.encode('latin-1'))
                for k, v in self.request.headers
            ),
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
                cache=False, as_text=False, parse_form_data=False
            )
            or b'',
            'more_body': False,
        }

    @property
    def response(self) -> Response:
        return self.body, self.status_code, self.headers
