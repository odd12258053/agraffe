from azure.functions import HttpRequest, HttpResponse

from agraffe.services.base import HttpCycleBase
from agraffe.types import Message, Scope


class HttpCycle(HttpCycleBase[HttpRequest, HttpResponse]):
    @property
    def scope(self) -> Scope:

        return {
            'type': 'http',
            'asgi': {'version': '3.0'},
            'http_version': '1.1',
            'method': self.request.method,
            'scheme': 'http',
            # TODO: Check this value.
            'path': self.request.url,
            'query_string': self.request.route_params,
            'root_path': '',
            'headers': tuple(
                (k.lower().encode('latin-1'), v.encode('latin-1'))
                for k, v in self.request.headers
            ),
            'server': None,
            'client': None,
        }

    async def receive(self) -> Message:
        return {
            'type': 'http.request',
            # TODO: Check this value.
            'body': self.request.get_body(),
            'more_body': False,
        }

    @property
    def response(self) -> HttpResponse:
        return HttpResponse(
            body=self.body,
            status_code=self.status_code,
            headers=dict(self.headers),
            # TODO: the following args is set.
            # mimetype=...,
            # charset=...,
        )
