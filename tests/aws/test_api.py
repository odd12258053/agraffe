import pytest
import base64


@pytest.fixture()
def app():
    from main import entry_point

    return entry_point


def test_simple(app):
    event = {
        'body': None,
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'X-Forwarded-Port': '3000',
            'X-Forwarded-Proto': 'http',
        },
        'httpMethod': 'GET',
        'isBase64Encoded': False,
        'multiValueHeaders': {
            'Accept': ['*/*'],
            'Accept-Encoding': ['gzip, deflate, br'],
            'Connection': ['keep-alive'],
            'Host': ['127.0.0.1:3000'],
            'User-Agent': ['python-requests/2.27.0'],
            'X-Forwarded-Port': ['3000'],
            'X-Forwarded-Proto': ['http'],
        },
        'multiValueQueryStringParameters': None,
        'path': '/',
        'pathParameters': None,
        'queryStringParameters': None,
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'domainName': '127.0.0.1:3000',
            'extendedRequestId': None,
            'httpMethod': 'GET',
            'identity': {
                'accountId': None,
                'apiKey': None,
                'caller': None,
                'cognitoAuthenticationProvider': None,
                'cognitoAuthenticationType': None,
                'cognitoIdentityPoolId': None,
                'sourceIp': '127.0.0.1',
                'user': None,
                'userAgent': 'Custom User Agent String',
                'userArn': None,
            },
            'path': '/',
            'protocol': 'HTTP/1.1',
            'requestId': '884737a5-13cc-4308-b61c-54e068c8649b',
            'requestTime': '19/Feb/2022:07:07:23 +0000',
            'requestTimeEpoch': 1645254443,
            'resourceId': '123456',
            'resourcePath': '/',
            'stage': 'Prod',
        },
        'resource': '/',
        'stageVariables': None,
        'version': '1.0',
    }
    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    assert res['isBase64Encoded']
    body = base64.b64decode(res['body'])
    assert body == b'{"Hello":"World"}', body


def test_empty(app):
    event = {
        'body': None,
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'X-Forwarded-Port': '3000',
            'X-Forwarded-Proto': 'http',
        },
        'httpMethod': 'GET',
        'isBase64Encoded': False,
        'multiValueHeaders': {
            'Accept': ['*/*'],
            'Accept-Encoding': ['gzip, deflate, br'],
            'Connection': ['keep-alive'],
            'Host': ['127.0.0.1:3000'],
            'User-Agent': ['python-requests/2.27.0'],
            'X-Forwarded-Port': ['3000'],
            'X-Forwarded-Proto': ['http'],
        },
        'multiValueQueryStringParameters': None,
        'path': '/empty',
        'pathParameters': None,
        'queryStringParameters': None,
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'domainName': '127.0.0.1:3000',
            'extendedRequestId': None,
            'httpMethod': 'GET',
            'identity': {
                'accountId': None,
                'apiKey': None,
                'caller': None,
                'cognitoAuthenticationProvider': None,
                'cognitoAuthenticationType': None,
                'cognitoIdentityPoolId': None,
                'sourceIp': '127.0.0.1',
                'user': None,
                'userAgent': 'Custom User Agent String',
                'userArn': None,
            },
            'path': '/empty',
            'protocol': 'HTTP/1.1',
            'requestId': '884737a5-13cc-4308-b61c-54e068c8649b',
            'requestTime': '19/Feb/2022:07:07:23 +0000',
            'requestTimeEpoch': 1645254443,
            'resourceId': '123456',
            'resourcePath': '/empty',
            'stage': 'Prod',
        },
        'resource': '/empty',
        'stageVariables': None,
        'version': '1.0',
    }
    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'{}', body


def test_empty_text(app):
    event = {
        'body': None,
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'X-Forwarded-Port': '3000',
            'X-Forwarded-Proto': 'http',
        },
        'httpMethod': 'GET',
        'isBase64Encoded': False,
        'multiValueHeaders': {
            'Accept': ['*/*'],
            'Accept-Encoding': ['gzip, deflate, br'],
            'Connection': ['keep-alive'],
            'Host': ['127.0.0.1:3000'],
            'User-Agent': ['python-requests/2.27.0'],
            'X-Forwarded-Port': ['3000'],
            'X-Forwarded-Proto': ['http'],
        },
        'multiValueQueryStringParameters': None,
        'path': '/empty/text',
        'pathParameters': None,
        'queryStringParameters': None,
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'domainName': '127.0.0.1:3000',
            'extendedRequestId': None,
            'httpMethod': 'GET',
            'identity': {
                'accountId': None,
                'apiKey': None,
                'caller': None,
                'cognitoAuthenticationProvider': None,
                'cognitoAuthenticationType': None,
                'cognitoIdentityPoolId': None,
                'sourceIp': '127.0.0.1',
                'user': None,
                'userAgent': 'Custom User Agent String',
                'userArn': None,
            },
            'path': '/empty/text',
            'protocol': 'HTTP/1.1',
            'requestId': '884737a5-13cc-4308-b61c-54e068c8649b',
            'requestTime': '19/Feb/2022:07:07:23 +0000',
            'requestTimeEpoch': 1645254443,
            'resourceId': '123456',
            'resourcePath': '/empty/text',
            'stage': 'Prod',
        },
        'resource': '/empty/text',
        'stageVariables': None,
        'version': '1.0',
    }
    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'""', body


def test_none(app):
    event = {
        'body': None,
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'X-Forwarded-Port': '3000',
            'X-Forwarded-Proto': 'http',
        },
        'httpMethod': 'GET',
        'isBase64Encoded': False,
        'multiValueHeaders': {
            'Accept': ['*/*'],
            'Accept-Encoding': ['gzip, deflate, br'],
            'Connection': ['keep-alive'],
            'Host': ['127.0.0.1:3000'],
            'User-Agent': ['python-requests/2.27.0'],
            'X-Forwarded-Port': ['3000'],
            'X-Forwarded-Proto': ['http'],
        },
        'multiValueQueryStringParameters': None,
        'path': '/none',
        'pathParameters': None,
        'queryStringParameters': None,
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'domainName': '127.0.0.1:3000',
            'extendedRequestId': None,
            'httpMethod': 'GET',
            'identity': {
                'accountId': None,
                'apiKey': None,
                'caller': None,
                'cognitoAuthenticationProvider': None,
                'cognitoAuthenticationType': None,
                'cognitoIdentityPoolId': None,
                'sourceIp': '127.0.0.1',
                'user': None,
                'userAgent': 'Custom User Agent String',
                'userArn': None,
            },
            'path': '/none',
            'protocol': 'HTTP/1.1',
            'requestId': '884737a5-13cc-4308-b61c-54e068c8649b',
            'requestTime': '19/Feb/2022:07:07:23 +0000',
            'requestTimeEpoch': 1645254443,
            'resourceId': '123456',
            'resourcePath': '/none',
            'stage': 'Prod',
        },
        'resource': '/none',
        'stageVariables': None,
        'version': '1.0',
    }
    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'null', body


def test_items_get(app):
    event = {
        'body': None,
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'X-Forwarded-Port': '3000',
            'X-Forwarded-Proto': 'http',
        },
        'httpMethod': 'GET',
        'isBase64Encoded': False,
        'multiValueHeaders': {
            'Accept': ['*/*'],
            'Accept-Encoding': ['gzip, deflate, br'],
            'Connection': ['keep-alive'],
            'Host': ['127.0.0.1:3000'],
            'User-Agent': ['python-requests/2.27.0'],
            'X-Forwarded-Port': ['3000'],
            'X-Forwarded-Proto': ['http'],
        },
        'multiValueQueryStringParameters': None,
        'path': '/items/1',
        'pathParameters': {'item_id': '1'},
        'queryStringParameters': None,
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'domainName': '127.0.0.1:3000',
            'extendedRequestId': None,
            'httpMethod': 'GET',
            'identity': {
                'accountId': None,
                'apiKey': None,
                'caller': None,
                'cognitoAuthenticationProvider': None,
                'cognitoAuthenticationType': None,
                'cognitoIdentityPoolId': None,
                'sourceIp': '127.0.0.1',
                'user': None,
                'userAgent': 'Custom User Agent String',
                'userArn': None,
            },
            'path': '/items/{item_id}',
            'protocol': 'HTTP/1.1',
            'requestId': '884737a5-13cc-4308-b61c-54e068c8649b',
            'requestTime': '19/Feb/2022:07:07:23 +0000',
            'requestTimeEpoch': 1645254443,
            'resourceId': '123456',
            'resourcePath': '/items/{item_id}',
            'stage': 'Prod',
        },
        'resource': '/items/{item_id}',
        'stageVariables': None,
        'version': '1.0',
    }
    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'{"item_id":1,"q":null}', body

    event = {
        'body': None,
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'X-Forwarded-Port': '3000',
            'X-Forwarded-Proto': 'http',
        },
        'httpMethod': 'GET',
        'isBase64Encoded': False,
        'multiValueHeaders': {
            'Accept': ['*/*'],
            'Accept-Encoding': ['gzip, deflate, br'],
            'Connection': ['keep-alive'],
            'Host': ['127.0.0.1:3000'],
            'User-Agent': ['python-requests/2.27.0'],
            'X-Forwarded-Port': ['3000'],
            'X-Forwarded-Proto': ['http'],
        },
        'multiValueQueryStringParameters': {'q': ['aaa']},
        'path': '/items/1',
        'pathParameters': {'item_id': '1'},
        'queryStringParameters': {'q': 'aaa'},
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'domainName': '127.0.0.1:3000',
            'extendedRequestId': None,
            'httpMethod': 'GET',
            'identity': {
                'accountId': None,
                'apiKey': None,
                'caller': None,
                'cognitoAuthenticationProvider': None,
                'cognitoAuthenticationType': None,
                'cognitoIdentityPoolId': None,
                'sourceIp': '127.0.0.1',
                'user': None,
                'userAgent': 'Custom User Agent String',
                'userArn': None,
            },
            'path': '/items/{item_id}',
            'protocol': 'HTTP/1.1',
            'requestId': '884737a5-13cc-4308-b61c-54e068c8649b',
            'requestTime': '19/Feb/2022:07:07:23 +0000',
            'requestTimeEpoch': 1645254443,
            'resourceId': '123456',
            'resourcePath': '/items/{item_id}',
            'stage': 'Prod',
        },
        'resource': '/items/{item_id}',
        'stageVariables': None,
        'version': '1.0',
    }

    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'{"item_id":1,"q":"aaa"}', body


def test_items_post(app):
    event = {
        'body': '{"name": "abc"}',
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Content-Length': '15',
            'Content-Type': 'application/json',
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'X-Forwarded-Port': '3000',
            'X-Forwarded-Proto': 'http',
        },
        'httpMethod': 'POST',
        'isBase64Encoded': False,
        'multiValueHeaders': {
            'Accept': ['*/*'],
            'Accept-Encoding': ['gzip, deflate, br'],
            'Connection': ['keep-alive'],
            'Content-Length': ['15'],
            'Content-Type': ['application/json'],
            'Host': ['127.0.0.1:3000'],
            'User-Agent': ['python-requests/2.27.0'],
            'X-Forwarded-Port': ['3000'],
            'X-Forwarded-Proto': ['http'],
        },
        'multiValueQueryStringParameters': None,
        'path': '/items',
        'pathParameters': None,
        'queryStringParameters': None,
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'domainName': '127.0.0.1:3000',
            'extendedRequestId': None,
            'httpMethod': 'POST',
            'identity': {
                'accountId': None,
                'apiKey': None,
                'caller': None,
                'cognitoAuthenticationProvider': None,
                'cognitoAuthenticationType': None,
                'cognitoIdentityPoolId': None,
                'sourceIp': '127.0.0.1',
                'user': None,
                'userAgent': 'Custom User Agent String',
                'userArn': None,
            },
            'path': '/items',
            'protocol': 'HTTP/1.1',
            'requestId': '884737a5-13cc-4308-b61c-54e068c8649b',
            'requestTime': '19/Feb/2022:07:07:23 +0000',
            'requestTimeEpoch': 1645254443,
            'resourceId': '123456',
            'resourcePath': '/items',
            'stage': 'Prod',
        },
        'resource': '/items',
        'stageVariables': None,
        'version': '1.0',
    }

    res = app(event, {})
    assert res['statusCode'] == 401, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']

    event = {
        'body': '{"name": "abc"}',
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Authorization': 'Bearer foobar',
            'Connection': 'keep-alive',
            'Content-Length': '15',
            'Content-Type': 'application/json',
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'X-Forwarded-Port': '3000',
            'X-Forwarded-Proto': 'http',
        },
        'httpMethod': 'POST',
        'isBase64Encoded': False,
        'multiValueHeaders': {
            'Accept': ['*/*'],
            'Accept-Encoding': ['gzip, deflate, br'],
            'Authorization': ['Bearer foobar'],
            'Connection': ['keep-alive'],
            'Content-Length': ['15'],
            'Content-Type': ['application/json'],
            'Host': ['127.0.0.1:3000'],
            'User-Agent': ['python-requests/2.27.0'],
            'X-Forwarded-Port': ['3000'],
            'X-Forwarded-Proto': ['http'],
        },
        'multiValueQueryStringParameters': None,
        'path': '/items',
        'pathParameters': None,
        'queryStringParameters': None,
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'domainName': '127.0.0.1:3000',
            'extendedRequestId': None,
            'httpMethod': 'POST',
            'identity': {
                'accountId': None,
                'apiKey': None,
                'caller': None,
                'cognitoAuthenticationProvider': None,
                'cognitoAuthenticationType': None,
                'cognitoIdentityPoolId': None,
                'sourceIp': '127.0.0.1',
                'user': None,
                'userAgent': 'Custom User Agent String',
                'userArn': None,
            },
            'path': '/items',
            'protocol': 'HTTP/1.1',
            'requestId': '884737a5-13cc-4308-b61c-54e068c8649b',
            'requestTime': '19/Feb/2022:07:07:23 +0000',
            'requestTimeEpoch': 1645254443,
            'resourceId': '123456',
            'resourcePath': '/items',
            'stage': 'Prod',
        },
        'resource': '/items',
        'stageVariables': None,
        'version': '1.0',
    }

    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'{"name":"abc"}', body


def test_cookies(app):
    event = {
        'body': None,
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'X-Forwarded-Port': '3000',
            'X-Forwarded-Proto': 'http',
        },
        'httpMethod': 'GET',
        'isBase64Encoded': False,
        'multiValueHeaders': {
            'Accept': ['*/*'],
            'Accept-Encoding': ['gzip, deflate, br'],
            'Connection': ['keep-alive'],
            'Host': ['127.0.0.1:3000'],
            'User-Agent': ['python-requests/2.27.0'],
            'X-Forwarded-Port': ['3000'],
            'X-Forwarded-Proto': ['http'],
        },
        'multiValueQueryStringParameters': None,
        'path': '/cookies',
        'pathParameters': None,
        'queryStringParameters': None,
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'domainName': '127.0.0.1:3000',
            'extendedRequestId': None,
            'httpMethod': 'GET',
            'identity': {
                'accountId': None,
                'apiKey': None,
                'caller': None,
                'cognitoAuthenticationProvider': None,
                'cognitoAuthenticationType': None,
                'cognitoIdentityPoolId': None,
                'sourceIp': '127.0.0.1',
                'user': None,
                'userAgent': 'Custom User Agent String',
                'userArn': None,
            },
            'path': '/cookies',
            'protocol': 'HTTP/1.1',
            'requestId': '884737a5-13cc-4308-b61c-54e068c8649b',
            'requestTime': '19/Feb/2022:07:07:23 +0000',
            'requestTimeEpoch': 1645254443,
            'resourceId': '123456',
            'resourcePath': '/cookies',
            'stage': 'Prod',
        },
        'resource': '/cookies',
        'stageVariables': None,
        'version': '1.0',
    }

    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'{"c1":null,"c2":null}', body

    event = {
        'body': None,
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Cookie': 'c1=123',
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'X-Forwarded-Port': '3000',
            'X-Forwarded-Proto': 'http',
        },
        'httpMethod': 'GET',
        'isBase64Encoded': False,
        'multiValueHeaders': {
            'Accept': ['*/*'],
            'Accept-Encoding': ['gzip, deflate, br'],
            'Connection': ['keep-alive'],
            'Cookie': ['c1=123'],
            'Host': ['127.0.0.1:3000'],
            'User-Agent': ['python-requests/2.27.0'],
            'X-Forwarded-Port': ['3000'],
            'X-Forwarded-Proto': ['http'],
        },
        'multiValueQueryStringParameters': None,
        'path': '/cookies',
        'pathParameters': None,
        'queryStringParameters': None,
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'domainName': '127.0.0.1:3000',
            'extendedRequestId': None,
            'httpMethod': 'GET',
            'identity': {
                'accountId': None,
                'apiKey': None,
                'caller': None,
                'cognitoAuthenticationProvider': None,
                'cognitoAuthenticationType': None,
                'cognitoIdentityPoolId': None,
                'sourceIp': '127.0.0.1',
                'user': None,
                'userAgent': 'Custom User Agent String',
                'userArn': None,
            },
            'path': '/cookies',
            'protocol': 'HTTP/1.1',
            'requestId': '884737a5-13cc-4308-b61c-54e068c8649b',
            'requestTime': '19/Feb/2022:07:07:23 +0000',
            'requestTimeEpoch': 1645254443,
            'resourceId': '123456',
            'resourcePath': '/cookies',
            'stage': 'Prod',
        },
        'resource': '/cookies',
        'stageVariables': None,
        'version': '1.0',
    }

    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'{"c1":"123","c2":null}', body

    event = {
        'body': None,
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Cookie': 'c1=123; c2=abc',
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'X-Forwarded-Port': '3000',
            'X-Forwarded-Proto': 'http',
        },
        'httpMethod': 'GET',
        'isBase64Encoded': False,
        'multiValueHeaders': {
            'Accept': ['*/*'],
            'Accept-Encoding': ['gzip, deflate, br'],
            'Connection': ['keep-alive'],
            'Cookie': ['c1=123; c2=abc'],
            'Host': ['127.0.0.1:3000'],
            'User-Agent': ['python-requests/2.27.0'],
            'X-Forwarded-Port': ['3000'],
            'X-Forwarded-Proto': ['http'],
        },
        'multiValueQueryStringParameters': None,
        'path': '/cookies',
        'pathParameters': None,
        'queryStringParameters': None,
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'domainName': '127.0.0.1:3000',
            'extendedRequestId': None,
            'httpMethod': 'GET',
            'identity': {
                'accountId': None,
                'apiKey': None,
                'caller': None,
                'cognitoAuthenticationProvider': None,
                'cognitoAuthenticationType': None,
                'cognitoIdentityPoolId': None,
                'sourceIp': '127.0.0.1',
                'user': None,
                'userAgent': 'Custom User Agent String',
                'userArn': None,
            },
            'path': '/cookies',
            'protocol': 'HTTP/1.1',
            'requestId': '884737a5-13cc-4308-b61c-54e068c8649b',
            'requestTime': '19/Feb/2022:07:07:23 +0000',
            'requestTimeEpoch': 1645254443,
            'resourceId': '123456',
            'resourcePath': '/cookies',
            'stage': 'Prod',
        },
        'resource': '/cookies',
        'stageVariables': None,
        'version': '1.0',
    }

    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'{"c1":"123","c2":"abc"}', body


def test_text(app):
    event = {
        'body': None,
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'X-Forwarded-Port': '3000',
            'X-Forwarded-Proto': 'http',
        },
        'httpMethod': 'GET',
        'isBase64Encoded': False,
        'multiValueHeaders': {
            'Accept': ['*/*'],
            'Accept-Encoding': ['gzip, deflate, br'],
            'Connection': ['keep-alive'],
            'Host': ['127.0.0.1:3000'],
            'User-Agent': ['python-requests/2.27.0'],
            'X-Forwarded-Port': ['3000'],
            'X-Forwarded-Proto': ['http'],
        },
        'multiValueQueryStringParameters': None,
        'path': '/text',
        'pathParameters': None,
        'queryStringParameters': None,
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'domainName': '127.0.0.1:3000',
            'extendedRequestId': None,
            'httpMethod': 'GET',
            'identity': {
                'accountId': None,
                'apiKey': None,
                'caller': None,
                'cognitoAuthenticationProvider': None,
                'cognitoAuthenticationType': None,
                'cognitoIdentityPoolId': None,
                'sourceIp': '127.0.0.1',
                'user': None,
                'userAgent': 'Custom User Agent String',
                'userArn': None,
            },
            'path': '/text',
            'protocol': 'HTTP/1.1',
            'requestId': '884737a5-13cc-4308-b61c-54e068c8649b',
            'requestTime': '19/Feb/2022:07:07:23 +0000',
            'requestTimeEpoch': 1645254443,
            'resourceId': '123456',
            'resourcePath': '/text',
            'stage': 'Prod',
        },
        'resource': '/text',
        'stageVariables': None,
        'version': '1.0',
    }

    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'].startswith('text/plain'), res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'test message!', body


def test_image(app):
    event = {
        'body': None,
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'X-Forwarded-Port': '3000',
            'X-Forwarded-Proto': 'http',
        },
        'httpMethod': 'GET',
        'isBase64Encoded': False,
        'multiValueHeaders': {
            'Accept': ['*/*'],
            'Accept-Encoding': ['gzip, deflate, br'],
            'Connection': ['keep-alive'],
            'Host': ['127.0.0.1:3000'],
            'User-Agent': ['python-requests/2.27.0'],
            'X-Forwarded-Port': ['3000'],
            'X-Forwarded-Proto': ['http'],
        },
        'multiValueQueryStringParameters': None,
        'path': '/image',
        'pathParameters': None,
        'queryStringParameters': None,
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'domainName': '127.0.0.1:3000',
            'extendedRequestId': None,
            'httpMethod': 'GET',
            'identity': {
                'accountId': None,
                'apiKey': None,
                'caller': None,
                'cognitoAuthenticationProvider': None,
                'cognitoAuthenticationType': None,
                'cognitoIdentityPoolId': None,
                'sourceIp': '127.0.0.1',
                'user': None,
                'userAgent': 'Custom User Agent String',
                'userArn': None,
            },
            'path': '/image',
            'protocol': 'HTTP/1.1',
            'requestId': '884737a5-13cc-4308-b61c-54e068c8649b',
            'requestTime': '19/Feb/2022:07:07:23 +0000',
            'requestTimeEpoch': 1645254443,
            'resourceId': '123456',
            'resourcePath': '/image',
            'stage': 'Prod',
        },
        'resource': '/image',
        'stageVariables': None,
        'version': '1.0',
    }

    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'image/png', res['headers']
    body = base64.b64decode(res['body'])
    assert (
        body
        == b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0c\x00\x00\x00\x0c\x08\x02\x00\x00\x00\xd9\x17\xcb\xb0\x00\x00\x00\x16IDATx\x9ccLIIa \x04\x98\x08\xaa\x18U4\x00\x8a\x00\x1c\xa2\x01D2\xdd\xa6B\x00\x00\x00\x00IEND\xaeB`\x82'
    ), body


def test_form(app):
    event = {
        'body': '--5a3f74f74809037868662ef4311302e3\r\nContent-Disposition: form-data; name="token"\r\n\r\nabc\r\n--5a3f74f74809037868662ef4311302e3--\r\n',
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Content-Length': '127',
            'Content-Type': 'multipart/form-data; boundary=5a3f74f74809037868662ef4311302e3',
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'X-Forwarded-Port': '3000',
            'X-Forwarded-Proto': 'http',
        },
        'httpMethod': 'POST',
        'isBase64Encoded': False,
        'multiValueHeaders': {
            'Accept': ['*/*'],
            'Accept-Encoding': ['gzip, deflate, br'],
            'Connection': ['keep-alive'],
            'Content-Length': ['127'],
            'Content-Type': [
                'multipart/form-data; boundary=5a3f74f74809037868662ef4311302e3'
            ],
            'Host': ['127.0.0.1:3000'],
            'User-Agent': ['python-requests/2.27.0'],
            'X-Forwarded-Port': ['3000'],
            'X-Forwarded-Proto': ['http'],
        },
        'multiValueQueryStringParameters': None,
        'path': '/form',
        'pathParameters': None,
        'queryStringParameters': None,
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'domainName': '127.0.0.1:3000',
            'extendedRequestId': None,
            'httpMethod': 'POST',
            'identity': {
                'accountId': None,
                'apiKey': None,
                'caller': None,
                'cognitoAuthenticationProvider': None,
                'cognitoAuthenticationType': None,
                'cognitoIdentityPoolId': None,
                'sourceIp': '127.0.0.1',
                'user': None,
                'userAgent': 'Custom User Agent String',
                'userArn': None,
            },
            'path': '/form',
            'protocol': 'HTTP/1.1',
            'requestId': '884737a5-13cc-4308-b61c-54e068c8649b',
            'requestTime': '19/Feb/2022:07:07:23 +0000',
            'requestTimeEpoch': 1645254443,
            'resourceId': '123456',
            'resourcePath': '/form',
            'stage': 'Prod',
        },
        'resource': '/form',
        'stageVariables': None,
        'version': '1.0',
    }

    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'{"token":"abc"}', body


def test_file(app):
    event = {
        'body': '--0f8c93977acb69401587fd5aaf2ee9c1\r\nContent-Disposition: form-data; name="file"; filename="test.file"\r\nContent-Type: text/plain\r\n\r\nabc\r\n--0f8c93977acb69401587fd5aaf2ee9c1--\r\n',
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Content-Length': '174',
            'Content-Type': 'multipart/form-data; boundary=0f8c93977acb69401587fd5aaf2ee9c1',
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'X-Forwarded-Port': '3000',
            'X-Forwarded-Proto': 'http',
        },
        'httpMethod': 'POST',
        'isBase64Encoded': False,
        'multiValueHeaders': {
            'Accept': ['*/*'],
            'Accept-Encoding': ['gzip, deflate, br'],
            'Connection': ['keep-alive'],
            'Content-Length': ['174'],
            'Content-Type': [
                'multipart/form-data; boundary=0f8c93977acb69401587fd5aaf2ee9c1'
            ],
            'Host': ['127.0.0.1:3000'],
            'User-Agent': ['python-requests/2.27.0'],
            'X-Forwarded-Port': ['3000'],
            'X-Forwarded-Proto': ['http'],
        },
        'multiValueQueryStringParameters': None,
        'path': '/file',
        'pathParameters': None,
        'queryStringParameters': None,
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'domainName': '127.0.0.1:3000',
            'extendedRequestId': None,
            'httpMethod': 'POST',
            'identity': {
                'accountId': None,
                'apiKey': None,
                'caller': None,
                'cognitoAuthenticationProvider': None,
                'cognitoAuthenticationType': None,
                'cognitoIdentityPoolId': None,
                'sourceIp': '127.0.0.1',
                'user': None,
                'userAgent': 'Custom User Agent String',
                'userArn': None,
            },
            'path': '/file',
            'protocol': 'HTTP/1.1',
            'requestId': '884737a5-13cc-4308-b61c-54e068c8649b',
            'requestTime': '19/Feb/2022:07:07:23 +0000',
            'requestTimeEpoch': 1645254443,
            'resourceId': '123456',
            'resourcePath': '/file',
            'stage': 'Prod',
        },
        'resource': '/file',
        'stageVariables': None,
        'version': '1.0',
    }

    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'{"file_size":3}', body


def test_uploadfile(app):
    event = {
        'body': '--d37f40a4a2ea35b98a812aed99a32d66\r\nContent-Disposition: form-data; name="file"; filename="test.file"\r\nContent-Type: text/plain\r\n\r\nabc\r\n--d37f40a4a2ea35b98a812aed99a32d66--\r\n',
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Content-Length': '174',
            'Content-Type': 'multipart/form-data; boundary=d37f40a4a2ea35b98a812aed99a32d66',
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'X-Forwarded-Port': '3000',
            'X-Forwarded-Proto': 'http',
        },
        'httpMethod': 'POST',
        'isBase64Encoded': False,
        'multiValueHeaders': {
            'Accept': ['*/*'],
            'Accept-Encoding': ['gzip, deflate, br'],
            'Connection': ['keep-alive'],
            'Content-Length': ['174'],
            'Content-Type': [
                'multipart/form-data; boundary=d37f40a4a2ea35b98a812aed99a32d66'
            ],
            'Host': ['127.0.0.1:3000'],
            'User-Agent': ['python-requests/2.27.0'],
            'X-Forwarded-Port': ['3000'],
            'X-Forwarded-Proto': ['http'],
        },
        'multiValueQueryStringParameters': None,
        'path': '/uploadfile',
        'pathParameters': None,
        'queryStringParameters': None,
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'domainName': '127.0.0.1:3000',
            'extendedRequestId': None,
            'httpMethod': 'POST',
            'identity': {
                'accountId': None,
                'apiKey': None,
                'caller': None,
                'cognitoAuthenticationProvider': None,
                'cognitoAuthenticationType': None,
                'cognitoIdentityPoolId': None,
                'sourceIp': '127.0.0.1',
                'user': None,
                'userAgent': 'Custom User Agent String',
                'userArn': None,
            },
            'path': '/uploadfile',
            'protocol': 'HTTP/1.1',
            'requestId': '884737a5-13cc-4308-b61c-54e068c8649b',
            'requestTime': '19/Feb/2022:07:07:23 +0000',
            'requestTimeEpoch': 1645254443,
            'resourceId': '123456',
            'resourcePath': '/uploadfile',
            'stage': 'Prod',
        },
        'resource': '/uploadfile',
        'stageVariables': None,
        'version': '1.0',
    }

    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'{"filename":"test.file"}', body


def test_file_and_form(app):
    event = {
        'body': '--20de67a24309dc60edf59fe113e9edb5\r\nContent-Disposition: form-data; name="file"; filename="test.file"\r\nContent-Type: text/plain\r\n\r\nabc\r\n--20de67a24309dc60edf59fe113e9edb5\r\nContent-Disposition: form-data; name="fileb"; filename="test.fileb"\r\nContent-Type: text/csv\r\n\r\nabcb\r\n--20de67a24309dc60edf59fe113e9edb5\r\nContent-Disposition: form-data; name="token"\r\n\r\nfoo\r\n--20de67a24309dc60edf59fe113e9edb5--\r\n',
        'headers': {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Content-Length': '400',
            'Content-Type': 'multipart/form-data; boundary=20de67a24309dc60edf59fe113e9edb5',
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'X-Forwarded-Port': '3000',
            'X-Forwarded-Proto': 'http',
        },
        'httpMethod': 'POST',
        'isBase64Encoded': False,
        'multiValueHeaders': {
            'Accept': ['*/*'],
            'Accept-Encoding': ['gzip, deflate, br'],
            'Connection': ['keep-alive'],
            'Content-Length': ['400'],
            'Content-Type': [
                'multipart/form-data; boundary=20de67a24309dc60edf59fe113e9edb5'
            ],
            'Host': ['127.0.0.1:3000'],
            'User-Agent': ['python-requests/2.27.0'],
            'X-Forwarded-Port': ['3000'],
            'X-Forwarded-Proto': ['http'],
        },
        'multiValueQueryStringParameters': None,
        'path': '/file_and_form',
        'pathParameters': None,
        'queryStringParameters': None,
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'domainName': '127.0.0.1:3000',
            'extendedRequestId': None,
            'httpMethod': 'POST',
            'identity': {
                'accountId': None,
                'apiKey': None,
                'caller': None,
                'cognitoAuthenticationProvider': None,
                'cognitoAuthenticationType': None,
                'cognitoIdentityPoolId': None,
                'sourceIp': '127.0.0.1',
                'user': None,
                'userAgent': 'Custom User Agent String',
                'userArn': None,
            },
            'path': '/file_and_form',
            'protocol': 'HTTP/1.1',
            'requestId': '884737a5-13cc-4308-b61c-54e068c8649b',
            'requestTime': '19/Feb/2022:07:07:23 +0000',
            'requestTimeEpoch': 1645254443,
            'resourceId': '123456',
            'resourcePath': '/file_and_form',
            'stage': 'Prod',
        },
        'resource': '/file_and_form',
        'stageVariables': None,
        'version': '1.0',
    }

    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == (
        b'{'
        b'"file_size":3,'
        b'"token":"foo",'
        b'"fileb_content_type":"text/csv",'
        b'"filename":"test.fileb"'
        b'}'
    ), body
