# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from pydantic import Field as FieldInfo

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = [
    "Exception",
    "Properties",
    "Stack",
    "StackFrame",
    "StackFrameLocation",
    "StackFrameLocationAnnotation",
    "StackFrameLocationAnnotationMessage",
    "StackFrameLocationAnnotationMessageProperties",
    "StackFrameLocationAnnotationProperties",
    "StackFrameLocationAnnotationSnippet",
    "StackFrameLocationAnnotationSnippetProperties",
    "StackFrameLocationAnnotationSnippetRendered",
    "StackFrameLocationAnnotationSnippetRenderedProperties",
    "StackFrameLocationLogicalLocation",
    "StackFrameLocationLogicalLocationProperties",
    "StackFrameLocationMessage",
    "StackFrameLocationMessageProperties",
    "StackFrameLocationPhysicalLocation",
    "StackFrameLocationPhysicalLocationAddress",
    "StackFrameLocationPhysicalLocationAddressProperties",
    "StackFrameLocationPhysicalLocationArtifactLocation",
    "StackFrameLocationPhysicalLocationArtifactLocationDescription",
    "StackFrameLocationPhysicalLocationArtifactLocationDescriptionProperties",
    "StackFrameLocationPhysicalLocationArtifactLocationProperties",
    "StackFrameLocationPhysicalLocationContextRegion",
    "StackFrameLocationPhysicalLocationContextRegionMessage",
    "StackFrameLocationPhysicalLocationContextRegionMessageProperties",
    "StackFrameLocationPhysicalLocationContextRegionProperties",
    "StackFrameLocationPhysicalLocationContextRegionSnippet",
    "StackFrameLocationPhysicalLocationContextRegionSnippetProperties",
    "StackFrameLocationPhysicalLocationContextRegionSnippetRendered",
    "StackFrameLocationPhysicalLocationContextRegionSnippetRenderedProperties",
    "StackFrameLocationPhysicalLocationProperties",
    "StackFrameLocationPhysicalLocationRegion",
    "StackFrameLocationPhysicalLocationRegionMessage",
    "StackFrameLocationPhysicalLocationRegionMessageProperties",
    "StackFrameLocationPhysicalLocationRegionProperties",
    "StackFrameLocationPhysicalLocationRegionSnippet",
    "StackFrameLocationPhysicalLocationRegionSnippetProperties",
    "StackFrameLocationPhysicalLocationRegionSnippetRendered",
    "StackFrameLocationPhysicalLocationRegionSnippetRenderedProperties",
    "StackFrameLocationProperties",
    "StackFrameLocationRelationship",
    "StackFrameLocationRelationshipDescription",
    "StackFrameLocationRelationshipDescriptionProperties",
    "StackFrameLocationRelationshipProperties",
    "StackFrameProperties",
    "StackMessage",
    "StackMessageProperties",
    "StackProperties",
]


class Properties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class StackFrameLocationAnnotationMessageProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class StackFrameLocationAnnotationMessage(BaseModel):
    id: Optional[str] = None
    """The identifier for this message."""

    arguments: Optional[List[str]] = None
    """An array of strings to substitute into the message string."""

    markdown: Optional[str] = None
    """A Markdown message string."""

    properties: Optional[StackFrameLocationAnnotationMessageProperties] = None
    """Key/value pairs that provide additional information about the message."""

    text: Optional[str] = None
    """A plain text message string."""


class StackFrameLocationAnnotationProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class StackFrameLocationAnnotationSnippetProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class StackFrameLocationAnnotationSnippetRenderedProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class StackFrameLocationAnnotationSnippetRendered(BaseModel):
    text: str
    """A plain text message string or format string."""

    markdown: Optional[str] = None
    """A Markdown message string or format string."""

    properties: Optional[StackFrameLocationAnnotationSnippetRenderedProperties] = None
    """Key/value pairs that provide additional information about the message."""


class StackFrameLocationAnnotationSnippet(BaseModel):
    binary: Optional[str] = None
    """
    MIME Base64-encoded content from a binary artifact, or from a text artifact in
    its original encoding.
    """

    properties: Optional[StackFrameLocationAnnotationSnippetProperties] = None
    """Key/value pairs that provide additional information about the artifact content."""

    rendered: Optional[StackFrameLocationAnnotationSnippetRendered] = None
    """
    An alternate rendered representation of the artifact (e.g., a decompiled
    representation of a binary region).
    """

    text: Optional[str] = None
    """UTF-8-encoded content from a text artifact."""


class StackFrameLocationAnnotation(BaseModel):
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

    message: Optional[StackFrameLocationAnnotationMessage] = None
    """A message relevant to the region."""

    properties: Optional[StackFrameLocationAnnotationProperties] = None
    """Key/value pairs that provide additional information about the region."""

    snippet: Optional[StackFrameLocationAnnotationSnippet] = None
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


class StackFrameLocationLogicalLocationProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class StackFrameLocationLogicalLocation(BaseModel):
    decorated_name: Optional[str] = FieldInfo(alias="decoratedName", default=None)
    """
    The machine-readable name for the logical location, such as a mangled function
    name provided by a C++ compiler that encodes calling convention, return type and
    other details along with the function name.
    """

    fully_qualified_name: Optional[str] = FieldInfo(alias="fullyQualifiedName", default=None)
    """The human-readable fully qualified name of the logical location."""

    index: Optional[int] = None
    """The index within the logical locations array."""

    kind: Optional[str] = None
    """The type of construct this logical location component refers to.

    Should be one of 'function', 'member', 'module', 'namespace', 'parameter',
    'resource', 'returnType', 'type', 'variable', 'object', 'array', 'property',
    'value', 'element', 'text', 'attribute', 'comment', 'declaration', 'dtd' or
    'processingInstruction', if any of those accurately describe the construct.
    """

    name: Optional[str] = None
    """Identifies the construct in which the result occurred.

    For example, this property might contain the name of a class or a method.
    """

    parent_index: Optional[int] = FieldInfo(alias="parentIndex", default=None)
    """
    Identifies the index of the immediate parent of the construct in which the
    result was detected. For example, this property might point to a logical
    location that represents the namespace that holds a type.
    """

    properties: Optional[StackFrameLocationLogicalLocationProperties] = None
    """Key/value pairs that provide additional information about the logical location."""


class StackFrameLocationMessageProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class StackFrameLocationMessage(BaseModel):
    id: Optional[str] = None
    """The identifier for this message."""

    arguments: Optional[List[str]] = None
    """An array of strings to substitute into the message string."""

    markdown: Optional[str] = None
    """A Markdown message string."""

    properties: Optional[StackFrameLocationMessageProperties] = None
    """Key/value pairs that provide additional information about the message."""

    text: Optional[str] = None
    """A plain text message string."""


class StackFrameLocationPhysicalLocationAddressProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class StackFrameLocationPhysicalLocationAddress(BaseModel):
    absolute_address: Optional[int] = FieldInfo(alias="absoluteAddress", default=None)
    """
    The address expressed as a byte offset from the start of the addressable region.
    """

    fully_qualified_name: Optional[str] = FieldInfo(alias="fullyQualifiedName", default=None)
    """A human-readable fully qualified name that is associated with the address."""

    index: Optional[int] = None
    """The index within run.addresses of the cached object for this address."""

    kind: Optional[str] = None
    """An open-ended string that identifies the address kind.

    'data', 'function', 'header','instruction', 'module', 'page', 'section',
    'segment', 'stack', 'stackFrame', 'table' are well-known values.
    """

    length: Optional[int] = None
    """The number of bytes in this range of addresses."""

    name: Optional[str] = None
    """A name that is associated with the address, e.g., '.text'."""

    offset_from_parent: Optional[int] = FieldInfo(alias="offsetFromParent", default=None)
    """
    The byte offset of this address from the absolute or relative address of the
    parent object.
    """

    parent_index: Optional[int] = FieldInfo(alias="parentIndex", default=None)
    """The index within run.addresses of the parent object."""

    properties: Optional[StackFrameLocationPhysicalLocationAddressProperties] = None
    """Key/value pairs that provide additional information about the address."""

    relative_address: Optional[int] = FieldInfo(alias="relativeAddress", default=None)
    """
    The address expressed as a byte offset from the absolute address of the top-most
    parent object.
    """


class StackFrameLocationPhysicalLocationArtifactLocationDescriptionProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class StackFrameLocationPhysicalLocationArtifactLocationDescription(BaseModel):
    id: Optional[str] = None
    """The identifier for this message."""

    arguments: Optional[List[str]] = None
    """An array of strings to substitute into the message string."""

    markdown: Optional[str] = None
    """A Markdown message string."""

    properties: Optional[StackFrameLocationPhysicalLocationArtifactLocationDescriptionProperties] = None
    """Key/value pairs that provide additional information about the message."""

    text: Optional[str] = None
    """A plain text message string."""


class StackFrameLocationPhysicalLocationArtifactLocationProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class StackFrameLocationPhysicalLocationArtifactLocation(BaseModel):
    description: Optional[StackFrameLocationPhysicalLocationArtifactLocationDescription] = None
    """A short description of the artifact location."""

    index: Optional[int] = None
    """
    The index within the run artifacts array of the artifact object associated with
    the artifact location.
    """

    properties: Optional[StackFrameLocationPhysicalLocationArtifactLocationProperties] = None
    """
    Key/value pairs that provide additional information about the artifact location.
    """

    uri: Optional[str] = None
    """A string containing a valid relative or absolute URI."""

    uri_base_id: Optional[str] = FieldInfo(alias="uriBaseId", default=None)
    """
    A string which indirectly specifies the absolute URI with respect to which a
    relative URI in the "uri" property is interpreted.
    """


class StackFrameLocationPhysicalLocationContextRegionMessageProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class StackFrameLocationPhysicalLocationContextRegionMessage(BaseModel):
    id: Optional[str] = None
    """The identifier for this message."""

    arguments: Optional[List[str]] = None
    """An array of strings to substitute into the message string."""

    markdown: Optional[str] = None
    """A Markdown message string."""

    properties: Optional[StackFrameLocationPhysicalLocationContextRegionMessageProperties] = None
    """Key/value pairs that provide additional information about the message."""

    text: Optional[str] = None
    """A plain text message string."""


class StackFrameLocationPhysicalLocationContextRegionProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class StackFrameLocationPhysicalLocationContextRegionSnippetProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class StackFrameLocationPhysicalLocationContextRegionSnippetRenderedProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class StackFrameLocationPhysicalLocationContextRegionSnippetRendered(BaseModel):
    text: str
    """A plain text message string or format string."""

    markdown: Optional[str] = None
    """A Markdown message string or format string."""

    properties: Optional[StackFrameLocationPhysicalLocationContextRegionSnippetRenderedProperties] = None
    """Key/value pairs that provide additional information about the message."""


class StackFrameLocationPhysicalLocationContextRegionSnippet(BaseModel):
    binary: Optional[str] = None
    """
    MIME Base64-encoded content from a binary artifact, or from a text artifact in
    its original encoding.
    """

    properties: Optional[StackFrameLocationPhysicalLocationContextRegionSnippetProperties] = None
    """Key/value pairs that provide additional information about the artifact content."""

    rendered: Optional[StackFrameLocationPhysicalLocationContextRegionSnippetRendered] = None
    """
    An alternate rendered representation of the artifact (e.g., a decompiled
    representation of a binary region).
    """

    text: Optional[str] = None
    """UTF-8-encoded content from a text artifact."""


class StackFrameLocationPhysicalLocationContextRegion(BaseModel):
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

    message: Optional[StackFrameLocationPhysicalLocationContextRegionMessage] = None
    """A message relevant to the region."""

    properties: Optional[StackFrameLocationPhysicalLocationContextRegionProperties] = None
    """Key/value pairs that provide additional information about the region."""

    snippet: Optional[StackFrameLocationPhysicalLocationContextRegionSnippet] = None
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


class StackFrameLocationPhysicalLocationProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class StackFrameLocationPhysicalLocationRegionMessageProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class StackFrameLocationPhysicalLocationRegionMessage(BaseModel):
    id: Optional[str] = None
    """The identifier for this message."""

    arguments: Optional[List[str]] = None
    """An array of strings to substitute into the message string."""

    markdown: Optional[str] = None
    """A Markdown message string."""

    properties: Optional[StackFrameLocationPhysicalLocationRegionMessageProperties] = None
    """Key/value pairs that provide additional information about the message."""

    text: Optional[str] = None
    """A plain text message string."""


class StackFrameLocationPhysicalLocationRegionProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class StackFrameLocationPhysicalLocationRegionSnippetProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class StackFrameLocationPhysicalLocationRegionSnippetRenderedProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class StackFrameLocationPhysicalLocationRegionSnippetRendered(BaseModel):
    text: str
    """A plain text message string or format string."""

    markdown: Optional[str] = None
    """A Markdown message string or format string."""

    properties: Optional[StackFrameLocationPhysicalLocationRegionSnippetRenderedProperties] = None
    """Key/value pairs that provide additional information about the message."""


class StackFrameLocationPhysicalLocationRegionSnippet(BaseModel):
    binary: Optional[str] = None
    """
    MIME Base64-encoded content from a binary artifact, or from a text artifact in
    its original encoding.
    """

    properties: Optional[StackFrameLocationPhysicalLocationRegionSnippetProperties] = None
    """Key/value pairs that provide additional information about the artifact content."""

    rendered: Optional[StackFrameLocationPhysicalLocationRegionSnippetRendered] = None
    """
    An alternate rendered representation of the artifact (e.g., a decompiled
    representation of a binary region).
    """

    text: Optional[str] = None
    """UTF-8-encoded content from a text artifact."""


class StackFrameLocationPhysicalLocationRegion(BaseModel):
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

    message: Optional[StackFrameLocationPhysicalLocationRegionMessage] = None
    """A message relevant to the region."""

    properties: Optional[StackFrameLocationPhysicalLocationRegionProperties] = None
    """Key/value pairs that provide additional information about the region."""

    snippet: Optional[StackFrameLocationPhysicalLocationRegionSnippet] = None
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


class StackFrameLocationPhysicalLocation(BaseModel):
    address: Optional[StackFrameLocationPhysicalLocationAddress] = None
    """The address of the location."""

    artifact_location: Optional[StackFrameLocationPhysicalLocationArtifactLocation] = FieldInfo(
        alias="artifactLocation", default=None
    )
    """The location of the artifact."""

    context_region: Optional[StackFrameLocationPhysicalLocationContextRegion] = FieldInfo(
        alias="contextRegion", default=None
    )
    """Specifies a portion of the artifact that encloses the region.

    Allows a viewer to display additional context around the region.
    """

    properties: Optional[StackFrameLocationPhysicalLocationProperties] = None
    """
    Key/value pairs that provide additional information about the physical location.
    """

    region: Optional[StackFrameLocationPhysicalLocationRegion] = None
    """Specifies a portion of the artifact."""


class StackFrameLocationProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class StackFrameLocationRelationshipDescriptionProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class StackFrameLocationRelationshipDescription(BaseModel):
    id: Optional[str] = None
    """The identifier for this message."""

    arguments: Optional[List[str]] = None
    """An array of strings to substitute into the message string."""

    markdown: Optional[str] = None
    """A Markdown message string."""

    properties: Optional[StackFrameLocationRelationshipDescriptionProperties] = None
    """Key/value pairs that provide additional information about the message."""

    text: Optional[str] = None
    """A plain text message string."""


class StackFrameLocationRelationshipProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class StackFrameLocationRelationship(BaseModel):
    target: int
    """A reference to the related location."""

    description: Optional[StackFrameLocationRelationshipDescription] = None
    """A description of the location relationship."""

    kinds: Optional[List[str]] = None
    """A set of distinct strings that categorize the relationship.

    Well-known kinds include 'includes', 'isIncludedBy' and 'relevant'.
    """

    properties: Optional[StackFrameLocationRelationshipProperties] = None
    """
    Key/value pairs that provide additional information about the location
    relationship.
    """


class StackFrameLocation(BaseModel):
    id: Optional[int] = None
    """
    Value that distinguishes this location from all other locations within a single
    result object.
    """

    annotations: Optional[List[StackFrameLocationAnnotation]] = None
    """A set of regions relevant to the location."""

    logical_locations: Optional[List[StackFrameLocationLogicalLocation]] = FieldInfo(
        alias="logicalLocations", default=None
    )
    """The logical locations associated with the result."""

    message: Optional[StackFrameLocationMessage] = None
    """A message relevant to the location."""

    physical_location: Optional[StackFrameLocationPhysicalLocation] = FieldInfo(alias="physicalLocation", default=None)
    """Identifies the artifact and region."""

    properties: Optional[StackFrameLocationProperties] = None
    """Key/value pairs that provide additional information about the location."""

    relationships: Optional[List[StackFrameLocationRelationship]] = None
    """
    An array of objects that describe relationships between this location and
    others.
    """


class StackFrameProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class StackFrame(BaseModel):
    location: Optional[StackFrameLocation] = None
    """The location to which this stack frame refers."""

    module: Optional[str] = None
    """The name of the module that contains the code of this stack frame."""

    parameters: Optional[List[str]] = None
    """The parameters of the call that is executing."""

    properties: Optional[StackFrameProperties] = None
    """Key/value pairs that provide additional information about the stack frame."""

    thread_id: Optional[int] = FieldInfo(alias="threadId", default=None)
    """The thread identifier of the stack frame."""


class StackMessageProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class StackMessage(BaseModel):
    id: Optional[str] = None
    """The identifier for this message."""

    arguments: Optional[List[str]] = None
    """An array of strings to substitute into the message string."""

    markdown: Optional[str] = None
    """A Markdown message string."""

    properties: Optional[StackMessageProperties] = None
    """Key/value pairs that provide additional information about the message."""

    text: Optional[str] = None
    """A plain text message string."""


class StackProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class Stack(BaseModel):
    frames: List[StackFrame]
    """
    An array of stack frames that represents a sequence of calls, rendered in
    reverse chronological order, that comprise the call stack.
    """

    message: Optional[StackMessage] = None
    """A message relevant to this call stack."""

    properties: Optional[StackProperties] = None
    """Key/value pairs that provide additional information about the stack."""


class Exception(BaseModel):
    inner_exceptions: Optional[List["Exception"]] = FieldInfo(alias="innerExceptions", default=None)
    """
    An array of exception objects each of which is considered a cause of this
    exception.
    """

    kind: Optional[str] = None
    """
    A string that identifies the kind of exception, for example, the fully qualified
    type name of an object that was thrown, or the symbolic name of a signal.
    """

    message: Optional[str] = None
    """A message that describes the exception."""

    properties: Optional[Properties] = None
    """Key/value pairs that provide additional information about the exception."""

    stack: Optional[Stack] = None
    """The sequence of function calls leading to the exception."""


if PYDANTIC_V2:
    Exception.model_rebuild()
    Properties.model_rebuild()
    Stack.model_rebuild()
    StackFrame.model_rebuild()
    StackFrameLocation.model_rebuild()
    StackFrameLocationAnnotation.model_rebuild()
    StackFrameLocationAnnotationMessage.model_rebuild()
    StackFrameLocationAnnotationMessageProperties.model_rebuild()
    StackFrameLocationAnnotationProperties.model_rebuild()
    StackFrameLocationAnnotationSnippet.model_rebuild()
    StackFrameLocationAnnotationSnippetProperties.model_rebuild()
    StackFrameLocationAnnotationSnippetRendered.model_rebuild()
    StackFrameLocationAnnotationSnippetRenderedProperties.model_rebuild()
    StackFrameLocationLogicalLocation.model_rebuild()
    StackFrameLocationLogicalLocationProperties.model_rebuild()
    StackFrameLocationMessage.model_rebuild()
    StackFrameLocationMessageProperties.model_rebuild()
    StackFrameLocationPhysicalLocation.model_rebuild()
    StackFrameLocationPhysicalLocationAddress.model_rebuild()
    StackFrameLocationPhysicalLocationAddressProperties.model_rebuild()
    StackFrameLocationPhysicalLocationArtifactLocation.model_rebuild()
    StackFrameLocationPhysicalLocationArtifactLocationDescription.model_rebuild()
    StackFrameLocationPhysicalLocationArtifactLocationDescriptionProperties.model_rebuild()
    StackFrameLocationPhysicalLocationArtifactLocationProperties.model_rebuild()
    StackFrameLocationPhysicalLocationContextRegion.model_rebuild()
    StackFrameLocationPhysicalLocationContextRegionMessage.model_rebuild()
    StackFrameLocationPhysicalLocationContextRegionMessageProperties.model_rebuild()
    StackFrameLocationPhysicalLocationContextRegionProperties.model_rebuild()
    StackFrameLocationPhysicalLocationContextRegionSnippet.model_rebuild()
    StackFrameLocationPhysicalLocationContextRegionSnippetProperties.model_rebuild()
    StackFrameLocationPhysicalLocationContextRegionSnippetRendered.model_rebuild()
    StackFrameLocationPhysicalLocationContextRegionSnippetRenderedProperties.model_rebuild()
    StackFrameLocationPhysicalLocationProperties.model_rebuild()
    StackFrameLocationPhysicalLocationRegion.model_rebuild()
    StackFrameLocationPhysicalLocationRegionMessage.model_rebuild()
    StackFrameLocationPhysicalLocationRegionMessageProperties.model_rebuild()
    StackFrameLocationPhysicalLocationRegionProperties.model_rebuild()
    StackFrameLocationPhysicalLocationRegionSnippet.model_rebuild()
    StackFrameLocationPhysicalLocationRegionSnippetProperties.model_rebuild()
    StackFrameLocationPhysicalLocationRegionSnippetRendered.model_rebuild()
    StackFrameLocationPhysicalLocationRegionSnippetRenderedProperties.model_rebuild()
    StackFrameLocationProperties.model_rebuild()
    StackFrameLocationRelationship.model_rebuild()
    StackFrameLocationRelationshipDescription.model_rebuild()
    StackFrameLocationRelationshipDescriptionProperties.model_rebuild()
    StackFrameLocationRelationshipProperties.model_rebuild()
    StackFrameProperties.model_rebuild()
    StackMessage.model_rebuild()
    StackMessageProperties.model_rebuild()
    StackProperties.model_rebuild()
else:
    Exception.update_forward_refs()  # type: ignore
    Properties.update_forward_refs()  # type: ignore
    Stack.update_forward_refs()  # type: ignore
    StackFrame.update_forward_refs()  # type: ignore
    StackFrameLocation.update_forward_refs()  # type: ignore
    StackFrameLocationAnnotation.update_forward_refs()  # type: ignore
    StackFrameLocationAnnotationMessage.update_forward_refs()  # type: ignore
    StackFrameLocationAnnotationMessageProperties.update_forward_refs()  # type: ignore
    StackFrameLocationAnnotationProperties.update_forward_refs()  # type: ignore
    StackFrameLocationAnnotationSnippet.update_forward_refs()  # type: ignore
    StackFrameLocationAnnotationSnippetProperties.update_forward_refs()  # type: ignore
    StackFrameLocationAnnotationSnippetRendered.update_forward_refs()  # type: ignore
    StackFrameLocationAnnotationSnippetRenderedProperties.update_forward_refs()  # type: ignore
    StackFrameLocationLogicalLocation.update_forward_refs()  # type: ignore
    StackFrameLocationLogicalLocationProperties.update_forward_refs()  # type: ignore
    StackFrameLocationMessage.update_forward_refs()  # type: ignore
    StackFrameLocationMessageProperties.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocation.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocationAddress.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocationAddressProperties.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocationArtifactLocation.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocationArtifactLocationDescription.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocationArtifactLocationDescriptionProperties.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocationArtifactLocationProperties.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocationContextRegion.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocationContextRegionMessage.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocationContextRegionMessageProperties.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocationContextRegionProperties.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocationContextRegionSnippet.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocationContextRegionSnippetProperties.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocationContextRegionSnippetRendered.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocationContextRegionSnippetRenderedProperties.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocationProperties.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocationRegion.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocationRegionMessage.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocationRegionMessageProperties.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocationRegionProperties.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocationRegionSnippet.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocationRegionSnippetProperties.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocationRegionSnippetRendered.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocationRegionSnippetRenderedProperties.update_forward_refs()  # type: ignore
    StackFrameLocationProperties.update_forward_refs()  # type: ignore
    StackFrameLocationRelationship.update_forward_refs()  # type: ignore
    StackFrameLocationRelationshipDescription.update_forward_refs()  # type: ignore
    StackFrameLocationRelationshipDescriptionProperties.update_forward_refs()  # type: ignore
    StackFrameLocationRelationshipProperties.update_forward_refs()  # type: ignore
    StackFrameProperties.update_forward_refs()  # type: ignore
    StackMessage.update_forward_refs()  # type: ignore
    StackMessageProperties.update_forward_refs()  # type: ignore
    StackProperties.update_forward_refs()  # type: ignore
