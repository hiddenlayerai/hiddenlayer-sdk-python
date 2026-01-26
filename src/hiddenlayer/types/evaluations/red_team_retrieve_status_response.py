# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RedTeamRetrieveStatusResponse"]


class RedTeamRetrieveStatusResponse(BaseModel):
    """Status of a red team workflow."""

    name: str
    """Workflow name"""

    run_id: str
    """Run identifier"""

    status: str
    """Workflow status"""

    workflow_id: str
    """Workflow identifier"""

    active_sessions: Optional[int] = None
    """Number of active sessions"""

    completed_sessions: Optional[int] = None
    """Number of completed sessions"""

    elapsed_seconds: Optional[float] = None
    """Elapsed time in seconds"""

    error: Optional[str] = None
    """Error message if failed"""

    eta_seconds: Optional[float] = None
    """Estimated time remaining in seconds"""

    failed_sessions: Optional[int] = None
    """Number of failed sessions"""

    message: Optional[str] = None
    """Status message"""

    percent_complete: Optional[float] = None
    """Percentage complete"""

    phase: Optional[str] = None
    """Current workflow phase"""

    progress_completed: Optional[int] = None
    """Completed progress items"""

    progress_percent: Optional[float] = None
    """Progress percentage"""

    progress_total: Optional[int] = None
    """Total progress items"""

    ready_prompts_in_queue: Optional[int] = None
    """Number of prompts ready in queue"""

    tenant_id: Optional[str] = None
    """Tenant identifier"""

    total_sessions: Optional[int] = None
    """Total number of sessions"""
