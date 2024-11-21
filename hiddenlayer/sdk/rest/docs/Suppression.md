# Suppression

A suppression that is relevant to a result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | A stable, unique identifier for the suppression in the form of a GUID. | [optional] 
**kind** | **str** | A string that indicates where the suppression is persisted. | 
**status** | **str** | A string that indicates the review status of the suppression. | [optional] 
**justification** | **str** | A string representing the justification for the suppression. | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.suppression import Suppression

# TODO update the JSON string below
json = "{}"
# create an instance of Suppression from a JSON string
suppression_instance = Suppression.from_json(json)
# print the JSON string representation of the object
print(Suppression.to_json())

# convert the object into a dict
suppression_dict = suppression_instance.to_dict()
# create an instance of Suppression from a dict
suppression_from_dict = Suppression.from_dict(suppression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


