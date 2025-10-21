# HiddenLayer Python SDK API Reference

## Models

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
from hiddenlayer.types.models import CardListResponse, CardListParams
```

Methods:

- <code title="get /models/v4/cards">client.models.cards.<a href="./src/hiddenlayer/resources/models/cards.py">list</a>(\*\*<a href="src/hiddenlayer/types/models/card_list_params.py">params</a>) -> <a href="./src/hiddenlayer/types/models/card_list_response.py">SyncOffsetPage[CardListResponse]</a></code>

# PromptAnalyzer

Types:

```python
from hiddenlayer.types import PromptAnalyzerCreateResponse, PromptAnalyzerCreateParams
```

Methods:

- <code title="post /api/v1/submit/prompt-analyzer">client.prompt_analyzer.<a href="./src/hiddenlayer/resources/prompt_analyzer.py">create</a>(\*\*<a href="src/hiddenlayer/types/prompt_analyzer_create_params.py">params</a>) -> <a href="./src/hiddenlayer/types/prompt_analyzer_create_response.py">PromptAnalyzerCreateResponse</a></code>

# Interactions

Types:

```python
from hiddenlayer.types import InteractionAnalyzeResponse
```

Methods:

- <code title="post /detection/v1/interactions">client.interactions.<a href="./src/hiddenlayer/resources/interactions.py">analyze</a>(\*\*<a href="src/hiddenlayer/types/interaction_analyze_params.py">params</a>) -> <a href="./src/hiddenlayer/types/interaction_analyze_response.py">InteractionAnalyzeResponse</a></code>

# Sensors

Types:

```python
from hiddenlayer.types import (
    SensorCreateResponse,
    SensorRetrieveResponse,
    SensorUpdateResponse,
    SensorQueryResponse,
    SensorCreateParams,
    SensorUpdateParams,
    SensorQueryParams,
)
```

Methods:

- <code title="post /api/v2/sensors/create">client.sensors.<a href="./src/hiddenlayer/resources/sensors.py">create</a>(\*\*<a href="src/hiddenlayer/types/sensor_create_params.py">params</a>) -> <a href="./src/hiddenlayer/types/sensor_create_response.py">SensorCreateResponse</a></code>
- <code title="get /api/v2/sensors/{sensor_id}">client.sensors.<a href="./src/hiddenlayer/resources/sensors.py">retrieve</a>(sensor_id) -> <a href="./src/hiddenlayer/types/sensor_retrieve_response.py">SensorRetrieveResponse</a></code>
- <code title="put /api/v2/sensors/{sensor_id}">client.sensors.<a href="./src/hiddenlayer/resources/sensors.py">update</a>(sensor_id, \*\*<a href="src/hiddenlayer/types/sensor_update_params.py">params</a>) -> <a href="./src/hiddenlayer/types/sensor_update_response.py">SensorUpdateResponse</a></code>
- <code title="delete /api/v2/sensors/{sensor_id}">client.sensors.<a href="./src/hiddenlayer/resources/sensors.py">delete</a>(sensor_id) -> None</code>
- <code title="post /api/v2/sensors/query">client.sensors.<a href="./src/hiddenlayer/resources/sensors.py">query</a>(\*\*<a href="src/hiddenlayer/types/sensor_query_params.py">params</a>) -> <a href="./src/hiddenlayer/types/sensor_query_response.py">SensorQueryResponse</a></code>

# Scans

## Results

Types:

```python
from hiddenlayer.types.scans import ScanReport, ResultSarifResponse
```

Methods:

- <code title="get /scan/v3/results/{scan_id}/sarif">client.scans.results.<a href="./src/hiddenlayer/resources/scans/results.py">sarif</a>(scan_id) -> str</code>

## Jobs

Types:

```python
from hiddenlayer.types.scans import JobListResponse, ScanJob, ScanReport
```

Methods:

- <code title="get /scan/v3/results/{scan_id}">client.scans.jobs.<a href="./src/hiddenlayer/resources/scans/jobs.py">retrieve</a>(scan_id, \*\*<a href="src/hiddenlayer/types/scans/job_retrieve_params.py">params</a>) -> <a href="./src/hiddenlayer/types/scans/scan_report.py">ScanReport</a></code>
- <code title="get /scan/v3/results">client.scans.jobs.<a href="./src/hiddenlayer/resources/scans/jobs.py">list</a>(\*\*<a href="src/hiddenlayer/types/scans/job_list_params.py">params</a>) -> <a href="./src/hiddenlayer/types/scans/job_list_response.py">JobListResponse</a></code>
- <code title="post /scan/v3/jobs">client.scans.jobs.<a href="./src/hiddenlayer/resources/scans/jobs.py">request</a>(\*\*<a href="src/hiddenlayer/types/scans/job_request_params.py">params</a>) -> <a href="./src/hiddenlayer/types/scans/scan_job.py">ScanJob</a></code>

## Upload

Types:

```python
from hiddenlayer.types.scans import (
    UploadCompleteAllResponse, 
    UploadStartResponse,
    UploadStartParams,
)
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

- <code title="post /scan/v3/upload/{scan_id}/file">client.scans.upload.file.<a href="./src/hiddenlayer/resources/scans/upload/file.py">add</a>(scan_id, \*, file_content_length: int, file_name: str) -> <a href="./src/hiddenlayer/types/scans/upload/file_add_response.py">FileAddResponse</a></code>
- <code title="patch /scan/v3/upload/{scan_id}/file/{file_id}">client.scans.upload.file.<a href="./src/hiddenlayer/resources/scans/upload/file.py">complete</a>(file_id, \*, scan_id) -> <a href="./src/hiddenlayer/types/scans/upload/file_complete_response.py">FileCompleteResponse</a></code>

# Library Extensions

The SDK includes high-level convenience functions for common operations:

## ModelScanner

```python
from hiddenlayer.lib import ModelScanner, AsyncModelScanner
```

Methods:

- **scan_file(model_name, model_path, model_version="1", wait_for_results=True, request_source="API Upload", origin="") -> ScanReport**  
  Scan a local model file using multipart upload.

- **scan_folder(model_name, path, model_version="1", allow_file_patterns=None, ignore_file_patterns=None, wait_for_results=True, request_source="API Upload", origin="") -> ScanReport**  
  Submits all files in a directory and its subdirectories to be scanned.

- **scan_s3_model(model_name, bucket, key, model_version="1", s3_client=None, wait_for_results=True, request_source="API Upload") -> ScanReport**  
  Scan a model file stored on S3.

## CommunityScanner

```python
from hiddenlayer.lib import CommunityScanner, AsyncCommunityScanner
```

Methods:

- **community_scan(model_name, model_path, model_source, model_version="main", wait_for_results=True, request_source="API Upload", origin="") -> ScanReport**  
  Scan a model available at a remote location using the HiddenLayer Model Scanner.

### Community Scan Sources

```python
from hiddenlayer.lib import CommunityScanSource

# Available sources:
CommunityScanSource.LOCAL = "LOCAL"
CommunityScanSource.AWS_PRESIGNED = "AWS_PRESIGNED"
CommunityScanSource.AWS_IAM_ROLE = "AWS_IAM_ROLE"
CommunityScanSource.AZURE_BLOB_SAS = "AZURE_BLOB_SAS"
CommunityScanSource.AZURE_BLOB_AD = "AZURE_BLOB_AD"
CommunityScanSource.GOOGLE_OAUTH = "GOOGLE_OAUTH"
CommunityScanSource.HUGGING_FACE = "HUGGING_FACE"
```

# Client Usage

## Authentication Methods

### Bearer Token Authentication
```python
import hiddenlayer

# Using explicit bearer token
client = hiddenlayer.HiddenLayer(
    bearer_token="your-bearer-token"
)

# Using environment variable (recommended)
# Set HIDDENLAYER_TOKEN in your environment
client = hiddenlayer.HiddenLayer()  # Automatically reads from HIDDENLAYER_TOKEN
```

### OAuth2 Client Credentials
```python
import hiddenlayer

# Using explicit client credentials
client = hiddenlayer.HiddenLayer(
    client_id="your-client-id",
    client_secret="your-client-secret"
)

# Using environment variables (recommended)
# Set HIDDENLAYER_CLIENT_ID and HIDDENLAYER_CLIENT_SECRET in your environment
client = hiddenlayer.HiddenLayer()  # Automatically reads from environment variables
```

## Regional Configuration

### Environment Selection
```python
import hiddenlayer

# US Production (default)
client = hiddenlayer.HiddenLayer(
    bearer_token="your-token",
    environment="prod-us"  # https://api.hiddenlayer.ai
)

# EU Production
client = hiddenlayer.HiddenLayer(
    bearer_token="your-token", 
    environment="prod-eu"  # https://api.eu.hiddenlayer.ai
)

# Custom base URL
client = hiddenlayer.HiddenLayer(
    bearer_token="your-token",
    base_url="https://your-custom-endpoint.com"
)

# Using environment variable for base URL
# Set HIDDEN_LAYER_BASE_URL in your environment
client = hiddenlayer.HiddenLayer(bearer_token="your-token")
```

## Advanced Configuration

```python
import hiddenlayer
import httpx

client = hiddenlayer.HiddenLayer(
    bearer_token="your-token",
    environment="prod-us",
    timeout=30.0,  # Request timeout in seconds
    max_retries=3,  # Maximum retry attempts
    default_headers={"Custom-Header": "value"},
    default_query={"param": "value"},
    http_client=httpx.Client()  # Custom HTTP client
)
```

## Environment Variables

The SDK automatically reads configuration from these environment variables:
- `HIDDENLAYER_TOKEN` - Bearer token for authentication
- `HIDDENLAYER_CLIENT_ID` - OAuth2 client ID
- `HIDDENLAYER_CLIENT_SECRET` - OAuth2 client secret  
- `HIDDEN_LAYER_BASE_URL` - Custom API base URL

## Basic Usage Examples

```python
import hiddenlayer

# Initialize client (reads from environment variables)
client = hiddenlayer.HiddenLayer()

# Access resources
client.models.retrieve("model_id")
client.sensors.create(plaintext_name="sensor_name")
client.scans.jobs.list()

# Access library functions
client.model_scanner.scan_file(model_name="my-model", model_path="/path/to/model")
client.community_scanner.community_scan(
    model_name="my-model",
    model_path="s3://bucket/path",
    model_source=hiddenlayer.lib.CommunityScanSource.AWS_PRESIGNED
)
```

## Async Client

```python
import hiddenlayer

# All authentication and configuration options work the same
async_client = hiddenlayer.AsyncHiddenLayer(
    bearer_token="your-token",
    environment="prod-eu"
)

# All the same methods available with async/await
await async_client.models.retrieve("model_id")
await async_client.model_scanner.scan_file(model_name="my-model", model_path="/path/to/model")
```