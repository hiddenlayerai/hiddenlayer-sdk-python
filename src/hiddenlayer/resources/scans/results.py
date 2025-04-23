# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.scans import result_list_params, result_patch_params, result_start_params, result_retrieve_params
from ..._base_client import make_request_options
from ...types.scans.scan_report import ScanReport
from ...types.scans.result_list_response import ResultListResponse
from ...types.scans.result_patch_response import ResultPatchResponse
from ...types.scans.file_scan_report_param import FileScanReportParam

__all__ = ["ResultsResource", "AsyncResultsResource"]


class ResultsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hiddenlayer-sdk-python#with_streaming_response
        """
        return ResultsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        scan_id: str,
        *,
        has_detections: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScanReport:
        """
        Get Result of a Model Scan

        Args:
          has_detections: Filter file_results to only those that have detections (and parents)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        extra_headers = {"Accept": "application/json; charset=utf-8", **(extra_headers or {})}
        return self._get(
            f"/scan/v3/results/{scan_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"has_detections": has_detections}, result_retrieve_params.ResultRetrieveParams),
            ),
            cast_to=ScanReport,
        )

    def list(
        self,
        *,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        latest_per_model_version_only: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        model_ids: List[str] | NotGiven = NOT_GIVEN,
        model_version_ids: List[str] | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        severity: List[str] | NotGiven = NOT_GIVEN,
        sort: str | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResultListResponse:
        """
        Get condensed reports for a Model Scan

        Args:
          end_time: End Time

          latest_per_model_version_only: only return latest result per model version

          model_ids: Model ID

          model_version_ids: Model Version ID

          severity: Severities

          sort: allow sorting by status, severity or created at, ascending (+) or the default
              descending (-)

          start_time: Start Time

          status: Statuses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/json; charset=utf-8", **(extra_headers or {})}
        return self._get(
            "/scan/v3/results",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_time": end_time,
                        "latest_per_model_version_only": latest_per_model_version_only,
                        "limit": limit,
                        "model_ids": model_ids,
                        "model_version_ids": model_version_ids,
                        "offset": offset,
                        "severity": severity,
                        "sort": sort,
                        "start_time": start_time,
                        "status": status,
                    },
                    result_list_params.ResultListParams,
                ),
            ),
            cast_to=ResultListResponse,
        )

    def patch(
        self,
        path_scan_id: str,
        *,
        detection_count: int,
        file_count: int,
        files_with_detections_count: int,
        inventory: result_patch_params.Inventory,
        body_scan_id: str,
        start_time: Union[str, datetime],
        status: Literal["pending", "running", "done", "failed", "canceled"],
        version: str,
        has_detections: bool | NotGiven = NOT_GIVEN,
        detection_categories: List[str] | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        file_results: Iterable[FileScanReportParam] | NotGiven = NOT_GIVEN,
        severity: Literal["low", "medium", "high", "critical", "safe", "unknown"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResultPatchResponse:
        """
        Indicate part (file or files) of a model scan has completed

        Args:
          detection_count: number of detections found

          file_count: number of files scanned

          files_with_detections_count: number of files with detections found

          inventory: information about model and version that this scan relates to

          body_scan_id: unique identifier for the scan

          start_time: time the scan started

          status: status of the scan

          version: scanner version

          has_detections: Filter file_results to only those that have detections (and parents)

          detection_categories: list of detection categories found

          end_time: time the scan ended

          severity: detection severity

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_scan_id:
            raise ValueError(f"Expected a non-empty value for `path_scan_id` but received {path_scan_id!r}")
        return self._patch(
            f"/scan/v3/results/{path_scan_id}",
            body=maybe_transform(
                {
                    "detection_count": detection_count,
                    "file_count": file_count,
                    "files_with_detections_count": files_with_detections_count,
                    "inventory": inventory,
                    "body_scan_id": body_scan_id,
                    "start_time": start_time,
                    "status": status,
                    "version": version,
                    "detection_categories": detection_categories,
                    "end_time": end_time,
                    "file_results": file_results,
                    "severity": severity,
                },
                result_patch_params.ResultPatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"has_detections": has_detections}, result_patch_params.ResultPatchParams),
            ),
            cast_to=ResultPatchResponse,
        )

    def start(
        self,
        path_scan_id: str,
        *,
        detection_count: int,
        file_count: int,
        files_with_detections_count: int,
        inventory: result_start_params.Inventory,
        body_scan_id: str,
        start_time: Union[str, datetime],
        status: Literal["pending", "running", "done", "failed", "canceled"],
        version: str,
        has_detections: bool | NotGiven = NOT_GIVEN,
        detection_categories: List[str] | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        file_results: Iterable[FileScanReportParam] | NotGiven = NOT_GIVEN,
        severity: Literal["low", "medium", "high", "critical", "safe", "unknown"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Indicate model scan has started

        Args:
          detection_count: number of detections found

          file_count: number of files scanned

          files_with_detections_count: number of files with detections found

          inventory: information about model and version that this scan relates to

          body_scan_id: unique identifier for the scan

          start_time: time the scan started

          status: status of the scan

          version: scanner version

          has_detections: Filter file_results to only those that have detections (and parents)

          detection_categories: list of detection categories found

          end_time: time the scan ended

          severity: detection severity

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_scan_id:
            raise ValueError(f"Expected a non-empty value for `path_scan_id` but received {path_scan_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/scan/v3/results/{path_scan_id}",
            body=maybe_transform(
                {
                    "detection_count": detection_count,
                    "file_count": file_count,
                    "files_with_detections_count": files_with_detections_count,
                    "inventory": inventory,
                    "body_scan_id": body_scan_id,
                    "start_time": start_time,
                    "status": status,
                    "version": version,
                    "detection_categories": detection_categories,
                    "end_time": end_time,
                    "file_results": file_results,
                    "severity": severity,
                },
                result_start_params.ResultStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"has_detections": has_detections}, result_start_params.ResultStartParams),
            ),
            cast_to=NoneType,
        )


class AsyncResultsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hiddenlayer-sdk-python#with_streaming_response
        """
        return AsyncResultsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        scan_id: str,
        *,
        has_detections: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScanReport:
        """
        Get Result of a Model Scan

        Args:
          has_detections: Filter file_results to only those that have detections (and parents)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        extra_headers = {"Accept": "application/json; charset=utf-8", **(extra_headers or {})}
        return await self._get(
            f"/scan/v3/results/{scan_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"has_detections": has_detections}, result_retrieve_params.ResultRetrieveParams
                ),
            ),
            cast_to=ScanReport,
        )

    async def list(
        self,
        *,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        latest_per_model_version_only: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        model_ids: List[str] | NotGiven = NOT_GIVEN,
        model_version_ids: List[str] | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        severity: List[str] | NotGiven = NOT_GIVEN,
        sort: str | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResultListResponse:
        """
        Get condensed reports for a Model Scan

        Args:
          end_time: End Time

          latest_per_model_version_only: only return latest result per model version

          model_ids: Model ID

          model_version_ids: Model Version ID

          severity: Severities

          sort: allow sorting by status, severity or created at, ascending (+) or the default
              descending (-)

          start_time: Start Time

          status: Statuses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/json; charset=utf-8", **(extra_headers or {})}
        return await self._get(
            "/scan/v3/results",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_time": end_time,
                        "latest_per_model_version_only": latest_per_model_version_only,
                        "limit": limit,
                        "model_ids": model_ids,
                        "model_version_ids": model_version_ids,
                        "offset": offset,
                        "severity": severity,
                        "sort": sort,
                        "start_time": start_time,
                        "status": status,
                    },
                    result_list_params.ResultListParams,
                ),
            ),
            cast_to=ResultListResponse,
        )

    async def patch(
        self,
        path_scan_id: str,
        *,
        detection_count: int,
        file_count: int,
        files_with_detections_count: int,
        inventory: result_patch_params.Inventory,
        body_scan_id: str,
        start_time: Union[str, datetime],
        status: Literal["pending", "running", "done", "failed", "canceled"],
        version: str,
        has_detections: bool | NotGiven = NOT_GIVEN,
        detection_categories: List[str] | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        file_results: Iterable[FileScanReportParam] | NotGiven = NOT_GIVEN,
        severity: Literal["low", "medium", "high", "critical", "safe", "unknown"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResultPatchResponse:
        """
        Indicate part (file or files) of a model scan has completed

        Args:
          detection_count: number of detections found

          file_count: number of files scanned

          files_with_detections_count: number of files with detections found

          inventory: information about model and version that this scan relates to

          body_scan_id: unique identifier for the scan

          start_time: time the scan started

          status: status of the scan

          version: scanner version

          has_detections: Filter file_results to only those that have detections (and parents)

          detection_categories: list of detection categories found

          end_time: time the scan ended

          severity: detection severity

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_scan_id:
            raise ValueError(f"Expected a non-empty value for `path_scan_id` but received {path_scan_id!r}")
        return await self._patch(
            f"/scan/v3/results/{path_scan_id}",
            body=await async_maybe_transform(
                {
                    "detection_count": detection_count,
                    "file_count": file_count,
                    "files_with_detections_count": files_with_detections_count,
                    "inventory": inventory,
                    "body_scan_id": body_scan_id,
                    "start_time": start_time,
                    "status": status,
                    "version": version,
                    "detection_categories": detection_categories,
                    "end_time": end_time,
                    "file_results": file_results,
                    "severity": severity,
                },
                result_patch_params.ResultPatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"has_detections": has_detections}, result_patch_params.ResultPatchParams
                ),
            ),
            cast_to=ResultPatchResponse,
        )

    async def start(
        self,
        path_scan_id: str,
        *,
        detection_count: int,
        file_count: int,
        files_with_detections_count: int,
        inventory: result_start_params.Inventory,
        body_scan_id: str,
        start_time: Union[str, datetime],
        status: Literal["pending", "running", "done", "failed", "canceled"],
        version: str,
        has_detections: bool | NotGiven = NOT_GIVEN,
        detection_categories: List[str] | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        file_results: Iterable[FileScanReportParam] | NotGiven = NOT_GIVEN,
        severity: Literal["low", "medium", "high", "critical", "safe", "unknown"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Indicate model scan has started

        Args:
          detection_count: number of detections found

          file_count: number of files scanned

          files_with_detections_count: number of files with detections found

          inventory: information about model and version that this scan relates to

          body_scan_id: unique identifier for the scan

          start_time: time the scan started

          status: status of the scan

          version: scanner version

          has_detections: Filter file_results to only those that have detections (and parents)

          detection_categories: list of detection categories found

          end_time: time the scan ended

          severity: detection severity

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_scan_id:
            raise ValueError(f"Expected a non-empty value for `path_scan_id` but received {path_scan_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/scan/v3/results/{path_scan_id}",
            body=await async_maybe_transform(
                {
                    "detection_count": detection_count,
                    "file_count": file_count,
                    "files_with_detections_count": files_with_detections_count,
                    "inventory": inventory,
                    "body_scan_id": body_scan_id,
                    "start_time": start_time,
                    "status": status,
                    "version": version,
                    "detection_categories": detection_categories,
                    "end_time": end_time,
                    "file_results": file_results,
                    "severity": severity,
                },
                result_start_params.ResultStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"has_detections": has_detections}, result_start_params.ResultStartParams
                ),
            ),
            cast_to=NoneType,
        )


class ResultsResourceWithRawResponse:
    def __init__(self, results: ResultsResource) -> None:
        self._results = results

        self.retrieve = to_raw_response_wrapper(
            results.retrieve,
        )
        self.list = to_raw_response_wrapper(
            results.list,
        )
        self.patch = to_raw_response_wrapper(
            results.patch,
        )
        self.start = to_raw_response_wrapper(
            results.start,
        )


class AsyncResultsResourceWithRawResponse:
    def __init__(self, results: AsyncResultsResource) -> None:
        self._results = results

        self.retrieve = async_to_raw_response_wrapper(
            results.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            results.list,
        )
        self.patch = async_to_raw_response_wrapper(
            results.patch,
        )
        self.start = async_to_raw_response_wrapper(
            results.start,
        )


class ResultsResourceWithStreamingResponse:
    def __init__(self, results: ResultsResource) -> None:
        self._results = results

        self.retrieve = to_streamed_response_wrapper(
            results.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            results.list,
        )
        self.patch = to_streamed_response_wrapper(
            results.patch,
        )
        self.start = to_streamed_response_wrapper(
            results.start,
        )


class AsyncResultsResourceWithStreamingResponse:
    def __init__(self, results: AsyncResultsResource) -> None:
        self._results = results

        self.retrieve = async_to_streamed_response_wrapper(
            results.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            results.list,
        )
        self.patch = async_to_streamed_response_wrapper(
            results.patch,
        )
        self.start = async_to_streamed_response_wrapper(
            results.start,
        )
