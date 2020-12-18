---
id: azure-functions
title: Azure Functions
description: Support to Azure Functions
slug: /services/azure-functions
---

## Example

```py {1-3,14-15}
from agraffe import Agraffe
from agraffe.services.azure_functions import HttpCycle
from azure.functions import HttpRequest, HttpResponse
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


def entry_point(req: HttpRequest) -> HttpResponse:
    return Agraffe(app, HttpCycle)(request=req)
```
