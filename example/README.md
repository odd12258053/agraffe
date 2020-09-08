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
$ export AWS_REGION={your aws region}
$ export AWS_PROJECT={your aws project}
$ export AWS_ACCESS_KEY_ID={your aws secret access key}
$ export AWS_SECRET_ACCESS_KEY={your aws secret access key}
$ npm install
$ npm run deploy -- --config serverless_rest.yml
```

> Prerequisites  
> Installed `serverless` (ref: https://www.serverless.com/)

