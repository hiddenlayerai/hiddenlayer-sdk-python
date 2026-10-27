# Hiddenlayer Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fhiddenlayerai%2Fhiddenlayer-sdk-python)
[![pypi](https://img.shields.io/pypi/v/hiddenlayer)](https://pypi.python.org/pypi/hiddenlayer)

The Hiddenlayer Python library provides convenient access to the Hiddenlayer APIs from Python.

## Table of Contents

- [Documentation](#documentation)
- [Beta Apis](#beta-apis)
- [Installation](#installation)
- [Reference](#reference)
- [Usage](#usage)
- [Async Usage](#async-usage)
- [Using Types](#using-types)
- [Environments](#environments)
- [Async Client](#async-client)
- [Exception Handling](#exception-handling)
- [Pagination](#pagination)
- [Nested Params](#nested-params)
- [Handling Errors](#handling-errors)
- [Advanced](#advanced)
  - [Access Raw Response Data](#access-raw-response-data)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Custom Client](#custom-client)
- [Versioning](#versioning)
- [Requirements](#requirements)
- [Contributing](#contributing)

## Documentation

The REST API documentation can be found on [dev.hiddenlayer.ai](https://dev.hiddenlayer.ai). The full API of this library can be found in [api.md](api.md).

## Beta APIs

Some HiddenLayer APIs are marked as **Beta**, meaning they are not yet generally available (GA) or production ready. Beta APIs can be used in a production environment, but at your own risk and discretion. For full details, see the [Beta API Guidelines](https://dev.hiddenlayer.ai/docs/beta-api-faq) on the developer portal.

- HiddenLayer does not provide compatibility guarantees for Beta APIs. Breaking changes may occur at any time.
- SDK functions and types associated with Beta APIs are excluded when determining semver release versions.

## Installation

```sh
pip install hiddenlayer
```

## Reference

A full reference for this library is available [here](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/blob/HEAD/./reference.md).

## Usage

Instantiate and use the client with the following:

```python
from hiddenlayer import HiddenLayer

client = HiddenLayer(
    token="<token>",
)

client.credentials.create(
    name="some-name",
)
```

## Async usage

Simply import `AsyncHiddenLayer` instead of `HiddenLayer` and use `await` with each API call:

```python
import asyncio
from hiddenlayer import AsyncHiddenLayer

client = AsyncHiddenLayer(
    # defaults to "prod-us".
    environment="prod-eu",
)


async def main() -> None:
    response = await client.interactions.analyze(
        metadata={
            "model": "REPLACE_ME",
            "requester_id": "REPLACE_ME",
        },
        input={
            "messages": [
                {
                    "role": "user",
                    "content": "REPLACE_ME",
                }
            ]
        },
    )
    print(response.analysis)


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

### With aiohttp

By default, the async client uses `httpx` for HTTP requests. However, for improved concurrency performance you may also use `aiohttp` as the HTTP backend.

You can enable this by installing `aiohttp`:

```sh
# install from PyPI
pip install hiddenlayer-sdk[aiohttp]
```

Then you can enable it by instantiating the client with `http_client=DefaultAioHttpClient()`:

```python
import asyncio
from hiddenlayer import DefaultAioHttpClient
from hiddenlayer import AsyncHiddenLayer


async def main() -> None:
    async with AsyncHiddenLayer(
        http_client=DefaultAioHttpClient(),
    ) as client:
        response = await client.interactions.analyze(
            metadata={
                "model": "REPLACE_ME",
                "requester_id": "REPLACE_ME",
            },
            input={
                "messages": [
                    {
                        "role": "user",
                        "content": "REPLACE_ME",
                    }
                ]
            },
        )
        print(response.analysis)


asyncio.run(main())
```

## Using types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Responses are [Pydantic models](https://docs.pydantic.dev) which also provide helper methods for things like:

- Serializing back into JSON, `model.to_json()`
- Converting to a dictionary, `model.to_dict()`

Typed requests and responses provide autocomplete and documentation within your editor. If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `basic`.

## Environments

This SDK allows you to configure different environments for API requests.

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    environment=HiddenLayerEnvironment.PROD_US,
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio

from hiddenlayer import AsyncHiddenLayer

client = AsyncHiddenLayer(
    token="<token>",
)


async def main() -> None:
    await client.credentials.create(
        name="some-name",
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from hiddenlayer.core.api_error import ApiError

try:
    client.credentials.create(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Pagination

Paginated requests will return a `SyncPager` or `AsyncPager`, which can be used as generators for the underlying object.

```python
from hiddenlayer import HiddenLayer

client = HiddenLayer(
    token="<token>",
)

client.sensors.query_legacy()
```

```python
# You can also iterate through pages and access the typed response per page
pager = client.sensors.query_legacy(...)
for page in pager.iter_pages():
    print(page.response)  # access the typed response for each page
    for item in page:
        print(item)
```

## Nested params

Nested parameters are dictionaries, typed using `TypedDict`, for example:

```python
from hiddenlayer import HiddenLayer

client = HiddenLayer()

response = client.interactions.analyze(
    metadata={
        "model": "gpt-5",
        "requester_id": "user-1234",
        "provider": "openai",
    },
)
print(response.metadata)
```

## Handling errors

When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of `hiddenlayer.APIConnectionError` is raised.

When the API returns a non-success status code (that is, 4xx or 5xx
response), a subclass of `hiddenlayer.APIStatusError` is raised, containing `status_code` and `response` properties.

All errors inherit from `hiddenlayer.APIError`.

```python
import hiddenlayer
from hiddenlayer import HiddenLayer

client = HiddenLayer()

try:
    client.interactions.analyze(
        metadata={
            "model": "REPLACE_ME",
            "requester_id": "REPLACE_ME",
        },
        input={
            "messages": [
                {
                    "role": "user",
                    "content": "REPLACE_ME",
                }
            ]
        },
    )
except hiddenlayer.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except hiddenlayer.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except hiddenlayer.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as follows:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors are automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and >=500 Internal errors are all retried by default.

You can use the `max_retries` option to configure or disable retry settings:

```python
from hiddenlayer import HiddenLayer

# Configure the default for all requests:
client = HiddenLayer(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).interactions.analyze(
    metadata={
        "model": "REPLACE_ME",
        "requester_id": "REPLACE_ME",
    },
    input={
        "messages": [
            {
                "role": "user",
                "content": "REPLACE_ME",
            }
        ]
    },
)
```

### Timeouts

By default requests time out after 1 minute. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration) object:

```python
from hiddenlayer import HiddenLayer

# Configure the default for all requests:
client = HiddenLayer(
    # 20 seconds (default is 1 minute)
    timeout=20.0,
)

# More granular control:
client = HiddenLayer(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5.0).interactions.analyze(
    metadata={
        "model": "REPLACE_ME",
        "requester_id": "REPLACE_ME",
    },
    input={
        "messages": [
            {
                "role": "user",
                "content": "REPLACE_ME",
            }
        ]
    },
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from hiddenlayer import HiddenLayer

client = HiddenLayer(...)
response = client.credentials.with_raw_response.create(...)
print(response.headers)  # access the response headers
print(response.status_code)  # access the response status code
print(response.data)  # access the underlying object
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

Which status codes are retried depends on the `retryStatusCodes` generator configuration:

**`legacy`** (current default): retries on
- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409) (Conflict)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#server_error_responses) (All server errors, including 500)

**`recommended`**: retries on
- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409) (Conflict)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [502](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/502) (Bad Gateway)
- [503](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503) (Service Unavailable)
- [504](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/504) (Gateway Timeout)

Use the `max_retries` request option to configure this behavior.

```python
client.credentials.create(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python
from hiddenlayer import HiddenLayer

client = HiddenLayer(..., timeout=20.0)

# Override timeout for a specific method
client.credentials.create(..., request_options={
    "timeout": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from hiddenlayer import HiddenLayer

client = HiddenLayer(
    ...,
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals.)_
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python/issues) with questions, bugs, or suggestions.

### Determining the installed version

If you've upgraded to the latest version but aren't seeing any new features you were expecting then your python environment is likely still using an older version.

You can determine the version that is being used at runtime with:

```py
import hiddenlayer
print(hiddenlayer.__version__)
```

## Requirements

Python 3.9 or higher.

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
