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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from hiddenlayer.sdk.rest.models.scan_report_v3 import ScanReportV3
from typing import Optional, Set
from typing_extensions import Self

class ModelScanApiV3ScanQuery200Response(BaseModel):
    """
    ModelScanApiV3ScanQuery200Response
    """ # noqa: E501
    items: Optional[List[ScanReportV3]] = None
    total: Annotated[int, Field(strict=True, ge=0)] = Field(description="Total number of items available based on the query criteria.")
    limit: Annotated[int, Field(le=100, strict=True, ge=1)] = Field(description="Maximum number of items to return")
    offset: Annotated[int, Field(strict=True, ge=0)] = Field(description="Begin returning the results from this offset")
    __properties: ClassVar[List[str]] = ["items", "total", "limit", "offset"]

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
        """Create an instance of ModelScanApiV3ScanQuery200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ModelScanApiV3ScanQuery200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "items": [ScanReportV3.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "total": obj.get("total"),
            "limit": obj.get("limit") if obj.get("limit") is not None else 25,
            "offset": obj.get("offset") if obj.get("offset") is not None else 0
        })
        return _obj


