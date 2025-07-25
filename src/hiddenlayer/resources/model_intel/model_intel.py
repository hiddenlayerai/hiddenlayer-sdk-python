# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ModelIntelResource", "AsyncModelIntelResource"]


class ModelIntelResource(SyncAPIResource):
    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ModelIntelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayer-engineering/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ModelIntelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelIntelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayer-engineering/hiddenlayer-sdk-python#with_streaming_response
        """
        return ModelIntelResourceWithStreamingResponse(self)


class AsyncModelIntelResource(AsyncAPIResource):
    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncModelIntelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayer-engineering/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModelIntelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelIntelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayer-engineering/hiddenlayer-sdk-python#with_streaming_response
        """
        return AsyncModelIntelResourceWithStreamingResponse(self)


class ModelIntelResourceWithRawResponse:
    def __init__(self, model_intel: ModelIntelResource) -> None:
        self._model_intel = model_intel

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._model_intel.files)


class AsyncModelIntelResourceWithRawResponse:
    def __init__(self, model_intel: AsyncModelIntelResource) -> None:
        self._model_intel = model_intel

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._model_intel.files)


class ModelIntelResourceWithStreamingResponse:
    def __init__(self, model_intel: ModelIntelResource) -> None:
        self._model_intel = model_intel

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._model_intel.files)


class AsyncModelIntelResourceWithStreamingResponse:
    def __init__(self, model_intel: AsyncModelIntelResource) -> None:
        self._model_intel = model_intel

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._model_intel.files)
