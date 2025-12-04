# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.models import card_list_params
from ...types.models.card_list_response import CardListResponse

__all__ = ["CardsResource", "AsyncCardsResource"]


class CardsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return CardsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        aidr_severity: List[Literal["SAFE", "UNSAFE", "SUSPICIOUS"]] | Omit = omit,
        aidr_status: Literal["ENABLED", "DISABLED", "ANY"] | Omit = omit,
        limit: int | Omit = omit,
        model_created: card_list_params.ModelCreated | Omit = omit,
        model_name: card_list_params.ModelName | Omit = omit,
        modscan_severity: List[
            Literal[
                "SAFE",
                "UNSAFE",
                "SUSPICIOUS",
                "UNKNOWN",
                "ERROR",
                "critical",
                "high",
                "medium",
                "low",
                "none",
                "unknown",
            ]
        ]
        | Omit = omit,
        modscan_status: Literal["ENABLED", "DISABLED", "ANY"] | Omit = omit,
        offset: int | Omit = omit,
        provider: List[Literal["AZURE", "ADHOC"]] | Omit = omit,
        sort: str | Omit = omit,
        source: card_list_params.Source | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPage[CardListResponse]:
        """
        List Model Cards

        Args:
          aidr_severity: Deprecated - use ModelCardAIDRThreatLevel(aidr_threat_level) instead

          aidr_status: filter by aidr enabled

          limit: Limit the number of items returned

          model_created: match on models created between dates

          model_name: substring match on model name

          offset: Begin returning the results from this offset

          sort: allow sorting by model name or created at timestamp, ascending (+) or the
              default descending (-)

          source: substring and full match on model source

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/models/v4/cards",
            page=SyncOffsetPage[CardListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "aidr_severity": aidr_severity,
                        "aidr_status": aidr_status,
                        "limit": limit,
                        "model_created": model_created,
                        "model_name": model_name,
                        "modscan_severity": modscan_severity,
                        "modscan_status": modscan_status,
                        "offset": offset,
                        "provider": provider,
                        "sort": sort,
                        "source": source,
                    },
                    card_list_params.CardListParams,
                ),
            ),
            model=CardListResponse,
        )


class AsyncCardsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return AsyncCardsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        aidr_severity: List[Literal["SAFE", "UNSAFE", "SUSPICIOUS"]] | Omit = omit,
        aidr_status: Literal["ENABLED", "DISABLED", "ANY"] | Omit = omit,
        limit: int | Omit = omit,
        model_created: card_list_params.ModelCreated | Omit = omit,
        model_name: card_list_params.ModelName | Omit = omit,
        modscan_severity: List[
            Literal[
                "SAFE",
                "UNSAFE",
                "SUSPICIOUS",
                "UNKNOWN",
                "ERROR",
                "critical",
                "high",
                "medium",
                "low",
                "none",
                "unknown",
            ]
        ]
        | Omit = omit,
        modscan_status: Literal["ENABLED", "DISABLED", "ANY"] | Omit = omit,
        offset: int | Omit = omit,
        provider: List[Literal["AZURE", "ADHOC"]] | Omit = omit,
        sort: str | Omit = omit,
        source: card_list_params.Source | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CardListResponse, AsyncOffsetPage[CardListResponse]]:
        """
        List Model Cards

        Args:
          aidr_severity: Deprecated - use ModelCardAIDRThreatLevel(aidr_threat_level) instead

          aidr_status: filter by aidr enabled

          limit: Limit the number of items returned

          model_created: match on models created between dates

          model_name: substring match on model name

          offset: Begin returning the results from this offset

          sort: allow sorting by model name or created at timestamp, ascending (+) or the
              default descending (-)

          source: substring and full match on model source

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/models/v4/cards",
            page=AsyncOffsetPage[CardListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "aidr_severity": aidr_severity,
                        "aidr_status": aidr_status,
                        "limit": limit,
                        "model_created": model_created,
                        "model_name": model_name,
                        "modscan_severity": modscan_severity,
                        "modscan_status": modscan_status,
                        "offset": offset,
                        "provider": provider,
                        "sort": sort,
                        "source": source,
                    },
                    card_list_params.CardListParams,
                ),
            ),
            model=CardListResponse,
        )


class CardsResourceWithRawResponse:
    def __init__(self, cards: CardsResource) -> None:
        self._cards = cards

        self.list = to_raw_response_wrapper(
            cards.list,
        )


class AsyncCardsResourceWithRawResponse:
    def __init__(self, cards: AsyncCardsResource) -> None:
        self._cards = cards

        self.list = async_to_raw_response_wrapper(
            cards.list,
        )


class CardsResourceWithStreamingResponse:
    def __init__(self, cards: CardsResource) -> None:
        self._cards = cards

        self.list = to_streamed_response_wrapper(
            cards.list,
        )


class AsyncCardsResourceWithStreamingResponse:
    def __init__(self, cards: AsyncCardsResource) -> None:
        self._cards = cards

        self.list = async_to_streamed_response_wrapper(
            cards.list,
        )
