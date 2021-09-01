# Example

## Deploy it

```sh
$ func azure functionapp publish <APP_NAME>
```

## Change python version
```shell
$ az functionapp config set --name <FUNCTION_APP> \
    --resource-group <RESOURCE_GROUP> \
    --linux-fx-version <LINUX_FX_VERSION>
```

ref: https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python?tabs=azurecli-linux%2Capplication-level#changing-python-version
