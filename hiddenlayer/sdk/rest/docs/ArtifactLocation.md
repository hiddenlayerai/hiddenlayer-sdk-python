# ArtifactLocation

Specifies the location of an artifact.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | A string containing a valid relative or absolute URI. | [optional] 
**uri_base_id** | **str** | A string which indirectly specifies the absolute URI with respect to which a relative URI in the \&quot;uri\&quot; property is interpreted. | [optional] 
**index** | **int** | The index within the run artifacts array of the artifact object associated with the artifact location. | [optional] [default to -1]
**description** | [**Message**](Message.md) |  | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.artifact_location import ArtifactLocation

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactLocation from a JSON string
artifact_location_instance = ArtifactLocation.from_json(json)
# print the JSON string representation of the object
print(ArtifactLocation.to_json())

# convert the object into a dict
artifact_location_dict = artifact_location_instance.to_dict()
# create an instance of ArtifactLocation from a dict
artifact_location_from_dict = ArtifactLocation.from_dict(artifact_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


