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
from hiddenlayer.sdk.rest.models.multiformat_message_string import MultiformatMessageString
from hiddenlayer.sdk.rest.models.property_bag import PropertyBag
from typing import Optional, Set
from typing_extensions import Self

class TranslationMetadata(BaseModel):
    """
    Provides additional metadata related to translation.
    """ # noqa: E501
    name: StrictStr = Field(description="The name associated with the translation metadata.")
    full_name: Optional[StrictStr] = Field(default=None, description="The full name associated with the translation metadata.", alias="fullName")
    short_description: Optional[MultiformatMessageString] = Field(default=None, alias="shortDescription")
    full_description: Optional[MultiformatMessageString] = Field(default=None, alias="fullDescription")
    download_uri: Optional[StrictStr] = Field(default=None, description="The absolute URI from which the translation metadata can be downloaded.", alias="downloadUri")
    information_uri: Optional[StrictStr] = Field(default=None, description="The absolute URI from which information related to the translation metadata can be downloaded.", alias="informationUri")
    properties: Optional[PropertyBag] = None
    __properties: ClassVar[List[str]] = ["name", "fullName", "shortDescription", "fullDescription", "downloadUri", "informationUri", "properties"]

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
        """Create an instance of TranslationMetadata from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of short_description
        if self.short_description:
            _dict['shortDescription'] = self.short_description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of full_description
        if self.full_description:
            _dict['fullDescription'] = self.full_description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of properties
        if self.properties:
            _dict['properties'] = self.properties.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TranslationMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "fullName": obj.get("fullName"),
            "shortDescription": MultiformatMessageString.from_dict(obj["shortDescription"]) if obj.get("shortDescription") is not None else None,
            "fullDescription": MultiformatMessageString.from_dict(obj["fullDescription"]) if obj.get("fullDescription") is not None else None,
            "downloadUri": obj.get("downloadUri"),
            "informationUri": obj.get("informationUri"),
            "properties": PropertyBag.from_dict(obj["properties"]) if obj.get("properties") is not None else None
        })
        return _obj


