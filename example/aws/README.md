# Example

## Deploy it
```sh
# To deploy REST API
$ sam build -t template_api.yaml --use-container
$ sam deploy

# To deploy HTTP API
$ sam build -t template_httpapi.yaml --use-container
$ sam run deploy

# To deploy lambda with function url
$ sam build -t template_function_url.yaml --use-container
$ sam run deploy

```
