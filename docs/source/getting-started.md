# Getting Started

## Installation

To install the HiddenLayer SDK for Python, simply run:

```bash
pip install git+https://github.com/hiddenlayerai/hiddenlayer-sdk-python.git
```

The HiddenLayer Python SDK offers functionality to interact with other services such as HuggingFace, AWS, etc.

As an example if you want to scan models from HuggingFace, you can install the necessary HuggingFace dependencies via:

```bash
pip install 'hiddenlayer[hf] @ git+https://github.com/hiddenlayerai/hiddenlayer-sdk-python.git'
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
  host="https://api.us.hiddenlayer.ai",
  api_id=..., # Your Hiddenlayer API Client ID
  api_key=... # Your Hiddenlayer API Secret Key
)

hl_client.model_scanner.scan_file(
  model_name="name_of_the_model",
  model_path="path/to/model/file.pkl"
)
```

## Authentication

To authenticate to HiddenLayer, you have to generate a client ID and secret from the platform UI.

Once you have those, you can authenticate using the SDK like so:

```python
hl_client = HiddenlayerServiceClient(
  host="https://api.us.hiddenlayer.ai",
  api_id=..., # Your Hiddenlayer API Client ID
  api_key=... # Your Hiddenalyer API Secret Key
)
```

## Data Models

The Hiddenlayer SDK uses Pydantic to represent data for APIs making the code more readable and typsafe, while also making it easier to work with the code.

Specific data models are organized under `hiddenlayer.sdk.rest.models`.

For more information, consult the [Data Models API Reference](api/hiddenlayer.sdk.rest.models.rst).

## Examples

The HiddenLayer Python SDK comes with a number of examples demonstrating how to use the library for various common use-cases, including

* [Scanning models](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/blob/main/examples/model_scanning.py)
* [Submitting vectors to AIDR for Predictive Models](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/blob/main/examples/aidr_predictive.py)

These examples and more are located in the [`examples/` directory of the Github repository](https://github.com/hiddenlayerai/hiddenlayer-sdk-python).
