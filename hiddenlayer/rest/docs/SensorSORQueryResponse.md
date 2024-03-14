# SensorSORQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**page_size** | **int** |  | 
**page_number** | **int** |  | 
**results** | [**List[SensorSORItemResponse]**](SensorSORItemResponse.md) |  | 

## Example

```python
from hiddenlayer.rest.models.sensor_sor_query_response import SensorSORQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SensorSORQueryResponse from a JSON string
sensor_sor_query_response_instance = SensorSORQueryResponse.from_json(json)
# print the JSON string representation of the object
print SensorSORQueryResponse.to_json()

# convert the object into a dict
sensor_sor_query_response_dict = sensor_sor_query_response_instance.to_dict()
# create an instance of SensorSORQueryResponse from a dict
sensor_sor_query_response_form_dict = sensor_sor_query_response.from_dict(sensor_sor_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


