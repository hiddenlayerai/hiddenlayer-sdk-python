# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import scans, models, sensors
    from .resources.sensors import SensorsResource, AsyncSensorsResource
    from .resources.scans.scans import ScansResource, AsyncScansResource
    from .resources.models.models import ModelsResource, AsyncModelsResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "HiddenLayer",
    "AsyncHiddenLayer",
    "Client",
    "AsyncClient",
]


class HiddenLayer(SyncAPIClient):
    # client options
    bearer_token: str | None
    client_id: str | None
    client_secret: str | None

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous HiddenLayer client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `bearer_token` from `HIDDENLAYER_TOKEN`
        - `client_id` from `HIDDENLAYER_CLIENT_ID`
        - `client_secret` from `HIDDENLAYER_CLIENT_SECRET`
        """
        if bearer_token is None:
            bearer_token = os.environ.get("HIDDENLAYER_TOKEN")
        self.bearer_token = bearer_token

        if client_id is None:
            client_id = os.environ.get("HIDDENLAYER_CLIENT_ID")
        self.client_id = client_id

        if client_secret is None:
            client_secret = os.environ.get("HIDDENLAYER_CLIENT_SECRET")
        self.client_secret = client_secret

        if base_url is None:
            base_url = os.environ.get("HIDDEN_LAYER_BASE_URL")
        if base_url is None:
            base_url = f"https://api.hiddenlayer.ai"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def models(self) -> ModelsResource:
        from .resources.models import ModelsResource

        return ModelsResource(self)

    @cached_property
    def sensors(self) -> SensorsResource:
        from .resources.sensors import SensorsResource

        return SensorsResource(self)

    @cached_property
    def scans(self) -> ScansResource:
        from .resources.scans import ScansResource

        return ScansResource(self)

    @cached_property
    def with_raw_response(self) -> HiddenLayerWithRawResponse:
        return HiddenLayerWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HiddenLayerWithStreamedResponse:
        return HiddenLayerWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._bearer_auth, **self._hidden_layer_user_auth}

    @property
    def _bearer_auth(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    def _hidden_layer_user_auth(self) -> httpx.Auth | None:
        raise NotImplementedError("This auth method has not been implemented yet.")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            client_id=client_id or self.client_id,
            client_secret=client_secret or self.client_secret,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncHiddenLayer(AsyncAPIClient):
    # client options
    bearer_token: str | None
    client_id: str | None
    client_secret: str | None

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncHiddenLayer client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `bearer_token` from `HIDDENLAYER_TOKEN`
        - `client_id` from `HIDDENLAYER_CLIENT_ID`
        - `client_secret` from `HIDDENLAYER_CLIENT_SECRET`
        """
        if bearer_token is None:
            bearer_token = os.environ.get("HIDDENLAYER_TOKEN")
        self.bearer_token = bearer_token

        if client_id is None:
            client_id = os.environ.get("HIDDENLAYER_CLIENT_ID")
        self.client_id = client_id

        if client_secret is None:
            client_secret = os.environ.get("HIDDENLAYER_CLIENT_SECRET")
        self.client_secret = client_secret

        if base_url is None:
            base_url = os.environ.get("HIDDEN_LAYER_BASE_URL")
        if base_url is None:
            base_url = f"https://api.hiddenlayer.ai"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def models(self) -> AsyncModelsResource:
        from .resources.models import AsyncModelsResource

        return AsyncModelsResource(self)

    @cached_property
    def sensors(self) -> AsyncSensorsResource:
        from .resources.sensors import AsyncSensorsResource

        return AsyncSensorsResource(self)

    @cached_property
    def scans(self) -> AsyncScansResource:
        from .resources.scans import AsyncScansResource

        return AsyncScansResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncHiddenLayerWithRawResponse:
        return AsyncHiddenLayerWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHiddenLayerWithStreamedResponse:
        return AsyncHiddenLayerWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._bearer_auth, **self._hidden_layer_user_auth}

    @property
    def _bearer_auth(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    def _hidden_layer_user_auth(self) -> httpx.Auth | None:
        raise NotImplementedError("This auth method has not been implemented yet.")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            client_id=client_id or self.client_id,
            client_secret=client_secret or self.client_secret,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class HiddenLayerWithRawResponse:
    _client: HiddenLayer

    def __init__(self, client: HiddenLayer) -> None:
        self._client = client

    @cached_property
    def models(self) -> models.ModelsResourceWithRawResponse:
        from .resources.models import ModelsResourceWithRawResponse

        return ModelsResourceWithRawResponse(self._client.models)

    @cached_property
    def sensors(self) -> sensors.SensorsResourceWithRawResponse:
        from .resources.sensors import SensorsResourceWithRawResponse

        return SensorsResourceWithRawResponse(self._client.sensors)

    @cached_property
    def scans(self) -> scans.ScansResourceWithRawResponse:
        from .resources.scans import ScansResourceWithRawResponse

        return ScansResourceWithRawResponse(self._client.scans)


class AsyncHiddenLayerWithRawResponse:
    _client: AsyncHiddenLayer

    def __init__(self, client: AsyncHiddenLayer) -> None:
        self._client = client

    @cached_property
    def models(self) -> models.AsyncModelsResourceWithRawResponse:
        from .resources.models import AsyncModelsResourceWithRawResponse

        return AsyncModelsResourceWithRawResponse(self._client.models)

    @cached_property
    def sensors(self) -> sensors.AsyncSensorsResourceWithRawResponse:
        from .resources.sensors import AsyncSensorsResourceWithRawResponse

        return AsyncSensorsResourceWithRawResponse(self._client.sensors)

    @cached_property
    def scans(self) -> scans.AsyncScansResourceWithRawResponse:
        from .resources.scans import AsyncScansResourceWithRawResponse

        return AsyncScansResourceWithRawResponse(self._client.scans)


class HiddenLayerWithStreamedResponse:
    _client: HiddenLayer

    def __init__(self, client: HiddenLayer) -> None:
        self._client = client

    @cached_property
    def models(self) -> models.ModelsResourceWithStreamingResponse:
        from .resources.models import ModelsResourceWithStreamingResponse

        return ModelsResourceWithStreamingResponse(self._client.models)

    @cached_property
    def sensors(self) -> sensors.SensorsResourceWithStreamingResponse:
        from .resources.sensors import SensorsResourceWithStreamingResponse

        return SensorsResourceWithStreamingResponse(self._client.sensors)

    @cached_property
    def scans(self) -> scans.ScansResourceWithStreamingResponse:
        from .resources.scans import ScansResourceWithStreamingResponse

        return ScansResourceWithStreamingResponse(self._client.scans)


class AsyncHiddenLayerWithStreamedResponse:
    _client: AsyncHiddenLayer

    def __init__(self, client: AsyncHiddenLayer) -> None:
        self._client = client

    @cached_property
    def models(self) -> models.AsyncModelsResourceWithStreamingResponse:
        from .resources.models import AsyncModelsResourceWithStreamingResponse

        return AsyncModelsResourceWithStreamingResponse(self._client.models)

    @cached_property
    def sensors(self) -> sensors.AsyncSensorsResourceWithStreamingResponse:
        from .resources.sensors import AsyncSensorsResourceWithStreamingResponse

        return AsyncSensorsResourceWithStreamingResponse(self._client.sensors)

    @cached_property
    def scans(self) -> scans.AsyncScansResourceWithStreamingResponse:
        from .resources.scans import AsyncScansResourceWithStreamingResponse

        return AsyncScansResourceWithStreamingResponse(self._client.scans)


Client = HiddenLayer

AsyncClient = AsyncHiddenLayer
