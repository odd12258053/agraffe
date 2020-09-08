import os
from typing import Optional

from fastapi import Cookie, FastAPI, Header, HTTPException
from models import Item

from agraffe import Agraffe

app = FastAPI()


@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.get('/items/{item_id}')
def read_item(item_id: int, q: Optional[str] = None):
    return {'item_id': item_id, 'q': q}


@app.post('/items')
def post_item(item: Item, authorization: Optional[str] = Header(None)):
    if authorization is None or authorization != 'Bearer foobar':
        raise HTTPException(status_code=401)
    return item


@app.get('/cookies')
def read_root(c1: Optional[str] = Cookie(None), c2: Optional[str] = Cookie(None)):
    return {
        'c1': c1,
        'c2': c2,
    }


entry_point = Agraffe.entry_point(app, os.environ['AgraffeService'])
