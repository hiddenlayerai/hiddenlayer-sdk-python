# SecurityPosture


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_scan** | **bool** |  | [optional] 
**attack_monitoring** | **bool** |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.security_posture import SecurityPosture

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityPosture from a JSON string
security_posture_instance = SecurityPosture.from_json(json)
# print the JSON string representation of the object
print(SecurityPosture.to_json())

# convert the object into a dict
security_posture_dict = security_posture_instance.to_dict()
# create an instance of SecurityPosture from a dict
security_posture_from_dict = SecurityPosture.from_dict(security_posture_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


