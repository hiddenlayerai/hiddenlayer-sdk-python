# SensorSORModelCardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **str** |  | 
**created_at** | **datetime** |  | 
**plaintext_name** | **str** |  | 
**active_versions** | **List[str]** |  | 
**source** | **str** |  | 
**tags** | **Dict[str, object]** |  | [optional] 
**model_scan_threat_level** | **str** |  | [optional] 
**attack_monitoring_threat_level** | **str** |  | [optional] 
**security_posture** | [**SecurityPosture**](SecurityPosture.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.sensor_sor_model_card_response import SensorSORModelCardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SensorSORModelCardResponse from a JSON string
sensor_sor_model_card_response_instance = SensorSORModelCardResponse.from_json(json)
# print the JSON string representation of the object
print(SensorSORModelCardResponse.to_json())

# convert the object into a dict
sensor_sor_model_card_response_dict = sensor_sor_model_card_response_instance.to_dict()
# create an instance of SensorSORModelCardResponse from a dict
sensor_sor_model_card_response_from_dict = SensorSORModelCardResponse.from_dict(sensor_sor_model_card_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


