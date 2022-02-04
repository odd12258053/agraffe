""" Agraffe, build API with ASGI in Serverless services (e.g AWS lambda, Google Cloud Functions and Azure Functions). """  # noqa: E501

__version__ = "0.5.0"

import asyncio
from enum import Enum
from typing import Any, Callable, Type, Union

from .types import ASGIApp, ASGICycle


class Service(str, Enum):
    google_cloud_functions = 'Google Cloud Functions'
    aws_lambda = 'AWS Lambda'
    azure_functions = 'Azure Functions'


class Agraffe:
    def __init__(self, app: ASGIApp, http_cycle: Type[ASGICycle]):
        self.app = app
        self._http_cycle = http_cycle
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    def __call__(self, request: Any) -> Any:
        cycle = self._http_cycle(request)
        cycle(app=self.app)
        return cycle.response

    @classmethod
    def entry_point(
        cls, app: ASGIApp, service: Union[str, Service]
    ) -> Callable[..., Any]:
        if service == Service.google_cloud_functions:
            from .services.google_cloud_functions import HttpCycle as GCPHttpCycle

            def _entry_point4gcf(request: Any) -> Any:
                return cls(app, GCPHttpCycle)(request=request)

            return _entry_point4gcf

        elif service == Service.aws_lambda:
            from .services.aws_lambda import HttpCycle as AWSHttpCycle

            def _entry_point4aws_lambda(event: Any, context: Any) -> Any:
                return cls(app, AWSHttpCycle)(
                    request={'event': event, 'context': context}
                )

            return _entry_point4aws_lambda
        elif service == Service.azure_functions:
            from .services.azure_functions import HttpCycle as AzureHttpCycle
            from .services.azure_functions import HttpRequest, HttpResponse

            def _entry_point4azure_functions(req: HttpRequest) -> HttpResponse:
                return cls(app, AzureHttpCycle)(request=req)

            return _entry_point4azure_functions

        else:
            service = ', '.join(map(lambda x: x.value, Service))
            raise ValueError(f'Please set service either {service}.')
