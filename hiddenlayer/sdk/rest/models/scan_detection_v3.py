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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from hiddenlayer.sdk.rest.models.mitre_atlas_inner import MITREAtlasInner
from hiddenlayer.sdk.rest.models.rule_details_inner import RuleDetailsInner
from typing import Optional, Set
from typing_extensions import Self

class ScanDetectionV3(BaseModel):
    """
    ScanDetectionV3
    """ # noqa: E501
    description: StrictStr = Field(description="detection description")
    risk: Optional[StrictStr] = Field(default=None, description="detection risk")
    severity: StrictStr = Field(description="detection severity")
    detection_id: StrictStr = Field(description="unique identifier for the detection")
    impact: Optional[StrictStr] = Field(default=None, description="detection impact")
    likelihood: Optional[StrictStr] = Field(default=None, description="detection likelihood")
    rule_details: Optional[List[RuleDetailsInner]] = None
    rule_id: StrictStr = Field(description="unique identifier for the rule that sourced the detection")
    category: StrictStr = Field(description="Vulnerability category for the detection")
    mitre_atlas: List[MITREAtlasInner]
    owasp: List[Annotated[str, Field(strict=True)]]
    cve: Optional[List[Annotated[str, Field(strict=True)]]] = None
    cwe: Optional[Annotated[str, Field(strict=True)]] = None
    cwe_href: Optional[StrictStr] = Field(default=None, description="CWE URL for the detection")
    technical_blog_href: Optional[StrictStr] = Field(default=None, description="Hiddenlayer Technical Blog URL for the detection")
    __properties: ClassVar[List[str]] = ["description", "risk", "severity", "detection_id", "impact", "likelihood", "rule_details", "rule_id", "category", "mitre_atlas", "owasp", "cve", "cwe", "cwe_href", "technical_blog_href"]

    @field_validator('risk')
    def risk_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['MALICIOUS', 'SUSPICIOUS', 'BENIGN']):
            raise ValueError("must be one of enum values ('MALICIOUS', 'SUSPICIOUS', 'BENIGN')")
        return value

    @field_validator('severity')
    def severity_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['low', 'medium', 'high', 'critical']):
            raise ValueError("must be one of enum values ('low', 'medium', 'high', 'critical')")
        return value

    @field_validator('cwe')
    def cwe_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^CWE-\d{1,4}.*$|^$", value):
            raise ValueError(r"must validate the regular expression /^CWE-\d{1,4}.*$|^$/")
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
        """Create an instance of ScanDetectionV3 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in rule_details (list)
        _items = []
        if self.rule_details:
            for _item in self.rule_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rule_details'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in mitre_atlas (list)
        _items = []
        if self.mitre_atlas:
            for _item in self.mitre_atlas:
                if _item:
                    _items.append(_item.to_dict())
            _dict['mitre_atlas'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScanDetectionV3 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "risk": obj.get("risk"),
            "severity": obj.get("severity"),
            "detection_id": obj.get("detection_id"),
            "impact": obj.get("impact"),
            "likelihood": obj.get("likelihood"),
            "rule_details": [RuleDetailsInner.from_dict(_item) for _item in obj["rule_details"]] if obj.get("rule_details") is not None else None,
            "rule_id": obj.get("rule_id"),
            "category": obj.get("category"),
            "mitre_atlas": [MITREAtlasInner.from_dict(_item) for _item in obj["mitre_atlas"]] if obj.get("mitre_atlas") is not None else None,
            "owasp": obj.get("owasp"),
            "cve": obj.get("cve"),
            "cwe": obj.get("cwe"),
            "cwe_href": obj.get("cwe_href"),
            "technical_blog_href": obj.get("technical_blog_href")
        })
        return _obj


