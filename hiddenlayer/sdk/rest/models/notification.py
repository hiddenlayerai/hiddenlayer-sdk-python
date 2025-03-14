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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from hiddenlayer.sdk.rest.models.exception import Exception
from hiddenlayer.sdk.rest.models.location import Location
from hiddenlayer.sdk.rest.models.message import Message
from hiddenlayer.sdk.rest.models.property_bag import PropertyBag
from hiddenlayer.sdk.rest.models.reporting_descriptor_reference import ReportingDescriptorReference
from typing import Optional, Set
from typing_extensions import Self

class Notification(BaseModel):
    """
    Describes a condition relevant to the tool itself, as opposed to being relevant to a target being analyzed by the tool.
    """ # noqa: E501
    locations: Optional[Annotated[List[Location], Field(min_length=0)]] = Field(default=None, description="The locations relevant to this notification.")
    message: Optional[Message]
    level: Optional[StrictStr] = Field(default='warning', description="A value specifying the severity level of the notification.")
    thread_id: Optional[StrictInt] = Field(default=None, description="The thread identifier of the code that generated the notification.", alias="threadId")
    time_utc: Optional[datetime] = Field(default=None, description="The Coordinated Universal Time (UTC) date and time at which the analysis tool generated the notification.", alias="timeUtc")
    exception: Optional[Exception] = None
    descriptor: Optional[ReportingDescriptorReference] = None
    associated_rule: Optional[ReportingDescriptorReference] = Field(default=None, alias="associatedRule")
    properties: Optional[PropertyBag] = None
    __properties: ClassVar[List[str]] = ["locations", "message", "level", "threadId", "timeUtc", "exception", "descriptor", "associatedRule", "properties"]

    @field_validator('level')
    def level_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['none', 'note', 'warning', 'error']):
            raise ValueError("must be one of enum values ('none', 'note', 'warning', 'error')")
        return value

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
        """Create an instance of Notification from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in locations (list)
        _items = []
        if self.locations:
            for _item in self.locations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['locations'] = _items
        # override the default output from pydantic by calling `to_dict()` of message
        if self.message:
            _dict['message'] = self.message.to_dict()
        # override the default output from pydantic by calling `to_dict()` of exception
        if self.exception:
            _dict['exception'] = self.exception.to_dict()
        # override the default output from pydantic by calling `to_dict()` of descriptor
        if self.descriptor:
            _dict['descriptor'] = self.descriptor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of associated_rule
        if self.associated_rule:
            _dict['associatedRule'] = self.associated_rule.to_dict()
        # override the default output from pydantic by calling `to_dict()` of properties
        if self.properties:
            _dict['properties'] = self.properties.to_dict()
        # set to None if message (nullable) is None
        # and model_fields_set contains the field
        if self.message is None and "message" in self.model_fields_set:
            _dict['message'] = None

        # set to None if descriptor (nullable) is None
        # and model_fields_set contains the field
        if self.descriptor is None and "descriptor" in self.model_fields_set:
            _dict['descriptor'] = None

        # set to None if associated_rule (nullable) is None
        # and model_fields_set contains the field
        if self.associated_rule is None and "associated_rule" in self.model_fields_set:
            _dict['associatedRule'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Notification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "locations": [Location.from_dict(_item) for _item in obj["locations"]] if obj.get("locations") is not None else None,
            "message": Message.from_dict(obj["message"]) if obj.get("message") is not None else None,
            "level": obj.get("level") if obj.get("level") is not None else 'warning',
            "threadId": obj.get("threadId"),
            "timeUtc": obj.get("timeUtc"),
            "exception": Exception.from_dict(obj["exception"]) if obj.get("exception") is not None else None,
            "descriptor": ReportingDescriptorReference.from_dict(obj["descriptor"]) if obj.get("descriptor") is not None else None,
            "associatedRule": ReportingDescriptorReference.from_dict(obj["associatedRule"]) if obj.get("associatedRule") is not None else None,
            "properties": PropertyBag.from_dict(obj["properties"]) if obj.get("properties") is not None else None
        })
        return _obj


