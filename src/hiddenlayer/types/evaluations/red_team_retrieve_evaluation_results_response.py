# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["RedTeamRetrieveEvaluationResultsResponse", "Result"]


class Result(BaseModel):
    """Full red team workflow result payload."""

    attacker_results: Optional[Dict[str, object]] = None
    """Detailed attacker session results including prompts, responses, and judgements"""

    evaluation_report: Optional[str] = None
    """Final evaluation report text"""

    name: Optional[str] = None
    """Workflow name"""

    report: Optional[Dict[str, object]] = None
    """Structured evaluation report with metrics and analysis"""

    settings: Optional[Dict[str, object]] = None
    """Workflow configuration settings used for this evaluation"""

    target_context: Optional[str] = None
    """Target context description"""

    usage: Optional[Dict[str, object]] = None
    """Token usage statistics across all models"""


class RedTeamRetrieveEvaluationResultsResponse(BaseModel):
    """Complete result of a red team workflow."""

    result: Result
    """Full red team workflow result payload."""

    run_id: str
    """Run identifier"""

    workflow_id: str
    """Workflow identifier"""

    status: Optional[str] = None
    """Workflow status (e.g., "completed")"""
