# Example

## Deploy it
```sh
$ gcloud functions deploy example \
    --entry-point entry_point \
    --runtime python310 \
    --trigger-http \
    --allow-unauthenticated
```

> Prerequisites  
> Installed `gcloud` (ref: https://cloud.google.com/sdk/install)
