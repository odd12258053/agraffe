
![icon](./resources/icon.png)

[![PyPI version](https://badge.fury.io/py/agraffe.svg)](https://badge.fury.io/py/agraffe)

Agraffe, build API with ASGI in Serverless services (e.g AWS lambda, Google Cloud Functions and Azure Functions).

## Support Services
- [x] Google Cloud Functions
- [x] AWS lambda (with API Gateway HTTP API and REST API)
- [x] Azure Functions

## Requirements

Python 3.7, 3.8, 3.9

## Installation
```sh
$ pip install agraffe
```

## Example
Create it

- Create a file `main.py` with:

```python
from agraffe import Agraffe, Service

from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

entry_point = Agraffe.entry_point(app, Service.google_cloud_functions)
```
```python
# or
from agraffe.services.google_cloud_functions import HttpCycle

def entry_point(request):
    return Agraffe(app, HttpCycle)(request=request)
```

Deploy it

- Deploy the api with:

```sh
$ gcloud functions deploy {FUNCTION NAME} --entry-point entry_point --runtime python37 --trigger-http --allow-unauthenticated
```

## License
This project is licensed under the terms of the MIT license.
