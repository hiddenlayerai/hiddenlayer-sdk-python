# Detections


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.detections import Detections

# TODO update the JSON string below
json = "{}"
# create an instance of Detections from a JSON string
detections_instance = Detections.from_json(json)
# print the JSON string representation of the object
print(Detections.to_json())

# convert the object into a dict
detections_dict = detections_instance.to_dict()
# create an instance of Detections from a dict
detections_from_dict = Detections.from_dict(detections_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


