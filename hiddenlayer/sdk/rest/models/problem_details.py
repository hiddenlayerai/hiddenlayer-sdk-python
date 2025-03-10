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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from hiddenlayer.sdk.rest.models.errors_inner import ErrorsInner
from typing import Optional, Set
from typing_extensions import Self

class ProblemDetails(BaseModel):
    """
    ProblemDetails
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="https://www.rfc-editor.org/rfc/rfc9457.html#name-type")
    title: Optional[StrictStr] = Field(default=None, description="https://www.rfc-editor.org/rfc/rfc9457.html#name-title")
    detail: Optional[StrictStr] = Field(default=None, description="https://www.rfc-editor.org/rfc/rfc9457.html#name-detail")
    instance: Optional[StrictStr] = Field(default=None, description="https://www.rfc-editor.org/rfc/rfc9457.html#name-instance")
    errors: List[ErrorsInner] = Field(description="Error details")
    __properties: ClassVar[List[str]] = ["type", "title", "detail", "instance", "errors"]

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
        """Create an instance of ProblemDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item in self.errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['errors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProblemDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "title": obj.get("title"),
            "detail": obj.get("detail"),
            "instance": obj.get("instance"),
            "errors": [ErrorsInner.from_dict(_item) for _item in obj["errors"]] if obj.get("errors") is not None else None
        })
        return _obj


