
![icon](./resources/icon.png)

[![PyPI version](https://badge.fury.io/py/agraffe.svg)](https://badge.fury.io/py/agraffe)
![Test](https://github.com/odd12258053/agraffe/workflows/Test/badge.svg)

Agraffe, build API with ASGI in Serverless services (e.g AWS lambda, Google Cloud Functions and Azure Functions).

## Support Services
- [x] Google Cloud Functions
  - Python 3.7, 3.8, 3.9, 3.10, 3.11
- [x] AWS lambda (with API Gateway HTTP API or REST API, or with Function URL)
  - Python 3.7, 3.8, 3.9
- [x] Azure Functions
  - Python 3.7, 3.8, 3.9, 3.10

## Requirements

Python 3.7+

## Installation
```sh
$ pip install agraffe
```

## Example
Create it

- Create a file `main.py` with:

```python
import contextlib

from agraffe import Agraffe
from fastapi import FastAPI, Request


@contextlib.asynccontextmanager
async def lifespan(app):
    yield {'message': 'hello'}

app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.get("/lifespan")
def lifespan_(request: Request):
    return {"count": request.state.message}


entry_point = Agraffe.entry_point(app)
```
```python
# or, for on GCP
from agraffe.services.google_cloud_functions import HttpCycle

def entry_point(request):
    return Agraffe(app, HttpCycle)(request=request)
```

Deploy it

- Deploy the api with:

```sh
$ gcloud functions deploy {FUNCTION NAME} --entry-point entry_point --runtime python310 --trigger-http --allow-unauthenticated
```

See `/example` for other services.

## License
This project is licensed under the terms of the MIT license.
