# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["RedTeamCreateResponse"]


class RedTeamCreateResponse(BaseModel):
    """Response from starting a workflow."""

    run_id: str
    """Run identifier"""

    workflow_id: str
    """Workflow identifier"""
