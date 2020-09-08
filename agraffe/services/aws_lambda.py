from typing import Any, Dict, Iterator
from urllib.parse import urlencode

from agraffe.services.base import HttpCycleBase
from agraffe.types import Message, Scope

Request = Dict[str, Dict[str, Any]]


class HttpCycle(HttpCycleBase[Request]):
    @property
    def scope(self) -> Scope:
        event = self.request['event']

        def gene_query_string() -> Iterator[str]:
            params = event['multiValueQueryStringParameters'] or {}
            for key, values in params.items():
                for vale in values:
                    yield urlencode({key: vale})

        query_string = '&'.join(gene_query_string()).encode()

        return {
            'type': 'http',
            'asgi': {'version': '3.0'},
            'http_version': '1.1',
            'method': event['httpMethod'],
            'scheme': 'http',
            'path': event['path'],
            'query_string': query_string,
            'root_path': '',
            'headers': tuple(
                (k.lower().encode('latin-1'), v.encode('latin-1'))
                for k, v in event['headers'].items()
            ),
            'server': None,
            'client': None,
        }

    async def receive(self) -> Message:
        event = self.request['event']
        return {
            'type': 'http.request',
            'body': event.get('body', '').encode(),
            'more_body': False,
        }
