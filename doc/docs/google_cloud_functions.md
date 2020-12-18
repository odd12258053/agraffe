---
id: google-cloud-functions
title: Google Cloud Functions
description: Support to Google Cloud Functions
slug: /services/google-cloud-functions
---

## Example

```py {1-2,13-14}
from agraffe import Agraffe
from agraffe.services.google_cloud_functions import HttpCycle
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


def entry_point(request):
    return Agraffe(app, HttpCycle)(request=request)
```
