# PhysicalLocation

A physical location relevant to a result. Specifies a reference to a programming artifact together with a range of bytes or characters within that artifact.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) |  | [optional] 
**artifact_location** | [**ArtifactLocation**](ArtifactLocation.md) |  | [optional] 
**region** | [**Region**](Region.md) |  | [optional] 
**context_region** | [**Region**](Region.md) |  | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.physical_location import PhysicalLocation

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalLocation from a JSON string
physical_location_instance = PhysicalLocation.from_json(json)
# print the JSON string representation of the object
print(PhysicalLocation.to_json())

# convert the object into a dict
physical_location_dict = physical_location_instance.to_dict()
# create an instance of PhysicalLocation from a dict
physical_location_from_dict = PhysicalLocation.from_dict(physical_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


