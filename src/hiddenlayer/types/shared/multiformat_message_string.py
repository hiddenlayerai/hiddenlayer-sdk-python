# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .property_bag import PropertyBag

__all__ = ["MultiformatMessageString"]


class MultiformatMessageString(BaseModel):
    text: str
    """A plain text message string or format string."""

    markdown: Optional[str] = None
    """A Markdown message string or format string."""

    properties: Optional[PropertyBag] = None
    """Key/value pairs that provide additional information about the message."""
