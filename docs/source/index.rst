Welcome to HiddenLayer's SDK documentation!
###########################################

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Home

   clients
   services
   data-models

The HiddenLayer platform enhances the developer experience for protecting artificial intelligence (AI) and machine learning (ML) models without needing to write complex code or manage the underlying infrastructure.

The HiddenLayer SDK uses Python to provide a simple and efficient way to interact with the HiddenLayer API. This guide will walk you through how to install and use the HiddenLayer Python SDK to retrieve AI Detect and Response (AIDR) and Model Scanner information.

This SDK includes the following HiddenLayer services:

1. Model Scanner
2. AIDR

.. note::

   This project is under active development.

Before You Begin
****************

The following are required for using the HiddenLayer Python SDK:

- Python (latest version is recommended; this should include pip)
- HiddenLayer API key and secret (see the `Getting Started Guide <https://hiddenlayersec.atlassian.net/wiki/spaces/docs/pages/474021889/Getting+Started+Guide+for+HiddenLayer+AISec+Platform+-+Release+v1.3.0#API-Keys>`_)

Installation
************

Install the ``hiddenlayer-python`` package with `pip
<https://pypi.org/project/hiddenlayer-sdk>`_:

.. code-block:: console

    $ python -m pip install hiddenlayer-sdk

The HiddenLayer Python SDK offers functionality to interact with other services, such as HuggingFace, AWS, etc.

To scan models from HuggingFace, install the necessary HuggingFace dependencies via:

.. code-block:: console

   $ python -m pip install hiddenlayer-sdk[hf]

To scan models from AWS, install the necessary AWS dependencies via:

.. code-block:: console

   $ python -m pip install hiddenlayer-sdk[aws]

Usage Overview
**************

The main client that gets exposed is `hiddenlayer.HiddenlayerServiceClient` and can be used to interact with all HiddenLayer services exposed via API.

To use the SDK to call an API, first find the API in the  `Service API Reference <services.html>`_. Then, on the appropriate client, call the corresponding method. All API calls have the form:

.. code-block:: python 

   hl_client.<SERVICE>.<METHOD>(<parameters>)


For example, to scan a model, run:

.. code-block:: python 

   from hiddenlayer import HiddenlayerServiceClient

   hl_client = HiddenlayerServiceClient(
      host="https://api.hiddenlayer.ai",
      api_id=..., # Your Hiddenlayer API Client ID
      api_key=... # Your Hiddenlayer API Secret Key
   )

   hl_client.model_scanner.scan_file(
      model_name="name_of_the_model",
      model_path="path/to/model/file.pkl"
   )


Authentication
**************

To authenticate to HiddenLayer, you have to generate a client ID and secret from the platform UI. (See the `Getting Started Guide <https://hiddenlayersec.atlassian.net/wiki/spaces/docs/pages/474021889/Getting+Started+Guide+for+HiddenLayer+AISec+Platform+-+Release+v1.3.0#API-Keys>`_)

Once you have those, you can authenticate using the SDK like so:

.. code-block:: python 

   hl_client = HiddenlayerServiceClient(
      host="https://api.hiddenlayer.ai",
      api_id=..., # Your Hiddenlayer API Client ID
      api_key=... # Your Hiddenalyer API Secret Key
   )


Data Models
***********

The Hiddenlayer Python SDK uses Pydantic to represent data for APIs making the code more readable and type-safe, while also making it easier to work with the code.

Specific data models are organized under `hiddenlayer.sdk.rest.models`.

For more information, consult the `Data Models API Reference <api/hiddenlayer.sdk.rest.models.html>`_.

Example Usage
*************

The HiddenLayer Python SDK comes with a number of examples demonstrating how to use the library for various common use-cases.

These examples and more are located in the `examples` directory of the `Github repository <https://github.com/hiddenlayerai/hiddenlayer-sdk-python>`_.

Initiate Client
===============

.. code:: python

   from hiddenlayer import HiddenlayerServiceClient

   hl_client = HiddenlayerServiceClient(
     host="https://api.hiddenlayer.ai",
     api_id=..., # Your Hiddenlayer API Client ID
     api_key=... # Your Hiddenalyer API Secret Key
   )

Scanning Models
===============

Scanning a model on disk
------------------------

.. literalinclude:: ../../examples/model_scanning.py
  :start-after: [docs_scan_local_file_start]
  :end-before: [docs_scan_local_file_end]

Scanning a HuggingFace model
----------------------------

.. literalinclude:: ../../examples/model_scanning.py
  :start-after: [docs_scan_hf_model_start]
  :end-before: [docs_scan_hf_model_end]

AIDR
====

Submitting vectors to AIDR
--------------------------

.. literalinclude:: ../../examples/mldr.py
  :start-after: [docs_submit_vectors_start]
  :end-before: [docs_submit_vectors_end]
