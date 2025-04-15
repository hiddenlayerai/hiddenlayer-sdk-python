# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from pydantic import Field as FieldInfo

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = [
    "Node",
    "Label",
    "LabelProperties",
    "Location",
    "LocationAnnotation",
    "LocationAnnotationMessage",
    "LocationAnnotationMessageProperties",
    "LocationAnnotationProperties",
    "LocationAnnotationSnippet",
    "LocationAnnotationSnippetProperties",
    "LocationAnnotationSnippetRendered",
    "LocationAnnotationSnippetRenderedProperties",
    "LocationLogicalLocation",
    "LocationLogicalLocationProperties",
    "LocationMessage",
    "LocationMessageProperties",
    "LocationPhysicalLocation",
    "LocationPhysicalLocationAddress",
    "LocationPhysicalLocationAddressProperties",
    "LocationPhysicalLocationArtifactLocation",
    "LocationPhysicalLocationArtifactLocationDescription",
    "LocationPhysicalLocationArtifactLocationDescriptionProperties",
    "LocationPhysicalLocationArtifactLocationProperties",
    "LocationPhysicalLocationContextRegion",
    "LocationPhysicalLocationContextRegionMessage",
    "LocationPhysicalLocationContextRegionMessageProperties",
    "LocationPhysicalLocationContextRegionProperties",
    "LocationPhysicalLocationContextRegionSnippet",
    "LocationPhysicalLocationContextRegionSnippetProperties",
    "LocationPhysicalLocationContextRegionSnippetRendered",
    "LocationPhysicalLocationContextRegionSnippetRenderedProperties",
    "LocationPhysicalLocationProperties",
    "LocationPhysicalLocationRegion",
    "LocationPhysicalLocationRegionMessage",
    "LocationPhysicalLocationRegionMessageProperties",
    "LocationPhysicalLocationRegionProperties",
    "LocationPhysicalLocationRegionSnippet",
    "LocationPhysicalLocationRegionSnippetProperties",
    "LocationPhysicalLocationRegionSnippetRendered",
    "LocationPhysicalLocationRegionSnippetRenderedProperties",
    "LocationProperties",
    "LocationRelationship",
    "LocationRelationshipDescription",
    "LocationRelationshipDescriptionProperties",
    "LocationRelationshipProperties",
    "Properties",
]


class LabelProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class Label(BaseModel):
    id: Optional[str] = None
    """The identifier for this message."""

    arguments: Optional[List[str]] = None
    """An array of strings to substitute into the message string."""

    markdown: Optional[str] = None
    """A Markdown message string."""

    properties: Optional[LabelProperties] = None
    """Key/value pairs that provide additional information about the message."""

    text: Optional[str] = None
    """A plain text message string."""


class LocationAnnotationMessageProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class LocationAnnotationMessage(BaseModel):
    id: Optional[str] = None
    """The identifier for this message."""

    arguments: Optional[List[str]] = None
    """An array of strings to substitute into the message string."""

    markdown: Optional[str] = None
    """A Markdown message string."""

    properties: Optional[LocationAnnotationMessageProperties] = None
    """Key/value pairs that provide additional information about the message."""

    text: Optional[str] = None
    """A plain text message string."""


class LocationAnnotationProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class LocationAnnotationSnippetProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class LocationAnnotationSnippetRenderedProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class LocationAnnotationSnippetRendered(BaseModel):
    text: str
    """A plain text message string or format string."""

    markdown: Optional[str] = None
    """A Markdown message string or format string."""

    properties: Optional[LocationAnnotationSnippetRenderedProperties] = None
    """Key/value pairs that provide additional information about the message."""


class LocationAnnotationSnippet(BaseModel):
    binary: Optional[str] = None
    """
    MIME Base64-encoded content from a binary artifact, or from a text artifact in
    its original encoding.
    """

    properties: Optional[LocationAnnotationSnippetProperties] = None
    """Key/value pairs that provide additional information about the artifact content."""

    rendered: Optional[LocationAnnotationSnippetRendered] = None
    """
    An alternate rendered representation of the artifact (e.g., a decompiled
    representation of a binary region).
    """

    text: Optional[str] = None
    """UTF-8-encoded content from a text artifact."""


class LocationAnnotation(BaseModel):
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

    message: Optional[LocationAnnotationMessage] = None
    """A message relevant to the region."""

    properties: Optional[LocationAnnotationProperties] = None
    """Key/value pairs that provide additional information about the region."""

    snippet: Optional[LocationAnnotationSnippet] = None
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


class LocationLogicalLocationProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class LocationLogicalLocation(BaseModel):
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

    properties: Optional[LocationLogicalLocationProperties] = None
    """Key/value pairs that provide additional information about the logical location."""


class LocationMessageProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class LocationMessage(BaseModel):
    id: Optional[str] = None
    """The identifier for this message."""

    arguments: Optional[List[str]] = None
    """An array of strings to substitute into the message string."""

    markdown: Optional[str] = None
    """A Markdown message string."""

    properties: Optional[LocationMessageProperties] = None
    """Key/value pairs that provide additional information about the message."""

    text: Optional[str] = None
    """A plain text message string."""


class LocationPhysicalLocationAddressProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class LocationPhysicalLocationAddress(BaseModel):
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

    properties: Optional[LocationPhysicalLocationAddressProperties] = None
    """Key/value pairs that provide additional information about the address."""

    relative_address: Optional[int] = FieldInfo(alias="relativeAddress", default=None)
    """
    The address expressed as a byte offset from the absolute address of the top-most
    parent object.
    """


class LocationPhysicalLocationArtifactLocationDescriptionProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class LocationPhysicalLocationArtifactLocationDescription(BaseModel):
    id: Optional[str] = None
    """The identifier for this message."""

    arguments: Optional[List[str]] = None
    """An array of strings to substitute into the message string."""

    markdown: Optional[str] = None
    """A Markdown message string."""

    properties: Optional[LocationPhysicalLocationArtifactLocationDescriptionProperties] = None
    """Key/value pairs that provide additional information about the message."""

    text: Optional[str] = None
    """A plain text message string."""


class LocationPhysicalLocationArtifactLocationProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class LocationPhysicalLocationArtifactLocation(BaseModel):
    description: Optional[LocationPhysicalLocationArtifactLocationDescription] = None
    """A short description of the artifact location."""

    index: Optional[int] = None
    """
    The index within the run artifacts array of the artifact object associated with
    the artifact location.
    """

    properties: Optional[LocationPhysicalLocationArtifactLocationProperties] = None
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


class LocationPhysicalLocationContextRegionMessageProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class LocationPhysicalLocationContextRegionMessage(BaseModel):
    id: Optional[str] = None
    """The identifier for this message."""

    arguments: Optional[List[str]] = None
    """An array of strings to substitute into the message string."""

    markdown: Optional[str] = None
    """A Markdown message string."""

    properties: Optional[LocationPhysicalLocationContextRegionMessageProperties] = None
    """Key/value pairs that provide additional information about the message."""

    text: Optional[str] = None
    """A plain text message string."""


class LocationPhysicalLocationContextRegionProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class LocationPhysicalLocationContextRegionSnippetProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class LocationPhysicalLocationContextRegionSnippetRenderedProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class LocationPhysicalLocationContextRegionSnippetRendered(BaseModel):
    text: str
    """A plain text message string or format string."""

    markdown: Optional[str] = None
    """A Markdown message string or format string."""

    properties: Optional[LocationPhysicalLocationContextRegionSnippetRenderedProperties] = None
    """Key/value pairs that provide additional information about the message."""


class LocationPhysicalLocationContextRegionSnippet(BaseModel):
    binary: Optional[str] = None
    """
    MIME Base64-encoded content from a binary artifact, or from a text artifact in
    its original encoding.
    """

    properties: Optional[LocationPhysicalLocationContextRegionSnippetProperties] = None
    """Key/value pairs that provide additional information about the artifact content."""

    rendered: Optional[LocationPhysicalLocationContextRegionSnippetRendered] = None
    """
    An alternate rendered representation of the artifact (e.g., a decompiled
    representation of a binary region).
    """

    text: Optional[str] = None
    """UTF-8-encoded content from a text artifact."""


class LocationPhysicalLocationContextRegion(BaseModel):
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

    message: Optional[LocationPhysicalLocationContextRegionMessage] = None
    """A message relevant to the region."""

    properties: Optional[LocationPhysicalLocationContextRegionProperties] = None
    """Key/value pairs that provide additional information about the region."""

    snippet: Optional[LocationPhysicalLocationContextRegionSnippet] = None
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


class LocationPhysicalLocationProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class LocationPhysicalLocationRegionMessageProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class LocationPhysicalLocationRegionMessage(BaseModel):
    id: Optional[str] = None
    """The identifier for this message."""

    arguments: Optional[List[str]] = None
    """An array of strings to substitute into the message string."""

    markdown: Optional[str] = None
    """A Markdown message string."""

    properties: Optional[LocationPhysicalLocationRegionMessageProperties] = None
    """Key/value pairs that provide additional information about the message."""

    text: Optional[str] = None
    """A plain text message string."""


class LocationPhysicalLocationRegionProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class LocationPhysicalLocationRegionSnippetProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class LocationPhysicalLocationRegionSnippetRenderedProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class LocationPhysicalLocationRegionSnippetRendered(BaseModel):
    text: str
    """A plain text message string or format string."""

    markdown: Optional[str] = None
    """A Markdown message string or format string."""

    properties: Optional[LocationPhysicalLocationRegionSnippetRenderedProperties] = None
    """Key/value pairs that provide additional information about the message."""


class LocationPhysicalLocationRegionSnippet(BaseModel):
    binary: Optional[str] = None
    """
    MIME Base64-encoded content from a binary artifact, or from a text artifact in
    its original encoding.
    """

    properties: Optional[LocationPhysicalLocationRegionSnippetProperties] = None
    """Key/value pairs that provide additional information about the artifact content."""

    rendered: Optional[LocationPhysicalLocationRegionSnippetRendered] = None
    """
    An alternate rendered representation of the artifact (e.g., a decompiled
    representation of a binary region).
    """

    text: Optional[str] = None
    """UTF-8-encoded content from a text artifact."""


class LocationPhysicalLocationRegion(BaseModel):
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

    message: Optional[LocationPhysicalLocationRegionMessage] = None
    """A message relevant to the region."""

    properties: Optional[LocationPhysicalLocationRegionProperties] = None
    """Key/value pairs that provide additional information about the region."""

    snippet: Optional[LocationPhysicalLocationRegionSnippet] = None
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


class LocationPhysicalLocation(BaseModel):
    address: Optional[LocationPhysicalLocationAddress] = None
    """The address of the location."""

    artifact_location: Optional[LocationPhysicalLocationArtifactLocation] = FieldInfo(
        alias="artifactLocation", default=None
    )
    """The location of the artifact."""

    context_region: Optional[LocationPhysicalLocationContextRegion] = FieldInfo(alias="contextRegion", default=None)
    """Specifies a portion of the artifact that encloses the region.

    Allows a viewer to display additional context around the region.
    """

    properties: Optional[LocationPhysicalLocationProperties] = None
    """
    Key/value pairs that provide additional information about the physical location.
    """

    region: Optional[LocationPhysicalLocationRegion] = None
    """Specifies a portion of the artifact."""


class LocationProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class LocationRelationshipDescriptionProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class LocationRelationshipDescription(BaseModel):
    id: Optional[str] = None
    """The identifier for this message."""

    arguments: Optional[List[str]] = None
    """An array of strings to substitute into the message string."""

    markdown: Optional[str] = None
    """A Markdown message string."""

    properties: Optional[LocationRelationshipDescriptionProperties] = None
    """Key/value pairs that provide additional information about the message."""

    text: Optional[str] = None
    """A plain text message string."""


class LocationRelationshipProperties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class LocationRelationship(BaseModel):
    target: int
    """A reference to the related location."""

    description: Optional[LocationRelationshipDescription] = None
    """A description of the location relationship."""

    kinds: Optional[List[str]] = None
    """A set of distinct strings that categorize the relationship.

    Well-known kinds include 'includes', 'isIncludedBy' and 'relevant'.
    """

    properties: Optional[LocationRelationshipProperties] = None
    """
    Key/value pairs that provide additional information about the location
    relationship.
    """


class Location(BaseModel):
    id: Optional[int] = None
    """
    Value that distinguishes this location from all other locations within a single
    result object.
    """

    annotations: Optional[List[LocationAnnotation]] = None
    """A set of regions relevant to the location."""

    logical_locations: Optional[List[LocationLogicalLocation]] = FieldInfo(alias="logicalLocations", default=None)
    """The logical locations associated with the result."""

    message: Optional[LocationMessage] = None
    """A message relevant to the location."""

    physical_location: Optional[LocationPhysicalLocation] = FieldInfo(alias="physicalLocation", default=None)
    """Identifies the artifact and region."""

    properties: Optional[LocationProperties] = None
    """Key/value pairs that provide additional information about the location."""

    relationships: Optional[List[LocationRelationship]] = None
    """
    An array of objects that describe relationships between this location and
    others.
    """


class Properties(BaseModel):
    tags: Optional[List[str]] = None
    """A set of distinct strings that provide additional information."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class Node(BaseModel):
    id: str
    """A string that uniquely identifies the node within its graph."""

    children: Optional[List["Node"]] = None
    """Array of child nodes."""

    label: Optional[Label] = None
    """A short description of the node."""

    location: Optional[Location] = None
    """A code location associated with the node."""

    properties: Optional[Properties] = None
    """Key/value pairs that provide additional information about the node."""


if PYDANTIC_V2:
    Node.model_rebuild()
    Label.model_rebuild()
    LabelProperties.model_rebuild()
    Location.model_rebuild()
    LocationAnnotation.model_rebuild()
    LocationAnnotationMessage.model_rebuild()
    LocationAnnotationMessageProperties.model_rebuild()
    LocationAnnotationProperties.model_rebuild()
    LocationAnnotationSnippet.model_rebuild()
    LocationAnnotationSnippetProperties.model_rebuild()
    LocationAnnotationSnippetRendered.model_rebuild()
    LocationAnnotationSnippetRenderedProperties.model_rebuild()
    LocationLogicalLocation.model_rebuild()
    LocationLogicalLocationProperties.model_rebuild()
    LocationMessage.model_rebuild()
    LocationMessageProperties.model_rebuild()
    LocationPhysicalLocation.model_rebuild()
    LocationPhysicalLocationAddress.model_rebuild()
    LocationPhysicalLocationAddressProperties.model_rebuild()
    LocationPhysicalLocationArtifactLocation.model_rebuild()
    LocationPhysicalLocationArtifactLocationDescription.model_rebuild()
    LocationPhysicalLocationArtifactLocationDescriptionProperties.model_rebuild()
    LocationPhysicalLocationArtifactLocationProperties.model_rebuild()
    LocationPhysicalLocationContextRegion.model_rebuild()
    LocationPhysicalLocationContextRegionMessage.model_rebuild()
    LocationPhysicalLocationContextRegionMessageProperties.model_rebuild()
    LocationPhysicalLocationContextRegionProperties.model_rebuild()
    LocationPhysicalLocationContextRegionSnippet.model_rebuild()
    LocationPhysicalLocationContextRegionSnippetProperties.model_rebuild()
    LocationPhysicalLocationContextRegionSnippetRendered.model_rebuild()
    LocationPhysicalLocationContextRegionSnippetRenderedProperties.model_rebuild()
    LocationPhysicalLocationProperties.model_rebuild()
    LocationPhysicalLocationRegion.model_rebuild()
    LocationPhysicalLocationRegionMessage.model_rebuild()
    LocationPhysicalLocationRegionMessageProperties.model_rebuild()
    LocationPhysicalLocationRegionProperties.model_rebuild()
    LocationPhysicalLocationRegionSnippet.model_rebuild()
    LocationPhysicalLocationRegionSnippetProperties.model_rebuild()
    LocationPhysicalLocationRegionSnippetRendered.model_rebuild()
    LocationPhysicalLocationRegionSnippetRenderedProperties.model_rebuild()
    LocationProperties.model_rebuild()
    LocationRelationship.model_rebuild()
    LocationRelationshipDescription.model_rebuild()
    LocationRelationshipDescriptionProperties.model_rebuild()
    LocationRelationshipProperties.model_rebuild()
    Properties.model_rebuild()
else:
    Node.update_forward_refs()  # type: ignore
    Label.update_forward_refs()  # type: ignore
    LabelProperties.update_forward_refs()  # type: ignore
    Location.update_forward_refs()  # type: ignore
    LocationAnnotation.update_forward_refs()  # type: ignore
    LocationAnnotationMessage.update_forward_refs()  # type: ignore
    LocationAnnotationMessageProperties.update_forward_refs()  # type: ignore
    LocationAnnotationProperties.update_forward_refs()  # type: ignore
    LocationAnnotationSnippet.update_forward_refs()  # type: ignore
    LocationAnnotationSnippetProperties.update_forward_refs()  # type: ignore
    LocationAnnotationSnippetRendered.update_forward_refs()  # type: ignore
    LocationAnnotationSnippetRenderedProperties.update_forward_refs()  # type: ignore
    LocationLogicalLocation.update_forward_refs()  # type: ignore
    LocationLogicalLocationProperties.update_forward_refs()  # type: ignore
    LocationMessage.update_forward_refs()  # type: ignore
    LocationMessageProperties.update_forward_refs()  # type: ignore
    LocationPhysicalLocation.update_forward_refs()  # type: ignore
    LocationPhysicalLocationAddress.update_forward_refs()  # type: ignore
    LocationPhysicalLocationAddressProperties.update_forward_refs()  # type: ignore
    LocationPhysicalLocationArtifactLocation.update_forward_refs()  # type: ignore
    LocationPhysicalLocationArtifactLocationDescription.update_forward_refs()  # type: ignore
    LocationPhysicalLocationArtifactLocationDescriptionProperties.update_forward_refs()  # type: ignore
    LocationPhysicalLocationArtifactLocationProperties.update_forward_refs()  # type: ignore
    LocationPhysicalLocationContextRegion.update_forward_refs()  # type: ignore
    LocationPhysicalLocationContextRegionMessage.update_forward_refs()  # type: ignore
    LocationPhysicalLocationContextRegionMessageProperties.update_forward_refs()  # type: ignore
    LocationPhysicalLocationContextRegionProperties.update_forward_refs()  # type: ignore
    LocationPhysicalLocationContextRegionSnippet.update_forward_refs()  # type: ignore
    LocationPhysicalLocationContextRegionSnippetProperties.update_forward_refs()  # type: ignore
    LocationPhysicalLocationContextRegionSnippetRendered.update_forward_refs()  # type: ignore
    LocationPhysicalLocationContextRegionSnippetRenderedProperties.update_forward_refs()  # type: ignore
    LocationPhysicalLocationProperties.update_forward_refs()  # type: ignore
    LocationPhysicalLocationRegion.update_forward_refs()  # type: ignore
    LocationPhysicalLocationRegionMessage.update_forward_refs()  # type: ignore
    LocationPhysicalLocationRegionMessageProperties.update_forward_refs()  # type: ignore
    LocationPhysicalLocationRegionProperties.update_forward_refs()  # type: ignore
    LocationPhysicalLocationRegionSnippet.update_forward_refs()  # type: ignore
    LocationPhysicalLocationRegionSnippetProperties.update_forward_refs()  # type: ignore
    LocationPhysicalLocationRegionSnippetRendered.update_forward_refs()  # type: ignore
    LocationPhysicalLocationRegionSnippetRenderedProperties.update_forward_refs()  # type: ignore
    LocationProperties.update_forward_refs()  # type: ignore
    LocationRelationship.update_forward_refs()  # type: ignore
    LocationRelationshipDescription.update_forward_refs()  # type: ignore
    LocationRelationshipDescriptionProperties.update_forward_refs()  # type: ignore
    LocationRelationshipProperties.update_forward_refs()  # type: ignore
    Properties.update_forward_refs()  # type: ignore
