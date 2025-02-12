# SensorQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**page_size** | **int** |  | 
**page_number** | **int** |  | 
**results** | [**List[Sensor]**](Sensor.md) |  | 

## Example

```python
from hiddenlayer.sdk.rest.models.sensor_query_response import SensorQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SensorQueryResponse from a JSON string
sensor_query_response_instance = SensorQueryResponse.from_json(json)
# print the JSON string representation of the object
print(SensorQueryResponse.to_json())

# convert the object into a dict
sensor_query_response_dict = sensor_query_response_instance.to_dict()
# create an instance of SensorQueryResponse from a dict
sensor_query_response_from_dict = SensorQueryResponse.from_dict(sensor_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


