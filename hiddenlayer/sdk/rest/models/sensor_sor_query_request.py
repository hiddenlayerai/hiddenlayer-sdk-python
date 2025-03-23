# coding: utf-8

"""
    HiddenLayer Sensor SOR

    HiddenLayer Sensor SOR API for operations to sensor data storage

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
from hiddenlayer.sdk.rest.models.sensor_sor_query_filter import SensorSORQueryFilter
from typing import Optional, Set
from typing_extensions import Self

class SensorSORQueryRequest(BaseModel):
    """
    SensorSORQueryRequest
    """ # noqa: E501
    filter: Optional[SensorSORQueryFilter] = None
    order_by: Optional[StrictStr] = 'created_at'
    order_dir: Optional[StrictStr] = None
    page_size: Optional[StrictInt] = 25
    page_number: Optional[StrictInt] = 0
    __properties: ClassVar[List[str]] = ["filter", "order_by", "order_dir", "page_size", "page_number"]

    @field_validator('order_dir')
    def order_dir_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['asc', 'desc', 'ASC', 'DESC']):
            raise ValueError("must be one of enum values ('asc', 'desc', 'ASC', 'DESC')")
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
        """Create an instance of SensorSORQueryRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SensorSORQueryRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "filter": SensorSORQueryFilter.from_dict(obj["filter"]) if obj.get("filter") is not None else None,
            "order_by": obj.get("order_by") if obj.get("order_by") is not None else 'created_at',
            "order_dir": obj.get("order_dir"),
            "page_size": obj.get("page_size") if obj.get("page_size") is not None else 25,
            "page_number": obj.get("page_number") if obj.get("page_number") is not None else 0
        })
        return _obj


