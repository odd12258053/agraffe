from typing import Any, Awaitable, Callable, Iterable, MutableMapping, Tuple

from typing_extensions import Protocol

Message = MutableMapping[str, Any]
Scope = MutableMapping[str, Any]
Receive = Callable[[], Awaitable[Message]]
Send = Callable[[Message], Awaitable[None]]
Response = Tuple[bytes, int, Iterable[Tuple[str, str]]]


class ASGIApp(Protocol):
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        ...


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
