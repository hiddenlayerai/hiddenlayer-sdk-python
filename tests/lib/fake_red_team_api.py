"""A scripted red team workflow behind httpx.MockTransport, and a clock for the sessions that poll it."""

from __future__ import annotations

import asyncio
import json
from typing import Any, Dict, List, Optional, Sequence, Union

import httpx

API_URL = "https://api.hiddenlayer.test"
WORKFLOW_ID = "0c1e7f52-9b3a-4d68-a5e1-2f4b6c8d0e9a"
NOT_READY: Dict[str, Any] = {"is_ready": False, "is_processing": True}
COMPLETE: Dict[str, Any] = {"is_ready": True, "action_type": "complete"}

_real_sleep = asyncio.sleep


def attack(session_id: Optional[str], prompt: str) -> Dict[str, Any]:
    return {
        "is_ready": True,
        "action_type": "attack_task",
        "session_id": session_id,
        "attack_prompt": prompt,
        "history": [{"role": "user", "content": "Hello"}],
        "target_system_prompt": "You are a bank's support assistant.",
    }


def failed(message: Optional[str]) -> Dict[str, Any]:
    return {"is_ready": True, "action_type": "failed", "message": message}


class FakeClock:
    """Stands in for the time module: a sleep moves the clock on and returns at once."""

    def __init__(self) -> None:
        self.now = 1000.0
        self.sleeps: List[float] = []

    def monotonic(self) -> float:
        return self.now

    def sleep(self, delay: float) -> None:
        self.sleeps.append(delay)
        self.now += delay

    async def async_sleep(self, delay: float) -> None:
        self.sleep(delay)
        await _real_sleep(0)


class FakeRedTeamApi:
    """Serves one workflow.

    Args:
        next_actions: What the next-action endpoint answers, call by call, as a body or an error
            status; the last one repeats.
        statuses: What the status endpoint answers, call by call, as a workflow status or an error
            status; the last one repeats.
        error: The workflow's error message, reported with its status.
        submit_status: What submitting a target response answers.
        terminate_status: What terminating the workflow answers.
    """

    def __init__(
        self,
        *,
        next_actions: Sequence[Union[Dict[str, Any], int]] = (COMPLETE,),
        statuses: Sequence[Union[str, int]] = ("COMPLETED",),
        error: Optional[str] = None,
        submit_status: int = 200,
        terminate_status: int = 204,
    ) -> None:
        self._next_actions = list(next_actions)
        self._statuses = list(statuses)
        self._error = error
        self._submit_status = submit_status
        self._terminate_status = terminate_status
        self.requests: List[httpx.Request] = []

    @property
    def transport(self) -> httpx.MockTransport:
        return httpx.MockTransport(self._handle)

    def calls(self, method: str, path: str) -> List[httpx.Request]:
        return [request for request in self.requests if request.method == method and request.url.path == path]

    def bodies(self, method: str, path: str) -> List[Dict[str, Any]]:
        return [json.loads(request.content) for request in self.calls(method, path)]

    @property
    def submitted(self) -> List[Dict[str, Any]]:
        return self.bodies("POST", f"/evaluations/v1/red-team/{WORKFLOW_ID}/target-response")

    def _handle(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        path, method = request.url.path, request.method
        workflow = f"/evaluations/v1/red-team/{WORKFLOW_ID}"
        if (method, path) == ("POST", "/evaluations/v1/red-team"):
            return httpx.Response(200, json={"workflow_id": WORKFLOW_ID, "run_id": "run-1"})
        if (method, path) == ("GET", f"{workflow}/next-action"):
            return self._scripted(self._next_actions)
        if (method, path) == ("GET", f"{workflow}/status"):
            return self._scripted(self._statuses)
        if (method, path) == ("POST", f"{workflow}/target-response"):
            if self._submit_status != 200:
                return self._error_response(self._submit_status)
            return httpx.Response(200, json={"is_ok": True, "message": "accepted"})
        if (method, path) == ("POST", f"/evaluations/v1/jobs/{WORKFLOW_ID}/termination"):
            if self._terminate_status != 204:
                return self._error_response(self._terminate_status)
            return httpx.Response(204)
        return httpx.Response(404, json={"detail": f"no route for {method} {path}"})

    def _scripted(self, answers: List[Any]) -> httpx.Response:
        answer = answers.pop(0) if len(answers) > 1 else answers[0]
        if isinstance(answer, int):
            return self._error_response(answer)
        if isinstance(answer, str):
            answer = {
                "workflow_id": WORKFLOW_ID,
                "run_id": "run-1",
                "status": answer,
                "name": "bank-assistant-red-team",
                "error": self._error,
            }
        return httpx.Response(200, json=answer)

    @staticmethod
    def _error_response(status: int) -> httpx.Response:
        return httpx.Response(status, json={"detail": f"scripted {status}"})
