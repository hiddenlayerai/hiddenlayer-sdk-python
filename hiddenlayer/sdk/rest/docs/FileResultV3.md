# FileResultV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_location** | **str** |  | 
**status** | **str** |  | 
**start_time** | **int** |  | [optional] 
**end_time** | **int** |  | [optional] 
**details** | [**FileDetailsV3**](.md) |  | [optional] 
**seen** | **int** |  | [optional] 
**detections** | [**List[ScanDetectionV31]**](ScanDetectionV31.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.file_result_v3 import FileResultV3

# TODO update the JSON string below
json = "{}"
# create an instance of FileResultV3 from a JSON string
file_result_v3_instance = FileResultV3.from_json(json)
# print the JSON string representation of the object
print(FileResultV3.to_json())

# convert the object into a dict
file_result_v3_dict = file_result_v3_instance.to_dict()
# create an instance of FileResultV3 from a dict
file_result_v3_from_dict = FileResultV3.from_dict(file_result_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


