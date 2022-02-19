import io
import pytest


@pytest.fixture
def client():
    from functions_framework import create_app
    app = create_app('entry_point')
    app.debug = True
    with app.test_client() as client:
        yield client


def test_simple(client):
    res = client.get('/')
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.json == {'Hello': 'World'}, res.json


def test_empty(client):
    res = client.get('/empty')
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.data == b'{}', res.data


def test_empty_text(client):
    res = client.get('/empty/text')
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.json == '', res.json


def test_none(client):
    res = client.get('/none')
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.json is None, res.json


def test_items_get(client):
    res = client.get('/items/1')
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.json == {'item_id': 1, 'q': None}, res.json

    res = client.get('/items/1?q=aaa')
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.json == {'item_id': 1, 'q': 'aaa'}, res.json


def test_items_post(client):
    res = client.post('/items', json={'name': 'abc'})
    assert res.status_code == 401, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers

    res = client.post(
        '/items',
        json={'name': 'abc'},
        headers={'Authorization': 'Bearer foobar'}
    )
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.json == {'name': 'abc'}, res.json


def test_cookies(client):
    res = client.get('/cookies')
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.json == {'c1': None, 'c2': None}, res.json

    client.set_cookie('localhost', 'c1', '123')
    res = client.get('/cookies')
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.json == {'c1': '123', 'c2': None}, res.json
    client.delete_cookie('localhost', 'c1')

    client.set_cookie('localhost', 'c1', '123')
    client.set_cookie('localhost', 'c2', 'abc')
    res = client.get('/cookies')
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.json == {'c1': '123', 'c2': 'abc'}, res.json


def test_text(client):
    res = client.get('/text')
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'].startswith('text/plain'), res.headers
    assert res.data == b'test message!', res.data


def test_image(client):
    res = client.get('/image')
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'image/png', res.headers
    assert res.data == b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0c\x00\x00\x00\x0c\x08\x02\x00\x00\x00\xd9\x17\xcb\xb0\x00\x00\x00\x16IDATx\x9ccLIIa \x04\x98\x08\xaa\x18U4\x00\x8a\x00\x1c\xa2\x01D2\xdd\xa6B\x00\x00\x00\x00IEND\xaeB`\x82', res.data


def test_form(client):
    files = {
        'token': 'abc',
    }
    res = client.post(
        '/form',
        data=files,
        content_type='multipart/form-data',
    )
    assert res.status_code == 200, (res.status_code, res.data)
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.json == {'token': 'abc'}, res.json


def test_file(client):
    files = {
        'file': (io.BytesIO(b'abc'), 'test.file'),
    }
    res = client.post(
        '/file',
        data=files,
        content_type='multipart/form-data',
    )
    assert res.status_code == 200, (res.status_code, res.text)
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.json == {'file_size': 3}, res.json


def test_uploadfile(client):
    files = {
        'file': (io.BytesIO(b'abc'), 'test.file'),
    }
    res = client.post(
        '/uploadfile',
        data=files,
        content_type='multipart/form-data',
    )
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.json == {'filename': 'test.file'}, res.json


def test_file_and_form(client):
    files = {
        'file': (io.BytesIO(b'abc'), 'test.file'),
        'fileb': (io.BytesIO(b'abcb'), 'test.fileb', 'text/csv'),
        'token': 'foo',
    }
    res = client.post(
        '/file_and_form',
        data=files,
        content_type='multipart/form-data',
    )
    assert res.status_code == 200, res.status_code
    assert res.headers['Content-Type'] == 'application/json', res.headers
    assert res.json == {
        'file_size': 3,
        'token': 'foo',
        'fileb_content_type': 'text/csv',
        'filename': 'test.fileb',
    }, res.json
