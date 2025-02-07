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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from hiddenlayer.sdk.rest.models.file_result_v3 import FileResultV3
from typing import Optional, Set
from typing_extensions import Self

class ScanResultsV3(BaseModel):
    """
    ScanResultsV3
    """ # noqa: E501
    scan_id: Optional[StrictStr] = None
    start_time: Optional[StrictInt] = None
    end_time: Optional[StrictInt] = None
    status: Optional[StrictStr] = None
    version: Optional[StrictStr] = None
    inventory: Optional[Dict[str, Any]] = None
    file_results: List[FileResultV3]
    __properties: ClassVar[List[str]] = ["scan_id", "start_time", "end_time", "status", "version", "inventory", "file_results"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['done', 'running', 'failed', 'pending', 'canceled']):
            raise ValueError("must be one of enum values ('done', 'running', 'failed', 'pending', 'canceled')")
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
        """Create an instance of ScanResultsV3 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of inventory
        if self.inventory:
            _dict['inventory'] = self.inventory.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in file_results (list)
        _items = []
        if self.file_results:
            for _item in self.file_results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['file_results'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScanResultsV3 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "scan_id": obj.get("scan_id"),
            "start_time": obj.get("start_time"),
            "end_time": obj.get("end_time"),
            "status": obj.get("status"),
            "version": obj.get("version"),
            "inventory": InventoryV3.from_dict(obj["inventory"]) if obj.get("inventory") is not None else None,
            "file_results": [FileResultV3.from_dict(_item) for _item in obj["file_results"]] if obj.get("file_results") is not None else None
        })
        return _obj


