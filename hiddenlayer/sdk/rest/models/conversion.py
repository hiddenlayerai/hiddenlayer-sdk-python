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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from hiddenlayer.sdk.rest.models.artifact_location import ArtifactLocation
from hiddenlayer.sdk.rest.models.invocation import Invocation
from hiddenlayer.sdk.rest.models.property_bag import PropertyBag
from hiddenlayer.sdk.rest.models.tool import Tool
from typing import Optional, Set
from typing_extensions import Self

class Conversion(BaseModel):
    """
    Describes how a converter transformed the output of a static analysis tool from the analysis tool's native output format into the SARIF format.
    """ # noqa: E501
    tool: Tool
    invocation: Optional[Invocation] = None
    analysis_tool_log_files: Optional[Annotated[List[ArtifactLocation], Field(min_length=0)]] = Field(default=None, description="The locations of the analysis tool's per-run log files.", alias="analysisToolLogFiles")
    properties: Optional[PropertyBag] = None
    __properties: ClassVar[List[str]] = ["tool", "invocation", "analysisToolLogFiles", "properties"]

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
        """Create an instance of Conversion from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of invocation
        if self.invocation:
            _dict['invocation'] = self.invocation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in analysis_tool_log_files (list)
        _items = []
        if self.analysis_tool_log_files:
            for _item in self.analysis_tool_log_files:
                if _item:
                    _items.append(_item.to_dict())
            _dict['analysisToolLogFiles'] = _items
        # override the default output from pydantic by calling `to_dict()` of properties
        if self.properties:
            _dict['properties'] = self.properties.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Conversion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tool": Tool.from_dict(obj["tool"]) if obj.get("tool") is not None else None,
            "invocation": Invocation.from_dict(obj["invocation"]) if obj.get("invocation") is not None else None,
            "analysisToolLogFiles": [ArtifactLocation.from_dict(_item) for _item in obj["analysisToolLogFiles"]] if obj.get("analysisToolLogFiles") is not None else None,
            "properties": PropertyBag.from_dict(obj["properties"]) if obj.get("properties") is not None else None
        })
        return _obj


