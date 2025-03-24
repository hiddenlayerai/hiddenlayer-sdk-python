# coding: utf-8

"""
    HiddenLayer-API

    HiddenLayer-API

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from hiddenlayer.sdk.rest.models.property_bag import PropertyBag
from typing import Optional, Set
from typing_extensions import Self

class LogicalLocation(BaseModel):
    """
    A logical location of a construct that produced a result.
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Identifies the construct in which the result occurred. For example, this property might contain the name of a class or a method.")
    index: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=-1, description="The index within the logical locations array.")
    fully_qualified_name: Optional[StrictStr] = Field(default=None, description="The human-readable fully qualified name of the logical location.", alias="fullyQualifiedName")
    decorated_name: Optional[StrictStr] = Field(default=None, description="The machine-readable name for the logical location, such as a mangled function name provided by a C++ compiler that encodes calling convention, return type and other details along with the function name.", alias="decoratedName")
    parent_index: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=-1, description="Identifies the index of the immediate parent of the construct in which the result was detected. For example, this property might point to a logical location that represents the namespace that holds a type.", alias="parentIndex")
    kind: Optional[StrictStr] = Field(default=None, description="The type of construct this logical location component refers to. Should be one of 'function', 'member', 'module', 'namespace', 'parameter', 'resource', 'returnType', 'type', 'variable', 'object', 'array', 'property', 'value', 'element', 'text', 'attribute', 'comment', 'declaration', 'dtd' or 'processingInstruction', if any of those accurately describe the construct.")
    properties: Optional[PropertyBag] = None
    __properties: ClassVar[List[str]] = ["name", "index", "fullyQualifiedName", "decoratedName", "parentIndex", "kind", "properties"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of LogicalLocation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of properties
        if self.properties:
            _dict['properties'] = self.properties.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LogicalLocation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "index": obj.get("index") if obj.get("index") is not None else -1,
            "fullyQualifiedName": obj.get("fullyQualifiedName"),
            "decoratedName": obj.get("decoratedName"),
            "parentIndex": obj.get("parentIndex") if obj.get("parentIndex") is not None else -1,
            "kind": obj.get("kind"),
            "properties": PropertyBag.from_dict(obj["properties"]) if obj.get("properties") is not None else None
        })
        return _obj


