# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from .results import (
    ResultsResource,
    AsyncResultsResource,
    ResultsResourceWithRawResponse,
    AsyncResultsResourceWithRawResponse,
    ResultsResourceWithStreamingResponse,
    AsyncResultsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .upload.upload import (
    UploadResource,
    AsyncUploadResource,
    UploadResourceWithRawResponse,
    AsyncUploadResourceWithRawResponse,
    UploadResourceWithStreamingResponse,
    AsyncUploadResourceWithStreamingResponse,
)

__all__ = ["ScansResource", "AsyncScansResource"]


class ScansResource(SyncAPIResource):
    @cached_property
    def results(self) -> ResultsResource:
        return ResultsResource(self._client)

    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def upload(self) -> UploadResource:
        return UploadResource(self._client)

    @cached_property
    def with_raw_response(self) -> ScansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ScansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return ScansResourceWithStreamingResponse(self)


class AsyncScansResource(AsyncAPIResource):
    @cached_property
    def results(self) -> AsyncResultsResource:
        return AsyncResultsResource(self._client)

    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def upload(self) -> AsyncUploadResource:
        return AsyncUploadResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncScansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return AsyncScansResourceWithStreamingResponse(self)


class ScansResourceWithRawResponse:
    def __init__(self, scans: ScansResource) -> None:
        self._scans = scans

    @cached_property
    def results(self) -> ResultsResourceWithRawResponse:
        return ResultsResourceWithRawResponse(self._scans.results)

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._scans.jobs)

    @cached_property
    def upload(self) -> UploadResourceWithRawResponse:
        return UploadResourceWithRawResponse(self._scans.upload)


class AsyncScansResourceWithRawResponse:
    def __init__(self, scans: AsyncScansResource) -> None:
        self._scans = scans

    @cached_property
    def results(self) -> AsyncResultsResourceWithRawResponse:
        return AsyncResultsResourceWithRawResponse(self._scans.results)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._scans.jobs)

    @cached_property
    def upload(self) -> AsyncUploadResourceWithRawResponse:
        return AsyncUploadResourceWithRawResponse(self._scans.upload)


class ScansResourceWithStreamingResponse:
    def __init__(self, scans: ScansResource) -> None:
        self._scans = scans

    @cached_property
    def results(self) -> ResultsResourceWithStreamingResponse:
        return ResultsResourceWithStreamingResponse(self._scans.results)

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._scans.jobs)

    @cached_property
    def upload(self) -> UploadResourceWithStreamingResponse:
        return UploadResourceWithStreamingResponse(self._scans.upload)


class AsyncScansResourceWithStreamingResponse:
    def __init__(self, scans: AsyncScansResource) -> None:
        self._scans = scans

    @cached_property
    def results(self) -> AsyncResultsResourceWithStreamingResponse:
        return AsyncResultsResourceWithStreamingResponse(self._scans.results)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._scans.jobs)

    @cached_property
    def upload(self) -> AsyncUploadResourceWithStreamingResponse:
        return AsyncUploadResourceWithStreamingResponse(self._scans.upload)
