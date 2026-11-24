# HiddenLayer Python API Library

[![PyPI version](<https://img.shields.io/pypi/v/hiddenlayer-sdk.svg?label=pypi%20(stable)>)](https://pypi.org/project/hiddenlayer-sdk/)

This library provides access to the HiddenLayer REST API from Python 3.10 or later, with synchronous and asynchronous clients built on [httpx](https://github.com/encode/httpx). The REST API documentation is on [dev.hiddenlayer.ai](https://dev.hiddenlayer.ai); every method of this library is in [reference.md](reference.md).

Upgrading from 3.x? [docs/BREAKING_CHANGES_v4.0.0.md](docs/BREAKING_CHANGES_v4.0.0.md) lists every change.

## Installation

```sh
pip install hiddenlayer-sdk
```

## Usage

```python
from hiddenlayer import HiddenLayer, InteractionsInput, InteractionsMetadata, InteractionsTextContent

client = HiddenLayer(
    environment="prod-eu",  # defaults to "prod-us"
)

response = client.interactions.analyze(
    metadata=InteractionsMetadata(model="gpt-5", requester_id="user-1234", provider="openai"),
    input=InteractionsInput(messages=[InteractionsTextContent(role="user", content="Hello")]),
)
print(response.analysis)
```

`AsyncHiddenLayer` has the same methods, as coroutines:

```python
import asyncio

from hiddenlayer import AsyncHiddenLayer, InteractionsMetadata


async def main() -> None:
    client = AsyncHiddenLayer()
    response = await client.interactions.analyze(
        metadata=InteractionsMetadata(model="gpt-5", requester_id="user-1234"),
    )
    print(response.analysis)


asyncio.run(main())
```

With the `aiohttp` extra installed, `pip install hiddenlayer-sdk[aiohttp]`, the async client sends its requests with aiohttp instead of httpx's own transport.

### Credentials

Give the client a client ID and secret, created under Client Credentials in the HiddenLayer Console. It exchanges them for an access token on its first call, reuses that token, and gets a new one two minutes before it expires:

```python
import os

from hiddenlayer import HiddenLayer

client = HiddenLayer(
    client_id=os.environ["HIDDENLAYER_CLIENT_ID"],
    client_secret=os.environ["HIDDENLAYER_CLIENT_SECRET"],
)
```

The client authenticates with the first of these it finds, arguments before the environment:

1. `token`: a Static API Key or a JWT, sent as a bearer token. The client never refreshes a token it's given. To keep one current, pass a function that returns it, which the client calls before every request. `AsyncHiddenLayer` also takes `async_token`, an async function.
2. `client_id` and `client_secret`.
3. The `HIDDENLAYER_TOKEN` environment variable.
4. The `HIDDENLAYER_CLIENT_ID` and `HIDDENLAYER_CLIENT_SECRET` environment variables.

The variables are read when the client is constructed. With no credentials at all, each request raises an `ApiError` that names what to set.

### Environments

`environment` takes a region by name, `"prod-us"` or `"prod-eu"`, or a `HiddenLayerEnvironment` value. `base_url` overrides it with any URL. With neither argument, the client uses `HIDDENLAYER_BASE_URL` if it is set, and `prod-us` otherwise.

## Model scanning

```python
report = client.model_scanner.scan_file(
    model_name="my-model",
    model_path="./models/model.pkl",
)
print(report.summary.severity)
```

`client.model_scanner` also has `scan_folder`, `scan_s3_model`, `scan_azure_blob_model` and `scan_huggingface_model`; `client.community_scanner.community_scan` scans a model the scanner fetches from a remote location. Each waits for the scan to finish unless you pass `wait_for_results=False`. [examples/demo.py](examples/demo.py) shows every scan.

The S3, Azure Blob Storage and Hugging Face scans download the model first, and need `boto3`, `azure-identity` with `azure-storage-blob`, or `huggingface_hub`. The SDK doesn't install them: install the ones for the scans you run.

## Red team sessions

`client.evaluation_sessions.red_team` starts a red team evaluation and hands each attack prompt to a function of yours, which calls your target and returns its reply:

```python
import asyncio

from hiddenlayer import AsyncHiddenLayer


async def handler(prompt, history, session_id, target_system_prompt) -> str:
    return "I can't help with that."  # call your target here


async def main() -> None:
    client = AsyncHiddenLayer()
    session = await client.evaluation_sessions.red_team.start_session(
        name="my-evaluation",
        target_model="my-target-model",
    )
    await session.run_with_callback_parallel(handler=handler)
    results = await client.evaluations.red_team.retrieve_evaluation_results(session.workflow_id)
    print(results.status)


asyncio.run(main())
```

[examples/red_team](examples/red_team) has a notebook for each kind of target.

## Request and response types

Every request and response type is importable from `hiddenlayer`:

```python
from hiddenlayer import EnrichedResponse, InteractionsMetadata

metadata = InteractionsMetadata(model="gpt-5", requester_id="user-1234")
response: EnrichedResponse = client.interactions.analyze(metadata=metadata)
```

Responses are pydantic models: `response.dict()` gives a plain dict, and a field the API adds after this release is still readable as an attribute.

## Handling errors

A response outside 2xx raises an `ApiError`, with `status_code`, `headers` and the decoded `body`, or the subclass the endpoint declares for that status, such as `NotFoundError`:

```python
from hiddenlayer import NotFoundError
from hiddenlayer.core import ApiError

try:
    client.sensors.retrieve("unknown")
except NotFoundError:
    print("no such sensor")
except ApiError as error:
    print(error.status_code, error.body)
```

A request that times out raises `httpx.TimeoutException`, and one that can't connect `httpx.ConnectError`.

## Pagination

List methods return a pager. Iterating it walks every item across pages:

```python
from hiddenlayer import SensorSorQueryFilter

for sensor in client.sensors.query(filter=SensorSorQueryFilter(active=True)):
    print(sensor.sensor_id)
```

`page.items` holds the current page's items, `page.response` the whole response, and `page.has_next` and `page.next_page()` move through pages by hand. Call `page.next_page()` only while `page.has_next` is true: after the last page it sends another request instead of returning `None`. The async client's pager is awaited first: `async for sensor in await client.sensors.query()`.

## Retries and timeouts

408, 409, 429 and 5xx responses and failed connections are retried twice by default, with exponential backoff. Requests time out after 60 seconds. Both can be set for the client or for one call:

```python
client = HiddenLayer(max_retries=0, timeout=20.0)

client.sensors.retrieve("sensor-id", request_options={"max_retries": 5, "timeout": 5.0})
```

## Raw responses

```python
response = client.sensors.with_raw_response.retrieve("sensor-id")
print(response.headers.get("x-request-id"))
print(response.data.sensor_id)
```

## Beta APIs

Some HiddenLayer APIs are marked **Beta**: not yet generally available or production ready. They can be used in production at your own risk; see the [Beta API Guidelines](https://dev.hiddenlayer.ai/docs/beta-api-faq).

- HiddenLayer makes no compatibility guarantees for Beta APIs. Breaking changes may occur at any time.
- Changes to Beta APIs don't count towards this package's semantic version.
- The first call a client makes to each beta endpoint emits a `hiddenlayer.BetaWarning`. Python's [warnings filter](https://docs.python.org/3/library/warnings.html#the-warnings-filter) silences it or turns it into an error.

## Requirements

Python 3.10 or later.

## Versioning and changelog

Releases follow [SemVer](https://semver.org/spec/v2.0.0.html), apart from Beta APIs. [CHANGELOG.md](CHANGELOG.md) lists each release, and `hiddenlayer.__version__` is the installed version.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). A pull request that changes `src/` needs a changeset: run `npx changeset` and describe the change for the changelog.
