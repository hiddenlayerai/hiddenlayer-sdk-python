# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import sensor_query_params, sensor_create_params, sensor_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.sensor_query_response import SensorQueryResponse
from ..types.sensor_create_response import SensorCreateResponse
from ..types.sensor_update_response import SensorUpdateResponse
from ..types.sensor_retrieve_response import SensorRetrieveResponse

__all__ = ["SensorsResource", "AsyncSensorsResource"]


class SensorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SensorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SensorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SensorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return SensorsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def create(
        self,
        *,
        plaintext_name: str,
        active: bool | Omit = omit,
        adhoc: bool | Omit = omit,
        tags: Dict[str, object] | Omit = omit,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SensorCreateResponse:
        """
        ⚠️ **DEPRECATED**: This endpoint will be removed after April 13, 2026.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v2/sensors/create",
            body=maybe_transform(
                {
                    "plaintext_name": plaintext_name,
                    "active": active,
                    "adhoc": adhoc,
                    "tags": tags,
                    "version": version,
                },
                sensor_create_params.SensorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SensorCreateResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def retrieve(
        self,
        sensor_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SensorRetrieveResponse:
        """
        ⚠️ **DEPRECATED**: This endpoint will be removed after April 13, 2026.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sensor_id:
            raise ValueError(f"Expected a non-empty value for `sensor_id` but received {sensor_id!r}")
        return self._get(
            f"/api/v2/sensors/{sensor_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SensorRetrieveResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def update(
        self,
        sensor_id: str,
        *,
        active: bool | Omit = omit,
        plaintext_name: str | Omit = omit,
        tags: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SensorUpdateResponse:
        """
        ⚠️ **DEPRECATED**: This endpoint will be removed after April 13, 2026.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sensor_id:
            raise ValueError(f"Expected a non-empty value for `sensor_id` but received {sensor_id!r}")
        return self._put(
            f"/api/v2/sensors/{sensor_id}",
            body=maybe_transform(
                {
                    "active": active,
                    "plaintext_name": plaintext_name,
                    "tags": tags,
                },
                sensor_update_params.SensorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SensorUpdateResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def delete(
        self,
        sensor_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        ⚠️ **DEPRECATED**: This endpoint will be removed after April 13, 2026.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sensor_id:
            raise ValueError(f"Expected a non-empty value for `sensor_id` but received {sensor_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/v2/sensors/{sensor_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    def query(
        self,
        *,
        filter: sensor_query_params.Filter | Omit = omit,
        order_by: str | Omit = omit,
        order_dir: Literal["asc", "desc"] | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SensorQueryResponse:
        """
        ⚠️ **DEPRECATED**: This endpoint will be removed after April 13, 2026.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v2/sensors/query",
            body=maybe_transform(
                {
                    "filter": filter,
                    "order_by": order_by,
                    "order_dir": order_dir,
                    "page_number": page_number,
                    "page_size": page_size,
                },
                sensor_query_params.SensorQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SensorQueryResponse,
        )


class AsyncSensorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSensorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSensorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSensorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return AsyncSensorsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def create(
        self,
        *,
        plaintext_name: str,
        active: bool | Omit = omit,
        adhoc: bool | Omit = omit,
        tags: Dict[str, object] | Omit = omit,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SensorCreateResponse:
        """
        ⚠️ **DEPRECATED**: This endpoint will be removed after April 13, 2026.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v2/sensors/create",
            body=await async_maybe_transform(
                {
                    "plaintext_name": plaintext_name,
                    "active": active,
                    "adhoc": adhoc,
                    "tags": tags,
                    "version": version,
                },
                sensor_create_params.SensorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SensorCreateResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def retrieve(
        self,
        sensor_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SensorRetrieveResponse:
        """
        ⚠️ **DEPRECATED**: This endpoint will be removed after April 13, 2026.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sensor_id:
            raise ValueError(f"Expected a non-empty value for `sensor_id` but received {sensor_id!r}")
        return await self._get(
            f"/api/v2/sensors/{sensor_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SensorRetrieveResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def update(
        self,
        sensor_id: str,
        *,
        active: bool | Omit = omit,
        plaintext_name: str | Omit = omit,
        tags: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SensorUpdateResponse:
        """
        ⚠️ **DEPRECATED**: This endpoint will be removed after April 13, 2026.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sensor_id:
            raise ValueError(f"Expected a non-empty value for `sensor_id` but received {sensor_id!r}")
        return await self._put(
            f"/api/v2/sensors/{sensor_id}",
            body=await async_maybe_transform(
                {
                    "active": active,
                    "plaintext_name": plaintext_name,
                    "tags": tags,
                },
                sensor_update_params.SensorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SensorUpdateResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def delete(
        self,
        sensor_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        ⚠️ **DEPRECATED**: This endpoint will be removed after April 13, 2026.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sensor_id:
            raise ValueError(f"Expected a non-empty value for `sensor_id` but received {sensor_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/v2/sensors/{sensor_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    async def query(
        self,
        *,
        filter: sensor_query_params.Filter | Omit = omit,
        order_by: str | Omit = omit,
        order_dir: Literal["asc", "desc"] | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SensorQueryResponse:
        """
        ⚠️ **DEPRECATED**: This endpoint will be removed after April 13, 2026.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v2/sensors/query",
            body=await async_maybe_transform(
                {
                    "filter": filter,
                    "order_by": order_by,
                    "order_dir": order_dir,
                    "page_number": page_number,
                    "page_size": page_size,
                },
                sensor_query_params.SensorQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SensorQueryResponse,
        )


class SensorsResourceWithRawResponse:
    def __init__(self, sensors: SensorsResource) -> None:
        self._sensors = sensors

        self.create = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                sensors.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                sensors.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                sensors.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                sensors.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.query = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                sensors.query,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncSensorsResourceWithRawResponse:
    def __init__(self, sensors: AsyncSensorsResource) -> None:
        self._sensors = sensors

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                sensors.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                sensors.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                sensors.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                sensors.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.query = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                sensors.query,  # pyright: ignore[reportDeprecated],
            )
        )


class SensorsResourceWithStreamingResponse:
    def __init__(self, sensors: SensorsResource) -> None:
        self._sensors = sensors

        self.create = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                sensors.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                sensors.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                sensors.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                sensors.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.query = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                sensors.query,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncSensorsResourceWithStreamingResponse:
    def __init__(self, sensors: AsyncSensorsResource) -> None:
        self._sensors = sensors

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                sensors.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                sensors.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                sensors.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                sensors.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.query = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                sensors.query,  # pyright: ignore[reportDeprecated],
            )
        )
