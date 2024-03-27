# Getting Started

## Installation

To install the HiddenLayer SDK for Python, simply run:

```bash
python -m pip install hiddenlayer-sdk
```

The HiddenLayer Python SDK offers functionality to interact with other services such as HuggingFace, AWS, etc.

As an example if you want to scan models from HuggingFace, you can install the necessary HuggingFace dependencies via:

```bash
python -m pip install hiddenlayer-sdk[hf]
```


## Usage Overview

The main client that gets exposed is `hiddenlayer.HiddenlayerServiceClient` and can be used to interact with all HiddenLayer services exposed via API.

To use the SDK to call an API, first find the API in the [Service API Reference](api.rst). Then, on the appropriate client, call the corresponding method. All API calls have the form

```
hl_client.<SERVICE>.<METHOD>(<parameters>)
```

For example, to scan a model, run:

```python
from hiddenlayer import HiddenlayerServiceClient

hl_client = HiddenlayerServiceClient(
  host="https://api.hiddenlayer.ai",
  api_id=..., # Your Hiddenlayer API Client ID
  api_key=... # Your Hiddenalyer API Secret Key
)

hl_client.model_scanner.scan_file(
  model_name="name_of_the_model",
  model_path="path/to/model/file.pkl"
)
```

## Authentication

Authentication currently depends on whether you are using the SaaS version of HiddenLayer or the OEM version.

To tell if you are using the SaaS or the OEM, you can use the url. If you the URL you use to access HiddenLayer is `https://api.hiddenlayer.ai` then you're using the SaaS version, otherwise you're using the OEM version.

### SAAS

To authenticate to the SaaS version of HiddenLayer, you have to generate a client ID and secret from the platform UI.

Once you have those, you can authenticate using the SDK like so:

```python
hl_client = HiddenlayerServiceClient(
  host="https://api.hiddenlayer.ai",
  api_id=..., # Your Hiddenlayer API Client ID
  api_key=... # Your Hiddenalyer API Secret Key
)
```

### OEM

Coming soon...

## Data Models

The Hiddenlayer SDK uses Pydantic to represent data for APIs making the code more readable and typsafe, while also making it easier to work with the code.

Specific data models are organized under `hiddenlayer.sdk.rest.models`.

For more information, consult the [Data Models API Reference](data_models.rst).

## Examples

The HiddenLayer Python SDK comes with a number of examples demonstrating how to use the library for various common use-cases, including

* [Scanning models](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/blob/main/examples/model_scanning.py)
* [Submitting vectors to MLDR](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/blob/main/examples/mldr.py)

These examples and more are located in the [`examples/` directory of the Github repository](https://github.com/hiddenlayerai/hiddenlayer-sdk-python).
