Example Usage
=============

For information on how to authenticate using the HiddenLayer Python SDK,
please read the `docs on
authentication <getting-started.md#authentication>`__

Initiate Client Connection
--------------------------

.. code:: python

   from hiddenlayer import HiddenlayerServiceClient

   hl_client = HiddenlayerServiceClient(
     host="https://api.hiddenlayer.ai",
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
