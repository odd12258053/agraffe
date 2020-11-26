from urllib.parse import urlsplit

from azure.functions import HttpRequest, HttpResponse

from agraffe.services.base import HttpCycleBase
from agraffe.types import Message, Scope


class HttpCycle(HttpCycleBase[HttpRequest, HttpResponse]):
    @property
    def scope(self) -> Scope:
        parsed = urlsplit(self.request.url)
        return {
            'type': 'http',
            'asgi': {'version': '3.0'},
            'http_version': '1.1',
            'method': self.request.method,
            'scheme': 'http',
            'path': parsed.path,
            'query_string': '&' + parsed.query,
            'headers': tuple(
                (k.lower().encode('latin-1'), v.encode('latin-1'))
                for k, v in self.request.headers.items()
            ),
            'server': None,
            'client': None,
        }

    async def receive(self) -> Message:
        return {
            'type': 'http.request',
            'body': self.request.get_body(),
            'more_body': False,
        }

    @property
    def response(self) -> HttpResponse:
        return HttpResponse(
            body=self.body,
            status_code=self.status_code,
            headers=dict(self.headers),
        )
