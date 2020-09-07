# Example

## Deploy it

### To Google Cloud Functions

```sh
$ gcloud functions deploy example \
    --entry-point entry_point \
    --runtime python37 \
    --trigger-http \
    --allow-unauthenticated \
    --set-env-vars AgraffeService="Google Cloud Functions"
```

> Prerequisites  
> Installed `gcloud` (ref: https://cloud.google.com/sdk/install)

### To AWS lambda

```sh
$ lambda deploy --profile {PROFILE}
```

> Prerequisites  
> Installed `python-lambda` (ref: https://github.com/nficano/python-lambda)

