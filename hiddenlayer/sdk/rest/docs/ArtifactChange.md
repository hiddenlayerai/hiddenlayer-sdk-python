# ArtifactChange

A change to a single artifact.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact_location** | [**ArtifactLocation**](ArtifactLocation.md) |  | 
**replacements** | [**List[Replacement]**](Replacement.md) | An array of replacement objects, each of which represents the replacement of a single region in a single artifact specified by &#39;artifactLocation&#39;. | 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.artifact_change import ArtifactChange

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactChange from a JSON string
artifact_change_instance = ArtifactChange.from_json(json)
# print the JSON string representation of the object
print(ArtifactChange.to_json())

# convert the object into a dict
artifact_change_dict = artifact_change_instance.to_dict()
# create an instance of ArtifactChange from a dict
artifact_change_from_dict = ArtifactChange.from_dict(artifact_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


