# LocationRelationship

Information about the relation of one location to another.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **int** | A reference to the related location. | 
**kinds** | **List[str]** | A set of distinct strings that categorize the relationship. Well-known kinds include &#39;includes&#39;, &#39;isIncludedBy&#39; and &#39;relevant&#39;. | [optional] [default to ["relevant"]]
**description** | [**Message**](Message.md) |  | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.location_relationship import LocationRelationship

# TODO update the JSON string below
json = "{}"
# create an instance of LocationRelationship from a JSON string
location_relationship_instance = LocationRelationship.from_json(json)
# print the JSON string representation of the object
print(LocationRelationship.to_json())

# convert the object into a dict
location_relationship_dict = location_relationship_instance.to_dict()
# create an instance of LocationRelationship from a dict
location_relationship_from_dict = LocationRelationship.from_dict(location_relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


