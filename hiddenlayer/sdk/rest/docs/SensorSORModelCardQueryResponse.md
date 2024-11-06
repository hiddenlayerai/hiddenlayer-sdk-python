# SensorSORModelCardQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**page_size** | **int** |  | 
**page_number** | **int** |  | 
**results** | [**List[SensorSORModelCardResponse]**](SensorSORModelCardResponse.md) |  | 

## Example

```python
from hiddenlayer.sdk.rest.models.sensor_sor_model_card_query_response import SensorSORModelCardQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SensorSORModelCardQueryResponse from a JSON string
sensor_sor_model_card_query_response_instance = SensorSORModelCardQueryResponse.from_json(json)
# print the JSON string representation of the object
print(SensorSORModelCardQueryResponse.to_json())

# convert the object into a dict
sensor_sor_model_card_query_response_dict = sensor_sor_model_card_query_response_instance.to_dict()
# create an instance of SensorSORModelCardQueryResponse from a dict
sensor_sor_model_card_query_response_from_dict = SensorSORModelCardQueryResponse.from_dict(sensor_sor_model_card_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


