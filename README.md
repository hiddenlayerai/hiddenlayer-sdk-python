# HiddenLayer SDK Python (Beta)

Hiddenlayer is a Python SDK that provides a simple and efficient way to interact with the Hiddenlayer API, a platform for building and deploying machine learning models. The SDK allows developers to easily protect models using the Hiddenlayer API, without having to write complex code or manage the underlying infrastructure.

## Contents

- [Installation](#installation)
- [Getting started](#getting-started)
- [Code examples](#code-examples)
- [Interface stability](#interface-stability)


## Installation

Install from PyPi using [pip](https://pip.pypa.io/en/latest/), a package manager for Python.

`python -m pip install hiddenlayer-sdk`

Scanning models on different platforms such as AWS S3 and Huggingface are supported. You can install the dependenices yourself or via optional dependencies:

```bash
python -m pip install 'hiddenlayer-sdk[aws]'

python -m pip install 'hiddenlayer-sdk[hf]'
```

## Getting Started

Once you've installed the hiddenlayer package, instantiate the `HiddenlayerServiceClient`:

```python
from hiddenlayer import HiddenlayerServiceClient

hl_client = HiddenlayerServiceClient(
  host="https://api.hiddenlayer.ai",
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

### Using MLDR

```python
model = hl_client.mldr.create_model(model_name="example_model")

hl_client.mldr.submit_vectors(
  model_id=model.sensor_id,
  input_vectors=X,
  output=y
)
```

## Code Examples

Code examples can be found in the repo [here](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/tree/main/examples)

## Interface Stability

Hiddenlayer is actively working on stabilizing the Hiddenlayer SDK for Python's interfaces. You are highly encouraged to pin the exact dependency version.
