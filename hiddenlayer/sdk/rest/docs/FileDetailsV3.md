# FileDetailsV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**estimated_time** | **str** | estimated time to scan the file | 
**md5** | **str** | hexadecimal md5 hash of file | 
**sha256** | **str** | hexadecimal sha256 hash of file | 
**tlsh** | **str** | TLSH hash of file | 
**file_size** | **str** | size of the file in human readable format | [optional] 
**file_size_bytes** | **int** | size of the file in bytes | [optional] 
**file_type** | **str** | type of the file | 
**file_type_details** | **Dict[str, object]** |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.file_details_v3 import FileDetailsV3

# TODO update the JSON string below
json = "{}"
# create an instance of FileDetailsV3 from a JSON string
file_details_v3_instance = FileDetailsV3.from_json(json)
# print the JSON string representation of the object
print(FileDetailsV3.to_json())

# convert the object into a dict
file_details_v3_dict = file_details_v3_instance.to_dict()
# create an instance of FileDetailsV3 from a dict
file_details_v3_from_dict = FileDetailsV3.from_dict(file_details_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


