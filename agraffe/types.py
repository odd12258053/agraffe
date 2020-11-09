from typing import Any, Awaitable, Callable, MutableMapping

from typing_extensions import Protocol

Message = MutableMapping[str, Any]
Scope = MutableMapping[str, Any]
Receive = Callable[[], Awaitable[Message]]
Send = Callable[[Message], Awaitable[None]]
Request = Any
Response = Any


class ASGIApp(Protocol):
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        ...


class ASGICycle(Protocol):
    def __init__(self, request: Request) -> None:
        ...

    def __call__(self, app: ASGIApp) -> None:
        ...

    async def run(self, app: ASGIApp) -> None:
        ...

    async def receive(self) -> Message:
        ...

    async def send(self, message: Message) -> None:
        ...

    @property
    def scope(self) -> Scope:
        ...

    @property
    def response(self) -> Response:
        ...
