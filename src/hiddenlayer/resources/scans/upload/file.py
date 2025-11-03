# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.scans.upload.file_add_response import FileAddResponse
from ....types.scans.upload.file_complete_response import FileCompleteResponse

__all__ = ["FileResource", "AsyncFileResource"]


class FileResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return FileResourceWithStreamingResponse(self)

    def add(
        self,
        scan_id: str,
        *,
        file_content_length: int,
        file_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileAddResponse:
        """
        Upload a model file

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        extra_headers = {
            "file-content-length": str(file_content_length),
            "file-name": file_name,
            **(extra_headers or {}),
        }
        return self._post(
            f"/scan/v3/upload/{scan_id}/file",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileAddResponse,
        )

    def complete(
        self,
        file_id: str,
        *,
        scan_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileCompleteResponse:
        """
        Complete a file upload

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._patch(
            f"/scan/v3/upload/{scan_id}/file/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileCompleteResponse,
        )


class AsyncFileResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return AsyncFileResourceWithStreamingResponse(self)

    async def add(
        self,
        scan_id: str,
        *,
        file_content_length: int,
        file_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileAddResponse:
        """
        Upload a model file

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        extra_headers = {
            "file-content-length": str(file_content_length),
            "file-name": file_name,
            **(extra_headers or {}),
        }
        return await self._post(
            f"/scan/v3/upload/{scan_id}/file",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileAddResponse,
        )

    async def complete(
        self,
        file_id: str,
        *,
        scan_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileCompleteResponse:
        """
        Complete a file upload

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._patch(
            f"/scan/v3/upload/{scan_id}/file/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileCompleteResponse,
        )


class FileResourceWithRawResponse:
    def __init__(self, file: FileResource) -> None:
        self._file = file

        self.add = to_raw_response_wrapper(
            file.add,
        )
        self.complete = to_raw_response_wrapper(
            file.complete,
        )


class AsyncFileResourceWithRawResponse:
    def __init__(self, file: AsyncFileResource) -> None:
        self._file = file

        self.add = async_to_raw_response_wrapper(
            file.add,
        )
        self.complete = async_to_raw_response_wrapper(
            file.complete,
        )


class FileResourceWithStreamingResponse:
    def __init__(self, file: FileResource) -> None:
        self._file = file

        self.add = to_streamed_response_wrapper(
            file.add,
        )
        self.complete = to_streamed_response_wrapper(
            file.complete,
        )


class AsyncFileResourceWithStreamingResponse:
    def __init__(self, file: AsyncFileResource) -> None:
        self._file = file

        self.add = async_to_streamed_response_wrapper(
            file.add,
        )
        self.complete = async_to_streamed_response_wrapper(
            file.complete,
        )
