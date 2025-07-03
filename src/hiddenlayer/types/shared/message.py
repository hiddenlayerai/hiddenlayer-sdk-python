# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .property_bag import PropertyBag

__all__ = ["Message"]


class Message(BaseModel):
    id: Optional[str] = None
    """The identifier for this message."""

    arguments: Optional[List[str]] = None
    """An array of strings to substitute into the message string."""

    markdown: Optional[str] = None
    """A Markdown message string."""

    properties: Optional[PropertyBag] = None
    """Key/value pairs that provide additional information about the message."""

    text: Optional[str] = None
    """A plain text message string."""
