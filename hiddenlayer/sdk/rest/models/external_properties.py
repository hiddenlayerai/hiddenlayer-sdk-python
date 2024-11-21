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
from hiddenlayer.sdk.rest.models.address import Address
from hiddenlayer.sdk.rest.models.artifact import Artifact
from hiddenlayer.sdk.rest.models.conversion import Conversion
from hiddenlayer.sdk.rest.models.graph import Graph
from hiddenlayer.sdk.rest.models.invocation import Invocation
from hiddenlayer.sdk.rest.models.logical_location import LogicalLocation
from hiddenlayer.sdk.rest.models.property_bag import PropertyBag
from hiddenlayer.sdk.rest.models.result import Result
from hiddenlayer.sdk.rest.models.thread_flow_location import ThreadFlowLocation
from hiddenlayer.sdk.rest.models.tool_component import ToolComponent
from hiddenlayer.sdk.rest.models.web_request import WebRequest
from hiddenlayer.sdk.rest.models.web_response import WebResponse
from typing import Optional, Set
from typing_extensions import Self

class ExternalProperties(BaseModel):
    """
    The top-level element of an external property file.
    """ # noqa: E501
    var_schema: Optional[StrictStr] = Field(default=None, description="The URI of the JSON schema corresponding to the version of the external property file format.", alias="schema")
    version: Optional[StrictStr] = Field(default=None, description="The SARIF format version of this external properties object.")
    guid: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="A stable, unique identifier for this external properties object, in the form of a GUID.")
    run_guid: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="A stable, unique identifier for the run associated with this external properties object, in the form of a GUID.", alias="runGuid")
    conversion: Optional[Conversion] = None
    graphs: Optional[Annotated[List[Graph], Field(min_length=0)]] = Field(default=None, description="An array of graph objects that will be merged with a separate run.")
    externalized_properties: Optional[PropertyBag] = Field(default=None, alias="externalizedProperties")
    artifacts: Optional[Annotated[List[Artifact], Field(min_length=0)]] = Field(default=None, description="An array of artifact objects that will be merged with a separate run.")
    invocations: Optional[Annotated[List[Invocation], Field(min_length=0)]] = Field(default=None, description="Describes the invocation of the analysis tool that will be merged with a separate run.")
    logical_locations: Optional[Annotated[List[LogicalLocation], Field(min_length=0)]] = Field(default=None, description="An array of logical locations such as namespaces, types or functions that will be merged with a separate run.", alias="logicalLocations")
    thread_flow_locations: Optional[Annotated[List[ThreadFlowLocation], Field(min_length=0)]] = Field(default=None, description="An array of threadFlowLocation objects that will be merged with a separate run.", alias="threadFlowLocations")
    results: Optional[Annotated[List[Result], Field(min_length=0)]] = Field(default=None, description="An array of result objects that will be merged with a separate run.")
    taxonomies: Optional[Annotated[List[ToolComponent], Field(min_length=0)]] = Field(default=None, description="Tool taxonomies that will be merged with a separate run.")
    driver: Optional[ToolComponent] = None
    extensions: Optional[Annotated[List[ToolComponent], Field(min_length=0)]] = Field(default=None, description="Tool extensions that will be merged with a separate run.")
    policies: Optional[Annotated[List[ToolComponent], Field(min_length=0)]] = Field(default=None, description="Tool policies that will be merged with a separate run.")
    translations: Optional[Annotated[List[ToolComponent], Field(min_length=0)]] = Field(default=None, description="Tool translations that will be merged with a separate run.")
    addresses: Optional[Annotated[List[Address], Field(min_length=0)]] = Field(default=None, description="Addresses that will be merged with a separate run.")
    web_requests: Optional[Annotated[List[WebRequest], Field(min_length=0)]] = Field(default=None, description="Requests that will be merged with a separate run.", alias="webRequests")
    web_responses: Optional[Annotated[List[WebResponse], Field(min_length=0)]] = Field(default=None, description="Responses that will be merged with a separate run.", alias="webResponses")
    properties: Optional[PropertyBag] = None
    __properties: ClassVar[List[str]] = ["schema", "version", "guid", "runGuid", "conversion", "graphs", "externalizedProperties", "artifacts", "invocations", "logicalLocations", "threadFlowLocations", "results", "taxonomies", "driver", "extensions", "policies", "translations", "addresses", "webRequests", "webResponses", "properties"]

    @field_validator('version')
    def version_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['2.1.0']):
            raise ValueError("must be one of enum values ('2.1.0')")
        return value

    @field_validator('guid')
    def guid_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$/")
        return value

    @field_validator('run_guid')
    def run_guid_validate_regular_expression(cls, value):
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
        """Create an instance of ExternalProperties from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of conversion
        if self.conversion:
            _dict['conversion'] = self.conversion.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in graphs (list)
        _items = []
        if self.graphs:
            for _item in self.graphs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['graphs'] = _items
        # override the default output from pydantic by calling `to_dict()` of externalized_properties
        if self.externalized_properties:
            _dict['externalizedProperties'] = self.externalized_properties.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in artifacts (list)
        _items = []
        if self.artifacts:
            for _item in self.artifacts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['artifacts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in invocations (list)
        _items = []
        if self.invocations:
            for _item in self.invocations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['invocations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in logical_locations (list)
        _items = []
        if self.logical_locations:
            for _item in self.logical_locations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['logicalLocations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in thread_flow_locations (list)
        _items = []
        if self.thread_flow_locations:
            for _item in self.thread_flow_locations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['threadFlowLocations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item in self.results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['results'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in taxonomies (list)
        _items = []
        if self.taxonomies:
            for _item in self.taxonomies:
                if _item:
                    _items.append(_item.to_dict())
            _dict['taxonomies'] = _items
        # override the default output from pydantic by calling `to_dict()` of driver
        if self.driver:
            _dict['driver'] = self.driver.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in extensions (list)
        _items = []
        if self.extensions:
            for _item in self.extensions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['extensions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in policies (list)
        _items = []
        if self.policies:
            for _item in self.policies:
                if _item:
                    _items.append(_item.to_dict())
            _dict['policies'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in translations (list)
        _items = []
        if self.translations:
            for _item in self.translations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['translations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in addresses (list)
        _items = []
        if self.addresses:
            for _item in self.addresses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['addresses'] = _items
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
        # override the default output from pydantic by calling `to_dict()` of properties
        if self.properties:
            _dict['properties'] = self.properties.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExternalProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": obj.get("schema"),
            "version": obj.get("version"),
            "guid": obj.get("guid"),
            "runGuid": obj.get("runGuid"),
            "conversion": Conversion.from_dict(obj["conversion"]) if obj.get("conversion") is not None else None,
            "graphs": [Graph.from_dict(_item) for _item in obj["graphs"]] if obj.get("graphs") is not None else None,
            "externalizedProperties": PropertyBag.from_dict(obj["externalizedProperties"]) if obj.get("externalizedProperties") is not None else None,
            "artifacts": [Artifact.from_dict(_item) for _item in obj["artifacts"]] if obj.get("artifacts") is not None else None,
            "invocations": [Invocation.from_dict(_item) for _item in obj["invocations"]] if obj.get("invocations") is not None else None,
            "logicalLocations": [LogicalLocation.from_dict(_item) for _item in obj["logicalLocations"]] if obj.get("logicalLocations") is not None else None,
            "threadFlowLocations": [ThreadFlowLocation.from_dict(_item) for _item in obj["threadFlowLocations"]] if obj.get("threadFlowLocations") is not None else None,
            "results": [Result.from_dict(_item) for _item in obj["results"]] if obj.get("results") is not None else None,
            "taxonomies": [ToolComponent.from_dict(_item) for _item in obj["taxonomies"]] if obj.get("taxonomies") is not None else None,
            "driver": ToolComponent.from_dict(obj["driver"]) if obj.get("driver") is not None else None,
            "extensions": [ToolComponent.from_dict(_item) for _item in obj["extensions"]] if obj.get("extensions") is not None else None,
            "policies": [ToolComponent.from_dict(_item) for _item in obj["policies"]] if obj.get("policies") is not None else None,
            "translations": [ToolComponent.from_dict(_item) for _item in obj["translations"]] if obj.get("translations") is not None else None,
            "addresses": [Address.from_dict(_item) for _item in obj["addresses"]] if obj.get("addresses") is not None else None,
            "webRequests": [WebRequest.from_dict(_item) for _item in obj["webRequests"]] if obj.get("webRequests") is not None else None,
            "webResponses": [WebResponse.from_dict(_item) for _item in obj["webResponses"]] if obj.get("webResponses") is not None else None,
            "properties": PropertyBag.from_dict(obj["properties"]) if obj.get("properties") is not None else None
        })
        return _obj

