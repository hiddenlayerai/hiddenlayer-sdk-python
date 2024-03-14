# SensorSORItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sensor_id** | **str** |  | 
**created_at** | **datetime** |  | 
**tenant_id** | **str** |  | 
**plaintext_name** | **str** |  | 
**active** | **bool** |  | 
**version** | **int** |  | 
**tags** | **Dict[str, object]** |  | [optional] 

## Example

```python
from hiddenlayer.rest.models.sensor_sor_item_response import SensorSORItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SensorSORItemResponse from a JSON string
sensor_sor_item_response_instance = SensorSORItemResponse.from_json(json)
# print the JSON string representation of the object
print SensorSORItemResponse.to_json()

# convert the object into a dict
sensor_sor_item_response_dict = sensor_sor_item_response_instance.to_dict()
# create an instance of SensorSORItemResponse from a dict
sensor_sor_item_response_form_dict = sensor_sor_item_response.from_dict(sensor_sor_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


