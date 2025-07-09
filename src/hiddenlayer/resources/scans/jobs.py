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
from ...types.scans import job_list_params, job_request_params
from ..._base_client import make_request_options
from ...types.scans.scan_job import ScanJob
from ...types.scans.job_list_response import JobListResponse

__all__ = ["JobsResource", "AsyncJobsResource"]


class JobsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return JobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hiddenlayer-sdk-python#with_streaming_response
        """
        return JobsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        x_correlation_id: str,
        detection_category: str | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        latest_per_model_version_only: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        model_ids: List[str] | NotGiven = NOT_GIVEN,
        model_name: job_list_params.ModelName | NotGiven = NOT_GIVEN,
        model_version_ids: List[str] | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        scanner_version: str | NotGiven = NOT_GIVEN,
        severity: List[str] | NotGiven = NOT_GIVEN,
        sort: str | NotGiven = NOT_GIVEN,
        source: job_list_params.Source | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobListResponse:
        """
        Get scan results (Summaries)

        Args:
          detection_category: filter by a single detection category

          end_time: End Time

          latest_per_model_version_only: only return latest result per model version

          model_ids: Model ID

          model_name: filter by the model name

          model_version_ids: Model Version IDs

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
                    job_list_params.JobListParams,
                ),
            ),
            cast_to=JobListResponse,
        )

    def request(
        self,
        *,
        access: job_request_params.Access,
        inventory: job_request_params.Inventory,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScanJob:
        """
        Scan a remote model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/scan/v3/jobs",
            body=maybe_transform(
                {
                    "access": access,
                    "inventory": inventory,
                },
                job_request_params.JobRequestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScanJob,
        )


class AsyncJobsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hiddenlayer-sdk-python#with_streaming_response
        """
        return AsyncJobsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        x_correlation_id: str,
        detection_category: str | NotGiven = NOT_GIVEN,
        end_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        latest_per_model_version_only: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        model_ids: List[str] | NotGiven = NOT_GIVEN,
        model_name: job_list_params.ModelName | NotGiven = NOT_GIVEN,
        model_version_ids: List[str] | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        scanner_version: str | NotGiven = NOT_GIVEN,
        severity: List[str] | NotGiven = NOT_GIVEN,
        sort: str | NotGiven = NOT_GIVEN,
        source: job_list_params.Source | NotGiven = NOT_GIVEN,
        start_time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobListResponse:
        """
        Get scan results (Summaries)

        Args:
          detection_category: filter by a single detection category

          end_time: End Time

          latest_per_model_version_only: only return latest result per model version

          model_ids: Model ID

          model_name: filter by the model name

          model_version_ids: Model Version IDs

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
                    job_list_params.JobListParams,
                ),
            ),
            cast_to=JobListResponse,
        )

    async def request(
        self,
        *,
        access: job_request_params.Access,
        inventory: job_request_params.Inventory,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScanJob:
        """
        Scan a remote model

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/scan/v3/jobs",
            body=await async_maybe_transform(
                {
                    "access": access,
                    "inventory": inventory,
                },
                job_request_params.JobRequestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScanJob,
        )


class JobsResourceWithRawResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.list = to_raw_response_wrapper(
            jobs.list,
        )
        self.request = to_raw_response_wrapper(
            jobs.request,
        )


class AsyncJobsResourceWithRawResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.list = async_to_raw_response_wrapper(
            jobs.list,
        )
        self.request = async_to_raw_response_wrapper(
            jobs.request,
        )


class JobsResourceWithStreamingResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.list = to_streamed_response_wrapper(
            jobs.list,
        )
        self.request = to_streamed_response_wrapper(
            jobs.request,
        )


class AsyncJobsResourceWithStreamingResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.list = async_to_streamed_response_wrapper(
            jobs.list,
        )
        self.request = async_to_streamed_response_wrapper(
            jobs.request,
        )
