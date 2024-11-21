# PropertyBag

Key/value pairs that provide additional information about the object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** | A set of distinct strings that provide additional information. | [optional] [default to []]

## Example

```python
from hiddenlayer.sdk.rest.models.property_bag import PropertyBag

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyBag from a JSON string
property_bag_instance = PropertyBag.from_json(json)
# print the JSON string representation of the object
print(PropertyBag.to_json())

# convert the object into a dict
property_bag_dict = property_bag_instance.to_dict()
# create an instance of PropertyBag from a dict
property_bag_from_dict = PropertyBag.from_dict(property_bag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


