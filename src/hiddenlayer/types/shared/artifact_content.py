# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .property_bag import PropertyBag
from .multiformat_message_string import MultiformatMessageString

__all__ = ["ArtifactContent"]


class ArtifactContent(BaseModel):
    binary: Optional[str] = None
    """
    MIME Base64-encoded content from a binary artifact, or from a text artifact in
    its original encoding.
    """

    properties: Optional[PropertyBag] = None
    """Key/value pairs that provide additional information about the artifact content."""

    rendered: Optional[MultiformatMessageString] = None
    """
    An alternate rendered representation of the artifact (e.g., a decompiled
    representation of a binary region).
    """

    text: Optional[str] = None
    """UTF-8-encoded content from a text artifact."""
