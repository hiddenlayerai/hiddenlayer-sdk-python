# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["RedTeamCreateParams"]


class RedTeamCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name for this evaluation"""

    target_model: Required[str]
    """Target model identifier"""

    attacker_max_generation_attempts: int
    """Maximum generation attempts for attacker"""

    attacker_model: str
    """Model for attacker"""

    evaluation_report_model: str
    """Model for evaluation report"""

    execution_strategy_type: str
    """Execution strategy type"""

    hl_project_id: str
    """HiddenLayer project ID"""

    max_parallel_techniques: int
    """Maximum parallel techniques"""

    max_turns: int
    """Maximum conversation turns"""

    n_random_techniques: int
    """Number of random techniques to use"""

    objective_ids: SequenceNotStr[str]
    """Objective IDs to evaluate"""

    objective_judge_model: str
    """Model for objective judging"""

    prompt_set_id: str
    """Prompt set ID for static prompt evaluation"""

    refusal_judge_model: str
    """Model for refusal judging"""

    sessions_per_technique: int
    """Number of sessions per technique"""

    target_system_prompt: str
    """System prompt for the target"""
