# Shared Types

```python
from hiddenlayer_sdk.types import Exception, Node
```

# Models

Types:

```python
from hiddenlayer_sdk.types import ModelRetrieveResponse
```

Methods:

- <code title="get /api/v2/models/{model_id}">client.models.<a href="./src/hiddenlayer_sdk/resources/models/models.py">retrieve</a>(model_id) -> <a href="./src/hiddenlayer_sdk/types/model_retrieve_response.py">ModelRetrieveResponse</a></code>
- <code title="delete /api/v2/models/{model_id}">client.models.<a href="./src/hiddenlayer_sdk/resources/models/models.py">delete</a>(model_id) -> None</code>

## Cards

Types:

```python
from hiddenlayer_sdk.types.models import CardListResponse
```

Methods:

- <code title="get /models/v3/cards">client.models.cards.<a href="./src/hiddenlayer_sdk/resources/models/cards.py">list</a>(\*\*<a href="src/hiddenlayer_sdk/types/models/card_list_params.py">params</a>) -> <a href="./src/hiddenlayer_sdk/types/models/card_list_response.py">CardListResponse</a></code>

# Sensors

Types:

```python
from hiddenlayer_sdk.types import Sensor, SensorQueryResponse
```

Methods:

- <code title="post /api/v2/sensors/create">client.sensors.<a href="./src/hiddenlayer_sdk/resources/sensors.py">create</a>(\*\*<a href="src/hiddenlayer_sdk/types/sensor_create_params.py">params</a>) -> <a href="./src/hiddenlayer_sdk/types/sensor.py">Sensor</a></code>
- <code title="get /api/v2/sensors/{sensor_id}">client.sensors.<a href="./src/hiddenlayer_sdk/resources/sensors.py">retrieve</a>(sensor_id) -> <a href="./src/hiddenlayer_sdk/types/sensor.py">Sensor</a></code>
- <code title="delete /api/v2/sensors/{sensor_id}">client.sensors.<a href="./src/hiddenlayer_sdk/resources/sensors.py">delete</a>(sensor_id) -> None</code>
- <code title="post /api/v2/sensors/query">client.sensors.<a href="./src/hiddenlayer_sdk/resources/sensors.py">query</a>(\*\*<a href="src/hiddenlayer_sdk/types/sensor_query_params.py">params</a>) -> <a href="./src/hiddenlayer_sdk/types/sensor_query_response.py">SensorQueryResponse</a></code>

# Vectors

Types:

```python
from hiddenlayer_sdk.types import VectorSubmitVectorsResponse
```

Methods:

- <code title="post /api/v2/submit">client.vectors.<a href="./src/hiddenlayer_sdk/resources/vectors.py">submit_vectors</a>(\*\*<a href="src/hiddenlayer_sdk/types/vector_submit_vectors_params.py">params</a>) -> <a href="./src/hiddenlayer_sdk/types/vector_submit_vectors_response.py">VectorSubmitVectorsResponse</a></code>

# Scans

Types:

```python
from hiddenlayer_sdk.types import ScanRetrieveResultsResponse
```

Methods:

- <code title="get /scans/v3/health">client.scans.<a href="./src/hiddenlayer_sdk/resources/scans/scans.py">check_health</a>() -> None</code>
- <code title="get /scans/v3/readiness">client.scans.<a href="./src/hiddenlayer_sdk/resources/scans/scans.py">check_readiness</a>() -> None</code>
- <code title="post /scans/v3/reports/{scan_id}">client.scans.<a href="./src/hiddenlayer_sdk/resources/scans/scans.py">create_report</a>(scan_id, \*\*<a href="src/hiddenlayer_sdk/types/scan_create_report_params.py">params</a>) -> None</code>
- <code title="get /scans/v3/results/{scan_id}">client.scans.<a href="./src/hiddenlayer_sdk/resources/scans/scans.py">retrieve_results</a>(scan_id, \*\*<a href="src/hiddenlayer_sdk/types/scan_retrieve_results_params.py">params</a>) -> <a href="./src/hiddenlayer_sdk/types/scan_retrieve_results_response.py">object</a></code>

## Results

Types:

```python
from hiddenlayer_sdk.types.scans import (
    FileScanReport,
    ScanReport,
    ResultListResponse,
    ResultPatchResponse,
)
```

Methods:

- <code title="get /scan/v3/results/{scan_id}">client.scans.results.<a href="./src/hiddenlayer_sdk/resources/scans/results.py">retrieve</a>(scan_id, \*\*<a href="src/hiddenlayer_sdk/types/scans/result_retrieve_params.py">params</a>) -> <a href="./src/hiddenlayer_sdk/types/scans/scan_report.py">ScanReport</a></code>
- <code title="get /scan/v3/results">client.scans.results.<a href="./src/hiddenlayer_sdk/resources/scans/results.py">list</a>(\*\*<a href="src/hiddenlayer_sdk/types/scans/result_list_params.py">params</a>) -> <a href="./src/hiddenlayer_sdk/types/scans/result_list_response.py">ResultListResponse</a></code>
- <code title="patch /scan/v3/results/{scan_id}">client.scans.results.<a href="./src/hiddenlayer_sdk/resources/scans/results.py">patch</a>(path_scan_id, \*\*<a href="src/hiddenlayer_sdk/types/scans/result_patch_params.py">params</a>) -> <a href="./src/hiddenlayer_sdk/types/scans/result_patch_response.py">ResultPatchResponse</a></code>
- <code title="post /scan/v3/results/{scan_id}">client.scans.results.<a href="./src/hiddenlayer_sdk/resources/scans/results.py">start</a>(path_scan_id, \*\*<a href="src/hiddenlayer_sdk/types/scans/result_start_params.py">params</a>) -> None</code>

## Jobs

Types:

```python
from hiddenlayer_sdk.types.scans import ScanJob
```

Methods:

- <code title="get /scan/v3/jobs">client.scans.jobs.<a href="./src/hiddenlayer_sdk/resources/scans/jobs.py">list</a>() -> <a href="./src/hiddenlayer_sdk/types/scans/scan_job.py">ScanJob</a></code>
- <code title="post /scan/v3/jobs">client.scans.jobs.<a href="./src/hiddenlayer_sdk/resources/scans/jobs.py">request</a>(\*\*<a href="src/hiddenlayer_sdk/types/scans/job_request_params.py">params</a>) -> <a href="./src/hiddenlayer_sdk/types/scans/scan_report.py">ScanReport</a></code>

## Upload

Types:

```python
from hiddenlayer_sdk.types.scans import UploadCompleteAllResponse, UploadStartResponse
```

Methods:

- <code title="patch /scan/v3/upload/{scan_id}">client.scans.upload.<a href="./src/hiddenlayer_sdk/resources/scans/upload/upload.py">complete_all</a>(scan_id) -> <a href="./src/hiddenlayer_sdk/types/scans/upload_complete_all_response.py">UploadCompleteAllResponse</a></code>
- <code title="post /scan/v3/upload">client.scans.upload.<a href="./src/hiddenlayer_sdk/resources/scans/upload/upload.py">start</a>(\*\*<a href="src/hiddenlayer_sdk/types/scans/upload_start_params.py">params</a>) -> <a href="./src/hiddenlayer_sdk/types/scans/upload_start_response.py">UploadStartResponse</a></code>

### File

Types:

```python
from hiddenlayer_sdk.types.scans.upload import FileAddResponse, FileCompleteResponse
```

Methods:

- <code title="post /scan/v3/upload/{scan_id}/file">client.scans.upload.file.<a href="./src/hiddenlayer_sdk/resources/scans/upload/file.py">add</a>(scan_id) -> <a href="./src/hiddenlayer_sdk/types/scans/upload/file_add_response.py">FileAddResponse</a></code>
- <code title="patch /scan/v3/upload/{scan_id}/file/{file_id}">client.scans.upload.file.<a href="./src/hiddenlayer_sdk/resources/scans/upload/file.py">complete</a>(file_id, \*, scan_id) -> <a href="./src/hiddenlayer_sdk/types/scans/upload/file_complete_response.py">FileCompleteResponse</a></code>
