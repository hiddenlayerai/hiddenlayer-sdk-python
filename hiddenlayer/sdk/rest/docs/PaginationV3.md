# PaginationV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **str** |  | 
**first** | **str** |  | 
**prev** | **str** |  | 
**next** | **str** |  | 
**last** | **str** |  | 

## Example

```python
from hiddenlayer.sdk.rest.models.pagination_v3 import PaginationV3

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationV3 from a JSON string
pagination_v3_instance = PaginationV3.from_json(json)
# print the JSON string representation of the object
print(PaginationV3.to_json())

# convert the object into a dict
pagination_v3_dict = pagination_v3_instance.to_dict()
# create an instance of PaginationV3 from a dict
pagination_v3_from_dict = PaginationV3.from_dict(pagination_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


