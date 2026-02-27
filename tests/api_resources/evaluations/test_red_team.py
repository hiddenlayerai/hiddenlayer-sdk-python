# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hiddenlayer import HiddenLayer, AsyncHiddenLayer
from tests.utils import assert_matches_type
from hiddenlayer.types.evaluations import (
    RedTeamCreateResponse,
    RedTeamRetrieveStatusResponse,
    RedTeamRetrieveNextActionResponse,
    RedTeamSubmitTargetResponseResponse,
    RedTeamRetrieveEvaluationResultsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRedTeam:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: HiddenLayer) -> None:
        red_team = client.evaluations.red_team.create(
            name="name",
            target_model="target_model",
        )
        assert_matches_type(RedTeamCreateResponse, red_team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HiddenLayer) -> None:
        red_team = client.evaluations.red_team.create(
            name="name",
            target_model="target_model",
            attacker_max_generation_attempts=0,
            attacker_model="attacker_model",
            evaluation_report_model="evaluation_report_model",
            execution_strategy_type="execution_strategy_type",
            hl_project_id="hl_project_id",
            max_parallel_techniques=0,
            max_turns=0,
            n_random_techniques=0,
            objective_ids=["string"],
            objective_judge_model="objective_judge_model",
            prompt_set_id="prompt_set_id",
            refusal_judge_model="refusal_judge_model",
            sessions_per_technique=0,
            target_system_prompt="target_system_prompt",
        )
        assert_matches_type(RedTeamCreateResponse, red_team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HiddenLayer) -> None:
        response = client.evaluations.red_team.with_raw_response.create(
            name="name",
            target_model="target_model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        red_team = response.parse()
        assert_matches_type(RedTeamCreateResponse, red_team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HiddenLayer) -> None:
        with client.evaluations.red_team.with_streaming_response.create(
            name="name",
            target_model="target_model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            red_team = response.parse()
            assert_matches_type(RedTeamCreateResponse, red_team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_evaluation_results(self, client: HiddenLayer) -> None:
        red_team = client.evaluations.red_team.retrieve_evaluation_results(
            "workflow_id",
        )
        assert_matches_type(RedTeamRetrieveEvaluationResultsResponse, red_team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_evaluation_results(self, client: HiddenLayer) -> None:
        response = client.evaluations.red_team.with_raw_response.retrieve_evaluation_results(
            "workflow_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        red_team = response.parse()
        assert_matches_type(RedTeamRetrieveEvaluationResultsResponse, red_team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_evaluation_results(self, client: HiddenLayer) -> None:
        with client.evaluations.red_team.with_streaming_response.retrieve_evaluation_results(
            "workflow_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            red_team = response.parse()
            assert_matches_type(RedTeamRetrieveEvaluationResultsResponse, red_team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_evaluation_results(self, client: HiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            client.evaluations.red_team.with_raw_response.retrieve_evaluation_results(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_next_action(self, client: HiddenLayer) -> None:
        red_team = client.evaluations.red_team.retrieve_next_action(
            "workflow_id",
        )
        assert_matches_type(RedTeamRetrieveNextActionResponse, red_team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_next_action(self, client: HiddenLayer) -> None:
        response = client.evaluations.red_team.with_raw_response.retrieve_next_action(
            "workflow_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        red_team = response.parse()
        assert_matches_type(RedTeamRetrieveNextActionResponse, red_team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_next_action(self, client: HiddenLayer) -> None:
        with client.evaluations.red_team.with_streaming_response.retrieve_next_action(
            "workflow_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            red_team = response.parse()
            assert_matches_type(RedTeamRetrieveNextActionResponse, red_team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_next_action(self, client: HiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            client.evaluations.red_team.with_raw_response.retrieve_next_action(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_status(self, client: HiddenLayer) -> None:
        red_team = client.evaluations.red_team.retrieve_status(
            "workflow_id",
        )
        assert_matches_type(RedTeamRetrieveStatusResponse, red_team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_status(self, client: HiddenLayer) -> None:
        response = client.evaluations.red_team.with_raw_response.retrieve_status(
            "workflow_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        red_team = response.parse()
        assert_matches_type(RedTeamRetrieveStatusResponse, red_team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_status(self, client: HiddenLayer) -> None:
        with client.evaluations.red_team.with_streaming_response.retrieve_status(
            "workflow_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            red_team = response.parse()
            assert_matches_type(RedTeamRetrieveStatusResponse, red_team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_status(self, client: HiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            client.evaluations.red_team.with_raw_response.retrieve_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_target_response(self, client: HiddenLayer) -> None:
        red_team = client.evaluations.red_team.submit_target_response(
            workflow_id="workflow_id",
            session_id="session_id",
            target_response="target_response",
        )
        assert_matches_type(RedTeamSubmitTargetResponseResponse, red_team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit_target_response(self, client: HiddenLayer) -> None:
        response = client.evaluations.red_team.with_raw_response.submit_target_response(
            workflow_id="workflow_id",
            session_id="session_id",
            target_response="target_response",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        red_team = response.parse()
        assert_matches_type(RedTeamSubmitTargetResponseResponse, red_team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit_target_response(self, client: HiddenLayer) -> None:
        with client.evaluations.red_team.with_streaming_response.submit_target_response(
            workflow_id="workflow_id",
            session_id="session_id",
            target_response="target_response",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            red_team = response.parse()
            assert_matches_type(RedTeamSubmitTargetResponseResponse, red_team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_submit_target_response(self, client: HiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            client.evaluations.red_team.with_raw_response.submit_target_response(
                workflow_id="",
                session_id="session_id",
                target_response="target_response",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_terminate(self, client: HiddenLayer) -> None:
        red_team = client.evaluations.red_team.terminate(
            "workflow_id",
        )
        assert red_team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_terminate(self, client: HiddenLayer) -> None:
        response = client.evaluations.red_team.with_raw_response.terminate(
            "workflow_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        red_team = response.parse()
        assert red_team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_terminate(self, client: HiddenLayer) -> None:
        with client.evaluations.red_team.with_streaming_response.terminate(
            "workflow_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            red_team = response.parse()
            assert red_team is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_terminate(self, client: HiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            client.evaluations.red_team.with_raw_response.terminate(
                "",
            )


class TestAsyncRedTeam:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHiddenLayer) -> None:
        red_team = await async_client.evaluations.red_team.create(
            name="name",
            target_model="target_model",
        )
        assert_matches_type(RedTeamCreateResponse, red_team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHiddenLayer) -> None:
        red_team = await async_client.evaluations.red_team.create(
            name="name",
            target_model="target_model",
            attacker_max_generation_attempts=0,
            attacker_model="attacker_model",
            evaluation_report_model="evaluation_report_model",
            execution_strategy_type="execution_strategy_type",
            hl_project_id="hl_project_id",
            max_parallel_techniques=0,
            max_turns=0,
            n_random_techniques=0,
            objective_ids=["string"],
            objective_judge_model="objective_judge_model",
            prompt_set_id="prompt_set_id",
            refusal_judge_model="refusal_judge_model",
            sessions_per_technique=0,
            target_system_prompt="target_system_prompt",
        )
        assert_matches_type(RedTeamCreateResponse, red_team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.evaluations.red_team.with_raw_response.create(
            name="name",
            target_model="target_model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        red_team = await response.parse()
        assert_matches_type(RedTeamCreateResponse, red_team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.evaluations.red_team.with_streaming_response.create(
            name="name",
            target_model="target_model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            red_team = await response.parse()
            assert_matches_type(RedTeamCreateResponse, red_team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_evaluation_results(self, async_client: AsyncHiddenLayer) -> None:
        red_team = await async_client.evaluations.red_team.retrieve_evaluation_results(
            "workflow_id",
        )
        assert_matches_type(RedTeamRetrieveEvaluationResultsResponse, red_team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_evaluation_results(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.evaluations.red_team.with_raw_response.retrieve_evaluation_results(
            "workflow_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        red_team = await response.parse()
        assert_matches_type(RedTeamRetrieveEvaluationResultsResponse, red_team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_evaluation_results(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.evaluations.red_team.with_streaming_response.retrieve_evaluation_results(
            "workflow_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            red_team = await response.parse()
            assert_matches_type(RedTeamRetrieveEvaluationResultsResponse, red_team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_evaluation_results(self, async_client: AsyncHiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            await async_client.evaluations.red_team.with_raw_response.retrieve_evaluation_results(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_next_action(self, async_client: AsyncHiddenLayer) -> None:
        red_team = await async_client.evaluations.red_team.retrieve_next_action(
            "workflow_id",
        )
        assert_matches_type(RedTeamRetrieveNextActionResponse, red_team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_next_action(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.evaluations.red_team.with_raw_response.retrieve_next_action(
            "workflow_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        red_team = await response.parse()
        assert_matches_type(RedTeamRetrieveNextActionResponse, red_team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_next_action(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.evaluations.red_team.with_streaming_response.retrieve_next_action(
            "workflow_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            red_team = await response.parse()
            assert_matches_type(RedTeamRetrieveNextActionResponse, red_team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_next_action(self, async_client: AsyncHiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            await async_client.evaluations.red_team.with_raw_response.retrieve_next_action(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncHiddenLayer) -> None:
        red_team = await async_client.evaluations.red_team.retrieve_status(
            "workflow_id",
        )
        assert_matches_type(RedTeamRetrieveStatusResponse, red_team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.evaluations.red_team.with_raw_response.retrieve_status(
            "workflow_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        red_team = await response.parse()
        assert_matches_type(RedTeamRetrieveStatusResponse, red_team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.evaluations.red_team.with_streaming_response.retrieve_status(
            "workflow_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            red_team = await response.parse()
            assert_matches_type(RedTeamRetrieveStatusResponse, red_team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_status(self, async_client: AsyncHiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            await async_client.evaluations.red_team.with_raw_response.retrieve_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_target_response(self, async_client: AsyncHiddenLayer) -> None:
        red_team = await async_client.evaluations.red_team.submit_target_response(
            workflow_id="workflow_id",
            session_id="session_id",
            target_response="target_response",
        )
        assert_matches_type(RedTeamSubmitTargetResponseResponse, red_team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit_target_response(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.evaluations.red_team.with_raw_response.submit_target_response(
            workflow_id="workflow_id",
            session_id="session_id",
            target_response="target_response",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        red_team = await response.parse()
        assert_matches_type(RedTeamSubmitTargetResponseResponse, red_team, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit_target_response(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.evaluations.red_team.with_streaming_response.submit_target_response(
            workflow_id="workflow_id",
            session_id="session_id",
            target_response="target_response",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            red_team = await response.parse()
            assert_matches_type(RedTeamSubmitTargetResponseResponse, red_team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_submit_target_response(self, async_client: AsyncHiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            await async_client.evaluations.red_team.with_raw_response.submit_target_response(
                workflow_id="",
                session_id="session_id",
                target_response="target_response",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_terminate(self, async_client: AsyncHiddenLayer) -> None:
        red_team = await async_client.evaluations.red_team.terminate(
            "workflow_id",
        )
        assert red_team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_terminate(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.evaluations.red_team.with_raw_response.terminate(
            "workflow_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        red_team = await response.parse()
        assert red_team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_terminate(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.evaluations.red_team.with_streaming_response.terminate(
            "workflow_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            red_team = await response.parse()
            assert red_team is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_terminate(self, async_client: AsyncHiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_id` but received ''"):
            await async_client.evaluations.red_team.with_raw_response.terminate(
                "",
            )
