# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .message import Message
from ..._models import BaseModel
from .property_bag import PropertyBag
from .artifact_content import ArtifactContent

__all__ = ["Region"]


class Region(BaseModel):
    byte_length: Optional[int] = FieldInfo(alias="byteLength", default=None)
    """The length of the region in bytes."""

    byte_offset: Optional[int] = FieldInfo(alias="byteOffset", default=None)
    """
    The zero-based offset from the beginning of the artifact of the first byte in
    the region.
    """

    char_length: Optional[int] = FieldInfo(alias="charLength", default=None)
    """The length of the region in characters."""

    char_offset: Optional[int] = FieldInfo(alias="charOffset", default=None)
    """
    The zero-based offset from the beginning of the artifact of the first character
    in the region.
    """

    end_column: Optional[int] = FieldInfo(alias="endColumn", default=None)
    """The column number of the character following the end of the region."""

    end_line: Optional[int] = FieldInfo(alias="endLine", default=None)
    """The line number of the last character in the region."""

    message: Optional[Message] = None
    """A message relevant to the region."""

    properties: Optional[PropertyBag] = None
    """Key/value pairs that provide additional information about the region."""

    snippet: Optional[ArtifactContent] = None
    """The portion of the artifact contents within the specified region."""

    source_language: Optional[str] = FieldInfo(alias="sourceLanguage", default=None)
    """
    Specifies the source language, if any, of the portion of the artifact specified
    by the region object.
    """

    start_column: Optional[int] = FieldInfo(alias="startColumn", default=None)
    """The column number of the first character in the region."""

    start_line: Optional[int] = FieldInfo(alias="startLine", default=None)
    """The line number of the first character in the region."""
