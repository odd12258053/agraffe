import pytest


def test_simple():
    import azure.functions as func
    from entry_point import main

    req = func.HttpRequest(
        method='GET',
        url='/',
        body=b''
    )

    res: func.HttpResponse = main(req)

    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.get_body() == b'{"Hello":"World"}', res.get_body()


def test_empty():
    import azure.functions as func
    from entry_point import main

    req = func.HttpRequest(
        method='GET',
        url='/empty',
        body=b''
    )

    res: func.HttpResponse = main(req)
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.get_body() == b'{}', res.get_body()


def test_empty_text():
    import azure.functions as func
    from entry_point import main

    req = func.HttpRequest(
        method='GET',
        url='/empty/text',
        body=b''
    )

    res: func.HttpResponse = main(req)
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.get_body() == b'""', res.get_body()


def test_none():
    import azure.functions as func
    from entry_point import main

    req = func.HttpRequest(
        method='GET',
        url='/none',
        body=b''
    )

    res: func.HttpResponse = main(req)
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.get_body() == b'null', res.get_body()


def test_items_get():
    import azure.functions as func
    from entry_point import main

    req = func.HttpRequest(
        method='GET',
        url='/items/1',
        body=b''
    )

    res: func.HttpResponse = main(req)
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.get_body() == b'{"item_id":1,"q":null}', res.get_body()

    req = func.HttpRequest(
        method='GET',
        url='/items/1?q=aaa',
        body=b''
    )
    res: func.HttpResponse = main(req)
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.get_body() == b'{"item_id":1,"q":"aaa"}', res.get_body()


def test_items_post():
    import azure.functions as func
    from entry_point import main

    req = func.HttpRequest(
        method='POST',
        url='/items',
        headers={
            'Content-Type': 'application/json'
        },
        body=b'{"name":"abc"}'
    )

    res: func.HttpResponse = main(req)
    assert res.status_code == 401, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers

    req = func.HttpRequest(
        method='POST',
        url='/items',
        headers={
            'Authorization': 'Bearer foobar',
            'Content-Type': 'application/json'
        },
        body=b'{"name":"abc"}'
    )
    res: func.HttpResponse = main(req)
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.get_body() == b'{"name":"abc"}', res.get_body()


def test_cookies():
    import azure.functions as func
    from entry_point import main

    req = func.HttpRequest(
        method='GET',
        url='/cookies',
        headers={
            'Content-Type': 'application/json'
        },
        body=b''
    )

    res: func.HttpResponse = main(req)
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.get_body() == b'{"c1":null,"c2":null}', res.get_body()

    req = func.HttpRequest(
        method='GET',
        url='/cookies',
        headers={
            'Cookie': 'c1=123',
            'Content-Type': 'application/json'
        },
        body=b''
    )
    res: func.HttpResponse = main(req)
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.get_body() == b'{"c1":"123","c2":null}', res.get_body()

    req = func.HttpRequest(
        method='GET',
        url='/cookies',
        headers={
            'Cookie': 'c1=123; c2=abc',
            'Content-Type': 'application/json'
        },
        body=b''
    )
    res: func.HttpResponse = main(req)
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.get_body() == b'{"c1":"123","c2":"abc"}', res.get_body()


def test_text():
    import azure.functions as func
    from entry_point import main

    req = func.HttpRequest(
        method='GET',
        url='/text',
        body=b''
    )

    res: func.HttpResponse = main(req)
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'].startswith('text/plain'), res.headers
    assert res.get_body() == b'test message!', res.get_body()


def test_image():
    import azure.functions as func
    from entry_point import main

    req = func.HttpRequest(
        method='GET',
        url='/image',
        body=b''
    )

    res: func.HttpResponse = main(req)
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'image/png', res.headers
    assert res.get_body() == b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0c\x00\x00\x00\x0c\x08\x02\x00\x00\x00\xd9\x17\xcb\xb0\x00\x00\x00\x16IDATx\x9ccLIIa \x04\x98\x08\xaa\x18U4\x00\x8a\x00\x1c\xa2\x01D2\xdd\xa6B\x00\x00\x00\x00IEND\xaeB`\x82', res.get_body()


def test_form():
    import azure.functions as func
    from entry_point import main

    req = func.HttpRequest(
        method='POST',
        url='/form',
        headers={
            'Content-Type': 'multipart/form-data; boundary=boundary'
        },
        body=(
            b'--boundary\r\n'
            b'Content-Disposition: form-data; name="token"\r\n'
            b'\r\n'
            b'abc\r\n'
            b'--boundary--\r\n'
        )
    )

    res: func.HttpResponse = main(req)
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.get_body() == b'{"token":"abc"}', res.get_body()


def test_file():
    import azure.functions as func
    from entry_point import main

    req = func.HttpRequest(
        method='POST',
        url='/file',
        headers={
            'Content-Type': 'multipart/form-data; boundary=boundary'
        },
        body=(
            b'--boundary\r\n'
            b'Content-Disposition: form-data; name="file"; filename="test.file"\r\n'
            b'Content-Type: text/plain\r\n'
            b'\r\n'
            b'abc\r\n'
            b'--boundary--\r\n'
        )
    )

    res: func.HttpResponse = main(req)
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.get_body() == b'{"file_size":3}', res.get_body()


def test_uploadfile():
    import azure.functions as func
    from entry_point import main

    req = func.HttpRequest(
        method='POST',
        url='/uploadfile',
        headers={
            'Content-Type': 'multipart/form-data; boundary=boundary'
        },
        body=(
            b'--boundary\r\n'
            b'Content-Disposition: form-data; name="file"; filename="test.file"\r\n'
            b'Content-Type: text/plain\r\n'
            b'\r\n'
            b'abc\r\n'
            b'--boundary--\r\n'
        )
    )

    res: func.HttpResponse = main(req)
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.get_body() == b'{"filename":"test.file"}', res.get_body()


def test_file_and_form():
    import azure.functions as func
    from entry_point import main

    req = func.HttpRequest(
        method='POST',
        url='/file_and_form',
        headers={
            'Content-Type': 'multipart/form-data; boundary=boundary'
        },
        body=(
            b'--boundary\r\n'
            b'Content-Disposition: form-data; name="file"; filename="test.file"\r\n'
            b'Content-Type: text/plain\r\n'
            b'\r\n'
            b'abc\r\n'
            b'--boundary\r\n'
            b'Content-Disposition: form-data; name="fileb"; filename="test.fileb"\r\n'
            b'Content-Type: text/csv\r\n'
            b'\r\n'
            b'abcb\r\n'
            b'--boundary\r\n'
            b'Content-Disposition: form-data; name="token"\r\n'
            b'\r\n'
            b'foo\r\n'
            b'--boundary--\r\n'
        )
    )

    res: func.HttpResponse = main(req)
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.get_body() == (
        b'{'
        b'"file_size":3,'
        b'"token":"foo",'
        b'"fileb_content_type":"text/csv",'
        b'"filename":"test.fileb"'
        b'}'
    ), res.get_body()
