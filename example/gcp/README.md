# Example

## Deploy it
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
