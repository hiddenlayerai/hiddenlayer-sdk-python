# CreateSensorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plaintext_name** | **str** |  | 
**version** | **int** |  | [optional] 
**active** | **bool** |  | [optional] [default to True]
**tags** | **Dict[str, object]** |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.create_sensor_request import CreateSensorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSensorRequest from a JSON string
create_sensor_request_instance = CreateSensorRequest.from_json(json)
# print the JSON string representation of the object
print CreateSensorRequest.to_json()

# convert the object into a dict
create_sensor_request_dict = create_sensor_request_instance.to_dict()
# create an instance of CreateSensorRequest from a dict
create_sensor_request_form_dict = create_sensor_request.from_dict(create_sensor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


