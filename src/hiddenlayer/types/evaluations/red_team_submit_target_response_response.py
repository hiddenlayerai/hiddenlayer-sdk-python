# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RedTeamSubmitTargetResponseResponse"]


class RedTeamSubmitTargetResponseResponse(BaseModel):
    """Response from submitting a target response."""

    is_ok: bool
    """Whether the submission was successful"""

    message: str
    """Human-readable status message"""

    error: Optional[str] = None
    """Error code if ok=false"""
