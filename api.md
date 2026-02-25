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

# Evaluations

## RedTeam

Types:

```python
from hiddenlayer.types.evaluations import (
    RedTeamCreateResponse,
    RedTeamRetrieveEvaluationResultsResponse,
    RedTeamRetrieveNextActionResponse,
    RedTeamRetrieveStatusResponse,
    RedTeamSubmitTargetResponseResponse,
)
```

Methods:

- <code title="post /evaluations/v1-beta/red-team">client.evaluations.red_team.<a href="./src/hiddenlayer/resources/evaluations/red_team.py">create</a>(\*\*<a href="src/hiddenlayer/types/evaluations/red_team_create_params.py">params</a>) -> <a href="./src/hiddenlayer/types/evaluations/red_team_create_response.py">RedTeamCreateResponse</a></code>
- <code title="get /evaluations/v1-beta/red-team/{workflow_id}">client.evaluations.red_team.<a href="./src/hiddenlayer/resources/evaluations/red_team.py">retrieve_evaluation_results</a>(workflow_id) -> <a href="./src/hiddenlayer/types/evaluations/red_team_retrieve_evaluation_results_response.py">RedTeamRetrieveEvaluationResultsResponse</a></code>
- <code title="get /evaluations/v1-beta/red-team/{workflow_id}/next-action">client.evaluations.red_team.<a href="./src/hiddenlayer/resources/evaluations/red_team.py">retrieve_next_action</a>(workflow_id) -> <a href="./src/hiddenlayer/types/evaluations/red_team_retrieve_next_action_response.py">RedTeamRetrieveNextActionResponse</a></code>
- <code title="get /evaluations/v1-beta/red-team/{workflow_id}/status">client.evaluations.red_team.<a href="./src/hiddenlayer/resources/evaluations/red_team.py">retrieve_status</a>(workflow_id) -> <a href="./src/hiddenlayer/types/evaluations/red_team_retrieve_status_response.py">RedTeamRetrieveStatusResponse</a></code>
- <code title="post /evaluations/v1-beta/red-team/{workflow_id}/target-response">client.evaluations.red_team.<a href="./src/hiddenlayer/resources/evaluations/red_team.py">submit_target_response</a>(workflow_id, \*\*<a href="src/hiddenlayer/types/evaluations/red_team_submit_target_response_params.py">params</a>) -> <a href="./src/hiddenlayer/types/evaluations/red_team_submit_target_response_response.py">RedTeamSubmitTargetResponseResponse</a></code>
- <code title="post /evaluations/v1-beta/red-team/terminations/{workflow_id}">client.evaluations.red_team.<a href="./src/hiddenlayer/resources/evaluations/red_team.py">terminate</a>(workflow_id) -> None</code>

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

## RedTeamSessions

High-level session management for red team evaluations. Wraps the low-level `client.evaluations.red_team.*` API into a stateful session abstraction with polling, iteration, and callback-driven execution.

```python
from hiddenlayer.lib import EvaluationSessionsResource, AsyncEvaluationSessionsResource
from hiddenlayer.lib.red_team_exceptions import (
    RedTeamSessionError,
    PollTimeoutError,
    WorkflowNotFoundError,
    InvalidSessionError,
)
```

### Session Manager

Accessed via `client.evaluation_sessions.red_team`.

Methods:

- **start_session(name, target_model, target_system_prompt="", max_turns=3, execution_strategy_type="random", attacker_max_generation_attempts=2, n_random_techniques=1, max_parallel_techniques=1, prompt_set_id="", hiddenlayer_project_id=None, poll_interval=2.0, poll_max_wait=None, sessions_per_technique=1) -> RedTeamSession**  
  Start a new red team session. Returns a `RedTeamSession` (sync) or `AsyncRedTeamSession` (async).
  Uses adaptive multi-objective evaluation: each session runs to `max_turns` (no short-circuit),
  tests all objectives, and maintains cross-session state for adaptive attacks.
  `sessions_per_technique` controls how many sessions run per technique (default 1).

- **resume_session(workflow_id, poll_interval=2.0, poll_max_wait=None, max_parallel_techniques=None) -> RedTeamSession**  
  Reconnect to a previously started workflow by its ID.

- **terminate_session(workflow_id) -> None**  
  Stop a running workflow.

### Session Object

Returned by `start_session()` and `resume_session()`. Available as `RedTeamSession` (sync) and `AsyncRedTeamSession` (async).

Properties:

- **workflow_id -> str**  
  The workflow ID for this session.

- **name -> str**  
  The session name.

Methods:

- **get_next_action(block=True) -> RedTeamRetrieveNextActionResponse**  
  Poll the server for the next action. When `block=True`, waits until an action is ready.

- **wait_for_completion(poll_interval=3.0, max_wait=300.0, verbose=False) -> None**  
  Poll status until the workflow reaches a terminal state (COMPLETED, FAILED, CANCELLED, TERMINATED, or TIMED_OUT). Automatically called by `run_with_callback()` and `run_with_callback_parallel()`.

- **iterate_actions() -> Iterator[RedTeamRetrieveNextActionResponse]**  
  Yield `attack_task` actions until the workflow completes or fails. Use with `for`/`async for`.

- **run_with_callback(handler) -> None**  
  Drive the full session sequentially. The handler receives `(attack_prompt, history, session_id, target_system_prompt)` and returns the target model's response string. Waits for workflow completion before returning.

### Async-Only Session Methods

These methods are only available on `AsyncRedTeamSession`:

- **get_available_actions(max_actions=10) -> list[RedTeamRetrieveNextActionResponse]**  
  Non-blocking batch fetch of up to `max_actions` currently ready actions.

- **run_with_callback_parallel(handler, max_parallel=None, poll_batch_interval=0.5) -> None**  
  Drive the session with parallel action processing. When `max_parallel` is None, uses the `max_parallel_techniques` value from session config.

### Exceptions

```python
from hiddenlayer.lib.red_team_exceptions import (
    RedTeamSessionError,
    PollTimeoutError,
    WorkflowNotFoundError,
    InvalidSessionError,
)
```

- **RedTeamSessionError** -- Base exception for red team session errors.
- **PollTimeoutError** -- Raised when polling exceeds `max_wait`.
- **WorkflowNotFoundError** -- Raised when a workflow ID does not exist (HTTP 404).
- **InvalidSessionError** -- Raised when a session ID is invalid during response submission (HTTP 400).

### Execution Strategies

Available values for `start_session(execution_strategy_type=...)`:

- `"single"` -- Single technique execution
- `"random"` -- Random technique selection (default)
- `"static_prompt_set"` -- Static prompt set evaluation (requires `prompt_set_id`)

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