---
id: introduction
title: Getting Started
slug: /
---

## Support Services

- Google Cloud Functions
- AWS lambda (with API Gateway HTTP API and REST API)
- Azure Functions

## Requirements

Python 3.7+

## Installation

```shell
$ pip install agraffe
```

## Example

Create a file `main.py` with:

```py
from typing import Optional

from agraffe import Agraffe, Service
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
```

And

### On Google Cloud Functions

```py
entry_point = Agraffe.entry_point(app, Service.google_cloud_functions)
```

### On AWS lambda

```py
entry_point = Agraffe.entry_point(app, Service.aws_lambda)
```

### On Azure Functions

```py
entry_point = Agraffe.entry_point(app, Service.azure_functions)
```

## Full Example

```py
from typing import Optional

from agraffe import Agraffe, Service
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
