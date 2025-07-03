# Shared Types

```python
from hiddenlayer.types import (
    ArtifactContent,
    Exception,
    Message,
    MultiformatMessageString,
    Node,
    PropertyBag,
    Region,
)
```

# Models

Types:

```python
from hiddenlayer.types import ModelRetrieveResponse
```

Methods:

- <code title="get /api/v2/models/{model_id}">client.models.<a href="./src/hiddenlayer/resources/models/models.py">retrieve</a>(model_id) -> <a href="./src/hiddenlayer/types/model_retrieve_response.py">ModelRetrieveResponse</a></code>
- <code title="delete /api/v2/models/{model_id}">client.models.<a href="./src/hiddenlayer/resources/models/models.py">delete</a>(model_id) -> None</code>

## Cards

Types:

```python
from hiddenlayer.types.models import CardListResponse
```

Methods:

- <code title="get /models/v3/cards">client.models.cards.<a href="./src/hiddenlayer/resources/models/cards.py">list</a>(\*\*<a href="src/hiddenlayer/types/models/card_list_params.py">params</a>) -> <a href="./src/hiddenlayer/types/models/card_list_response.py">CardListResponse</a></code>

# Sensors

Types:

```python
from hiddenlayer.types import SensorCreateResponse, SensorRetrieveResponse, SensorQueryResponse
```

Methods:

- <code title="post /api/v2/sensors/create">client.sensors.<a href="./src/hiddenlayer/resources/sensors.py">create</a>(\*\*<a href="src/hiddenlayer/types/sensor_create_params.py">params</a>) -> <a href="./src/hiddenlayer/types/sensor_create_response.py">SensorCreateResponse</a></code>
- <code title="get /api/v2/sensors/{sensor_id}">client.sensors.<a href="./src/hiddenlayer/resources/sensors.py">retrieve</a>(sensor_id) -> <a href="./src/hiddenlayer/types/sensor_retrieve_response.py">SensorRetrieveResponse</a></code>
- <code title="delete /api/v2/sensors/{sensor_id}">client.sensors.<a href="./src/hiddenlayer/resources/sensors.py">delete</a>(sensor_id) -> None</code>
- <code title="post /api/v2/sensors/query">client.sensors.<a href="./src/hiddenlayer/resources/sensors.py">query</a>(\*\*<a href="src/hiddenlayer/types/sensor_query_params.py">params</a>) -> <a href="./src/hiddenlayer/types/sensor_query_response.py">SensorQueryResponse</a></code>

# Scans

## Results

Types:

```python
from hiddenlayer.types.scans import FileScanReport, ScanReport
```

## Jobs

Types:

```python
from hiddenlayer.types.scans import ScanJob, JobListResponse
```

Methods:

- <code title="get /scan/v3/jobs">client.scans.jobs.<a href="./src/hiddenlayer/resources/scans/jobs.py">list</a>() -> <a href="./src/hiddenlayer/types/scans/job_list_response.py">JobListResponse</a></code>
- <code title="post /scan/v3/jobs">client.scans.jobs.<a href="./src/hiddenlayer/resources/scans/jobs.py">request</a>(\*\*<a href="src/hiddenlayer/types/scans/job_request_params.py">params</a>) -> <a href="./src/hiddenlayer/types/scans/scan_job.py">ScanJob</a></code>

## Upload

Types:

```python
from hiddenlayer.types.scans import UploadCompleteAllResponse, UploadStartResponse
```

Methods:

- <code title="patch /scan/v3/upload/{scan_id}">client.scans.upload.<a href="./src/hiddenlayer/resources/scans/upload/upload.py">complete_all</a>(scan_id) -> <a href="./src/hiddenlayer/types/scans/upload_complete_all_response.py">UploadCompleteAllResponse</a></code>
- <code title="post /scan/v3/upload">client.scans.upload.<a href="./src/hiddenlayer/resources/scans/upload/upload.py">start</a>(\*\*<a href="src/hiddenlayer/types/scans/upload_start_params.py">params</a>) -> <a href="./src/hiddenlayer/types/scans/upload_start_response.py">UploadStartResponse</a></code>

### File

Types:

```python
from hiddenlayer.types.scans.upload import FileAddResponse, FileCompleteResponse
```

Methods:

- <code title="post /scan/v3/upload/{scan_id}/file">client.scans.upload.file.<a href="./src/hiddenlayer/resources/scans/upload/file.py">add</a>(scan_id) -> <a href="./src/hiddenlayer/types/scans/upload/file_add_response.py">FileAddResponse</a></code>
- <code title="patch /scan/v3/upload/{scan_id}/file/{file_id}">client.scans.upload.file.<a href="./src/hiddenlayer/resources/scans/upload/file.py">complete</a>(file_id, \*, scan_id) -> <a href="./src/hiddenlayer/types/scans/upload/file_complete_response.py">FileCompleteResponse</a></code>
