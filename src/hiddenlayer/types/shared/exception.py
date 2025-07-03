# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field as FieldInfo

from .region import Region
from .message import Message
from ..._compat import PYDANTIC_V2
from ..._models import BaseModel
from .property_bag import PropertyBag

__all__ = [
    "Exception",
    "Stack",
    "StackFrame",
    "StackFrameLocation",
    "StackFrameLocationLogicalLocation",
    "StackFrameLocationPhysicalLocation",
    "StackFrameLocationPhysicalLocationAddress",
    "StackFrameLocationPhysicalLocationArtifactLocation",
    "StackFrameLocationRelationship",
]


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

    properties: Optional[PropertyBag] = None
    """Key/value pairs that provide additional information about the logical location."""


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

    properties: Optional[PropertyBag] = None
    """Key/value pairs that provide additional information about the address."""

    relative_address: Optional[int] = FieldInfo(alias="relativeAddress", default=None)
    """
    The address expressed as a byte offset from the absolute address of the top-most
    parent object.
    """


class StackFrameLocationPhysicalLocationArtifactLocation(BaseModel):
    description: Optional[Message] = None
    """A short description of the artifact location."""

    index: Optional[int] = None
    """
    The index within the run artifacts array of the artifact object associated with
    the artifact location.
    """

    properties: Optional[PropertyBag] = None
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


class StackFrameLocationPhysicalLocation(BaseModel):
    address: Optional[StackFrameLocationPhysicalLocationAddress] = None
    """The address of the location."""

    artifact_location: Optional[StackFrameLocationPhysicalLocationArtifactLocation] = FieldInfo(
        alias="artifactLocation", default=None
    )
    """The location of the artifact."""

    context_region: Optional[Region] = FieldInfo(alias="contextRegion", default=None)
    """Specifies a portion of the artifact that encloses the region.

    Allows a viewer to display additional context around the region.
    """

    properties: Optional[PropertyBag] = None
    """
    Key/value pairs that provide additional information about the physical location.
    """

    region: Optional[Region] = None
    """Specifies a portion of the artifact."""


class StackFrameLocationRelationship(BaseModel):
    target: int
    """A reference to the related location."""

    description: Optional[Message] = None
    """A description of the location relationship."""

    kinds: Optional[List[str]] = None
    """A set of distinct strings that categorize the relationship.

    Well-known kinds include 'includes', 'isIncludedBy' and 'relevant'.
    """

    properties: Optional[PropertyBag] = None
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

    annotations: Optional[List[Region]] = None
    """A set of regions relevant to the location."""

    logical_locations: Optional[List[StackFrameLocationLogicalLocation]] = FieldInfo(
        alias="logicalLocations", default=None
    )
    """The logical locations associated with the result."""

    message: Optional[Message] = None
    """A message relevant to the location."""

    physical_location: Optional[StackFrameLocationPhysicalLocation] = FieldInfo(alias="physicalLocation", default=None)
    """Identifies the artifact and region."""

    properties: Optional[PropertyBag] = None
    """Key/value pairs that provide additional information about the location."""

    relationships: Optional[List[StackFrameLocationRelationship]] = None
    """
    An array of objects that describe relationships between this location and
    others.
    """


class StackFrame(BaseModel):
    location: Optional[StackFrameLocation] = None
    """The location to which this stack frame refers."""

    module: Optional[str] = None
    """The name of the module that contains the code of this stack frame."""

    parameters: Optional[List[str]] = None
    """The parameters of the call that is executing."""

    properties: Optional[PropertyBag] = None
    """Key/value pairs that provide additional information about the stack frame."""

    thread_id: Optional[int] = FieldInfo(alias="threadId", default=None)
    """The thread identifier of the stack frame."""


class Stack(BaseModel):
    frames: List[StackFrame]
    """
    An array of stack frames that represents a sequence of calls, rendered in
    reverse chronological order, that comprise the call stack.
    """

    message: Optional[Message] = None
    """A message relevant to this call stack."""

    properties: Optional[PropertyBag] = None
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

    properties: Optional[PropertyBag] = None
    """Key/value pairs that provide additional information about the exception."""

    stack: Optional[Stack] = None
    """The sequence of function calls leading to the exception."""


if PYDANTIC_V2:
    Exception.model_rebuild()
    Stack.model_rebuild()
    StackFrame.model_rebuild()
    StackFrameLocation.model_rebuild()
    StackFrameLocationLogicalLocation.model_rebuild()
    StackFrameLocationPhysicalLocation.model_rebuild()
    StackFrameLocationPhysicalLocationAddress.model_rebuild()
    StackFrameLocationPhysicalLocationArtifactLocation.model_rebuild()
    StackFrameLocationRelationship.model_rebuild()
else:
    Exception.update_forward_refs()  # type: ignore
    Stack.update_forward_refs()  # type: ignore
    StackFrame.update_forward_refs()  # type: ignore
    StackFrameLocation.update_forward_refs()  # type: ignore
    StackFrameLocationLogicalLocation.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocation.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocationAddress.update_forward_refs()  # type: ignore
    StackFrameLocationPhysicalLocationArtifactLocation.update_forward_refs()  # type: ignore
    StackFrameLocationRelationship.update_forward_refs()  # type: ignore
