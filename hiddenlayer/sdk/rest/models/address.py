# coding: utf-8

"""
    HiddenLayer Sensor SOR

    HiddenLayer Sensor SOR API for operations to sensor data storage

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from hiddenlayer.sdk.rest.models.property_bag import PropertyBag
from typing import Optional, Set
from typing_extensions import Self

class Address(BaseModel):
    """
    A physical or virtual address, or a range of addresses, in an 'addressable region' (memory or a binary file).
    """ # noqa: E501
    absolute_address: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=-1, description="The address expressed as a byte offset from the start of the addressable region.", alias="absoluteAddress")
    relative_address: Optional[StrictInt] = Field(default=None, description="The address expressed as a byte offset from the absolute address of the top-most parent object.", alias="relativeAddress")
    length: Optional[StrictInt] = Field(default=None, description="The number of bytes in this range of addresses.")
    kind: Optional[StrictStr] = Field(default=None, description="An open-ended string that identifies the address kind. 'data', 'function', 'header','instruction', 'module', 'page', 'section', 'segment', 'stack', 'stackFrame', 'table' are well-known values.")
    name: Optional[StrictStr] = Field(default=None, description="A name that is associated with the address, e.g., '.text'.")
    fully_qualified_name: Optional[StrictStr] = Field(default=None, description="A human-readable fully qualified name that is associated with the address.", alias="fullyQualifiedName")
    offset_from_parent: Optional[StrictInt] = Field(default=None, description="The byte offset of this address from the absolute or relative address of the parent object.", alias="offsetFromParent")
    index: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=-1, description="The index within run.addresses of the cached object for this address.")
    parent_index: Optional[Annotated[int, Field(strict=True, ge=-1)]] = Field(default=-1, description="The index within run.addresses of the parent object.", alias="parentIndex")
    properties: Optional[PropertyBag] = None
    __properties: ClassVar[List[str]] = ["absoluteAddress", "relativeAddress", "length", "kind", "name", "fullyQualifiedName", "offsetFromParent", "index", "parentIndex", "properties"]

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
        """Create an instance of Address from a JSON string"""
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
        """Create an instance of Address from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "absoluteAddress": obj.get("absoluteAddress") if obj.get("absoluteAddress") is not None else -1,
            "relativeAddress": obj.get("relativeAddress"),
            "length": obj.get("length"),
            "kind": obj.get("kind"),
            "name": obj.get("name"),
            "fullyQualifiedName": obj.get("fullyQualifiedName"),
            "offsetFromParent": obj.get("offsetFromParent"),
            "index": obj.get("index") if obj.get("index") is not None else -1,
            "parentIndex": obj.get("parentIndex") if obj.get("parentIndex") is not None else -1,
            "properties": PropertyBag.from_dict(obj["properties"]) if obj.get("properties") is not None else None
        })
        return _obj


