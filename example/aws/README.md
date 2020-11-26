# Example

## Deploy it
```sh
$ export AWS_REGION={your aws region}
$ export AWS_PROJECT={your aws project}
$ export AWS_ACCESS_KEY_ID={your aws secret access key}
$ export AWS_SECRET_ACCESS_KEY={your aws secret access key}
$ npm install

# To deploy REST API
$ npm run deploy -- --config serverless_rest.yml

# To deploy HTTP API
$ npm run deploy -- --config serverless_http.yml
```

> Prerequisites  
> Installed `serverless` (ref: https://www.serverless.com/)
