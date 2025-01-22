# PagedResponseWithTotal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[str]** | List of items. If no matching items are found, then &#x60;[]&#x60; will be returned. | [optional] 
**total** | **int** | Total number of items available based on the query criteria. | 
**limit** | **int** | Maximum number of items to return | [default to 25]
**offset** | **int** | Begin returning the results from this offset | [default to 0]

## Example

```python
from hiddenlayer.sdk.rest.models.paged_response_with_total import PagedResponseWithTotal

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResponseWithTotal from a JSON string
paged_response_with_total_instance = PagedResponseWithTotal.from_json(json)
# print the JSON string representation of the object
print(PagedResponseWithTotal.to_json())

# convert the object into a dict
paged_response_with_total_dict = paged_response_with_total_instance.to_dict()
# create an instance of PagedResponseWithTotal from a dict
paged_response_with_total_from_dict = PagedResponseWithTotal.from_dict(paged_response_with_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


