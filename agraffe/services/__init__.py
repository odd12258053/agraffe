from enum import Enum


class Service(str, Enum):
    google_cloud_functions = 'Google Cloud Functions'
    aws_lambda = 'AWS Lambda'
    azure_functions = 'Azure Functions'
