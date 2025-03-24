# coding: utf-8

"""
    HiddenLayer-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

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
from hiddenlayer.sdk.rest.models.multiformat_message_string import MultiformatMessageString
from hiddenlayer.sdk.rest.models.property_bag import PropertyBag
from hiddenlayer.sdk.rest.models.reporting_configuration import ReportingConfiguration
from hiddenlayer.sdk.rest.models.reporting_descriptor_relationship import ReportingDescriptorRelationship
from typing import Optional, Set
from typing_extensions import Self

class ReportingDescriptor(BaseModel):
    """
    Metadata that describes a specific report produced by the tool, as part of the analysis it provides or its runtime reporting.
    """ # noqa: E501
    id: StrictStr = Field(description="A stable, opaque identifier for the report.")
    deprecated_ids: Optional[Annotated[List[StrictStr], Field(min_length=0)]] = Field(default=None, description="An array of stable, opaque identifiers by which this report was known in some previous version of the analysis tool.", alias="deprecatedIds")
    guid: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="A unique identifier for the reporting descriptor in the form of a GUID.")
    deprecated_guids: Optional[Annotated[List[Annotated[str, Field(strict=True)]], Field(min_length=0)]] = Field(default=None, description="An array of unique identifies in the form of a GUID by which this report was known in some previous version of the analysis tool.", alias="deprecatedGuids")
    name: Optional[StrictStr] = Field(default=None, description="A report identifier that is understandable to an end user.")
    deprecated_names: Optional[Annotated[List[StrictStr], Field(min_length=0)]] = Field(default=None, description="An array of readable identifiers by which this report was known in some previous version of the analysis tool.", alias="deprecatedNames")
    short_description: Optional[MultiformatMessageString] = Field(default=None, alias="shortDescription")
    full_description: Optional[MultiformatMessageString] = Field(default=None, alias="fullDescription")
    message_strings: Optional[Dict[str, MultiformatMessageString]] = Field(default=None, description="A set of name/value pairs with arbitrary names. Each value is a multiformatMessageString object, which holds message strings in plain text and (optionally) Markdown format. The strings can include placeholders, which can be used to construct a message in combination with an arbitrary number of additional string arguments.", alias="messageStrings")
    default_configuration: Optional[ReportingConfiguration] = Field(default=None, alias="defaultConfiguration")
    help_uri: Optional[StrictStr] = Field(default=None, description="A URI where the primary documentation for the report can be found.", alias="helpUri")
    help: Optional[MultiformatMessageString] = None
    relationships: Optional[Annotated[List[ReportingDescriptorRelationship], Field(min_length=0)]] = Field(default=None, description="An array of objects that describe relationships between this reporting descriptor and others.")
    properties: Optional[PropertyBag] = None
    __properties: ClassVar[List[str]] = ["id", "deprecatedIds", "guid", "deprecatedGuids", "name", "deprecatedNames", "shortDescription", "fullDescription", "messageStrings", "defaultConfiguration", "helpUri", "help", "relationships", "properties"]

    @field_validator('guid')
    def guid_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$/")
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
        """Create an instance of ReportingDescriptor from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in message_strings (dict)
        _field_dict = {}
        if self.message_strings:
            for _key in self.message_strings:
                if self.message_strings[_key]:
                    _field_dict[_key] = self.message_strings[_key].to_dict()
            _dict['messageStrings'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of default_configuration
        if self.default_configuration:
            _dict['defaultConfiguration'] = self.default_configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of help
        if self.help:
            _dict['help'] = self.help.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in relationships (list)
        _items = []
        if self.relationships:
            for _item in self.relationships:
                if _item:
                    _items.append(_item.to_dict())
            _dict['relationships'] = _items
        # override the default output from pydantic by calling `to_dict()` of properties
        if self.properties:
            _dict['properties'] = self.properties.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReportingDescriptor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "deprecatedIds": obj.get("deprecatedIds"),
            "guid": obj.get("guid"),
            "deprecatedGuids": obj.get("deprecatedGuids"),
            "name": obj.get("name"),
            "deprecatedNames": obj.get("deprecatedNames"),
            "shortDescription": MultiformatMessageString.from_dict(obj["shortDescription"]) if obj.get("shortDescription") is not None else None,
            "fullDescription": MultiformatMessageString.from_dict(obj["fullDescription"]) if obj.get("fullDescription") is not None else None,
            "messageStrings": dict(
                (_k, MultiformatMessageString.from_dict(_v))
                for _k, _v in obj["messageStrings"].items()
            )
            if obj.get("messageStrings") is not None
            else None,
            "defaultConfiguration": ReportingConfiguration.from_dict(obj["defaultConfiguration"]) if obj.get("defaultConfiguration") is not None else None,
            "helpUri": obj.get("helpUri"),
            "help": MultiformatMessageString.from_dict(obj["help"]) if obj.get("help") is not None else None,
            "relationships": [ReportingDescriptorRelationship.from_dict(_item) for _item in obj["relationships"]] if obj.get("relationships") is not None else None,
            "properties": PropertyBag.from_dict(obj["properties"]) if obj.get("properties") is not None else None
        })
        return _obj


