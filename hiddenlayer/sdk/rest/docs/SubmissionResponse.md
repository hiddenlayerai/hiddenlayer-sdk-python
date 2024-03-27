# SubmissionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**sensor_id** | **str** |  | 
**requester_id** | **str** |  | 
**group_id** | **str** |  | 
**event_time** | **str** |  | 

## Example

```python
from hiddenlayer.sdk.rest.models.submission_response import SubmissionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionResponse from a JSON string
submission_response_instance = SubmissionResponse.from_json(json)
# print the JSON string representation of the object
print SubmissionResponse.to_json()

# convert the object into a dict
submission_response_dict = submission_response_instance.to_dict()
# create an instance of SubmissionResponse from a dict
submission_response_form_dict = submission_response.from_dict(submission_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


