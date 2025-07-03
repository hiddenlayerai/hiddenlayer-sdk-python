# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.scans import result_list_params, result_retrieve_params
from ..._base_client import make_request_options
from ...types.scans.scan_report import ScanReport
from ...types.scans.result_list_response import ResultListResponse

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
        x_correlation_id: str,
        has_detections: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScanReport:
        """
        Get scan results (SARIF / V3)

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
        extra_headers = {"X-Correlation-Id": x_correlation_id, **(extra_headers or {})}
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
        x_correlation_id: str,
        detection_category: str | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        latest_per_model_version_only: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        model_ids: List[str] | NotGiven = NOT_GIVEN,
        model_name: result_list_params.ModelName | NotGiven = NOT_GIVEN,
        model_version_ids: List[str] | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        scanner_version: str | NotGiven = NOT_GIVEN,
        severity: List[str] | NotGiven = NOT_GIVEN,
        sort: str | NotGiven = NOT_GIVEN,
        source: result_list_params.Source | NotGiven = NOT_GIVEN,
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
        Get scan results (Summaries)

        Args:
          detection_category: filter by a single detection category

          end_time: End Time

          latest_per_model_version_only: only return latest result per model version

          model_ids: Model ID

          model_name: filter by the model name

          model_version_ids: Model Version ID

          scanner_version: filter by version of the scanner

          severity: Severities

          sort: allow sorting by model name, status, severity or created at, ascending (+) or
              the default descending (-)

          source: source of model related to scans

          start_time: Start Time

          status: Statuses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/json; charset=utf-8", **(extra_headers or {})}
        extra_headers = {"X-Correlation-Id": x_correlation_id, **(extra_headers or {})}
        return self._get(
            "/scan/v3/results",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "detection_category": detection_category,
                        "end_time": end_time,
                        "latest_per_model_version_only": latest_per_model_version_only,
                        "limit": limit,
                        "model_ids": model_ids,
                        "model_name": model_name,
                        "model_version_ids": model_version_ids,
                        "offset": offset,
                        "scanner_version": scanner_version,
                        "severity": severity,
                        "sort": sort,
                        "source": source,
                        "start_time": start_time,
                        "status": status,
                    },
                    result_list_params.ResultListParams,
                ),
            ),
            cast_to=ResultListResponse,
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
        x_correlation_id: str,
        has_detections: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScanReport:
        """
        Get scan results (SARIF / V3)

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
        extra_headers = {"X-Correlation-Id": x_correlation_id, **(extra_headers or {})}
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
        x_correlation_id: str,
        detection_category: str | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        latest_per_model_version_only: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        model_ids: List[str] | NotGiven = NOT_GIVEN,
        model_name: result_list_params.ModelName | NotGiven = NOT_GIVEN,
        model_version_ids: List[str] | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        scanner_version: str | NotGiven = NOT_GIVEN,
        severity: List[str] | NotGiven = NOT_GIVEN,
        sort: str | NotGiven = NOT_GIVEN,
        source: result_list_params.Source | NotGiven = NOT_GIVEN,
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
        Get scan results (Summaries)

        Args:
          detection_category: filter by a single detection category

          end_time: End Time

          latest_per_model_version_only: only return latest result per model version

          model_ids: Model ID

          model_name: filter by the model name

          model_version_ids: Model Version ID

          scanner_version: filter by version of the scanner

          severity: Severities

          sort: allow sorting by model name, status, severity or created at, ascending (+) or
              the default descending (-)

          source: source of model related to scans

          start_time: Start Time

          status: Statuses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/json; charset=utf-8", **(extra_headers or {})}
        extra_headers = {"X-Correlation-Id": x_correlation_id, **(extra_headers or {})}
        return await self._get(
            "/scan/v3/results",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "detection_category": detection_category,
                        "end_time": end_time,
                        "latest_per_model_version_only": latest_per_model_version_only,
                        "limit": limit,
                        "model_ids": model_ids,
                        "model_name": model_name,
                        "model_version_ids": model_version_ids,
                        "offset": offset,
                        "scanner_version": scanner_version,
                        "severity": severity,
                        "sort": sort,
                        "source": source,
                        "start_time": start_time,
                        "status": status,
                    },
                    result_list_params.ResultListParams,
                ),
            ),
            cast_to=ResultListResponse,
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


class AsyncResultsResourceWithRawResponse:
    def __init__(self, results: AsyncResultsResource) -> None:
        self._results = results

        self.retrieve = async_to_raw_response_wrapper(
            results.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            results.list,
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


class AsyncResultsResourceWithStreamingResponse:
    def __init__(self, results: AsyncResultsResource) -> None:
        self._results = results

        self.retrieve = async_to_streamed_response_wrapper(
            results.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            results.list,
        )
