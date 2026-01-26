# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .red_team import (
    RedTeamResource,
    AsyncRedTeamResource,
    RedTeamResourceWithRawResponse,
    AsyncRedTeamResourceWithRawResponse,
    RedTeamResourceWithStreamingResponse,
    AsyncRedTeamResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["EvaluationsResource", "AsyncEvaluationsResource"]


class EvaluationsResource(SyncAPIResource):
    @cached_property
    def red_team(self) -> RedTeamResource:
        return RedTeamResource(self._client)

    @cached_property
    def with_raw_response(self) -> EvaluationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EvaluationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return EvaluationsResourceWithStreamingResponse(self)


class AsyncEvaluationsResource(AsyncAPIResource):
    @cached_property
    def red_team(self) -> AsyncRedTeamResource:
        return AsyncRedTeamResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEvaluationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return AsyncEvaluationsResourceWithStreamingResponse(self)


class EvaluationsResourceWithRawResponse:
    def __init__(self, evaluations: EvaluationsResource) -> None:
        self._evaluations = evaluations

    @cached_property
    def red_team(self) -> RedTeamResourceWithRawResponse:
        return RedTeamResourceWithRawResponse(self._evaluations.red_team)


class AsyncEvaluationsResourceWithRawResponse:
    def __init__(self, evaluations: AsyncEvaluationsResource) -> None:
        self._evaluations = evaluations

    @cached_property
    def red_team(self) -> AsyncRedTeamResourceWithRawResponse:
        return AsyncRedTeamResourceWithRawResponse(self._evaluations.red_team)


class EvaluationsResourceWithStreamingResponse:
    def __init__(self, evaluations: EvaluationsResource) -> None:
        self._evaluations = evaluations

    @cached_property
    def red_team(self) -> RedTeamResourceWithStreamingResponse:
        return RedTeamResourceWithStreamingResponse(self._evaluations.red_team)


class AsyncEvaluationsResourceWithStreamingResponse:
    def __init__(self, evaluations: AsyncEvaluationsResource) -> None:
        self._evaluations = evaluations

    @cached_property
    def red_team(self) -> AsyncRedTeamResourceWithStreamingResponse:
        return AsyncRedTeamResourceWithStreamingResponse(self._evaluations.red_team)
