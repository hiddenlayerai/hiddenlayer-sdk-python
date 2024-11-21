# coding: utf-8

"""
    HiddenLayer ModelScan V2

    HiddenLayer ModelScan API for scanning of models

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
from hiddenlayer.sdk.rest.models.message import Message
from hiddenlayer.sdk.rest.models.multiformat_message_string import MultiformatMessageString
from hiddenlayer.sdk.rest.models.property_bag import PropertyBag
from typing import Optional, Set
from typing_extensions import Self

class EdgeTraversal(BaseModel):
    """
    Represents the traversal of a single edge during a graph traversal.
    """ # noqa: E501
    edge_id: StrictStr = Field(description="Identifies the edge being traversed.", alias="edgeId")
    message: Optional[Message] = None
    final_state: Optional[Dict[str, MultiformatMessageString]] = Field(default=None, description="The values of relevant expressions after the edge has been traversed.", alias="finalState")
    step_over_edge_count: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The number of edge traversals necessary to return from a nested graph.", alias="stepOverEdgeCount")
    properties: Optional[PropertyBag] = None
    __properties: ClassVar[List[str]] = ["edgeId", "message", "finalState", "stepOverEdgeCount", "properties"]

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
        """Create an instance of EdgeTraversal from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of message
        if self.message:
            _dict['message'] = self.message.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in final_state (dict)
        _field_dict = {}
        if self.final_state:
            for _key in self.final_state:
                if self.final_state[_key]:
                    _field_dict[_key] = self.final_state[_key].to_dict()
            _dict['finalState'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of properties
        if self.properties:
            _dict['properties'] = self.properties.to_dict()
        # set to None if message (nullable) is None
        # and model_fields_set contains the field
        if self.message is None and "message" in self.model_fields_set:
            _dict['message'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EdgeTraversal from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "edgeId": obj.get("edgeId"),
            "message": Message.from_dict(obj["message"]) if obj.get("message") is not None else None,
            "finalState": dict(
                (_k, MultiformatMessageString.from_dict(_v))
                for _k, _v in obj["finalState"].items()
            )
            if obj.get("finalState") is not None
            else None,
            "stepOverEdgeCount": obj.get("stepOverEdgeCount"),
            "properties": PropertyBag.from_dict(obj["properties"]) if obj.get("properties") is not None else None
        })
        return _obj


