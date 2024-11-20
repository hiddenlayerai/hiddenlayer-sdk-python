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
from hiddenlayer.sdk.rest.models.detections import Detections
from hiddenlayer.sdk.rest.models.scan_results import ScanResults
from typing import Optional, Set
from typing_extensions import Self

class ScanResultsV2(BaseModel):
    """
    ScanResultsV2
    """ # noqa: E501
    scan_id: StrictStr
    status: StrictStr
    start_time: StrictInt
    end_time: StrictInt
    results: Optional[ScanResults] = None
    severity: Optional[StrictStr] = None
    detections: List[Detections]
    __properties: ClassVar[List[str]] = ["scan_id", "status", "start_time", "end_time", "results", "severity", "detections"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['done', 'accepted', 'failed', 'pending', 'created', 'retry', 'unknown']):
            raise ValueError("must be one of enum values ('done', 'accepted', 'failed', 'pending', 'created', 'retry', 'unknown')")
        return value

    @field_validator('severity')
    def severity_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['UNKNOWN', 'SAFE', 'SUSPICIOUS', 'MALICIOUS']):
            raise ValueError("must be one of enum values ('UNKNOWN', 'SAFE', 'SUSPICIOUS', 'MALICIOUS')")
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
        """Create an instance of ScanResultsV2 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of results
        if self.results:
            _dict['results'] = self.results.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in detections (list)
        _items = []
        if self.detections:
            for _item in self.detections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['detections'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScanResultsV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "scan_id": obj.get("scan_id"),
            "status": obj.get("status"),
            "start_time": obj.get("start_time"),
            "end_time": obj.get("end_time"),
            "results": ScanResults.from_dict(obj["results"]) if obj.get("results") is not None else None,
            "severity": obj.get("severity"),
            "detections": [Detections.from_dict(_item) for _item in obj["detections"]] if obj.get("detections") is not None else None
        })
        return _obj


