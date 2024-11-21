# VersionControlDetails

Specifies the information necessary to retrieve a desired revision from a version control system.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_uri** | **str** | The absolute URI of the repository. | 
**revision_id** | **str** | A string that uniquely and permanently identifies the revision within the repository. | [optional] 
**branch** | **str** | The name of a branch containing the revision. | [optional] 
**revision_tag** | **str** | A tag that has been applied to the revision. | [optional] 
**as_of_time_utc** | **datetime** | A Coordinated Universal Time (UTC) date and time that can be used to synchronize an enlistment to the state of the repository at that time. | [optional] 
**mapped_to** | [**ArtifactLocation**](ArtifactLocation.md) |  | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.version_control_details import VersionControlDetails

# TODO update the JSON string below
json = "{}"
# create an instance of VersionControlDetails from a JSON string
version_control_details_instance = VersionControlDetails.from_json(json)
# print the JSON string representation of the object
print(VersionControlDetails.to_json())

# convert the object into a dict
version_control_details_dict = version_control_details_instance.to_dict()
# create an instance of VersionControlDetails from a dict
version_control_details_from_dict = VersionControlDetails.from_dict(version_control_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


