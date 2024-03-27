# SensorSORQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**SensorSORQueryFilter**](SensorSORQueryFilter.md) |  | [optional] 
**order_by** | **str** |  | [optional] [default to 'created_at']
**order_dir** | **str** |  | [optional] 
**page_size** | **int** |  | [optional] [default to 25]
**page_number** | **int** |  | [optional] [default to 0]

## Example

```python
from hiddenlayer.sdk.rest.models.sensor_sor_query_request import SensorSORQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SensorSORQueryRequest from a JSON string
sensor_sor_query_request_instance = SensorSORQueryRequest.from_json(json)
# print the JSON string representation of the object
print SensorSORQueryRequest.to_json()

# convert the object into a dict
sensor_sor_query_request_dict = sensor_sor_query_request_instance.to_dict()
# create an instance of SensorSORQueryRequest from a dict
sensor_sor_query_request_form_dict = sensor_sor_query_request.from_dict(sensor_sor_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


