# SpecialLocations

Defines locations of special significance to SARIF consumers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_base** | [**ArtifactLocation**](ArtifactLocation.md) |  | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.special_locations import SpecialLocations

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialLocations from a JSON string
special_locations_instance = SpecialLocations.from_json(json)
# print the JSON string representation of the object
print(SpecialLocations.to_json())

# convert the object into a dict
special_locations_dict = special_locations_instance.to_dict()
# create an instance of SpecialLocations from a dict
special_locations_from_dict = SpecialLocations.from_dict(special_locations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


