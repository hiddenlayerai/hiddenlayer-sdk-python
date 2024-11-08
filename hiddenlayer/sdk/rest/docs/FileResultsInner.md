# FileResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_instance_id** | **str** | unique ID of the file | 
**file_location** | **str** | full file path | 
**start_time** | **datetime** | time the scan started | 
**end_time** | **datetime** | time the scan ended | 
**details** | [**FileDetailsV3**](.md) |  | 
**status** | **str** | status of the scan | 
**seen** | **datetime** | time the scan was seen at | 
**detections** | [**List[ScanDetectionV3]**](ScanDetectionV3.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.file_results_inner import FileResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FileResultsInner from a JSON string
file_results_inner_instance = FileResultsInner.from_json(json)
# print the JSON string representation of the object
print(FileResultsInner.to_json())

# convert the object into a dict
file_results_inner_dict = file_results_inner_instance.to_dict()
# create an instance of FileResultsInner from a dict
file_results_inner_from_dict = FileResultsInner.from_dict(file_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


