# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.scans import job_list_params, job_request_params, job_retrieve_params
from ..._base_client import make_request_options
from ...types.scans.scan_job import ScanJob
from ...types.scans.scan_report import ScanReport
from ...types.scans.job_list_response import JobListResponse

__all__ = ["JobsResource", "AsyncJobsResource"]


class JobsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return JobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return JobsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        scan_id: str,
        *,
        has_detections: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScanReport:
        """
        Get scan results

        Args:
          has_detections: Filter file_results to only those that have detections (and parents)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        return self._get(
            f"/scan/v3/results/{scan_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"has_detections": has_detections}, job_retrieve_params.JobRetrieveParams),
            ),
            cast_to=ScanReport,
        )

    def list(
        self,
        *,
        compliance_status: List[Literal["COMPLIANT", "NONCOMPLIANT"]] | Omit = omit,
        deep_scan: bool | Omit = omit,
        detection_category: str | Omit = omit,
        end_time: Union[str, datetime] | Omit = omit,
        latest_per_model_version_only: bool | Omit = omit,
        limit: int | Omit = omit,
        model_ids: SequenceNotStr[str] | Omit = omit,
        model_name: job_list_params.ModelName | Omit = omit,
        model_version_ids: SequenceNotStr[str] | Omit = omit,
        offset: int | Omit = omit,
        provider: SequenceNotStr[str] | Omit = omit,
        region: SequenceNotStr[str] | Omit = omit,
        request_source: List[Literal["Hybrid Upload", "API Upload", "Integration", "UI Upload", "AI Asset Discovery"]]
        | Omit = omit,
        scanner_version: str | Omit = omit,
        severity: Literal["critical", "high", "medium", "low", "none", "unknown", "safe"] | Omit = omit,
        sort: str | Omit = omit,
        source: job_list_params.Source | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        status: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobListResponse:
        """
        Get scan results (Summaries)

        Args:
          compliance_status: A comma separated list of rule set evaluation statuses to include

          deep_scan: When true, returns only scans that with files. When false, returns only scans
              without files. When not provided, returns all scans.

          detection_category: filter by a single detection category

          end_time: End Time

          latest_per_model_version_only: only return latest result per model version

          model_ids: Model ID

          model_name: filter by the model name

          model_version_ids: Model Version IDs

          provider: Filter by model provider name

          region: Filter by region of the discovered asset

          request_source: Filter by request source using a comma-separated list

          scanner_version: filter by version of the scanner

          severity: Severities

          sort: allow sorting by model name, status, severity, scan start time, asset region, or
              model provider ascending (+) or the default descending (-)

          source: source of model related to scans

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
                        "compliance_status": compliance_status,
                        "deep_scan": deep_scan,
                        "detection_category": detection_category,
                        "end_time": end_time,
                        "latest_per_model_version_only": latest_per_model_version_only,
                        "limit": limit,
                        "model_ids": model_ids,
                        "model_name": model_name,
                        "model_version_ids": model_version_ids,
                        "offset": offset,
                        "provider": provider,
                        "region": region,
                        "request_source": request_source,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScanJob:
        """
        Scan a remote model

        Args:
          access: Access method for the location of files associated with the scan

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

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return AsyncJobsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        scan_id: str,
        *,
        has_detections: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScanReport:
        """
        Get scan results

        Args:
          has_detections: Filter file_results to only those that have detections (and parents)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        return await self._get(
            f"/scan/v3/results/{scan_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"has_detections": has_detections}, job_retrieve_params.JobRetrieveParams
                ),
            ),
            cast_to=ScanReport,
        )

    async def list(
        self,
        *,
        compliance_status: List[Literal["COMPLIANT", "NONCOMPLIANT"]] | Omit = omit,
        deep_scan: bool | Omit = omit,
        detection_category: str | Omit = omit,
        end_time: Union[str, datetime] | Omit = omit,
        latest_per_model_version_only: bool | Omit = omit,
        limit: int | Omit = omit,
        model_ids: SequenceNotStr[str] | Omit = omit,
        model_name: job_list_params.ModelName | Omit = omit,
        model_version_ids: SequenceNotStr[str] | Omit = omit,
        offset: int | Omit = omit,
        provider: SequenceNotStr[str] | Omit = omit,
        region: SequenceNotStr[str] | Omit = omit,
        request_source: List[Literal["Hybrid Upload", "API Upload", "Integration", "UI Upload", "AI Asset Discovery"]]
        | Omit = omit,
        scanner_version: str | Omit = omit,
        severity: Literal["critical", "high", "medium", "low", "none", "unknown", "safe"] | Omit = omit,
        sort: str | Omit = omit,
        source: job_list_params.Source | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        status: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobListResponse:
        """
        Get scan results (Summaries)

        Args:
          compliance_status: A comma separated list of rule set evaluation statuses to include

          deep_scan: When true, returns only scans that with files. When false, returns only scans
              without files. When not provided, returns all scans.

          detection_category: filter by a single detection category

          end_time: End Time

          latest_per_model_version_only: only return latest result per model version

          model_ids: Model ID

          model_name: filter by the model name

          model_version_ids: Model Version IDs

          provider: Filter by model provider name

          region: Filter by region of the discovered asset

          request_source: Filter by request source using a comma-separated list

          scanner_version: filter by version of the scanner

          severity: Severities

          sort: allow sorting by model name, status, severity, scan start time, asset region, or
              model provider ascending (+) or the default descending (-)

          source: source of model related to scans

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
                        "compliance_status": compliance_status,
                        "deep_scan": deep_scan,
                        "detection_category": detection_category,
                        "end_time": end_time,
                        "latest_per_model_version_only": latest_per_model_version_only,
                        "limit": limit,
                        "model_ids": model_ids,
                        "model_name": model_name,
                        "model_version_ids": model_version_ids,
                        "offset": offset,
                        "provider": provider,
                        "region": region,
                        "request_source": request_source,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScanJob:
        """
        Scan a remote model

        Args:
          access: Access method for the location of files associated with the scan

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

        self.retrieve = to_raw_response_wrapper(
            jobs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            jobs.list,
        )
        self.request = to_raw_response_wrapper(
            jobs.request,
        )


class AsyncJobsResourceWithRawResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.retrieve = async_to_raw_response_wrapper(
            jobs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            jobs.list,
        )
        self.request = async_to_raw_response_wrapper(
            jobs.request,
        )


class JobsResourceWithStreamingResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.retrieve = to_streamed_response_wrapper(
            jobs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            jobs.list,
        )
        self.request = to_streamed_response_wrapper(
            jobs.request,
        )


class AsyncJobsResourceWithStreamingResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.retrieve = async_to_streamed_response_wrapper(
            jobs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            jobs.list,
        )
        self.request = async_to_streamed_response_wrapper(
            jobs.request,
        )
