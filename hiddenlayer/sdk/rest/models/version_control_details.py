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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from hiddenlayer.sdk.rest.models.artifact_location import ArtifactLocation
from hiddenlayer.sdk.rest.models.property_bag import PropertyBag
from typing import Optional, Set
from typing_extensions import Self

class VersionControlDetails(BaseModel):
    """
    Specifies the information necessary to retrieve a desired revision from a version control system.
    """ # noqa: E501
    repository_uri: StrictStr = Field(description="The absolute URI of the repository.", alias="repositoryUri")
    revision_id: Optional[StrictStr] = Field(default=None, description="A string that uniquely and permanently identifies the revision within the repository.", alias="revisionId")
    branch: Optional[StrictStr] = Field(default=None, description="The name of a branch containing the revision.")
    revision_tag: Optional[StrictStr] = Field(default=None, description="A tag that has been applied to the revision.", alias="revisionTag")
    as_of_time_utc: Optional[datetime] = Field(default=None, description="A Coordinated Universal Time (UTC) date and time that can be used to synchronize an enlistment to the state of the repository at that time.", alias="asOfTimeUtc")
    mapped_to: Optional[ArtifactLocation] = Field(default=None, alias="mappedTo")
    properties: Optional[PropertyBag] = None
    __properties: ClassVar[List[str]] = ["repositoryUri", "revisionId", "branch", "revisionTag", "asOfTimeUtc", "mappedTo", "properties"]

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
        """Create an instance of VersionControlDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of mapped_to
        if self.mapped_to:
            _dict['mappedTo'] = self.mapped_to.to_dict()
        # override the default output from pydantic by calling `to_dict()` of properties
        if self.properties:
            _dict['properties'] = self.properties.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VersionControlDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "repositoryUri": obj.get("repositoryUri"),
            "revisionId": obj.get("revisionId"),
            "branch": obj.get("branch"),
            "revisionTag": obj.get("revisionTag"),
            "asOfTimeUtc": obj.get("asOfTimeUtc"),
            "mappedTo": ArtifactLocation.from_dict(obj["mappedTo"]) if obj.get("mappedTo") is not None else None,
            "properties": PropertyBag.from_dict(obj["properties"]) if obj.get("properties") is not None else None
        })
        return _obj


