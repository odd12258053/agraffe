""" Agraffe, build API with ASGI in Google Cloud Functions."""

__version__ = "0.2.0"

import asyncio
from enum import Enum
from typing import Any, Callable, Type, Union

from .types import ASGIApp, ASGICycle, Response


class Service(str, Enum):
    google_cloud_functions = 'Google Cloud Functions'
    aws_lambda = 'AWS Lambda'


class Agraffe:
    _HttpCycle: Type[ASGICycle]

    def __init__(self, app: ASGIApp, service: Union[str, Service]):
        if service == Service.google_cloud_functions:
            from .services import google_cloud_functions

            self._HttpCycle = google_cloud_functions.HttpCycle
        elif service == Service.aws_lambda:
            from .services import aws_lambda

            self._HttpCycle = aws_lambda.HttpCycle
        else:
            service = ', '.join(map(lambda x: x.value, Service))
            raise ValueError(f'Please set service either {service}.')

        self.app = app
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    def __call__(self, request: Any) -> Response:
        cycle = self._HttpCycle(request)
        cycle(app=self.app)
        return cycle.response

    @classmethod
    def entry_point(
        cls, app: ASGIApp, service: Union[str, Service]
    ) -> Callable[..., Response]:
        if service == Service.google_cloud_functions:

            def _entry_point4gcf(request: Any) -> Response:
                return cls(app, service)(request=request)

            return _entry_point4gcf

        elif service == Service.aws_lambda:

            def _entry_point4aws_lambda(event: Any, context: Any) -> Response:
                return cls(app, service)(request={'event': event, 'context': context})

            return _entry_point4aws_lambda
        else:
            service = ', '.join(map(lambda x: x.value, Service))
            raise ValueError(f'Please set service either {service}.')
