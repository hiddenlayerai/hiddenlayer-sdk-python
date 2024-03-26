# ModelQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**page_size** | **int** |  | 
**page_number** | **int** |  | 
**results** | [**List[Model]**](Model.md) |  | 

## Example

```python
from hiddenlayer.rest.models.model_query_response import ModelQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelQueryResponse from a JSON string
model_query_response_instance = ModelQueryResponse.from_json(json)
# print the JSON string representation of the object
print ModelQueryResponse.to_json()

# convert the object into a dict
model_query_response_dict = model_query_response_instance.to_dict()
# create an instance of ModelQueryResponse from a dict
model_query_response_form_dict = model_query_response.from_dict(model_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


