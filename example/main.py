from agraffe import Agraffe

import os
from typing import Optional

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.get('/items/{item_id}')
def read_item(item_id: int, q: Optional[str] = None):
    return {'item_id': item_id, 'q': q}


class Item(BaseModel):
    name: str


@app.post('/items')
def post_item(item: Item, authorization: Optional[str] = Header(None)):
    if authorization is None or authorization != 'Bearer foobar':
        raise HTTPException(status_code=401)
    return item


entry_point = Agraffe.entry_point(app, os.environ['AgraffeService'])
