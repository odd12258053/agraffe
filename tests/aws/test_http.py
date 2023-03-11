import pytest
import base64


@pytest.fixture()
def app():
    from main import entry_point

    return entry_point


def test_simple(app):
    event = {
        'version': '2.0',
        'routeKey': 'GET /',
        'rawPath': '/',
        'rawQueryString': '',
        'cookies': [],
        'headers': {
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'Accept': '*/*',
            'X-Forwarded-Proto': 'http',
            'X-Forwarded-Port': '3000',
        },
        'queryStringParameters': {},
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'http': {
                'method': 'GET',
                'path': '/',
                'protocol': 'HTTP/1.1',
                'sourceIp': '127.0.0.1',
                'userAgent': 'Custom User Agent String',
            },
            'requestId': 'd13a6872-ceb0-4fdf-85d0-f1e84f8e2b19',
            'routeKey': 'GET /',
            'stage': '$default',
            'time': '19/Feb/2022:06:36:04 +0000',
            'timeEpoch': 1645252564,
            'domainName': 'localhost',
            'domainPrefix': 'localhost',
        },
        'body': '',
        'pathParameters': {},
        'stageVariables': None,
        'isBase64Encoded': False,
    }
    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    assert res['isBase64Encoded']
    body = base64.b64decode(res['body'])
    assert body == b'{"Hello":"World"}', body


def test_empty(app):
    event = {
        'version': '2.0',
        'routeKey': 'GET /empty',
        'rawPath': '/empty',
        'rawQueryString': '',
        'cookies': [],
        'headers': {
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'X-Forwarded-Proto': 'http',
            'X-Forwarded-Port': '3000',
        },
        'queryStringParameters': {},
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'http': {
                'method': 'GET',
                'path': '/empty',
                'protocol': 'HTTP/1.1',
                'sourceIp': '127.0.0.1',
                'userAgent': 'Custom User Agent String',
            },
            'requestId': '3f0b3323-c570-4ede-9044-fd0bf3128ba8',
            'routeKey': 'GET /empty',
            'stage': '$default',
            'time': '19/Feb/2022:06:55:52 +0000',
            'timeEpoch': 1645253752,
            'domainName': 'localhost',
            'domainPrefix': 'localhost',
        },
        'body': '',
        'pathParameters': {},
        'stageVariables': None,
        'isBase64Encoded': False,
    }
    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'{}', body


def test_empty_text(app):
    event = {
        'version': '2.0',
        'routeKey': 'GET /empty/text',
        'rawPath': '/empty/text',
        'rawQueryString': '',
        'cookies': [],
        'headers': {
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'X-Forwarded-Proto': 'http',
            'X-Forwarded-Port': '3000',
        },
        'queryStringParameters': {},
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'http': {
                'method': 'GET',
                'path': '/empty/text',
                'protocol': 'HTTP/1.1',
                'sourceIp': '127.0.0.1',
                'userAgent': 'Custom User Agent String',
            },
            'requestId': '3f0b3323-c570-4ede-9044-fd0bf3128ba8',
            'routeKey': 'GET /empty/text',
            'stage': '$default',
            'time': '19/Feb/2022:06:55:52 +0000',
            'timeEpoch': 1645253752,
            'domainName': 'localhost',
            'domainPrefix': 'localhost',
        },
        'body': '',
        'pathParameters': {},
        'stageVariables': None,
        'isBase64Encoded': False,
    }
    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'""', body


def test_none(app):
    event = {
        'version': '2.0',
        'routeKey': 'GET /none',
        'rawPath': '/none',
        'rawQueryString': '',
        'cookies': [],
        'headers': {
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'X-Forwarded-Proto': 'http',
            'X-Forwarded-Port': '3000',
        },
        'queryStringParameters': {},
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'http': {
                'method': 'GET',
                'path': '/none',
                'protocol': 'HTTP/1.1',
                'sourceIp': '127.0.0.1',
                'userAgent': 'Custom User Agent String',
            },
            'requestId': '3f0b3323-c570-4ede-9044-fd0bf3128ba8',
            'routeKey': 'GET /none',
            'stage': '$default',
            'time': '19/Feb/2022:06:55:52 +0000',
            'timeEpoch': 1645253752,
            'domainName': 'localhost',
            'domainPrefix': 'localhost',
        },
        'body': '',
        'pathParameters': {},
        'stageVariables': None,
        'isBase64Encoded': False,
    }
    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'null', body


def test_items_get(app):
    event = {
        'version': '2.0',
        'routeKey': 'GET /items/<item_id>',
        'rawPath': '/items/1',
        'rawQueryString': '',
        'cookies': [],
        'headers': {
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'X-Forwarded-Proto': 'http',
            'X-Forwarded-Port': '3000',
        },
        'queryStringParameters': {},
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'http': {
                'method': 'GET',
                'path': '/items/1',
                'protocol': 'HTTP/1.1',
                'sourceIp': '127.0.0.1',
                'userAgent': 'Custom User Agent String',
            },
            'requestId': '3f0b3323-c570-4ede-9044-fd0bf3128ba8',
            'routeKey': 'GET /items/<item_id>',
            'stage': '$default',
            'time': '19/Feb/2022:06:55:52 +0000',
            'timeEpoch': 1645253752,
            'domainName': 'localhost',
            'domainPrefix': 'localhost',
        },
        'body': '',
        'pathParameters': {'item_id': '1'},
        'stageVariables': None,
        'isBase64Encoded': False,
    }
    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'{"item_id":1,"q":null}', body

    event = {
        'version': '2.0',
        'routeKey': 'GET /items/<item_id>',
        'rawPath': '/items/1',
        'rawQueryString': 'q=aaa',
        'cookies': [],
        'headers': {
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'X-Forwarded-Proto': 'http',
            'X-Forwarded-Port': '3000',
        },
        'queryStringParameters': {'q': 'aaa'},
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'http': {
                'method': 'GET',
                'path': '/items/1',
                'protocol': 'HTTP/1.1',
                'sourceIp': '127.0.0.1',
                'userAgent': 'Custom User Agent String',
            },
            'requestId': '32029027-5f43-496f-9dfa-0c04c0d7fbe0',
            'routeKey': 'GET /items/<item_id>',
            'stage': '$default',
            'time': '19/Feb/2022:06:59:34 +0000',
            'timeEpoch': 1645253974,
            'domainName': 'localhost',
            'domainPrefix': 'localhost',
        },
        'body': '',
        'pathParameters': {'item_id': '1'},
        'stageVariables': None,
        'isBase64Encoded': False,
    }
    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'{"item_id":1,"q":"aaa"}', body


def test_items_post(app):
    event = {
        'version': '2.0',
        'routeKey': 'POST /items',
        'rawPath': '/items',
        'rawQueryString': '',
        'cookies': [],
        'headers': {
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Content-Length': '15',
            'Content-Type': 'application/json',
            'X-Forwarded-Proto': 'http',
            'X-Forwarded-Port': '3000',
        },
        'queryStringParameters': {},
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'http': {
                'method': 'POST',
                'path': '/items',
                'protocol': 'HTTP/1.1',
                'sourceIp': '127.0.0.1',
                'userAgent': 'Custom User Agent String',
            },
            'requestId': '32029027-5f43-496f-9dfa-0c04c0d7fbe0',
            'routeKey': 'POST /items',
            'stage': '$default',
            'time': '19/Feb/2022:06:59:34 +0000',
            'timeEpoch': 1645253974,
            'domainName': 'localhost',
            'domainPrefix': 'localhost',
        },
        'body': '{"name": "abc"}',
        'pathParameters': {},
        'stageVariables': None,
        'isBase64Encoded': False,
    }
    res = app(event, {})
    assert res['statusCode'] == 401, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']

    event = {
        'version': '2.0',
        'routeKey': 'POST /items',
        'rawPath': '/items',
        'rawQueryString': '',
        'cookies': [],
        'headers': {
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Authorization': 'Bearer foobar',
            'Content-Length': '15',
            'Content-Type': 'application/json',
            'X-Forwarded-Proto': 'http',
            'X-Forwarded-Port': '3000',
        },
        'queryStringParameters': {},
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'http': {
                'method': 'POST',
                'path': '/items',
                'protocol': 'HTTP/1.1',
                'sourceIp': '127.0.0.1',
                'userAgent': 'Custom User Agent String',
            },
            'requestId': '32029027-5f43-496f-9dfa-0c04c0d7fbe0',
            'routeKey': 'POST /items',
            'stage': '$default',
            'time': '19/Feb/2022:06:59:34 +0000',
            'timeEpoch': 1645253974,
            'domainName': 'localhost',
            'domainPrefix': 'localhost',
        },
        'body': '{"name": "abc"}',
        'pathParameters': {},
        'stageVariables': None,
        'isBase64Encoded': False,
    }
    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'{"name":"abc"}', body


def test_cookies(app):
    event = {
        'version': '2.0',
        'routeKey': 'GET /cookies',
        'rawPath': '/cookies',
        'rawQueryString': '',
        'cookies': [],
        'headers': {
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'X-Forwarded-Proto': 'http',
            'X-Forwarded-Port': '3000',
        },
        'queryStringParameters': {},
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'http': {
                'method': 'GET',
                'path': '/cookies',
                'protocol': 'HTTP/1.1',
                'sourceIp': '127.0.0.1',
                'userAgent': 'Custom User Agent String',
            },
            'requestId': '32029027-5f43-496f-9dfa-0c04c0d7fbe0',
            'routeKey': 'GET /cookies',
            'stage': '$default',
            'time': '19/Feb/2022:06:59:34 +0000',
            'timeEpoch': 1645253974,
            'domainName': 'localhost',
            'domainPrefix': 'localhost',
        },
        'body': '',
        'pathParameters': {},
        'stageVariables': None,
        'isBase64Encoded': False,
    }
    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'{"c1":null,"c2":null}', body

    event = {
        'version': '2.0',
        'routeKey': 'GET /cookies',
        'rawPath': '/cookies',
        'rawQueryString': '',
        'cookies': ['c1=123'],
        'headers': {
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Cookie': 'c1=123',
            'X-Forwarded-Proto': 'http',
            'X-Forwarded-Port': '3000',
        },
        'queryStringParameters': {},
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'http': {
                'method': 'GET',
                'path': '/cookies',
                'protocol': 'HTTP/1.1',
                'sourceIp': '127.0.0.1',
                'userAgent': 'Custom User Agent String',
            },
            'requestId': '32029027-5f43-496f-9dfa-0c04c0d7fbe0',
            'routeKey': 'GET /cookies',
            'stage': '$default',
            'time': '19/Feb/2022:06:59:34 +0000',
            'timeEpoch': 1645253974,
            'domainName': 'localhost',
            'domainPrefix': 'localhost',
        },
        'body': '',
        'pathParameters': {},
        'stageVariables': None,
        'isBase64Encoded': False,
    }
    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'{"c1":"123","c2":null}', body

    event = {
        'version': '2.0',
        'routeKey': 'GET /cookies',
        'rawPath': '/cookies',
        'rawQueryString': '',
        'cookies': ['c1=123', 'c2=abc'],
        'headers': {
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Cookie': 'c1=123; c2=abc',
            'X-Forwarded-Proto': 'http',
            'X-Forwarded-Port': '3000',
        },
        'queryStringParameters': {},
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'http': {
                'method': 'GET',
                'path': '/cookies',
                'protocol': 'HTTP/1.1',
                'sourceIp': '127.0.0.1',
                'userAgent': 'Custom User Agent String',
            },
            'requestId': '32029027-5f43-496f-9dfa-0c04c0d7fbe0',
            'routeKey': 'GET /cookies',
            'stage': '$default',
            'time': '19/Feb/2022:06:59:34 +0000',
            'timeEpoch': 1645253974,
            'domainName': 'localhost',
            'domainPrefix': 'localhost',
        },
        'body': '',
        'pathParameters': {},
        'stageVariables': None,
        'isBase64Encoded': False,
    }
    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'{"c1":"123","c2":"abc"}', body


def test_text(app):
    event = {
        'version': '2.0',
        'routeKey': 'GET /text',
        'rawPath': '/text',
        'rawQueryString': '',
        'cookies': [],
        'headers': {
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'X-Forwarded-Proto': 'http',
            'X-Forwarded-Port': '3000',
        },
        'queryStringParameters': {},
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'http': {
                'method': 'GET',
                'path': '/text',
                'protocol': 'HTTP/1.1',
                'sourceIp': '127.0.0.1',
                'userAgent': 'Custom User Agent String',
            },
            'requestId': '32029027-5f43-496f-9dfa-0c04c0d7fbe0',
            'routeKey': 'GET /text',
            'stage': '$default',
            'time': '19/Feb/2022:06:59:34 +0000',
            'timeEpoch': 1645253974,
            'domainName': 'localhost',
            'domainPrefix': 'localhost',
        },
        'body': '',
        'pathParameters': {},
        'stageVariables': None,
        'isBase64Encoded': False,
    }
    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'].startswith('text/plain'), res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'test message!', body


def test_image(app):
    event = {
        'version': '2.0',
        'routeKey': 'GET /image',
        'rawPath': '/image',
        'rawQueryString': '',
        'cookies': [],
        'headers': {
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'X-Forwarded-Proto': 'http',
            'X-Forwarded-Port': '3000',
        },
        'queryStringParameters': {},
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'http': {
                'method': 'GET',
                'path': '/image',
                'protocol': 'HTTP/1.1',
                'sourceIp': '127.0.0.1',
                'userAgent': 'Custom User Agent String',
            },
            'requestId': '32029027-5f43-496f-9dfa-0c04c0d7fbe0',
            'routeKey': 'GET /image',
            'stage': '$default',
            'time': '19/Feb/2022:06:59:34 +0000',
            'timeEpoch': 1645253974,
            'domainName': 'localhost',
            'domainPrefix': 'localhost',
        },
        'body': '',
        'pathParameters': {},
        'stageVariables': None,
        'isBase64Encoded': False,
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
        'version': '2.0',
        'routeKey': 'POST /form',
        'rawPath': '/form',
        'rawQueryString': '',
        'cookies': [],
        'headers': {
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Content-Length': '127',
            'Content-Type': 'multipart/form-data; boundary=25372e895be785cd05ddf0a169c03ed4',
            'X-Forwarded-Proto': 'http',
            'X-Forwarded-Port': '3000',
        },
        'queryStringParameters': {},
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'http': {
                'method': 'POST',
                'path': '/form',
                'protocol': 'HTTP/1.1',
                'sourceIp': '127.0.0.1',
                'userAgent': 'Custom User Agent String',
            },
            'requestId': '32029027-5f43-496f-9dfa-0c04c0d7fbe0',
            'routeKey': 'POST /form',
            'stage': '$default',
            'time': '19/Feb/2022:06:59:34 +0000',
            'timeEpoch': 1645253974,
            'domainName': 'localhost',
            'domainPrefix': 'localhost',
        },
        'body': '--25372e895be785cd05ddf0a169c03ed4\r\nContent-Disposition: form-data; name="token"\r\n\r\nabc\r\n--25372e895be785cd05ddf0a169c03ed4--\r\n',
        'pathParameters': {},
        'stageVariables': None,
        'isBase64Encoded': False,
    }
    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'{"token":"abc"}', body


def test_file(app):
    event = {
        'version': '2.0',
        'routeKey': 'POST /file',
        'rawPath': '/file',
        'rawQueryString': '',
        'cookies': [],
        'headers': {
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Content-Length': '174',
            'Content-Type': 'multipart/form-data; boundary=870164ee14ae53fa9b1c67404812ce2b',
            'X-Forwarded-Proto': 'http',
            'X-Forwarded-Port': '3000',
        },
        'queryStringParameters': {},
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'http': {
                'method': 'POST',
                'path': '/file',
                'protocol': 'HTTP/1.1',
                'sourceIp': '127.0.0.1',
                'userAgent': 'Custom User Agent String',
            },
            'requestId': '32029027-5f43-496f-9dfa-0c04c0d7fbe0',
            'routeKey': 'POST /file',
            'stage': '$default',
            'time': '19/Feb/2022:06:59:34 +0000',
            'timeEpoch': 1645253974,
            'domainName': 'localhost',
            'domainPrefix': 'localhost',
        },
        'body': '--870164ee14ae53fa9b1c67404812ce2b\r\nContent-Disposition: form-data; name="file"; filename="test.file"\r\nContent-Type: text/plain\r\n\r\nabc\r\n--870164ee14ae53fa9b1c67404812ce2b--\r\n',
        'pathParameters': {},
        'stageVariables': None,
        'isBase64Encoded': False,
    }
    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'{"file_size":3}', body


def test_uploadfile(app):
    event = {
        'version': '2.0',
        'routeKey': 'POST /uploadfile',
        'rawPath': '/uploadfile',
        'rawQueryString': '',
        'cookies': [],
        'headers': {
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Content-Length': '174',
            'Content-Type': 'multipart/form-data; boundary=32505a09b173e369a0fbe7e9618e4f05',
            'X-Forwarded-Proto': 'http',
            'X-Forwarded-Port': '3000',
        },
        'queryStringParameters': {},
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'http': {
                'method': 'POST',
                'path': '/uploadfile',
                'protocol': 'HTTP/1.1',
                'sourceIp': '127.0.0.1',
                'userAgent': 'Custom User Agent String',
            },
            'requestId': '32029027-5f43-496f-9dfa-0c04c0d7fbe0',
            'routeKey': 'POST /uploadfile',
            'stage': '$default',
            'time': '19/Feb/2022:06:59:34 +0000',
            'timeEpoch': 1645253974,
            'domainName': 'localhost',
            'domainPrefix': 'localhost',
        },
        'body': '--32505a09b173e369a0fbe7e9618e4f05\r\nContent-Disposition: form-data; name="file"; filename="test.file"\r\nContent-Type: text/plain\r\n\r\nabc\r\n--32505a09b173e369a0fbe7e9618e4f05--\r\n',
        'pathParameters': {},
        'stageVariables': None,
        'isBase64Encoded': False,
    }
    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'{"filename":"test.file"}', body


def test_file_and_form(app):
    event = {
        'version': '2.0',
        'routeKey': 'POST /file_and_form',
        'rawPath': '/file_and_form',
        'rawQueryString': '',
        'cookies': [],
        'headers': {
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Content-Length': '400',
            'Content-Type': 'multipart/form-data; boundary=2d86210d57cf12c027cf46dfe1321668',
            'X-Forwarded-Proto': 'http',
            'X-Forwarded-Port': '3000',
        },
        'queryStringParameters': {},
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'http': {
                'method': 'POST',
                'path': '/file_and_form',
                'protocol': 'HTTP/1.1',
                'sourceIp': '127.0.0.1',
                'userAgent': 'Custom User Agent String',
            },
            'requestId': '32029027-5f43-496f-9dfa-0c04c0d7fbe0',
            'routeKey': 'POST /file_and_form',
            'stage': '$default',
            'time': '19/Feb/2022:06:59:34 +0000',
            'timeEpoch': 1645253974,
            'domainName': 'localhost',
            'domainPrefix': 'localhost',
        },
        'body': '--2d86210d57cf12c027cf46dfe1321668\r\nContent-Disposition: form-data; name="file"; filename="test.file"\r\nContent-Type: text/plain\r\n\r\nabc\r\n--2d86210d57cf12c027cf46dfe1321668\r\nContent-Disposition: form-data; name="fileb"; filename="test.fileb"\r\nContent-Type: text/csv\r\n\r\nabcb\r\n--2d86210d57cf12c027cf46dfe1321668\r\nContent-Disposition: form-data; name="token"\r\n\r\nfoo\r\n--2d86210d57cf12c027cf46dfe1321668--\r\n',
        'pathParameters': {},
        'stageVariables': None,
        'isBase64Encoded': False,
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


def test_lifespan(app):
    event = {
        'version': '2.0',
        'routeKey': 'GET /lifespan',
        'rawPath': '/lifespan',
        'rawQueryString': '',
        'cookies': [],
        'headers': {
            'Host': '127.0.0.1:3000',
            'User-Agent': 'python-requests/2.27.0',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'X-Forwarded-Proto': 'http',
            'X-Forwarded-Port': '3000',
        },
        'queryStringParameters': {},
        'requestContext': {
            'accountId': '123456789012',
            'apiId': '1234567890',
            'http': {
                'method': 'GET',
                'path': '/lifespan',
                'protocol': 'HTTP/1.1',
                'sourceIp': '127.0.0.1',
                'userAgent': 'Custom User Agent String',
            },
            'requestId': '3f0b3323-c570-4ede-9044-fd0bf3128ba8',
            'routeKey': 'GET /lifespan',
            'stage': '$default',
            'time': '19/Feb/2022:06:55:52 +0000',
            'timeEpoch': 1645253752,
            'domainName': 'localhost',
            'domainPrefix': 'localhost',
        },
        'body': '',
        'pathParameters': {},
        'stageVariables': None,
        'isBase64Encoded': False,
    }
    res = app(event, {})
    assert res['statusCode'] == 200, res['statusCode']
    assert res['headers']['content-type'] == 'application/json', res['headers']
    body = base64.b64decode(res['body'])
    assert body == b'{"message":"hello"}', body
