# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .file import (
    FileResource,
    AsyncFileResource,
    FileResourceWithRawResponse,
    AsyncFileResourceWithRawResponse,
    FileResourceWithStreamingResponse,
    AsyncFileResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.scans import upload_start_params
from ...._base_client import make_request_options
from ....types.scans.upload_start_response import UploadStartResponse
from ....types.scans.upload_complete_all_response import UploadCompleteAllResponse

__all__ = ["UploadResource", "AsyncUploadResource"]


class UploadResource(SyncAPIResource):
    @cached_property
    def file(self) -> FileResource:
        return FileResource(self._client)

    @cached_property
    def with_raw_response(self) -> UploadResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return UploadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UploadResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return UploadResourceWithStreamingResponse(self)

    def complete_all(
        self,
        scan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadCompleteAllResponse:
        """
        Scan uploaded files

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        return self._patch(
            f"/scan/v3/upload/{scan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadCompleteAllResponse,
        )

    def start(
        self,
        *,
        model_name: str,
        model_version: str,
        requesting_entity: str,
        location_alias: str | Omit = omit,
        origin: str | Omit = omit,
        request_source: Literal["Hybrid Upload", "API Upload", "Integration", "UI Upload", "AI Asset Discovery"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadStartResponse:
        """
        Start a model upload

        Args:
          model_name: Model name

          model_version: Model version

          requesting_entity: Requesting entity

          location_alias: Requested location alias

          origin: Specifies the platform or service where the model originated before being
              scanned

          request_source: Identifies the system that requested the scan

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/scan/v3/upload",
            body=maybe_transform(
                {
                    "model_name": model_name,
                    "model_version": model_version,
                    "requesting_entity": requesting_entity,
                    "location_alias": location_alias,
                    "origin": origin,
                    "request_source": request_source,
                },
                upload_start_params.UploadStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadStartResponse,
        )


class AsyncUploadResource(AsyncAPIResource):
    @cached_property
    def file(self) -> AsyncFileResource:
        return AsyncFileResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUploadResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUploadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUploadResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return AsyncUploadResourceWithStreamingResponse(self)

    async def complete_all(
        self,
        scan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadCompleteAllResponse:
        """
        Scan uploaded files

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        return await self._patch(
            f"/scan/v3/upload/{scan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadCompleteAllResponse,
        )

    async def start(
        self,
        *,
        model_name: str,
        model_version: str,
        requesting_entity: str,
        location_alias: str | Omit = omit,
        origin: str | Omit = omit,
        request_source: Literal["Hybrid Upload", "API Upload", "Integration", "UI Upload", "AI Asset Discovery"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadStartResponse:
        """
        Start a model upload

        Args:
          model_name: Model name

          model_version: Model version

          requesting_entity: Requesting entity

          location_alias: Requested location alias

          origin: Specifies the platform or service where the model originated before being
              scanned

          request_source: Identifies the system that requested the scan

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/scan/v3/upload",
            body=await async_maybe_transform(
                {
                    "model_name": model_name,
                    "model_version": model_version,
                    "requesting_entity": requesting_entity,
                    "location_alias": location_alias,
                    "origin": origin,
                    "request_source": request_source,
                },
                upload_start_params.UploadStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadStartResponse,
        )


class UploadResourceWithRawResponse:
    def __init__(self, upload: UploadResource) -> None:
        self._upload = upload

        self.complete_all = to_raw_response_wrapper(
            upload.complete_all,
        )
        self.start = to_raw_response_wrapper(
            upload.start,
        )

    @cached_property
    def file(self) -> FileResourceWithRawResponse:
        return FileResourceWithRawResponse(self._upload.file)


class AsyncUploadResourceWithRawResponse:
    def __init__(self, upload: AsyncUploadResource) -> None:
        self._upload = upload

        self.complete_all = async_to_raw_response_wrapper(
            upload.complete_all,
        )
        self.start = async_to_raw_response_wrapper(
            upload.start,
        )

    @cached_property
    def file(self) -> AsyncFileResourceWithRawResponse:
        return AsyncFileResourceWithRawResponse(self._upload.file)


class UploadResourceWithStreamingResponse:
    def __init__(self, upload: UploadResource) -> None:
        self._upload = upload

        self.complete_all = to_streamed_response_wrapper(
            upload.complete_all,
        )
        self.start = to_streamed_response_wrapper(
            upload.start,
        )

    @cached_property
    def file(self) -> FileResourceWithStreamingResponse:
        return FileResourceWithStreamingResponse(self._upload.file)


class AsyncUploadResourceWithStreamingResponse:
    def __init__(self, upload: AsyncUploadResource) -> None:
        self._upload = upload

        self.complete_all = async_to_streamed_response_wrapper(
            upload.complete_all,
        )
        self.start = async_to_streamed_response_wrapper(
            upload.start,
        )

    @cached_property
    def file(self) -> AsyncFileResourceWithStreamingResponse:
        return AsyncFileResourceWithStreamingResponse(self._upload.file)
