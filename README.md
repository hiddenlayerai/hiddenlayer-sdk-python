# HiddenLayer SDK Python (Beta)

Hiddenlayer is a Python SDK that provides a simple and efficient way to interact with the Hiddenlayer API, a platform for building and deploying machine learning models. The SDK allows developers to easily protect models using the Hiddenlayer API, without having to write complex code or manage the underlying infrastructure.

## Contents

- [Installation](#installation)
- [Getting started](#getting-started)
- [Code examples](#code-examples)
- [Interface stability](#interface-stability)


## Installation

Install from PyPi using [pip](https://pip.pypa.io/en/latest/), a package manager for Python.

`pip install hiddenlayer-sdk`

Scanning models on different platforms such as AWS S3 and Huggingface are supported. You can install the dependenices yourself or via optional dependencies:

```bash
pip install hiddenlayer-sdk[aws]
pip install hiddenlayer-sdk[azure]
pip install hiddenlayer-sdk[hf]
```

## Getting Started

Once you've installed the hiddenlayer package, you can instantiate the `HiddenlayerServiceClient` for the SaaS platform as follows:

```python
from hiddenlayer import HiddenlayerServiceClient

hl_client = HiddenlayerServiceClient(
  host="https://api.us.hiddenlayer.ai",
  api_id=..., # Your Hiddenlayer API Client ID
  api_key=... # Your Hiddenalyer API Secret Key
)
```

If you are using the on-prem Enterprise version of the model scanner, you can instantiate the `HiddenlayerServiceClient` as follows:

```python
from hiddenlayer import HiddenlayerServiceClient

hl_client = HiddenlayerServiceClient(
  host="https://your.hiddenlayer.enterprise.example",
)
```

If you are using the EU region, you will need to set the `HL_AUTH_URL` environment variable to the following:

```bash
export HL_AUTH_URL=https://auth.eu.hiddenlayer.ai
```

Then you will instantiate the `HiddenlayerServiceClient` as follows:

```python
from hiddenlayer import HiddenlayerServiceClient

hl_client = HiddenlayerServiceClient(
  host="https://api.eu.hiddenlayer.ai",
  api_id=..., # Your Hiddenlayer API Client ID
  api_key=... # Your Hiddenalyer API Secret Key
)
```

### Scanning Models

```python
hl_client.model_scanner.scan_file(
  model_name="name_of_the_model",
  model_path="path/to/model/file.pkl"
)
```

If you would like to specify the version associated with the model, you can pass that in as well. Note that the model version must not already exist.

```python
hl_client.model_scanner.scan_file(
  model_name="name_of_the_model",
  model_version=1,
  model_path="path/to/model/file.pkl"
)
```

### Scanning Folders

```python
hl_client.model_scanner.scan_folder(
  model_name="name_of_the_model",
  path="path/to/model/"
)
```

If you would like to specify the version associated with the model, you can pass that in as well. Note that the model version must not already exist.

```python
hl_client.model_scanner.scan_folder(
  model_name="name_of_the_model",
  model_version=1,
  path="path/to/model/"
)
```

### Using AIDR for Predictive Models

> Note: This is only supported using the SaaS version of the platform.

```python
sensor = hl_client.aidr_predicive.create_sensor(sensor_name="example_model")

hl_client.aidr_predictive.submit_vectors(
  model_id=model.sensor_id,
  requestor_id="custom-source-id",
  input_vectors=X,
  output=y
)
```

## Code Examples

Code examples can be found in the repo [here](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/tree/main/examples)

## Interface Stability

Hiddenlayer is actively working on stabilizing the Hiddenlayer SDK for Python's interfaces. You are highly encouraged to pin the exact dependency version.
