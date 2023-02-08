import os
import sys
from typing import Union

from .services import Service


def find_service() -> Union[Service, None]:
    # ref: https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html
    if 'AWS_LAMBDA_FUNCTION_NAME' in os.environ:
        return Service.aws_lambda

    # ref: https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings  # noqa: 501
    if 'FUNCTIONS_WORKER_RUNTIME' in os.environ:
        return Service.azure_functions

    # ref: https://cloud.google.com/functions/docs/configuring/env-var#newer_runtimes
    if sys.version_info >= (3, 8) and 'FUNCTION_TARGET' in os.environ:
        return Service.google_cloud_functions
    elif 'GCP_PROJECT' in os.environ and 'FUNCTION_NAME' in os.environ:
        return Service.google_cloud_functions

    return None
