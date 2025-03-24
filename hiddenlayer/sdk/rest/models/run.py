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
from hiddenlayer.sdk.rest.models.address import Address
from hiddenlayer.sdk.rest.models.artifact import Artifact
from hiddenlayer.sdk.rest.models.artifact_location import ArtifactLocation
from hiddenlayer.sdk.rest.models.conversion import Conversion
from hiddenlayer.sdk.rest.models.external_property_file_references import ExternalPropertyFileReferences
from hiddenlayer.sdk.rest.models.graph import Graph
from hiddenlayer.sdk.rest.models.invocation import Invocation
from hiddenlayer.sdk.rest.models.logical_location import LogicalLocation
from hiddenlayer.sdk.rest.models.property_bag import PropertyBag
from hiddenlayer.sdk.rest.models.result import Result
from hiddenlayer.sdk.rest.models.run_automation_details import RunAutomationDetails
from hiddenlayer.sdk.rest.models.special_locations import SpecialLocations
from hiddenlayer.sdk.rest.models.thread_flow_location import ThreadFlowLocation
from hiddenlayer.sdk.rest.models.tool import Tool
from hiddenlayer.sdk.rest.models.tool_component import ToolComponent
from hiddenlayer.sdk.rest.models.version_control_details import VersionControlDetails
from hiddenlayer.sdk.rest.models.web_request import WebRequest
from hiddenlayer.sdk.rest.models.web_response import WebResponse
from typing import Optional, Set
from typing_extensions import Self

class Run(BaseModel):
    """
    Describes a single run of an analysis tool, and contains the reported output of that run.
    """ # noqa: E501
    tool: Tool
    invocations: Optional[Annotated[List[Invocation], Field(min_length=0)]] = Field(default=None, description="Describes the invocation of the analysis tool.")
    conversion: Optional[Conversion] = None
    language: Optional[Annotated[str, Field(strict=True)]] = Field(default='en-US', description="The language of the messages emitted into the log file during this run (expressed as an ISO 639-1 two-letter lowercase culture code) and an optional region (expressed as an ISO 3166-1 two-letter uppercase subculture code associated with a country or region). The casing is recommended but not required (in order for this data to conform to RFC5646).")
    version_control_provenance: Optional[Annotated[List[VersionControlDetails], Field(min_length=0)]] = Field(default=None, description="Specifies the revision in version control of the artifacts that were scanned.", alias="versionControlProvenance")
    original_uri_base_ids: Optional[Dict[str, ArtifactLocation]] = Field(default=None, description="The artifact location specified by each uriBaseId symbol on the machine where the tool originally ran.", alias="originalUriBaseIds")
    artifacts: Optional[Annotated[List[Artifact], Field(min_length=0)]] = Field(default=None, description="An array of artifact objects relevant to the run.")
    logical_locations: Optional[Annotated[List[LogicalLocation], Field(min_length=0)]] = Field(default=None, description="An array of logical locations such as namespaces, types or functions.", alias="logicalLocations")
    graphs: Optional[Annotated[List[Graph], Field(min_length=0)]] = Field(default=None, description="An array of zero or more unique graph objects associated with the run.")
    results: Optional[Annotated[List[Result], Field(min_length=0)]] = Field(default=None, description="The set of results contained in an SARIF log. The results array can be omitted when a run is solely exporting rules metadata. It must be present (but may be empty) if a log file represents an actual scan.")
    automation_details: Optional[RunAutomationDetails] = Field(default=None, alias="automationDetails")
    run_aggregates: Optional[Annotated[List[RunAutomationDetails], Field(min_length=0)]] = Field(default=None, description="Automation details that describe the aggregate of runs to which this run belongs.", alias="runAggregates")
    baseline_guid: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The 'guid' property of a previous SARIF 'run' that comprises the baseline that was used to compute result 'baselineState' properties for the run.", alias="baselineGuid")
    redaction_tokens: Optional[Annotated[List[StrictStr], Field(min_length=0)]] = Field(default=None, description="An array of strings used to replace sensitive information in a redaction-aware property.", alias="redactionTokens")
    default_encoding: Optional[StrictStr] = Field(default=None, description="Specifies the default encoding for any artifact object that refers to a text file.", alias="defaultEncoding")
    default_source_language: Optional[StrictStr] = Field(default=None, description="Specifies the default source language for any artifact object that refers to a text file that contains source code.", alias="defaultSourceLanguage")
    newline_sequences: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(default=None, description="An ordered list of character sequences that were treated as line breaks when computing region information for the run.", alias="newlineSequences")
    column_kind: Optional[StrictStr] = Field(default=None, description="Specifies the unit in which the tool measures columns.", alias="columnKind")
    external_property_file_references: Optional[ExternalPropertyFileReferences] = Field(default=None, alias="externalPropertyFileReferences")
    thread_flow_locations: Optional[Annotated[List[ThreadFlowLocation], Field(min_length=0)]] = Field(default=None, description="An array of threadFlowLocation objects cached at run level.", alias="threadFlowLocations")
    taxonomies: Optional[Annotated[List[ToolComponent], Field(min_length=0)]] = Field(default=None, description="An array of toolComponent objects relevant to a taxonomy in which results are categorized.")
    addresses: Optional[Annotated[List[Address], Field(min_length=0)]] = Field(default=None, description="Addresses associated with this run instance, if any.")
    translations: Optional[Annotated[List[ToolComponent], Field(min_length=0)]] = Field(default=None, description="The set of available translations of the localized data provided by the tool.")
    policies: Optional[Annotated[List[ToolComponent], Field(min_length=0)]] = Field(default=None, description="Contains configurations that may potentially override both reportingDescriptor.defaultConfiguration (the tool's default severities) and invocation.configurationOverrides (severities established at run-time from the command line).")
    web_requests: Optional[Annotated[List[WebRequest], Field(min_length=0)]] = Field(default=None, description="An array of request objects cached at run level.", alias="webRequests")
    web_responses: Optional[Annotated[List[WebResponse], Field(min_length=0)]] = Field(default=None, description="An array of response objects cached at run level.", alias="webResponses")
    special_locations: Optional[SpecialLocations] = Field(default=None, alias="specialLocations")
    properties: Optional[PropertyBag] = None
    __properties: ClassVar[List[str]] = ["tool", "invocations", "conversion", "language", "versionControlProvenance", "originalUriBaseIds", "artifacts", "logicalLocations", "graphs", "results", "automationDetails", "runAggregates", "baselineGuid", "redactionTokens", "defaultEncoding", "defaultSourceLanguage", "newlineSequences", "columnKind", "externalPropertyFileReferences", "threadFlowLocations", "taxonomies", "addresses", "translations", "policies", "webRequests", "webResponses", "specialLocations", "properties"]

    @field_validator('language')
    def language_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z]{2}|^[a-zA-Z]{2}-[a-zA-Z]{2}?$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z]{2}|^[a-zA-Z]{2}-[a-zA-Z]{2}?$/")
        return value

    @field_validator('baseline_guid')
    def baseline_guid_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$/")
        return value

    @field_validator('column_kind')
    def column_kind_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['utf16CodeUnits', 'unicodeCodePoints']):
            raise ValueError("must be one of enum values ('utf16CodeUnits', 'unicodeCodePoints')")
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
        """Create an instance of Run from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of tool
        if self.tool:
            _dict['tool'] = self.tool.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in invocations (list)
        _items = []
        if self.invocations:
            for _item in self.invocations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['invocations'] = _items
        # override the default output from pydantic by calling `to_dict()` of conversion
        if self.conversion:
            _dict['conversion'] = self.conversion.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in version_control_provenance (list)
        _items = []
        if self.version_control_provenance:
            for _item in self.version_control_provenance:
                if _item:
                    _items.append(_item.to_dict())
            _dict['versionControlProvenance'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in original_uri_base_ids (dict)
        _field_dict = {}
        if self.original_uri_base_ids:
            for _key in self.original_uri_base_ids:
                if self.original_uri_base_ids[_key]:
                    _field_dict[_key] = self.original_uri_base_ids[_key].to_dict()
            _dict['originalUriBaseIds'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in artifacts (list)
        _items = []
        if self.artifacts:
            for _item in self.artifacts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['artifacts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in logical_locations (list)
        _items = []
        if self.logical_locations:
            for _item in self.logical_locations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['logicalLocations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in graphs (list)
        _items = []
        if self.graphs:
            for _item in self.graphs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['graphs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item in self.results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['results'] = _items
        # override the default output from pydantic by calling `to_dict()` of automation_details
        if self.automation_details:
            _dict['automationDetails'] = self.automation_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in run_aggregates (list)
        _items = []
        if self.run_aggregates:
            for _item in self.run_aggregates:
                if _item:
                    _items.append(_item.to_dict())
            _dict['runAggregates'] = _items
        # override the default output from pydantic by calling `to_dict()` of external_property_file_references
        if self.external_property_file_references:
            _dict['externalPropertyFileReferences'] = self.external_property_file_references.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in thread_flow_locations (list)
        _items = []
        if self.thread_flow_locations:
            for _item in self.thread_flow_locations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['threadFlowLocations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in taxonomies (list)
        _items = []
        if self.taxonomies:
            for _item in self.taxonomies:
                if _item:
                    _items.append(_item.to_dict())
            _dict['taxonomies'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in addresses (list)
        _items = []
        if self.addresses:
            for _item in self.addresses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['addresses'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in translations (list)
        _items = []
        if self.translations:
            for _item in self.translations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['translations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in policies (list)
        _items = []
        if self.policies:
            for _item in self.policies:
                if _item:
                    _items.append(_item.to_dict())
            _dict['policies'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in web_requests (list)
        _items = []
        if self.web_requests:
            for _item in self.web_requests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['webRequests'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in web_responses (list)
        _items = []
        if self.web_responses:
            for _item in self.web_responses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['webResponses'] = _items
        # override the default output from pydantic by calling `to_dict()` of special_locations
        if self.special_locations:
            _dict['specialLocations'] = self.special_locations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of properties
        if self.properties:
            _dict['properties'] = self.properties.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Run from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tool": Tool.from_dict(obj["tool"]) if obj.get("tool") is not None else None,
            "invocations": [Invocation.from_dict(_item) for _item in obj["invocations"]] if obj.get("invocations") is not None else None,
            "conversion": Conversion.from_dict(obj["conversion"]) if obj.get("conversion") is not None else None,
            "language": obj.get("language") if obj.get("language") is not None else 'en-US',
            "versionControlProvenance": [VersionControlDetails.from_dict(_item) for _item in obj["versionControlProvenance"]] if obj.get("versionControlProvenance") is not None else None,
            "originalUriBaseIds": dict(
                (_k, ArtifactLocation.from_dict(_v))
                for _k, _v in obj["originalUriBaseIds"].items()
            )
            if obj.get("originalUriBaseIds") is not None
            else None,
            "artifacts": [Artifact.from_dict(_item) for _item in obj["artifacts"]] if obj.get("artifacts") is not None else None,
            "logicalLocations": [LogicalLocation.from_dict(_item) for _item in obj["logicalLocations"]] if obj.get("logicalLocations") is not None else None,
            "graphs": [Graph.from_dict(_item) for _item in obj["graphs"]] if obj.get("graphs") is not None else None,
            "results": [Result.from_dict(_item) for _item in obj["results"]] if obj.get("results") is not None else None,
            "automationDetails": RunAutomationDetails.from_dict(obj["automationDetails"]) if obj.get("automationDetails") is not None else None,
            "runAggregates": [RunAutomationDetails.from_dict(_item) for _item in obj["runAggregates"]] if obj.get("runAggregates") is not None else None,
            "baselineGuid": obj.get("baselineGuid"),
            "redactionTokens": obj.get("redactionTokens"),
            "defaultEncoding": obj.get("defaultEncoding"),
            "defaultSourceLanguage": obj.get("defaultSourceLanguage"),
            "newlineSequences": obj.get("newlineSequences"),
            "columnKind": obj.get("columnKind"),
            "externalPropertyFileReferences": ExternalPropertyFileReferences.from_dict(obj["externalPropertyFileReferences"]) if obj.get("externalPropertyFileReferences") is not None else None,
            "threadFlowLocations": [ThreadFlowLocation.from_dict(_item) for _item in obj["threadFlowLocations"]] if obj.get("threadFlowLocations") is not None else None,
            "taxonomies": [ToolComponent.from_dict(_item) for _item in obj["taxonomies"]] if obj.get("taxonomies") is not None else None,
            "addresses": [Address.from_dict(_item) for _item in obj["addresses"]] if obj.get("addresses") is not None else None,
            "translations": [ToolComponent.from_dict(_item) for _item in obj["translations"]] if obj.get("translations") is not None else None,
            "policies": [ToolComponent.from_dict(_item) for _item in obj["policies"]] if obj.get("policies") is not None else None,
            "webRequests": [WebRequest.from_dict(_item) for _item in obj["webRequests"]] if obj.get("webRequests") is not None else None,
            "webResponses": [WebResponse.from_dict(_item) for _item in obj["webResponses"]] if obj.get("webResponses") is not None else None,
            "specialLocations": SpecialLocations.from_dict(obj["specialLocations"]) if obj.get("specialLocations") is not None else None,
            "properties": PropertyBag.from_dict(obj["properties"]) if obj.get("properties") is not None else None
        })
        return _obj


