# Sensor


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
from hiddenlayer.sdk.rest.models.sensor import Sensor

# TODO update the JSON string below
json = "{}"
# create an instance of Sensor from a JSON string
sensor_instance = Sensor.from_json(json)
# print the JSON string representation of the object
print(Sensor.to_json())

# convert the object into a dict
sensor_dict = sensor_instance.to_dict()
# create an instance of Sensor from a dict
sensor_from_dict = Sensor.from_dict(sensor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


