---
id: aws-lambda
title: AWS lambda
slug: /services/aws-lambda
---

## Example

```py {1-2,13-14}
from agraffe import Agraffe
from agraffe.services.aws_lambda import HttpCycle
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


def entry_point(event, context):
    return Agraffe(app, HttpCycle)(request={'event': event, 'context': context})
```
