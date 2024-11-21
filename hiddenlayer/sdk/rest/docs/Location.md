# Location

A location within a programming artifact.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Value that distinguishes this location from all other locations within a single result object. | [optional] [default to -1]
**physical_location** | [**PhysicalLocation**](PhysicalLocation.md) |  | [optional] 
**logical_locations** | [**List[LogicalLocation]**](LogicalLocation.md) | The logical locations associated with the result. | [optional] [default to []]
**message** | [**Message**](Message.md) |  | [optional] 
**annotations** | [**List[Region]**](Region.md) | A set of regions relevant to the location. | [optional] [default to []]
**relationships** | [**List[LocationRelationship]**](LocationRelationship.md) | An array of objects that describe relationships between this location and others. | [optional] [default to []]
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.location import Location

# TODO update the JSON string below
json = "{}"
# create an instance of Location from a JSON string
location_instance = Location.from_json(json)
# print the JSON string representation of the object
print(Location.to_json())

# convert the object into a dict
location_dict = location_instance.to_dict()
# create an instance of Location from a dict
location_from_dict = Location.from_dict(location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


