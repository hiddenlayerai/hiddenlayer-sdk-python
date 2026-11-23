"""Evaluation sessions the SDK drives itself, reached as `client.evaluation_sessions`."""

from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from .red_team_session import AsyncRedTeamSessionsResource, RedTeamSessionsResource

if TYPE_CHECKING:
    from ..client import AsyncHiddenLayer, HiddenLayer


class EvaluationSessionsResource:
    def __init__(self, client: "HiddenLayer") -> None:
        self._client = client

    @cached_property
    def red_team(self) -> RedTeamSessionsResource:
        return RedTeamSessionsResource(client=self._client)


class AsyncEvaluationSessionsResource:
    def __init__(self, client: "AsyncHiddenLayer") -> None:
        self._client = client

    @cached_property
    def red_team(self) -> AsyncRedTeamSessionsResource:
        return AsyncRedTeamSessionsResource(client=self._client)
