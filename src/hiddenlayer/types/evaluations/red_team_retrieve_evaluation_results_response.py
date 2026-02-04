# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from ..._models import BaseModel

__all__ = ["RedTeamRetrieveEvaluationResultsResponse"]


class RedTeamRetrieveEvaluationResultsResponse(BaseModel):
    """Complete result of a workflow."""

    result: Dict[str, object]
    """Full workflow result payload"""

    run_id: str
    """Run identifier"""

    workflow_id: str
    """Workflow identifier"""
