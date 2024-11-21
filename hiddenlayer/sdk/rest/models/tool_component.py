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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from hiddenlayer.sdk.rest.models.artifact_location import ArtifactLocation
from hiddenlayer.sdk.rest.models.multiformat_message_string import MultiformatMessageString
from hiddenlayer.sdk.rest.models.property_bag import PropertyBag
from hiddenlayer.sdk.rest.models.reporting_descriptor import ReportingDescriptor
from hiddenlayer.sdk.rest.models.tool_component_reference import ToolComponentReference
from hiddenlayer.sdk.rest.models.translation_metadata import TranslationMetadata
from typing import Optional, Set
from typing_extensions import Self

class ToolComponent(BaseModel):
    """
    A component, such as a plug-in or the driver, of the analysis tool that was run.
    """ # noqa: E501
    guid: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="A unique identifier for the tool component in the form of a GUID.")
    name: StrictStr = Field(description="The name of the tool component.")
    organization: Optional[StrictStr] = Field(default=None, description="The organization or company that produced the tool component.")
    product: Optional[StrictStr] = Field(default=None, description="A product suite to which the tool component belongs.")
    product_suite: Optional[StrictStr] = Field(default=None, description="A localizable string containing the name of the suite of products to which the tool component belongs.", alias="productSuite")
    short_description: Optional[MultiformatMessageString] = Field(default=None, alias="shortDescription")
    full_description: Optional[MultiformatMessageString] = Field(default=None, alias="fullDescription")
    full_name: Optional[StrictStr] = Field(default=None, description="The name of the tool component along with its version and any other useful identifying information, such as its locale.", alias="fullName")
    version: Optional[StrictStr] = Field(default=None, description="The tool component version, in whatever format the component natively provides.")
    semantic_version: Optional[StrictStr] = Field(default=None, description="The tool component version in the format specified by Semantic Versioning 2.0.", alias="semanticVersion")
    dotted_quad_file_version: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The binary version of the tool component's primary executable file expressed as four non-negative integers separated by a period (for operating systems that express file versions in this way).", alias="dottedQuadFileVersion")
    release_date_utc: Optional[StrictStr] = Field(default=None, description="A string specifying the UTC date (and optionally, the time) of the component's release.", alias="releaseDateUtc")
    download_uri: Optional[StrictStr] = Field(default=None, description="The absolute URI from which the tool component can be downloaded.", alias="downloadUri")
    information_uri: Optional[StrictStr] = Field(default=None, description="The absolute URI at which information about this version of the tool component can be found.", alias="informationUri")
    global_message_strings: Optional[Dict[str, MultiformatMessageString]] = Field(default=None, description="A dictionary, each of whose keys is a resource identifier and each of whose values is a multiformatMessageString object, which holds message strings in plain text and (optionally) Markdown format. The strings can include placeholders, which can be used to construct a message in combination with an arbitrary number of additional string arguments.", alias="globalMessageStrings")
    notifications: Optional[Annotated[List[ReportingDescriptor], Field(min_length=0)]] = Field(default=None, description="An array of reportingDescriptor objects relevant to the notifications related to the configuration and runtime execution of the tool component.")
    rules: Optional[Annotated[List[ReportingDescriptor], Field(min_length=0)]] = Field(default=None, description="An array of reportingDescriptor objects relevant to the analysis performed by the tool component.")
    taxa: Optional[Annotated[List[ReportingDescriptor], Field(min_length=0)]] = Field(default=None, description="An array of reportingDescriptor objects relevant to the definitions of both standalone and tool-defined taxonomies.")
    locations: Optional[Annotated[List[ArtifactLocation], Field(min_length=0)]] = Field(default=None, description="An array of the artifactLocation objects associated with the tool component.")
    language: Optional[Annotated[str, Field(strict=True)]] = Field(default='en-US', description="The language of the messages emitted into the log file during this run (expressed as an ISO 639-1 two-letter lowercase language code) and an optional region (expressed as an ISO 3166-1 two-letter uppercase subculture code associated with a country or region). The casing is recommended but not required (in order for this data to conform to RFC5646).")
    contents: Optional[List[StrictStr]] = Field(default=None, description="The kinds of data contained in this object.")
    is_comprehensive: Optional[StrictBool] = Field(default=False, description="Specifies whether this object contains a complete definition of the localizable and/or non-localizable data for this component, as opposed to including only data that is relevant to the results persisted to this log file.", alias="isComprehensive")
    localized_data_semantic_version: Optional[StrictStr] = Field(default=None, description="The semantic version of the localized strings defined in this component; maintained by components that provide translations.", alias="localizedDataSemanticVersion")
    minimum_required_localized_data_semantic_version: Optional[StrictStr] = Field(default=None, description="The minimum value of localizedDataSemanticVersion required in translations consumed by this component; used by components that consume translations.", alias="minimumRequiredLocalizedDataSemanticVersion")
    associated_component: Optional[ToolComponentReference] = Field(default=None, alias="associatedComponent")
    translation_metadata: Optional[TranslationMetadata] = Field(default=None, alias="translationMetadata")
    supported_taxonomies: Optional[Annotated[List[ToolComponentReference], Field(min_length=0)]] = Field(default=None, description="An array of toolComponentReference objects to declare the taxonomies supported by the tool component.", alias="supportedTaxonomies")
    properties: Optional[PropertyBag] = None
    __properties: ClassVar[List[str]] = ["guid", "name", "organization", "product", "productSuite", "shortDescription", "fullDescription", "fullName", "version", "semanticVersion", "dottedQuadFileVersion", "releaseDateUtc", "downloadUri", "informationUri", "globalMessageStrings", "notifications", "rules", "taxa", "locations", "language", "contents", "isComprehensive", "localizedDataSemanticVersion", "minimumRequiredLocalizedDataSemanticVersion", "associatedComponent", "translationMetadata", "supportedTaxonomies", "properties"]

    @field_validator('guid')
    def guid_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$/")
        return value

    @field_validator('dotted_quad_file_version')
    def dotted_quad_file_version_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[0-9]+(\.[0-9]+){3}", value):
            raise ValueError(r"must validate the regular expression /[0-9]+(\.[0-9]+){3}/")
        return value

    @field_validator('language')
    def language_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z]{2}|^[a-zA-Z]{2}-[a-zA-Z]{2}?$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z]{2}|^[a-zA-Z]{2}-[a-zA-Z]{2}?$/")
        return value

    @field_validator('contents')
    def contents_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['localizedData', 'nonLocalizedData']):
                raise ValueError("each list item must be one of ('localizedData', 'nonLocalizedData')")
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
        """Create an instance of ToolComponent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in global_message_strings (dict)
        _field_dict = {}
        if self.global_message_strings:
            for _key in self.global_message_strings:
                if self.global_message_strings[_key]:
                    _field_dict[_key] = self.global_message_strings[_key].to_dict()
            _dict['globalMessageStrings'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in notifications (list)
        _items = []
        if self.notifications:
            for _item in self.notifications:
                if _item:
                    _items.append(_item.to_dict())
            _dict['notifications'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item in self.rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rules'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in taxa (list)
        _items = []
        if self.taxa:
            for _item in self.taxa:
                if _item:
                    _items.append(_item.to_dict())
            _dict['taxa'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in locations (list)
        _items = []
        if self.locations:
            for _item in self.locations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['locations'] = _items
        # override the default output from pydantic by calling `to_dict()` of associated_component
        if self.associated_component:
            _dict['associatedComponent'] = self.associated_component.to_dict()
        # override the default output from pydantic by calling `to_dict()` of translation_metadata
        if self.translation_metadata:
            _dict['translationMetadata'] = self.translation_metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in supported_taxonomies (list)
        _items = []
        if self.supported_taxonomies:
            for _item in self.supported_taxonomies:
                if _item:
                    _items.append(_item.to_dict())
            _dict['supportedTaxonomies'] = _items
        # override the default output from pydantic by calling `to_dict()` of properties
        if self.properties:
            _dict['properties'] = self.properties.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ToolComponent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "guid": obj.get("guid"),
            "name": obj.get("name"),
            "organization": obj.get("organization"),
            "product": obj.get("product"),
            "productSuite": obj.get("productSuite"),
            "shortDescription": MultiformatMessageString.from_dict(obj["shortDescription"]) if obj.get("shortDescription") is not None else None,
            "fullDescription": MultiformatMessageString.from_dict(obj["fullDescription"]) if obj.get("fullDescription") is not None else None,
            "fullName": obj.get("fullName"),
            "version": obj.get("version"),
            "semanticVersion": obj.get("semanticVersion"),
            "dottedQuadFileVersion": obj.get("dottedQuadFileVersion"),
            "releaseDateUtc": obj.get("releaseDateUtc"),
            "downloadUri": obj.get("downloadUri"),
            "informationUri": obj.get("informationUri"),
            "globalMessageStrings": dict(
                (_k, MultiformatMessageString.from_dict(_v))
                for _k, _v in obj["globalMessageStrings"].items()
            )
            if obj.get("globalMessageStrings") is not None
            else None,
            "notifications": [ReportingDescriptor.from_dict(_item) for _item in obj["notifications"]] if obj.get("notifications") is not None else None,
            "rules": [ReportingDescriptor.from_dict(_item) for _item in obj["rules"]] if obj.get("rules") is not None else None,
            "taxa": [ReportingDescriptor.from_dict(_item) for _item in obj["taxa"]] if obj.get("taxa") is not None else None,
            "locations": [ArtifactLocation.from_dict(_item) for _item in obj["locations"]] if obj.get("locations") is not None else None,
            "language": obj.get("language") if obj.get("language") is not None else 'en-US',
            "contents": obj.get("contents"),
            "isComprehensive": obj.get("isComprehensive") if obj.get("isComprehensive") is not None else False,
            "localizedDataSemanticVersion": obj.get("localizedDataSemanticVersion"),
            "minimumRequiredLocalizedDataSemanticVersion": obj.get("minimumRequiredLocalizedDataSemanticVersion"),
            "associatedComponent": ToolComponentReference.from_dict(obj["associatedComponent"]) if obj.get("associatedComponent") is not None else None,
            "translationMetadata": TranslationMetadata.from_dict(obj["translationMetadata"]) if obj.get("translationMetadata") is not None else None,
            "supportedTaxonomies": [ToolComponentReference.from_dict(_item) for _item in obj["supportedTaxonomies"]] if obj.get("supportedTaxonomies") is not None else None,
            "properties": PropertyBag.from_dict(obj["properties"]) if obj.get("properties") is not None else None
        })
        return _obj


