Example Usage
=============

For information on how to authenticate using the HiddenLayer Python SDK,
please read the `docs on
authentication <getting-started.md#authentication>`__

Initiate Client
---------------

.. code:: python

   from hiddenlayer import HiddenlayerServiceClient

   hl_client = HiddenlayerServiceClient(
     host="https://api.us.hiddenlayer.ai",
     api_id=..., # Your Hiddenlayer API Client ID
     api_key=... # Your Hiddenalyer API Secret Key
   )

Scanning Models
---------------

Scanning a model on disk
^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../../examples/model_scanning.py
  :start-after: [docs_scan_local_file_start]
  :end-before: [docs_scan_local_file_end]

Scanning a HuggingFace model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../../examples/model_scanning.py
  :start-after: [docs_scan_hf_model_start]
  :end-before: [docs_scan_hf_model_end]

Scanning a model on Azure Blob
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../../examples/model_scanning.py
  :start-after: [docs_scan_azure_blob_model]
  :end-before: [docs_scan_azure_blob_model_end]

AIDR for Predictive Modelling
-----------------------------

.. note::
   This is currently only supported when using the SaaS version of the platform.

Submitting Vectors to AIDR for Predictive Modelling
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../../examples/aidr_predictive.py
  :start-after: [docs_submit_vectors_start]
  :end-before: [docs_submit_vectors_end]

