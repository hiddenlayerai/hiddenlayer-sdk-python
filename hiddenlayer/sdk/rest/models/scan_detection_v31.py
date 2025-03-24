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
from hiddenlayer.sdk.rest.models.mitre_atlas_inner import MITREAtlasInner
from hiddenlayer.sdk.rest.models.rule_details_inner import RuleDetailsInner
from typing import Optional, Set
from typing_extensions import Self

class ScanDetectionV31(BaseModel):
    """
    ScanDetectionV31
    """ # noqa: E501
    detection_id: StrictStr = Field(description="unique identifier for the detection")
    rule_id: StrictStr = Field(description="unique identifier for the rule that sourced the detection")
    risk: Optional[StrictStr] = Field(default=None, description="detection risk")
    category: StrictStr = Field(description="Vulnerability category for the detection")
    description: StrictStr = Field(description="detection description")
    likelihood: StrictStr = Field(description="detection likelihood")
    impact: StrictStr = Field(description="detection impact")
    severity: StrictStr = Field(description="detection severity")
    rule_details: Optional[List[RuleDetailsInner]] = None
    mitre_atlas: List[MITREAtlasInner]
    owasp: List[Annotated[str, Field(strict=True)]]
    cve: List[Annotated[str, Field(strict=True)]]
    cwe: Annotated[str, Field(strict=True)]
    cwe_href: StrictStr = Field(description="CWE URL for the detection")
    technical_blog_hrefs: Optional[List[StrictStr]] = Field(default=None, description="Hiddenlayer Technical Blog URLs for the detection")
    technical_blog_href: Optional[StrictStr] = Field(default=None, description="Hiddenlayer Technical Blog URL for the detection")
    __properties: ClassVar[List[str]] = ["detection_id", "rule_id", "risk", "category", "description", "likelihood", "impact", "severity", "rule_details", "mitre_atlas", "owasp", "cve", "cwe", "cwe_href", "technical_blog_hrefs", "technical_blog_href"]

    @field_validator('risk')
    def risk_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['MALICIOUS', 'SUSPICIOUS']):
            raise ValueError("must be one of enum values ('MALICIOUS', 'SUSPICIOUS')")
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
        """Create an instance of ScanDetectionV31 from a JSON string"""
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
        """Create an instance of ScanDetectionV31 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "detection_id": obj.get("detection_id"),
            "rule_id": obj.get("rule_id"),
            "risk": obj.get("risk"),
            "category": obj.get("category"),
            "description": obj.get("description"),
            "likelihood": obj.get("likelihood"),
            "impact": obj.get("impact"),
            "severity": obj.get("severity"),
            "rule_details": [RuleDetailsInner.from_dict(_item) for _item in obj["rule_details"]] if obj.get("rule_details") is not None else None,
            "mitre_atlas": [MITREAtlasInner.from_dict(_item) for _item in obj["mitre_atlas"]] if obj.get("mitre_atlas") is not None else None,
            "owasp": obj.get("owasp"),
            "cve": obj.get("cve"),
            "cwe": obj.get("cwe"),
            "cwe_href": obj.get("cwe_href"),
            "technical_blog_hrefs": obj.get("technical_blog_hrefs"),
            "technical_blog_href": obj.get("technical_blog_href")
        })
        return _obj


