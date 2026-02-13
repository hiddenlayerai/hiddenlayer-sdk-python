from __future__ import annotations

import time
import asyncio
import logging
from typing import TYPE_CHECKING, Any, Callable, Iterator, Awaitable, AsyncIterator

import httpx

from .._resource import SyncAPIResource, AsyncAPIResource
from ..types.evaluations import RedTeamCreateResponse, RedTeamRetrieveNextActionResponse
from .red_team_exceptions import PollTimeoutError, InvalidSessionError, RedTeamSessionError, WorkflowNotFoundError

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from .._client import HiddenLayer, AsyncHiddenLayer

class RedTeamSession:
    """Represents an active red team session (async-only).

    Usage:
        async for action in session.iterate_actions():
            ...
    Or:
        await session.run_with_callback(handler)
    Or:
        await session.run_with_callback_parallel(handler)
    """

    def __init__(
        self,
        client: HiddenLayer,
        workflow_id: str,
        name: str,
        poll_interval: float = 2.0,
        poll_max_wait: float | None = None,
        max_parallel_techniques: int = 1,
    ):
        self._client = client
        self._workflow_id = workflow_id
        self._name = name
        self._poll_interval = poll_interval
        self._poll_max_wait = poll_max_wait
        self._max_parallel_techniques = max_parallel_techniques
        self._start_monotonic = time.time()
        self._last_action: RedTeamRetrieveNextActionResponse | None = None

    @property
    def workflow_id(self) -> str:
        return self._workflow_id

    @property
    def name(self) -> str:
        return self._name

    def _check_timeout(self) -> None:
        if self._poll_max_wait is not None:
            elapsed = time.time() - self._start_monotonic
            if elapsed > self._poll_max_wait:
                raise Exception(
                    f"Polling timed out after {elapsed:.1f}s (max: {self._poll_max_wait}s)"
                )


    def get_next_action(self, *, block: bool = True) -> RedTeamRetrieveNextActionResponse:
        """Sync poll for next action."""
        while True:
            self._check_timeout()
            try:
                action = self._client.evaluations.red_team.retrieve_next_action(self._workflow_id)
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 404:
                    raise WorkflowNotFoundError(
                        f"Workflow not found: {self._workflow_id}"
                    ) from e
                if e.response.status_code == 500:
                    try:
                        status = self._client.evaluations.red_team.retrieve_status(self._workflow_id)
                        workflow_status = status.status
                        raise RedTeamSessionError(
                            f"Server error getting next action. "
                            f"Workflow status: {workflow_status}. "
                            f"Workflow ID: {self._workflow_id}"
                        ) from e
                    except Exception:
                        # If status check also fails, raise original error
                        raise RedTeamSessionError(
                            f"Server error getting next action "
                            f"for workflow {self._workflow_id}. "
                            f"The workflow may be in a bad state. "
                            f"Try checking the workflow status or restarting."
                        ) from e
                raise

            self._last_action = action

            if action.is_ready or not block:
                return action

            time.sleep(self._poll_interval)

    def wait_for_completion(
        self,
        poll_interval: float = 3.0,
        max_wait: float | None = 300.0,
        verbose: bool = False,
    ) -> None:
        """Poll status until workflow reaches terminal state.

        This method is automatically called by run_with_callback() and
        run_with_callback_parallel() to ensure the workflow has fully completed
        before returning.

        Args:
            poll_interval: How often to check status (default: 3.0s)
            max_wait: Maximum time to wait for completion (default: 300s / 5 min)
            verbose: If True, print status updates (default: False)

        Raises:
            PollTimeoutError: If max_wait is exceeded
            RedTeamSessionError: If workflow fails
        """
        start_time = time.time()
        terminal_states = {
            "COMPLETED",
            "FAILED",
            "CANCELLED",
            "TERMINATED",
            "TIMED_OUT",
        }

        if verbose:
            logger.info(f"⏳ Waiting for workflow {self._workflow_id[:8]}... to complete...")

        while True:
            # Check timeout
            if max_wait is not None:
                elapsed = time.time() - start_time
                if elapsed > max_wait:
                    raise PollTimeoutError(f"Workflow did not complete within {max_wait}s")

            try:
                status = self._client.evaluations.red_team.retrieve_status(self._workflow_id)
                workflow_status = status.status

                if workflow_status in terminal_states:
                    if workflow_status == "FAILED":
                        error_msg = status.error
                        raise RedTeamSessionError(f"Workflow failed: {error_msg}")

                    # Workflow is complete
                    if verbose:
                        elapsed = asyncio.get_event_loop().time() - start_time
                        logger.info(f"✅ Workflow completed in {elapsed:.1f}s.")
                    return

            except httpx.HTTPStatusError as e:
                # If we get 404, workflow doesn't exist
                if e.response.status_code == 404:
                    raise WorkflowNotFoundError(
                        f"Workflow not found: {self._workflow_id}"
                    ) from e
                # For other errors, keep retrying unless we're at max_wait
                if max_wait is not None:
                    elapsed = asyncio.get_event_loop().time() - start_time
                    if elapsed > max_wait:
                        raise

            time.sleep(poll_interval)

    def iterate_actions(self) -> Iterator[RedTeamRetrieveNextActionResponse]:
        """Yield attack_task actions until workflow completes/fails."""
        while True:
            action = self.get_next_action(block=True)

            if action.action_type == "complete":
                return
            if action.action_type == "failed":
                raise RedTeamSessionError(action.message if action.message else "Workflow failed")
            if action.is_ready and action.action_type == "attack_task":
                yield action

    def run_with_callback(
        self,
        handler: Callable[[str | None, list[dict[str, Any]] | None, str | None, str | None], str],
    ) -> None:
        """Run session with sequential action processing.

        Args:
            handler: Sync function that takes
                (attack_prompt, history, session_id, target_system_prompt)
                and returns target response
        """
        for action in self.iterate_actions():
            attack_prompt = action.attack_prompt
            history = action.history
            # TODO: the API should be updated to make this field mandatory in responses
            # TODO: since it is required downstream
            session_id = action.session_id if action.session_id else ""
            target_system_prompt = action.target_system_prompt
            target_response = handler(
                attack_prompt, history, session_id, target_system_prompt
            )
            self._client.evaluations.red_team.submit_target_response(
                workflow_id=self._workflow_id,
                session_id=session_id,
                target_response=target_response)
        # Wait for workflow to fully complete
        return self.wait_for_completion()


class RedTeamSessionsResource(SyncAPIResource):
    _available_objective_ids = ["HLO.01", "HLO.02", "HLO.03", "HLO.05", "HLO.07"]

    def __init__(
            self,
            client: HiddenLayer,
            *,
            default_refusal_judge_model: str = "openai/gpt-5-mini",
            default_objective_judge_model: str = "openai/gpt-5",
            default_attacker_model: str = "openai/gpt-5",
            default_evaluation_report_model: str = "openai/gpt-5",
    ):
        # Default models for red team evaluations
        self._default_refusal_judge_model = default_refusal_judge_model
        self._default_objective_judge_model = default_objective_judge_model
        self._default_attacker_model = default_attacker_model
        self._default_evaluation_report_model = default_evaluation_report_model
        super().__init__(client)

    def start_session(
            self,
            *,
            name: str,
            objective_ids: list[str] | None = None,
            target_model: str,
            target_system_prompt: str = "",
            refusal_judge_model: str | None = None,
            objective_judge_model: str | None = None,
            attacker_model: str | None = None,
            evaluation_report_model: str | None = None,
            max_turns: int = 3,
            execution_strategy_type: str = "random",
            attacker_max_generation_attempts: int = 2,
            n_random_techniques: int = 1,
            max_parallel_techniques: int = 1,
            prompt_set_id: str = "",
            hiddenlayer_project_id: str | None = None,
            poll_interval: float = 2.0,
            poll_max_wait: float | None = None,
            sessions_per_technique: int | None = 1,
    ) -> RedTeamSession:
        """Start a new red team session.

        Supports two modes:

        V1 Mode (objective-specific with short-circuit):
            - Provide objective_ids (required)
            - Do not set sessions_per_technique
            - Each session tests one objective and short-circuits on success

        V2 Mode (objective-agnostic adaptive):
            - Set sessions_per_technique (e.g., 3)
            - objective_ids optional (defaults to all available)
            - Each session tests all objectives, runs to max_turns
            - Adaptive attacker with cross-session state

        Args:
            name: Session name
            objective_ids: List of objective IDs to test (e.g., ["HLO.03"])
                V1: Required. V2: Optional (defaults to all available)
            target_model: Model identifier for the target being tested
            target_system_prompt: System prompt for the target model
            refusal_judge_model: Model to use for refusal judging
                (defaults to client default)
            objective_judge_model: Model to use for objective judging
                (defaults to client default)
            attacker_model: Model to use for generating attacks (defaults to client default)
            evaluation_report_model: Model to use for evaluation reports
                (defaults to client default)
            max_turns: Maximum conversation turns per session
            execution_strategy_type: Strategy type ("single", "random", or "static_prompt_set")
            attacker_max_generation_attempts: Max attempts for attacker to generate prompts
            n_random_techniques: Number of techniques to select per turn
            max_parallel_techniques: Number of techniques to run in parallel
            prompt_set_id: ID of prompt set (if using static_prompt_set strategy)
            hiddenlayer_project_id: Optional HiddenLayer project ID
            poll_interval: How often to poll for actions (seconds, default: 2.0s)
            poll_max_wait: Maximum time to wait for actions (seconds)
            sessions_per_technique: Number of sessions to run per technique (enables V2 mode)

        Returns:
            AsyncRedTeamSession instance

        Raises:
            ValueError: If objective_ids not provided in V1 mode
        """
        # Use defaults if not provided
        refusal_judge_model = refusal_judge_model or self._default_refusal_judge_model
        objective_judge_model = objective_judge_model or self._default_objective_judge_model
        attacker_model = attacker_model or self._default_attacker_model
        evaluation_report_model = evaluation_report_model or self._default_evaluation_report_model

        # V2 mode: objective_ids optional (defaults to all)
        if objective_ids is None:
            objective_ids = self._available_objective_ids.copy()

        # Validate execution strategy
        if execution_strategy_type not in ["single", "random", "static_prompt_set"]:
            raise ValueError(
                "execution_strategy_type must be 'single', 'random', or 'static_prompt_set'."
            )

        payload = {
            "name": name,
            "target_system_prompt": target_system_prompt,
            "objective_ids": objective_ids,
            "target_model": target_model,
            "refusal_judge_model": refusal_judge_model,
            "objective_judge_model": objective_judge_model,
            "attacker_model": attacker_model,
            "evaluation_report_model": evaluation_report_model,
            "execution_strategy_type": execution_strategy_type,
            "max_turns": max_turns,
            "attacker_max_generation_attempts": attacker_max_generation_attempts,
            "n_random_techniques": n_random_techniques,
            "max_parallel_techniques": max_parallel_techniques,
            "prompt_set_id": prompt_set_id,
        }
        if hiddenlayer_project_id is not None:
            payload["hl_project_id"] = hiddenlayer_project_id
        if sessions_per_technique is not None:
            payload["sessions_per_technique"] = sessions_per_technique

        resp: RedTeamCreateResponse = self._client.evaluations.red_team.create(
            name=name,
            target_system_prompt=target_system_prompt,
            objective_ids=objective_ids,
            target_model=target_model,
            refusal_judge_model=refusal_judge_model,
            objective_judge_model=objective_judge_model,
            attacker_model=attacker_model,
            evaluation_report_model=evaluation_report_model,
            execution_strategy_type=execution_strategy_type,
            max_turns=max_turns,
            attacker_max_generation_attempts=attacker_max_generation_attempts,
            n_random_techniques=n_random_techniques,
            max_parallel_techniques=max_parallel_techniques,
            prompt_set_id=prompt_set_id,
        )
        return RedTeamSession(
            client=self._client,
            workflow_id=resp.workflow_id,
            name=name,
            poll_interval=poll_interval,
            poll_max_wait=poll_max_wait,
            max_parallel_techniques=max_parallel_techniques,
        )

    def resume_session(
            self,
            workflow_id: str,
            *,
            poll_interval: float = 2.0,
            poll_max_wait: float | None = None,
            max_parallel_techniques: int | None = None,
    ) -> RedTeamSession:
        """Resume an existing red team session by workflow ID.

        This allows you to reconnect to a workflow that was previously started,
        either from a different process or after an interruption.

        Args:
            workflow_id: The workflow ID to resume
            poll_interval: How often to poll for actions (seconds, default: 2.0s)
            poll_max_wait: Maximum time to wait for actions (seconds)
            max_parallel_techniques: Override parallel techniques setting
                (if None, will fetch from workflow status)

        Returns:
            AsyncRedTeamSession instance connected to the existing workflow

        Raises:
            WorkflowNotFoundError: If workflow_id doesn't exist
            RedTeamSessionError: If unable to fetch workflow info
        """
        # Fetch workflow status to get metadata
        try:
            status = self._client.evaluations.red_team.retrieve_status(workflow_id)
        except httpx.HTTPStatusError as e:
            if hasattr(e, "response") and e.response.status_code == 404:
                raise WorkflowNotFoundError(f"Workflow not found: {workflow_id}") from e
            raise RedTeamSessionError(f"Failed to fetch workflow info: {e}") from e

        # Extract session metadata
        name = status.name

        # Use provided max_parallel or fetch from status
        if max_parallel_techniques is None:
            max_parallel_techniques = 1

        return RedTeamSession(
            client=self._client,
            workflow_id=workflow_id,
            name=name,
            poll_interval=poll_interval,
            poll_max_wait=poll_max_wait,
            max_parallel_techniques=max_parallel_techniques,
        )

    def terminate_session(
            self,
            workflow_id: str,
    ) -> None:
        """Terminate an existing red team session by workflow ID.

        This allows you to stop a workflow currently in progress.

        Args:
            workflow_id: The workflow ID to terminate

        Raises:
            WorkflowNotFoundError: If workflow_id doesn't exist
            RedTeamSessionError: If unable to fetch workflow info
        """

        try:
            self._client.evaluations.red_team.terminate(workflow_id)
        except httpx.HTTPStatusError as e:
            if hasattr(e, "response") and e.response.status_code == 404:
                raise WorkflowNotFoundError(f"Workflow not found: {workflow_id}") from e
            raise RedTeamSessionError(f"Failed to fetch workflow info: {e}") from e

        return


class AsyncRedTeamSession:
    """Represents an active red team session (async-only).

    Usage:
        async for action in session.iterate_actions():
            ...
    Or:
        await session.run_with_callback(handler)
    Or:
        await session.run_with_callback_parallel(handler)
    """

    def __init__(
        self,
        client: AsyncHiddenLayer,
        workflow_id: str,
        name: str,
        poll_interval: float = 2.0,
        poll_max_wait: float | None = None,
        max_parallel_techniques: int = 1,
    ):
        self._client = client
        self._workflow_id = workflow_id
        self._name = name
        self._poll_interval = poll_interval
        self._poll_max_wait = poll_max_wait
        self._max_parallel_techniques = max_parallel_techniques
        self._start_monotonic = asyncio.get_event_loop().time()
        self._last_action: RedTeamRetrieveNextActionResponse | None = None

    @property
    def workflow_id(self) -> str:
        return self._workflow_id

    @property
    def name(self) -> str:
        return self._name

    def _check_timeout(self) -> None:
        if self._poll_max_wait is not None:
            elapsed = asyncio.get_event_loop().time() - self._start_monotonic
            if elapsed > self._poll_max_wait:
                raise Exception(
                    f"Polling timed out after {elapsed:.1f}s (max: {self._poll_max_wait}s)"
                )


    async def get_next_action(self, *, block: bool = True) -> RedTeamRetrieveNextActionResponse:
        """Async poll for next action."""
        while True:
            self._check_timeout()
            try:
                action = await self._client.evaluations.red_team.retrieve_next_action(self._workflow_id)
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 404:
                    raise WorkflowNotFoundError(
                        f"Workflow not found: {self._workflow_id}"
                    ) from e
                if e.response.status_code == 500:
                    try:
                        status = await self._client.evaluations.red_team.retrieve_status(self._workflow_id)
                        workflow_status = status.status
                        raise RedTeamSessionError(
                            f"Server error getting next action. "
                            f"Workflow status: {workflow_status}. "
                            f"Workflow ID: {self._workflow_id}"
                        ) from e
                    except Exception:
                        # If status check also fails, raise original error
                        raise RedTeamSessionError(
                            f"Server error getting next action "
                            f"for workflow {self._workflow_id}. "
                            f"The workflow may be in a bad state. "
                            f"Try checking the workflow status or restarting."
                        ) from e
                raise

            self._last_action = action

            if action.is_ready or not block:
                return action

            await asyncio.sleep(self._poll_interval)

    async def wait_for_completion(
        self,
        poll_interval: float = 3.0,
        max_wait: float | None = 300.0,
        verbose: bool = False,
    ) -> None:
        """Poll status until workflow reaches terminal state.

        This method is automatically called by run_with_callback() and
        run_with_callback_parallel() to ensure the workflow has fully completed
        before returning.

        Args:
            poll_interval: How often to check status (default: 3.0s)
            max_wait: Maximum time to wait for completion (default: 300s / 5 min)
            verbose: If True, print status updates (default: False)

        Raises:
            PollTimeoutError: If max_wait is exceeded
            RedTeamSessionError: If workflow fails
        """
        start_time = asyncio.get_event_loop().time()
        terminal_states = {
            "COMPLETED",
            "FAILED",
            "CANCELLED",
            "TERMINATED",
            "TIMED_OUT",
        }

        if verbose:
            logger.info(f"⏳ Waiting for workflow {self._workflow_id[:8]}... to complete...")

        while True:
            # Check timeout
            if max_wait is not None:
                elapsed = asyncio.get_event_loop().time() - start_time
                if elapsed > max_wait:
                    raise PollTimeoutError(f"Workflow did not complete within {max_wait}s")

            try:
                status = await self._client.evaluations.red_team.retrieve_status(self._workflow_id)
                workflow_status = status.status

                if workflow_status in terminal_states:
                    if workflow_status == "FAILED":
                        error_msg = status.error
                        raise RedTeamSessionError(f"Workflow failed: {error_msg}")

                    # Workflow is complete
                    if verbose:
                        elapsed = asyncio.get_event_loop().time() - start_time
                        logger.info(f"✅ Workflow completed in {elapsed:.1f}s.")
                    return

            except httpx.HTTPStatusError as e:
                # If we get 404, workflow doesn't exist
                if e.response.status_code == 404:
                    raise WorkflowNotFoundError(
                        f"Workflow not found: {self._workflow_id}"
                    ) from e
                # For other errors, keep retrying unless we're at max_wait
                if max_wait is not None:
                    elapsed = asyncio.get_event_loop().time() - start_time
                    if elapsed > max_wait:
                        raise

            await asyncio.sleep(poll_interval)

    async def iterate_actions(self) -> AsyncIterator[RedTeamRetrieveNextActionResponse]:
        """Yield attack_task actions until workflow completes/fails."""
        while True:
            action = await self.get_next_action(block=True)

            if action.action_type == "complete":
                return
            if action.action_type == "failed":
                raise RedTeamSessionError(action.message if action.message else "Workflow failed")
            if action.is_ready and action.action_type == "attack_task":
                yield action

    async def run_with_callback(
        self,
        handler: Callable[[str | None, list[dict[str, Any]] | None, str | None, str | None], Awaitable[str]],
    ) -> None:
        """Run session with sequential action processing.

        Args:
            handler: Async function that takes
                (attack_prompt, history, session_id, target_system_prompt)
                and returns target response
        """
        async for action in self.iterate_actions():
            attack_prompt = action.attack_prompt
            history = action.history
            # TODO: same as sync; need to update API contract so this doesn't need to be handled
            session_id = action.session_id if action.session_id else ""
            target_system_prompt = action.target_system_prompt
            target_response = await handler(
                attack_prompt, history, session_id, target_system_prompt
            )
            await self._client.evaluations.red_team.submit_target_response(
                workflow_id=self._workflow_id,
                session_id=session_id,
                target_response=target_response)
        # Wait for workflow to fully complete
        return await self.wait_for_completion()

    async def get_available_actions(self, max_actions: int = 10) -> list[RedTeamRetrieveNextActionResponse]:
        """Get up to max_actions that are currently ready (non-blocking)."""
        actions: list[RedTeamRetrieveNextActionResponse] = []
        for _ in range(max_actions):
            action = await self.get_next_action(block=False)
            if action.action_type == "complete":
                return actions
            if action.action_type == "failed":
                raise RedTeamSessionError(action.message if action.message else "Workflow failed")
            if action.is_ready and action.action_type == "attack_task":
                actions.append(action)
            else:
                # No more ready actions
                break
        return actions

    async def _process_single_action(
        self,
        action: RedTeamRetrieveNextActionResponse,
        handler: Callable[[str | None, list[dict[str, Any]] | None, str | None, str | None], Awaitable[str]],
    ) -> None:
        """Process a single action with the handler and submit response."""
        attack_prompt = action.attack_prompt
        history = action.history if action.history else []
        session_id = action.session_id if action.session_id else ""
        target_system_prompt = action.target_system_prompt

        # Call handler to get target response
        target_response = await handler(attack_prompt, history, session_id, target_system_prompt)

        # Submit response
        try:
            await self._client.evaluations.red_team.submit_target_response(
                workflow_id=self._workflow_id, session_id=session_id, target_response=target_response
            )
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 400:
                raise InvalidSessionError(f"Invalid session_id: {session_id}") from e
            raise

    async def run_with_callback_parallel(
        self,
        handler: Callable[[str | None, list[dict[str, Any]] | None, str | None, str | None], Awaitable[str]],
        max_parallel: int | None = None,
        poll_batch_interval: float = 0.5,
    ) -> None:
        """Run session with parallel action processing.

        Args:
            handler: Async function to handle attack prompts and return target responses
            max_parallel: Maximum number of actions to process in parallel.
                         If None, automatically uses max_parallel_techniques from session config.
                         You may want to set this lower for rate limiting or higher if techniques
                         can generate multiple actions per turn.
            poll_batch_interval: How often to check for new actions when at max capacity
        """
        # Auto-detect max_parallel from session config if not specified
        if max_parallel is None:
            max_parallel = self._max_parallel_techniques

        pending_tasks: set[asyncio.Task[None]] = set()

        while True:
            self._check_timeout()

            # Wait for some tasks to complete if at max capacity
            if len(pending_tasks) >= max_parallel:
                done, pending_tasks = await asyncio.wait(
                    pending_tasks, return_when=asyncio.FIRST_COMPLETED
                )
                # Check for exceptions in completed tasks
                for task in done:
                    try:
                        task.result()
                    except Exception:
                        # Cancel remaining tasks and re-raise
                        for t in pending_tasks:
                            t.cancel()
                        raise

            # Get available actions
            try:
                available_actions = await self.get_available_actions(
                    max_actions=max_parallel - len(pending_tasks)
                )
            except RedTeamSessionError:
                # Workflow failed, wait for pending tasks and re-raise
                if pending_tasks:
                    await asyncio.gather(*pending_tasks, return_exceptions=True)
                raise

            if available_actions:
                # Start processing new actions
                for action in available_actions:
                    task = asyncio.create_task(self._process_single_action(action, handler))
                    pending_tasks.add(task)
            else:
                # Check if workflow is complete
                action = await self.get_next_action(block=True)

                if action.action_type == "complete":
                    # Wait for all pending tasks to complete
                    if pending_tasks:
                        await asyncio.gather(*pending_tasks)
                    # Wait for workflow to fully complete before
                    return await self.wait_for_completion()

                if action.action_type == "failed":
                    # Wait for pending tasks and raise error
                    if pending_tasks:
                        await asyncio.gather(*pending_tasks, return_exceptions=True)
                    raise RedTeamSessionError(action.message if action.message else "Workflow failed")

                if action.is_ready and action.action_type == "attack_task":
                    # Process this action
                    task = asyncio.create_task(self._process_single_action(action, handler))
                    pending_tasks.add(task)

            await asyncio.sleep(poll_batch_interval)


class AsyncRedTeamSessionsResource(AsyncAPIResource):
    _available_objective_ids = ["HLO.01", "HLO.02", "HLO.03", "HLO.05", "HLO.07"]

    def __init__(
            self,
            client: AsyncHiddenLayer,
            *,
            default_refusal_judge_model: str = "openai/gpt-5-mini",
            default_objective_judge_model: str = "openai/gpt-5",
            default_attacker_model: str = "openai/gpt-5",
            default_evaluation_report_model: str = "openai/gpt-5",
    ):
        # Default models for red team evaluations
        self._default_refusal_judge_model = default_refusal_judge_model
        self._default_objective_judge_model = default_objective_judge_model
        self._default_attacker_model = default_attacker_model
        self._default_evaluation_report_model = default_evaluation_report_model
        super().__init__(client)

    async def start_session(
            self,
            *,
            name: str,
            objective_ids: list[str] | None = None,
            target_model: str,
            target_system_prompt: str = "",
            refusal_judge_model: str | None = None,
            objective_judge_model: str | None = None,
            attacker_model: str | None = None,
            evaluation_report_model: str | None = None,
            max_turns: int = 3,
            execution_strategy_type: str = "random",
            attacker_max_generation_attempts: int = 2,
            n_random_techniques: int = 1,
            max_parallel_techniques: int = 1,
            prompt_set_id: str = "",
            hiddenlayer_project_id: str | None = None,
            poll_interval: float = 2.0,
            poll_max_wait: float | None = None,
            sessions_per_technique: int | None = 1,
    ) -> AsyncRedTeamSession:
        """Start a new red team session.

        Supports two modes:

        V1 Mode (objective-specific with short-circuit):
            - Provide objective_ids (required)
            - Do not set sessions_per_technique
            - Each session tests one objective and short-circuits on success

        V2 Mode (objective-agnostic adaptive):
            - Set sessions_per_technique (e.g., 3)
            - objective_ids optional (defaults to all available)
            - Each session tests all objectives, runs to max_turns
            - Adaptive attacker with cross-session state

        Args:
            name: Session name
            objective_ids: List of objective IDs to test (e.g., ["HLO.03"])
                V1: Required. V2: Optional (defaults to all available)
            target_model: Model identifier for the target being tested
            target_system_prompt: System prompt for the target model
            refusal_judge_model: Model to use for refusal judging
                (defaults to client default)
            objective_judge_model: Model to use for objective judging
                (defaults to client default)
            attacker_model: Model to use for generating attacks (defaults to client default)
            evaluation_report_model: Model to use for evaluation reports
                (defaults to client default)
            max_turns: Maximum conversation turns per session
            execution_strategy_type: Strategy type ("single", "random", or "static_prompt_set")
            attacker_max_generation_attempts: Max attempts for attacker to generate prompts
            n_random_techniques: Number of techniques to select per turn
            max_parallel_techniques: Number of techniques to run in parallel
            prompt_set_id: ID of prompt set (if using static_prompt_set strategy)
            hiddenlayer_project_id: Optional HiddenLayer project ID
            poll_interval: How often to poll for actions (seconds, default: 2.0s)
            poll_max_wait: Maximum time to wait for actions (seconds)
            sessions_per_technique: Number of sessions to run per technique (enables V2 mode)

        Returns:
            AsyncRedTeamSession instance

        Raises:
            ValueError: If objective_ids not provided in V1 mode
        """
        # Use defaults if not provided
        refusal_judge_model = refusal_judge_model or self._default_refusal_judge_model
        objective_judge_model = objective_judge_model or self._default_objective_judge_model
        attacker_model = attacker_model or self._default_attacker_model
        evaluation_report_model = evaluation_report_model or self._default_evaluation_report_model

        # V2 mode: objective_ids optional (defaults to all)
        if objective_ids is None:
            objective_ids = self._available_objective_ids.copy()

        # Validate execution strategy
        if execution_strategy_type not in ["single", "random", "static_prompt_set"]:
            raise ValueError(
                "execution_strategy_type must be 'single', 'random', or 'static_prompt_set'."
            )

        payload = {
            "name": name,
            "target_system_prompt": target_system_prompt,
            "objective_ids": objective_ids,
            "target_model": target_model,
            "refusal_judge_model": refusal_judge_model,
            "objective_judge_model": objective_judge_model,
            "attacker_model": attacker_model,
            "evaluation_report_model": evaluation_report_model,
            "execution_strategy_type": execution_strategy_type,
            "max_turns": max_turns,
            "attacker_max_generation_attempts": attacker_max_generation_attempts,
            "n_random_techniques": n_random_techniques,
            "max_parallel_techniques": max_parallel_techniques,
            "prompt_set_id": prompt_set_id,
        }
        if hiddenlayer_project_id is not None:
            payload["hl_project_id"] = hiddenlayer_project_id
        if sessions_per_technique is not None:
            payload["sessions_per_technique"] = sessions_per_technique

        resp: RedTeamCreateResponse = await self._client.evaluations.red_team.create(
            name=name,
            target_system_prompt=target_system_prompt,
            objective_ids=objective_ids,
            target_model=target_model,
            refusal_judge_model=refusal_judge_model,
            objective_judge_model=objective_judge_model,
            attacker_model=attacker_model,
            evaluation_report_model=evaluation_report_model,
            execution_strategy_type=execution_strategy_type,
            max_turns=max_turns,
            attacker_max_generation_attempts=attacker_max_generation_attempts,
            n_random_techniques=n_random_techniques,
            max_parallel_techniques=max_parallel_techniques,
            prompt_set_id=prompt_set_id,
        )
        return AsyncRedTeamSession(
            client=self._client,
            workflow_id=resp.workflow_id,
            name=name,
            poll_interval=poll_interval,
            poll_max_wait=poll_max_wait,
            max_parallel_techniques=max_parallel_techniques,
        )

    async def resume_session(
            self,
            workflow_id: str,
            *,
            poll_interval: float = 2.0,
            poll_max_wait: float | None = None,
            max_parallel_techniques: int | None = None,
    ) -> AsyncRedTeamSession:
        """Resume an existing red team session by workflow ID.

        This allows you to reconnect to a workflow that was previously started,
        either from a different process or after an interruption.

        Args:
            workflow_id: The workflow ID to resume
            poll_interval: How often to poll for actions (seconds, default: 2.0s)
            poll_max_wait: Maximum time to wait for actions (seconds)
            max_parallel_techniques: Override parallel techniques setting
                (if None, will fetch from workflow status)

        Returns:
            AsyncRedTeamSession instance connected to the existing workflow

        Raises:
            WorkflowNotFoundError: If workflow_id doesn't exist
            RedTeamSessionError: If unable to fetch workflow info
        """
        # Fetch workflow status to get metadata
        try:
            status = await self._client.evaluations.red_team.retrieve_status(workflow_id)
        except httpx.HTTPStatusError as e:
            if hasattr(e, "response") and e.response.status_code == 404:
                raise WorkflowNotFoundError(f"Workflow not found: {workflow_id}") from e
            raise RedTeamSessionError(f"Failed to fetch workflow info: {e}") from e

        # Extract session metadata
        name = status.name

        # Use provided max_parallel or fetch from status
        if max_parallel_techniques is None:
            max_parallel_techniques = 1

        return AsyncRedTeamSession(
            client=self._client,
            workflow_id=workflow_id,
            name=name,
            poll_interval=poll_interval,
            poll_max_wait=poll_max_wait,
            max_parallel_techniques=max_parallel_techniques,
        )

    async def terminate_session(
            self,
            workflow_id: str,
    ) -> None:
        """Terminate an existing red team session by workflow ID.

        This allows you to stop a workflow currently in progress.

        Args:
            workflow_id: The workflow ID to terminate

        Raises:
            WorkflowNotFoundError: If workflow_id doesn't exist
            RedTeamSessionError: If unable to fetch workflow info
        """

        try:
            await self._client.evaluations.red_team.terminate(workflow_id)
        except httpx.HTTPStatusError as e:
            if hasattr(e, "response") and e.response.status_code == 404:
                raise WorkflowNotFoundError(f"Workflow not found: {workflow_id}") from e
            raise RedTeamSessionError(f"Failed to fetch workflow info: {e}") from e

        return
