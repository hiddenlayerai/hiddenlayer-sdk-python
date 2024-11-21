# Replacement

The replacement of a single region of an artifact.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_region** | [**Region**](Region.md) |  | 
**inserted_content** | [**ArtifactContent**](ArtifactContent.md) |  | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.replacement import Replacement

# TODO update the JSON string below
json = "{}"
# create an instance of Replacement from a JSON string
replacement_instance = Replacement.from_json(json)
# print the JSON string representation of the object
print(Replacement.to_json())

# convert the object into a dict
replacement_dict = replacement_instance.to_dict()
# create an instance of Replacement from a dict
replacement_from_dict = Replacement.from_dict(replacement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


