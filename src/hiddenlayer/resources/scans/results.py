# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPagination, AsyncCursorPagination
from ...types.scans import result_list_files_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.scans.scan_file_result import ScanFileResult
from ...types.scans.scan_report_summary import ScanReportSummary

__all__ = ["ResultsResource", "AsyncResultsResource"]


class ResultsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return ResultsResourceWithStreamingResponse(self)

    def list_files(
        self,
        scan_id: str,
        *,
        cursor: str | Omit = omit,
        has_detections: bool | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[ScanFileResult]:
        """Returns a cursor-paginated list of file results for a given scan.

        Results are
        sorted by compliance status, then highest detection severity, then file path.

        Args:
          cursor: Cursor for pagination, used to navigate through pages of results

          has_detections: When true, only return files that have detections

          page_size: Number of items to return per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        return self._get_api_list(
            path_template("/scan/v3/results/{scan_id}/files", scan_id=scan_id),
            page=SyncCursorPagination[ScanFileResult],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "has_detections": has_detections,
                        "page_size": page_size,
                    },
                    result_list_files_params.ResultListFilesParams,
                ),
            ),
            model=ScanFileResult,
        )

    def retrieve_summary(
        self,
        scan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScanReportSummary:
        """
        Returns aggregated summary information for a scan without file-level results.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        return self._get(
            path_template("/scan/v3/results/{scan_id}/summary", scan_id=scan_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScanReportSummary,
        )

    def sarif(
        self,
        scan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Get scan results in SARIF format

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        extra_headers = {"Accept": "application/sarif+json", **(extra_headers or {})}
        return self._get(
            path_template("/scan/v3/results/{scan_id}/sarif", scan_id=scan_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncResultsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return AsyncResultsResourceWithStreamingResponse(self)

    def list_files(
        self,
        scan_id: str,
        *,
        cursor: str | Omit = omit,
        has_detections: bool | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ScanFileResult, AsyncCursorPagination[ScanFileResult]]:
        """Returns a cursor-paginated list of file results for a given scan.

        Results are
        sorted by compliance status, then highest detection severity, then file path.

        Args:
          cursor: Cursor for pagination, used to navigate through pages of results

          has_detections: When true, only return files that have detections

          page_size: Number of items to return per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        return self._get_api_list(
            path_template("/scan/v3/results/{scan_id}/files", scan_id=scan_id),
            page=AsyncCursorPagination[ScanFileResult],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "has_detections": has_detections,
                        "page_size": page_size,
                    },
                    result_list_files_params.ResultListFilesParams,
                ),
            ),
            model=ScanFileResult,
        )

    async def retrieve_summary(
        self,
        scan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScanReportSummary:
        """
        Returns aggregated summary information for a scan without file-level results.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        return await self._get(
            path_template("/scan/v3/results/{scan_id}/summary", scan_id=scan_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScanReportSummary,
        )

    async def sarif(
        self,
        scan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Get scan results in SARIF format

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        extra_headers = {"Accept": "application/sarif+json", **(extra_headers or {})}
        return await self._get(
            path_template("/scan/v3/results/{scan_id}/sarif", scan_id=scan_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class ResultsResourceWithRawResponse:
    def __init__(self, results: ResultsResource) -> None:
        self._results = results

        self.list_files = to_raw_response_wrapper(
            results.list_files,
        )
        self.retrieve_summary = to_raw_response_wrapper(
            results.retrieve_summary,
        )
        self.sarif = to_raw_response_wrapper(
            results.sarif,
        )


class AsyncResultsResourceWithRawResponse:
    def __init__(self, results: AsyncResultsResource) -> None:
        self._results = results

        self.list_files = async_to_raw_response_wrapper(
            results.list_files,
        )
        self.retrieve_summary = async_to_raw_response_wrapper(
            results.retrieve_summary,
        )
        self.sarif = async_to_raw_response_wrapper(
            results.sarif,
        )


class ResultsResourceWithStreamingResponse:
    def __init__(self, results: ResultsResource) -> None:
        self._results = results

        self.list_files = to_streamed_response_wrapper(
            results.list_files,
        )
        self.retrieve_summary = to_streamed_response_wrapper(
            results.retrieve_summary,
        )
        self.sarif = to_streamed_response_wrapper(
            results.sarif,
        )


class AsyncResultsResourceWithStreamingResponse:
    def __init__(self, results: AsyncResultsResource) -> None:
        self._results = results

        self.list_files = async_to_streamed_response_wrapper(
            results.list_files,
        )
        self.retrieve_summary = async_to_streamed_response_wrapper(
            results.retrieve_summary,
        )
        self.sarif = async_to_streamed_response_wrapper(
            results.sarif,
        )
