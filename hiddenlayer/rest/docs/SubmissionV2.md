# SubmissionV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **object** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**sensor_id** | **str** |  | [optional] 
**model_id** | **str** |  | 
**requester_id** | **str** |  | [optional] [default to 'UNKNOWN']
**input_layer** | **str** |  | 
**input_layer_dtype** | **str** |  | 
**input_layer_shape** | **List[float]** |  | 
**output_layer** | **str** |  | 
**output_layer_dtype** | **str** |  | 
**output_layer_shape** | **List[float]** |  | 
**predictions** | **List[float]** |  | [optional] 
**event_time** | **str** |  | [optional] 

## Example

```python
from hiddenlayer.rest.models.submission_v2 import SubmissionV2

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionV2 from a JSON string
submission_v2_instance = SubmissionV2.from_json(json)
# print the JSON string representation of the object
print SubmissionV2.to_json()

# convert the object into a dict
submission_v2_dict = submission_v2_instance.to_dict()
# create an instance of SubmissionV2 from a dict
submission_v2_form_dict = submission_v2.from_dict(submission_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


