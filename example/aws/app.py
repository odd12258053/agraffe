from typing import Optional

from fastapi import Cookie, FastAPI, Header, HTTPException
from fastapi.responses import PlainTextResponse, Response

from models import Item


app = FastAPI()


@app.get('/')
def root():
    return {'Hello': 'World'}


@app.get('/empty')
def empty():
    return {}


@app.get('/empty/text')
def empty_text():
    return ''


@app.get('/none')
def none():
    return None


@app.get('/items/{item_id}')
def read_item(item_id: int, q: Optional[str] = None):
    return {'item_id': item_id, 'q': q}


@app.post('/items')
def post_item(item: Item, authorization: Optional[str] = Header(None)):
    if authorization is None or authorization != 'Bearer foobar':
        raise HTTPException(status_code=401)
    return item


@app.get('/cookies')
def cookies(c1: Optional[str] = Cookie(None), c2: Optional[str] = Cookie(None)):
    return {
        'c1': c1,
        'c2': c2,
    }


@app.get('/text')
def text():
    return PlainTextResponse('test message!')


@app.get('/image')
def image():
    return Response(
        content=b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x0c\x00\x00\x00\x0c\x08\x02\x00\x00\x00\xd9\x17\xcb\xb0\x00\x00\x00\x16IDATx\x9ccLIIa \x04\x98\x08\xaa\x18U4\x00\x8a\x00\x1c\xa2\x01D2\xdd\xa6B\x00\x00\x00\x00IEND\xaeB`\x82',
        media_type='image/png'
    )
