# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["RedTeamRetrieveNextActionResponse"]


class RedTeamRetrieveNextActionResponse(BaseModel):
    """Response from next-action polling endpoint."""

    is_ready: bool
    """Whether an action is ready"""

    action_type: Optional[str] = None
    """Type of action (e.g., "attack", "complete")"""

    attack_prompt: Optional[str] = None
    """Attack prompt to send to target"""

    history: Optional[List[Dict[str, object]]] = None
    """Conversation history"""

    is_processing: Optional[bool] = None
    """Whether processing is in progress"""

    message: Optional[str] = None
    """Status message"""

    session_id: Optional[str] = None
    """Session identifier"""

    target_system_prompt: Optional[str] = None
    """Target's system prompt"""

    turn: Optional[int] = None
    """Current turn number"""
