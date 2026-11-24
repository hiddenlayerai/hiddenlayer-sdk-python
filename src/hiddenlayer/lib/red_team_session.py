"""Red team sessions: start or resume a workflow, answer its attack prompts, and wait for it to finish."""

from __future__ import annotations

import asyncio
import logging
import time
from typing import TYPE_CHECKING, Any, AsyncIterator, Awaitable, Callable, Dict, Iterator, List, Optional

from ..core.api_error import ApiError
from ..types.next_action_response import NextActionResponse
from ..types.severity_mapping import SeverityMapping
from .red_team_exceptions import InvalidSessionError, PollTimeoutError, RedTeamSessionError, WorkflowNotFoundError

if TYPE_CHECKING:
    from ..client import AsyncHiddenLayer, HiddenLayer

logger = logging.getLogger(__name__)

# attack_prompt, history, session_id and target_system_prompt, answered with the target's response.
Handler = Callable[[Optional[str], Optional[List[Dict[str, Any]]], Optional[str], Optional[str]], str]
AsyncHandler = Callable[[Optional[str], Optional[List[Dict[str, Any]]], Optional[str], Optional[str]], Awaitable[str]]

_EXECUTION_STRATEGY_TYPES = ("single", "random", "static_prompt_set")
_TERMINAL_STATES = frozenset({"COMPLETED", "FAILED", "CANCELLED", "TERMINATED", "TIMED_OUT"})


def _is_transient(error: ApiError) -> bool:
    status = error.status_code
    return status is not None and (status in (408, 429) or status >= 500)


def _not_found(workflow_id: str) -> WorkflowNotFoundError:
    return WorkflowNotFoundError(f"Workflow not found: {workflow_id}")


def _failed_action(action: NextActionResponse) -> RedTeamSessionError:
    return RedTeamSessionError(action.message if action.message else "Workflow failed")


def _still_running(tasks: set[asyncio.Task[None]]) -> set[asyncio.Task[None]]:
    """Returns the tasks that haven't finished, once every finished one is known to have succeeded.

    Raises:
        Exception: The error a finished task ended with, after the running tasks are cancelled.
    """
    running = {task for task in tasks if not task.done()}
    for task in tasks - running:
        try:
            task.result()
        except Exception:
            for other in running:
                other.cancel()
            raise
    return running


def _next_action_server_error(workflow_id: str, workflow_status: Optional[str]) -> RedTeamSessionError:
    if workflow_status is None:
        return RedTeamSessionError(
            f"Server error getting next action for workflow {workflow_id}. "
            "The workflow may be in a bad state. Try checking the workflow status or restarting."
        )
    return RedTeamSessionError(
        f"Server error getting next action. Workflow status: {workflow_status}. Workflow ID: {workflow_id}"
    )


def _poll_timeout(start: float, max_wait: Optional[float]) -> Optional[PollTimeoutError]:
    if max_wait is None:
        return None
    elapsed = time.monotonic() - start
    if elapsed <= max_wait:
        return None
    return PollTimeoutError(f"Polling timed out after {elapsed:.1f}s (max: {max_wait}s)")


def _create_arguments(
    *,
    name: str,
    objective_ids: Optional[List[str]],
    target_model: str,
    target_system_prompt: str,
    refusal_judge_model: Optional[str],
    objective_judge_model: Optional[str],
    attacker_model: Optional[str],
    evaluation_report_model: Optional[str],
    attacker_guidance: Optional[str],
    severity_mapping: Optional[SeverityMapping],
    config_id: Optional[str],
    max_turns: int,
    execution_strategy_type: str,
    attacker_max_generation_attempts: int,
    n_random_techniques: int,
    max_parallel_techniques: int,
    prompt_set_id: Optional[str],
    hiddenlayer_project_id: Optional[str],
    sessions_per_technique: Optional[int],
) -> Dict[str, Any]:
    """The arguments of `evaluations.red_team.create`: an option left as None isn't sent at all."""
    if execution_strategy_type not in _EXECUTION_STRATEGY_TYPES:
        raise ValueError("execution_strategy_type must be 'single', 'random', or 'static_prompt_set'.")
    optional = {
        "objective_ids": objective_ids,
        "refusal_judge_model": refusal_judge_model,
        "objective_judge_model": objective_judge_model,
        "attacker_model": attacker_model,
        "evaluation_report_model": evaluation_report_model,
        "attacker_guidance": attacker_guidance,
        "severity_mapping": severity_mapping,
        "config_id": config_id,
        "prompt_set_id": prompt_set_id,
        "hl_project_id": hiddenlayer_project_id,
        "sessions_per_technique": sessions_per_technique,
    }
    return {
        "name": name,
        "target_model": target_model,
        "target_system_prompt": target_system_prompt,
        # The API's values are upper case; callers pass lower case.
        "execution_strategy_type": execution_strategy_type.upper(),
        "max_turns": max_turns,
        "attacker_max_generation_attempts": attacker_max_generation_attempts,
        "n_random_techniques": n_random_techniques,
        "max_parallel_techniques": max_parallel_techniques,
        **{key: value for key, value in optional.items() if value is not None},
    }


class RedTeamSession:
    """A red team workflow in progress, driven synchronously.

    Usage:
        for action in session.iterate_actions():
            ...
    Or:
        session.run_with_callback(handler)
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
        self._start_monotonic = time.monotonic()
        self._last_action: NextActionResponse | None = None

    @property
    def workflow_id(self) -> str:
        return self._workflow_id

    @property
    def name(self) -> str:
        return self._name

    def _check_timeout(self) -> None:
        timeout = _poll_timeout(self._start_monotonic, self._poll_max_wait)
        if timeout is not None:
            raise timeout

    def _workflow_status(self) -> Optional[str]:
        try:
            return self._client.evaluations.red_team.retrieve_status(self._workflow_id).status
        except Exception:
            return None

    def get_next_action(self, *, block: bool = True) -> NextActionResponse:
        """Polls for the next action.

        Args:
            block: Whether to keep polling until an action is ready.

        Raises:
            WorkflowNotFoundError: If the workflow doesn't exist.
            RedTeamSessionError: If the API answers 500.
            PollTimeoutError: If the session's poll_max_wait has passed.
        """
        while True:
            self._check_timeout()
            try:
                action = self._client.evaluations.red_team.retrieve_next_action(self._workflow_id)
            except ApiError as e:
                if e.status_code == 404:
                    raise _not_found(self._workflow_id) from e
                if e.status_code == 500:
                    raise _next_action_server_error(self._workflow_id, self._workflow_status()) from e
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
        """Polls the workflow's status until it reaches a terminal state.

        run_with_callback calls this before it returns. A 408, 429 or 5xx answer is polled through
        until max_wait.

        Args:
            poll_interval: Seconds between status checks.
            max_wait: Seconds to wait before giving up, or None to wait indefinitely.
            verbose: Whether to log progress.

        Raises:
            PollTimeoutError: If max_wait passes first.
            RedTeamSessionError: If the workflow failed.
            WorkflowNotFoundError: If the workflow doesn't exist.
        """
        start = time.monotonic()
        if verbose:
            logger.info(f"⏳ Waiting for workflow {self._workflow_id[:8]}... to complete...")

        while True:
            if max_wait is not None and time.monotonic() - start > max_wait:
                raise PollTimeoutError(f"Workflow did not complete within {max_wait}s")

            try:
                status = self._client.evaluations.red_team.retrieve_status(self._workflow_id)
            except ApiError as e:
                if e.status_code == 404:
                    raise _not_found(self._workflow_id) from e
                if not _is_transient(e):
                    raise
            else:
                if status.status == "FAILED":
                    raise RedTeamSessionError(f"Workflow failed: {status.error}")
                if status.status in _TERMINAL_STATES:
                    if verbose:
                        logger.info(f"✅ Workflow completed in {time.monotonic() - start:.1f}s.")
                    return

            time.sleep(poll_interval)

    def iterate_actions(self) -> Iterator[NextActionResponse]:
        """Yields each attack task until the workflow completes.

        Raises:
            RedTeamSessionError: If the workflow fails.
        """
        while True:
            action = self.get_next_action(block=True)
            if action.action_type == "complete":
                return
            if action.action_type == "failed":
                raise _failed_action(action)
            if action.is_ready and action.action_type == "attack_task":
                yield action

    def run_with_callback(self, handler: Handler) -> None:
        """Answers each attack task with the handler, one at a time, then waits for the workflow to finish.

        Args:
            handler: Takes (attack_prompt, history, session_id, target_system_prompt) and returns
                the target's response.
        """
        for action in self.iterate_actions():
            # The API doesn't require session_id in its responses, though submitting needs one.
            session_id = action.session_id if action.session_id else ""
            target_response = handler(action.attack_prompt, action.history, session_id, action.target_system_prompt)
            self._client.evaluations.red_team.submit_target_response(
                self._workflow_id, session_id=session_id, target_response=target_response
            )
        return self.wait_for_completion()


class RedTeamSessionsResource:
    def __init__(self, client: HiddenLayer):
        self._client = client

    def start_session(
        self,
        *,
        name: str,
        objective_ids: Optional[List[str]] = None,
        target_model: str,
        target_system_prompt: str = "",
        refusal_judge_model: Optional[str] = None,
        objective_judge_model: Optional[str] = None,
        attacker_model: Optional[str] = None,
        evaluation_report_model: Optional[str] = None,
        attacker_guidance: Optional[str] = None,
        severity_mapping: Optional[SeverityMapping] = None,
        config_id: Optional[str] = None,
        max_turns: int = 3,
        execution_strategy_type: str = "random",
        attacker_max_generation_attempts: int = 2,
        n_random_techniques: int = 1,
        max_parallel_techniques: int = 1,
        prompt_set_id: Optional[str] = None,
        hiddenlayer_project_id: Optional[str] = None,
        poll_interval: float = 2.0,
        poll_max_wait: float | None = None,
        sessions_per_technique: Optional[int] = 1,
    ) -> RedTeamSession:
        """Starts a red team workflow.

        Each session runs to max_turns without stopping early, tests every objective given, and
        keeps state across sessions for adaptive attacks. An option left as None isn't sent.

        Args:
            name: Session name.
            objective_ids: Objective IDs to test, e.g. ["HLO.03"].
            target_model: Identifier of the model being tested.
            target_system_prompt: The target model's system prompt.
            refusal_judge_model: Model that judges refusals.
            objective_judge_model: Model that judges objectives.
            attacker_model: Model that generates attacks.
            evaluation_report_model: Model that writes evaluation reports.
            attacker_guidance: Intent-only natural-language text that focuses the attacker within
                the objectives. The static_prompt_set strategy ignores it.
            severity_mapping: Objective ID to severity level; a session's severity comes from the
                worst objective achieved.
            config_id: A preset config to start from. Any option also given here overrides it.
            max_turns: Maximum conversation turns per session.
            execution_strategy_type: "single", "random" or "static_prompt_set".
            attacker_max_generation_attempts: Attempts the attacker gets to generate a prompt.
            n_random_techniques: Techniques selected per turn.
            max_parallel_techniques: Techniques run in parallel.
            prompt_set_id: The prompt set, for the static_prompt_set strategy.
            hiddenlayer_project_id: A HiddenLayer project to scope the run to.
            poll_interval: Seconds between polls for actions.
            poll_max_wait: Seconds the session may poll for actions in all, or None for no limit.
            sessions_per_technique: Sessions run per technique.

        Raises:
            ValueError: If execution_strategy_type isn't one of the three.
        """
        response = self._client.evaluations.red_team.create(
            **_create_arguments(
                name=name,
                objective_ids=objective_ids,
                target_model=target_model,
                target_system_prompt=target_system_prompt,
                refusal_judge_model=refusal_judge_model,
                objective_judge_model=objective_judge_model,
                attacker_model=attacker_model,
                evaluation_report_model=evaluation_report_model,
                attacker_guidance=attacker_guidance,
                severity_mapping=severity_mapping,
                config_id=config_id,
                max_turns=max_turns,
                execution_strategy_type=execution_strategy_type,
                attacker_max_generation_attempts=attacker_max_generation_attempts,
                n_random_techniques=n_random_techniques,
                max_parallel_techniques=max_parallel_techniques,
                prompt_set_id=prompt_set_id,
                hiddenlayer_project_id=hiddenlayer_project_id,
                sessions_per_technique=sessions_per_technique,
            )
        )
        return RedTeamSession(
            client=self._client,
            workflow_id=response.workflow_id,
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
        """Reconnects to a workflow started earlier, from another process or after an interruption.

        Args:
            workflow_id: The workflow to resume.
            poll_interval: Seconds between polls for actions.
            poll_max_wait: Seconds the session may poll for actions in all, or None for no limit.
            max_parallel_techniques: Actions run_with_callback_parallel handles at once. Defaults to 1.

        Raises:
            WorkflowNotFoundError: If the workflow doesn't exist.
            RedTeamSessionError: If the workflow's status can't be fetched.
        """
        try:
            status = self._client.evaluations.red_team.retrieve_status(workflow_id)
        except ApiError as e:
            if e.status_code == 404:
                raise _not_found(workflow_id) from e
            raise RedTeamSessionError(f"Failed to fetch workflow info: {e}") from e

        return RedTeamSession(
            client=self._client,
            workflow_id=workflow_id,
            name=status.name,
            poll_interval=poll_interval,
            poll_max_wait=poll_max_wait,
            max_parallel_techniques=1 if max_parallel_techniques is None else max_parallel_techniques,
        )

    def terminate_session(self, workflow_id: str) -> None:
        """Stops a workflow in progress.

        Raises:
            WorkflowNotFoundError: If the workflow doesn't exist.
            RedTeamSessionError: If the workflow can't be terminated.
        """
        try:
            self._client.evaluations.red_team.terminate(workflow_id)
        except ApiError as e:
            if e.status_code == 404:
                raise _not_found(workflow_id) from e
            raise RedTeamSessionError(f"Failed to terminate workflow: {e}") from e


class AsyncRedTeamSession:
    """A red team workflow in progress, driven asynchronously.

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
        self._start_monotonic = time.monotonic()
        self._last_action: NextActionResponse | None = None

    @property
    def workflow_id(self) -> str:
        return self._workflow_id

    @property
    def name(self) -> str:
        return self._name

    def _check_timeout(self) -> None:
        timeout = _poll_timeout(self._start_monotonic, self._poll_max_wait)
        if timeout is not None:
            raise timeout

    async def _workflow_status(self) -> Optional[str]:
        try:
            return (await self._client.evaluations.red_team.retrieve_status(self._workflow_id)).status
        except Exception:
            return None

    async def get_next_action(self, *, block: bool = True) -> NextActionResponse:
        """Async version of RedTeamSession.get_next_action."""
        while True:
            self._check_timeout()
            try:
                action = await self._client.evaluations.red_team.retrieve_next_action(self._workflow_id)
            except ApiError as e:
                if e.status_code == 404:
                    raise _not_found(self._workflow_id) from e
                if e.status_code == 500:
                    raise _next_action_server_error(self._workflow_id, await self._workflow_status()) from e
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
        """Async version of RedTeamSession.wait_for_completion.

        run_with_callback and run_with_callback_parallel call this before they return.
        """
        start = time.monotonic()
        if verbose:
            logger.info(f"⏳ Waiting for workflow {self._workflow_id[:8]}... to complete...")

        while True:
            if max_wait is not None and time.monotonic() - start > max_wait:
                raise PollTimeoutError(f"Workflow did not complete within {max_wait}s")

            try:
                status = await self._client.evaluations.red_team.retrieve_status(self._workflow_id)
            except ApiError as e:
                if e.status_code == 404:
                    raise _not_found(self._workflow_id) from e
                if not _is_transient(e):
                    raise
            else:
                if status.status == "FAILED":
                    raise RedTeamSessionError(f"Workflow failed: {status.error}")
                if status.status in _TERMINAL_STATES:
                    if verbose:
                        logger.info(f"✅ Workflow completed in {time.monotonic() - start:.1f}s.")
                    return

            await asyncio.sleep(poll_interval)

    async def iterate_actions(self) -> AsyncIterator[NextActionResponse]:
        """Async version of RedTeamSession.iterate_actions."""
        while True:
            action = await self.get_next_action(block=True)
            if action.action_type == "complete":
                return
            if action.action_type == "failed":
                raise _failed_action(action)
            if action.is_ready and action.action_type == "attack_task":
                yield action

    async def run_with_callback(self, handler: AsyncHandler) -> None:
        """Async version of RedTeamSession.run_with_callback; the handler is awaited."""
        async for action in self.iterate_actions():
            session_id = action.session_id if action.session_id else ""
            target_response = await handler(
                action.attack_prompt, action.history, session_id, action.target_system_prompt
            )
            await self._client.evaluations.red_team.submit_target_response(
                self._workflow_id, session_id=session_id, target_response=target_response
            )
        return await self.wait_for_completion()

    async def get_available_actions(self, max_actions: int = 10) -> list[NextActionResponse]:
        """Returns up to max_actions attack tasks that are ready now, without waiting for more.

        Raises:
            RedTeamSessionError: If the workflow failed.
        """
        actions: list[NextActionResponse] = []
        for _ in range(max_actions):
            action = await self.get_next_action(block=False)
            if action.action_type == "complete":
                return actions
            if action.action_type == "failed":
                raise _failed_action(action)
            if not (action.is_ready and action.action_type == "attack_task"):
                break
            actions.append(action)
        return actions

    async def _process_single_action(self, action: NextActionResponse, handler: AsyncHandler) -> None:
        """Answers one attack task with the handler and submits the response."""
        session_id = action.session_id if action.session_id else ""
        target_response = await handler(
            action.attack_prompt, action.history if action.history else [], session_id, action.target_system_prompt
        )
        try:
            await self._client.evaluations.red_team.submit_target_response(
                self._workflow_id, session_id=session_id, target_response=target_response
            )
        except ApiError as e:
            if e.status_code == 400:
                raise InvalidSessionError(f"Invalid session_id: {session_id}") from e
            raise

    async def run_with_callback_parallel(
        self,
        handler: AsyncHandler,
        max_parallel: int | None = None,
        poll_batch_interval: float = 0.5,
    ) -> None:
        """Answers attack tasks with the handler, several at a time, then waits for the workflow to finish.

        Args:
            handler: Takes (attack_prompt, history, session_id, target_system_prompt) and returns
                the target's response.
            max_parallel: Actions handled at once. Defaults to the session's max_parallel_techniques;
                set it lower for rate limits, or higher if a technique produces several actions per turn.
            poll_batch_interval: Seconds between checks for new actions.

        Raises:
            RedTeamSessionError: If the workflow fails.
            InvalidSessionError: If the API refuses a response's session_id.
        """
        if max_parallel is None:
            max_parallel = self._max_parallel_techniques

        pending_tasks: set[asyncio.Task[None]] = set()

        while True:
            self._check_timeout()

            if len(pending_tasks) >= max_parallel:
                await asyncio.wait(pending_tasks, return_when=asyncio.FIRST_COMPLETED)
            pending_tasks = _still_running(pending_tasks)

            try:
                available_actions = await self.get_available_actions(max_actions=max_parallel - len(pending_tasks))
            except RedTeamSessionError:
                if pending_tasks:
                    await asyncio.gather(*pending_tasks, return_exceptions=True)
                raise

            if available_actions:
                for action in available_actions:
                    pending_tasks.add(asyncio.create_task(self._process_single_action(action, handler)))
            else:
                # Blocking here while a handler runs would hide its failure: the workflow waits for its response.
                action = await self.get_next_action(block=not pending_tasks)

                if action.action_type == "complete":
                    if pending_tasks:
                        await asyncio.gather(*pending_tasks)
                    return await self.wait_for_completion()

                if action.action_type == "failed":
                    if pending_tasks:
                        await asyncio.gather(*pending_tasks, return_exceptions=True)
                    raise _failed_action(action)

                if action.is_ready and action.action_type == "attack_task":
                    pending_tasks.add(asyncio.create_task(self._process_single_action(action, handler)))

            await asyncio.sleep(poll_batch_interval)


class AsyncRedTeamSessionsResource:
    def __init__(self, client: AsyncHiddenLayer):
        self._client = client

    async def start_session(
        self,
        *,
        name: str,
        objective_ids: Optional[List[str]] = None,
        target_model: str,
        target_system_prompt: str = "",
        refusal_judge_model: Optional[str] = None,
        objective_judge_model: Optional[str] = None,
        attacker_model: Optional[str] = None,
        evaluation_report_model: Optional[str] = None,
        attacker_guidance: Optional[str] = None,
        severity_mapping: Optional[SeverityMapping] = None,
        config_id: Optional[str] = None,
        max_turns: int = 3,
        execution_strategy_type: str = "random",
        attacker_max_generation_attempts: int = 2,
        n_random_techniques: int = 1,
        max_parallel_techniques: int = 1,
        prompt_set_id: Optional[str] = None,
        hiddenlayer_project_id: Optional[str] = None,
        poll_interval: float = 2.0,
        poll_max_wait: float | None = None,
        sessions_per_technique: Optional[int] = 1,
    ) -> AsyncRedTeamSession:
        """Async version of RedTeamSessionsResource.start_session."""
        response = await self._client.evaluations.red_team.create(
            **_create_arguments(
                name=name,
                objective_ids=objective_ids,
                target_model=target_model,
                target_system_prompt=target_system_prompt,
                refusal_judge_model=refusal_judge_model,
                objective_judge_model=objective_judge_model,
                attacker_model=attacker_model,
                evaluation_report_model=evaluation_report_model,
                attacker_guidance=attacker_guidance,
                severity_mapping=severity_mapping,
                config_id=config_id,
                max_turns=max_turns,
                execution_strategy_type=execution_strategy_type,
                attacker_max_generation_attempts=attacker_max_generation_attempts,
                n_random_techniques=n_random_techniques,
                max_parallel_techniques=max_parallel_techniques,
                prompt_set_id=prompt_set_id,
                hiddenlayer_project_id=hiddenlayer_project_id,
                sessions_per_technique=sessions_per_technique,
            )
        )
        return AsyncRedTeamSession(
            client=self._client,
            workflow_id=response.workflow_id,
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
        """Async version of RedTeamSessionsResource.resume_session."""
        try:
            status = await self._client.evaluations.red_team.retrieve_status(workflow_id)
        except ApiError as e:
            if e.status_code == 404:
                raise _not_found(workflow_id) from e
            raise RedTeamSessionError(f"Failed to fetch workflow info: {e}") from e

        return AsyncRedTeamSession(
            client=self._client,
            workflow_id=workflow_id,
            name=status.name,
            poll_interval=poll_interval,
            poll_max_wait=poll_max_wait,
            max_parallel_techniques=1 if max_parallel_techniques is None else max_parallel_techniques,
        )

    async def terminate_session(self, workflow_id: str) -> None:
        """Async version of RedTeamSessionsResource.terminate_session."""
        try:
            await self._client.evaluations.red_team.terminate(workflow_id)
        except ApiError as e:
            if e.status_code == 404:
                raise _not_found(workflow_id) from e
            raise RedTeamSessionError(f"Failed to terminate workflow: {e}") from e
