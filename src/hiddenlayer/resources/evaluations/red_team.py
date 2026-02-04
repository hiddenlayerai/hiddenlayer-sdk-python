# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.evaluations import red_team_create_params, red_team_submit_target_response_params
from ...types.evaluations.red_team_create_response import RedTeamCreateResponse
from ...types.evaluations.red_team_retrieve_status_response import RedTeamRetrieveStatusResponse
from ...types.evaluations.red_team_retrieve_next_action_response import RedTeamRetrieveNextActionResponse
from ...types.evaluations.red_team_submit_target_response_response import RedTeamSubmitTargetResponseResponse
from ...types.evaluations.red_team_retrieve_evaluation_results_response import RedTeamRetrieveEvaluationResultsResponse

__all__ = ["RedTeamResource", "AsyncRedTeamResource"]


class RedTeamResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RedTeamResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RedTeamResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RedTeamResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return RedTeamResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        target_model: str,
        attacker_max_generation_attempts: int | Omit = omit,
        attacker_model: str | Omit = omit,
        evaluation_report_model: str | Omit = omit,
        execution_strategy_type: str | Omit = omit,
        hl_project_id: str | Omit = omit,
        max_parallel_techniques: int | Omit = omit,
        max_turns: int | Omit = omit,
        n_random_techniques: int | Omit = omit,
        objective_ids: SequenceNotStr[str] | Omit = omit,
        objective_judge_model: str | Omit = omit,
        prompt_set_id: str | Omit = omit,
        refusal_judge_model: str | Omit = omit,
        sessions_per_technique: int | Omit = omit,
        target_system_prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamCreateResponse:
        """Start a new red team client workflow.

        Auto-triggers planning phase. Client
        should then poll /next-action.

        Args:
          name: Name for this evaluation

          target_model: Target model identifier

          attacker_max_generation_attempts: Maximum generation attempts for attacker

          attacker_model: Model for attacker

          evaluation_report_model: Model for evaluation report

          execution_strategy_type: Execution strategy type

          hl_project_id: HiddenLayer project ID

          max_parallel_techniques: Maximum parallel techniques

          max_turns: Maximum conversation turns

          n_random_techniques: Number of random techniques to use

          objective_ids: Objective IDs to evaluate

          objective_judge_model: Model for objective judging

          prompt_set_id: Prompt set ID for static prompt evaluation

          refusal_judge_model: Model for refusal judging

          sessions_per_technique: Number of sessions per technique

          target_system_prompt: System prompt for the target

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/evaluations/v1-beta/red-team",
            body=maybe_transform(
                {
                    "name": name,
                    "target_model": target_model,
                    "attacker_max_generation_attempts": attacker_max_generation_attempts,
                    "attacker_model": attacker_model,
                    "evaluation_report_model": evaluation_report_model,
                    "execution_strategy_type": execution_strategy_type,
                    "hl_project_id": hl_project_id,
                    "max_parallel_techniques": max_parallel_techniques,
                    "max_turns": max_turns,
                    "n_random_techniques": n_random_techniques,
                    "objective_ids": objective_ids,
                    "objective_judge_model": objective_judge_model,
                    "prompt_set_id": prompt_set_id,
                    "refusal_judge_model": refusal_judge_model,
                    "sessions_per_technique": sessions_per_technique,
                    "target_system_prompt": target_system_prompt,
                },
                red_team_create_params.RedTeamCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedTeamCreateResponse,
        )

    def retrieve_evaluation_results(
        self,
        workflow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamRetrieveEvaluationResultsResponse:
        """
        Get the complete result of a red team workflow.

        Args:
          workflow_id: The workflow identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        return self._get(
            f"/evaluations/v1-beta/red-team/{workflow_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedTeamRetrieveEvaluationResultsResponse,
        )

    def retrieve_next_action(
        self,
        workflow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamRetrieveNextActionResponse:
        """
        Poll for next action - CLIENT'S MAIN POLLING ENDPOINT.

        This endpoint is designed to be polled repeatedly by the client. Returns
        immediately with current state:

        - If attack ready: Returns attack_task with prompt
        - If processing: Returns processing=true (client continues polling)
        - If complete: Returns action_type=complete

        Args:
          workflow_id: The workflow identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        return self._get(
            f"/evaluations/v1-beta/red-team/{workflow_id}/next-action",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedTeamRetrieveNextActionResponse,
        )

    def retrieve_status(
        self,
        workflow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamRetrieveStatusResponse:
        """
        Get current status of a red team workflow.

        Args:
          workflow_id: The workflow identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        return self._get(
            f"/evaluations/v1-beta/red-team/{workflow_id}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedTeamRetrieveStatusResponse,
        )

    def submit_target_response(
        self,
        workflow_id: str,
        *,
        session_id: str,
        target_response: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamSubmitTargetResponseResponse:
        """
        Submit target's response.

        This triggers the ProcessTargetResponseWorkflow child workflow for the specified
        session. Returns immediately.

        Args:
          workflow_id: The workflow identifier

          session_id: Session identifier

          target_response: Target's response text

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        return self._post(
            f"/evaluations/v1-beta/red-team/{workflow_id}/target-response",
            body=maybe_transform(
                {
                    "session_id": session_id,
                    "target_response": target_response,
                },
                red_team_submit_target_response_params.RedTeamSubmitTargetResponseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedTeamSubmitTargetResponseResponse,
        )

    def terminate(
        self,
        workflow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Terminate a running workflow.

        Args:
          workflow_id: The workflow identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/evaluations/v1-beta/red-team/terminations/{workflow_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncRedTeamResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRedTeamResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRedTeamResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRedTeamResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hiddenlayerai/hiddenlayer-sdk-python#with_streaming_response
        """
        return AsyncRedTeamResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        target_model: str,
        attacker_max_generation_attempts: int | Omit = omit,
        attacker_model: str | Omit = omit,
        evaluation_report_model: str | Omit = omit,
        execution_strategy_type: str | Omit = omit,
        hl_project_id: str | Omit = omit,
        max_parallel_techniques: int | Omit = omit,
        max_turns: int | Omit = omit,
        n_random_techniques: int | Omit = omit,
        objective_ids: SequenceNotStr[str] | Omit = omit,
        objective_judge_model: str | Omit = omit,
        prompt_set_id: str | Omit = omit,
        refusal_judge_model: str | Omit = omit,
        sessions_per_technique: int | Omit = omit,
        target_system_prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamCreateResponse:
        """Start a new red team client workflow.

        Auto-triggers planning phase. Client
        should then poll /next-action.

        Args:
          name: Name for this evaluation

          target_model: Target model identifier

          attacker_max_generation_attempts: Maximum generation attempts for attacker

          attacker_model: Model for attacker

          evaluation_report_model: Model for evaluation report

          execution_strategy_type: Execution strategy type

          hl_project_id: HiddenLayer project ID

          max_parallel_techniques: Maximum parallel techniques

          max_turns: Maximum conversation turns

          n_random_techniques: Number of random techniques to use

          objective_ids: Objective IDs to evaluate

          objective_judge_model: Model for objective judging

          prompt_set_id: Prompt set ID for static prompt evaluation

          refusal_judge_model: Model for refusal judging

          sessions_per_technique: Number of sessions per technique

          target_system_prompt: System prompt for the target

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/evaluations/v1-beta/red-team",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "target_model": target_model,
                    "attacker_max_generation_attempts": attacker_max_generation_attempts,
                    "attacker_model": attacker_model,
                    "evaluation_report_model": evaluation_report_model,
                    "execution_strategy_type": execution_strategy_type,
                    "hl_project_id": hl_project_id,
                    "max_parallel_techniques": max_parallel_techniques,
                    "max_turns": max_turns,
                    "n_random_techniques": n_random_techniques,
                    "objective_ids": objective_ids,
                    "objective_judge_model": objective_judge_model,
                    "prompt_set_id": prompt_set_id,
                    "refusal_judge_model": refusal_judge_model,
                    "sessions_per_technique": sessions_per_technique,
                    "target_system_prompt": target_system_prompt,
                },
                red_team_create_params.RedTeamCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedTeamCreateResponse,
        )

    async def retrieve_evaluation_results(
        self,
        workflow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamRetrieveEvaluationResultsResponse:
        """
        Get the complete result of a red team workflow.

        Args:
          workflow_id: The workflow identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        return await self._get(
            f"/evaluations/v1-beta/red-team/{workflow_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedTeamRetrieveEvaluationResultsResponse,
        )

    async def retrieve_next_action(
        self,
        workflow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamRetrieveNextActionResponse:
        """
        Poll for next action - CLIENT'S MAIN POLLING ENDPOINT.

        This endpoint is designed to be polled repeatedly by the client. Returns
        immediately with current state:

        - If attack ready: Returns attack_task with prompt
        - If processing: Returns processing=true (client continues polling)
        - If complete: Returns action_type=complete

        Args:
          workflow_id: The workflow identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        return await self._get(
            f"/evaluations/v1-beta/red-team/{workflow_id}/next-action",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedTeamRetrieveNextActionResponse,
        )

    async def retrieve_status(
        self,
        workflow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamRetrieveStatusResponse:
        """
        Get current status of a red team workflow.

        Args:
          workflow_id: The workflow identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        return await self._get(
            f"/evaluations/v1-beta/red-team/{workflow_id}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedTeamRetrieveStatusResponse,
        )

    async def submit_target_response(
        self,
        workflow_id: str,
        *,
        session_id: str,
        target_response: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamSubmitTargetResponseResponse:
        """
        Submit target's response.

        This triggers the ProcessTargetResponseWorkflow child workflow for the specified
        session. Returns immediately.

        Args:
          workflow_id: The workflow identifier

          session_id: Session identifier

          target_response: Target's response text

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        return await self._post(
            f"/evaluations/v1-beta/red-team/{workflow_id}/target-response",
            body=await async_maybe_transform(
                {
                    "session_id": session_id,
                    "target_response": target_response,
                },
                red_team_submit_target_response_params.RedTeamSubmitTargetResponseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RedTeamSubmitTargetResponseResponse,
        )

    async def terminate(
        self,
        workflow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Terminate a running workflow.

        Args:
          workflow_id: The workflow identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/evaluations/v1-beta/red-team/terminations/{workflow_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class RedTeamResourceWithRawResponse:
    def __init__(self, red_team: RedTeamResource) -> None:
        self._red_team = red_team

        self.create = to_raw_response_wrapper(
            red_team.create,
        )
        self.retrieve_evaluation_results = to_raw_response_wrapper(
            red_team.retrieve_evaluation_results,
        )
        self.retrieve_next_action = to_raw_response_wrapper(
            red_team.retrieve_next_action,
        )
        self.retrieve_status = to_raw_response_wrapper(
            red_team.retrieve_status,
        )
        self.submit_target_response = to_raw_response_wrapper(
            red_team.submit_target_response,
        )
        self.terminate = to_raw_response_wrapper(
            red_team.terminate,
        )


class AsyncRedTeamResourceWithRawResponse:
    def __init__(self, red_team: AsyncRedTeamResource) -> None:
        self._red_team = red_team

        self.create = async_to_raw_response_wrapper(
            red_team.create,
        )
        self.retrieve_evaluation_results = async_to_raw_response_wrapper(
            red_team.retrieve_evaluation_results,
        )
        self.retrieve_next_action = async_to_raw_response_wrapper(
            red_team.retrieve_next_action,
        )
        self.retrieve_status = async_to_raw_response_wrapper(
            red_team.retrieve_status,
        )
        self.submit_target_response = async_to_raw_response_wrapper(
            red_team.submit_target_response,
        )
        self.terminate = async_to_raw_response_wrapper(
            red_team.terminate,
        )


class RedTeamResourceWithStreamingResponse:
    def __init__(self, red_team: RedTeamResource) -> None:
        self._red_team = red_team

        self.create = to_streamed_response_wrapper(
            red_team.create,
        )
        self.retrieve_evaluation_results = to_streamed_response_wrapper(
            red_team.retrieve_evaluation_results,
        )
        self.retrieve_next_action = to_streamed_response_wrapper(
            red_team.retrieve_next_action,
        )
        self.retrieve_status = to_streamed_response_wrapper(
            red_team.retrieve_status,
        )
        self.submit_target_response = to_streamed_response_wrapper(
            red_team.submit_target_response,
        )
        self.terminate = to_streamed_response_wrapper(
            red_team.terminate,
        )


class AsyncRedTeamResourceWithStreamingResponse:
    def __init__(self, red_team: AsyncRedTeamResource) -> None:
        self._red_team = red_team

        self.create = async_to_streamed_response_wrapper(
            red_team.create,
        )
        self.retrieve_evaluation_results = async_to_streamed_response_wrapper(
            red_team.retrieve_evaluation_results,
        )
        self.retrieve_next_action = async_to_streamed_response_wrapper(
            red_team.retrieve_next_action,
        )
        self.retrieve_status = async_to_streamed_response_wrapper(
            red_team.retrieve_status,
        )
        self.submit_target_response = async_to_streamed_response_wrapper(
            red_team.submit_target_response,
        )
        self.terminate = async_to_streamed_response_wrapper(
            red_team.terminate,
        )
