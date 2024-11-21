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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from hiddenlayer.sdk.rest.models.location import Location
from hiddenlayer.sdk.rest.models.property_bag import PropertyBag
from typing import Optional, Set
from typing_extensions import Self

class Suppression(BaseModel):
    """
    A suppression that is relevant to a result.
    """ # noqa: E501
    guid: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="A stable, unique identifier for the suppression in the form of a GUID.")
    kind: StrictStr = Field(description="A string that indicates where the suppression is persisted.")
    status: Optional[StrictStr] = Field(default=None, description="A string that indicates the review status of the suppression.")
    justification: Optional[StrictStr] = Field(default=None, description="A string representing the justification for the suppression.")
    location: Optional[Location] = None
    properties: Optional[PropertyBag] = None
    __properties: ClassVar[List[str]] = ["guid", "kind", "status", "justification", "location", "properties"]

    @field_validator('guid')
    def guid_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$/")
        return value

    @field_validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['inSource', 'external']):
            raise ValueError("must be one of enum values ('inSource', 'external')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['accepted', 'underReview', 'rejected']):
            raise ValueError("must be one of enum values ('accepted', 'underReview', 'rejected')")
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
        """Create an instance of Suppression from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of properties
        if self.properties:
            _dict['properties'] = self.properties.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Suppression from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "guid": obj.get("guid"),
            "kind": obj.get("kind"),
            "status": obj.get("status"),
            "justification": obj.get("justification"),
            "location": Location.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "properties": PropertyBag.from_dict(obj["properties"]) if obj.get("properties") is not None else None
        })
        return _obj

