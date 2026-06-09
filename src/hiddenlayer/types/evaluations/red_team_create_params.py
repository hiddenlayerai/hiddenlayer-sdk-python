# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["RedTeamCreateParams"]


class RedTeamCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name for this evaluation"""

    attacker_guidance: str
    """
    Optional intent-only natural-language text the operator supplies to focus the
    attacker LLM within the configured APE objectives. Example: "try to get the
    model to recommend candy with nuts to a user who's allergic to nuts."

    Sanitized server-side: input is NFKC-normalized, trimmed, and checked against a
    strict character whitelist (ASCII letters, digits, spaces/newlines/tabs, and
    sentence-level punctuation `. , ? ! ' " - : ; ( )`). Inputs containing
    XML/JSON/code/control/markdown characters are rejected with 422.

    No-op for the `STATIC_PROMPT_SET` execution strategy.
    """

    attacker_max_generation_attempts: int
    """Internal override; service default applies if omitted.

    Maximum number of generation attempts for the attacker model per turn.
    """

    attacker_model: str
    """Internal override; service default applies if omitted."""

    config_id: str
    """
    Optional preset config (see /evaluations/v1/red-team/configs) to seed the
    workflow settings. Any field also present in this body overrides the
    corresponding value from the config.
    """

    evaluation_report_model: str
    """Internal override; service default applies if omitted."""

    execution_strategy_type: Literal["RANDOM", "SINGLE", "STATIC_PROMPT_SET"]
    """Execution strategy type"""

    hl_project_id: str
    """HiddenLayer project UUID or alias"""

    max_parallel_techniques: int
    """Maximum parallel techniques"""

    max_turns: int
    """Maximum conversation turns"""

    n_random_techniques: int
    """Number of random techniques to use"""

    objective_ids: SequenceNotStr[str]
    """Objective IDs to evaluate"""

    objective_judge_model: str
    """Internal override; service default applies if omitted."""

    prompt_set_id: str
    """Prompt set UUID (built-in catalog or tenant DB)"""

    refusal_judge_model: str
    """Internal override; service default applies if omitted."""

    sessions_per_technique: int
    """Number of sessions per technique"""

    severity_mapping: Dict[str, Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "NONE"]]
    """Map from objective ID to a severity level.

    Determines the per-session severity derived from the worst objective achieved
    during a red team session.

    Keys must be objective IDs known to this service; unknown keys are rejected at
    validation time. Limited to 256 entries.
    """

    target_model: str
    """Target model identifier.

    Freeform for the client-driven workflow: the client owns and drives its own
    target, so this is NOT validated against the servable-model catalog. (The
    simulated start and config presets do validate against the catalog.)
    """

    target_system_prompt: str
    """System prompt for the target"""
