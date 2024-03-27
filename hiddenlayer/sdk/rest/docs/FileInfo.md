# FileInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**md5** | **str** |  | [optional] 
**sha256** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**subtype** | **List[str]** |  | [optional] 
**tlsh** | **str** |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.file_info import FileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FileInfo from a JSON string
file_info_instance = FileInfo.from_json(json)
# print the JSON string representation of the object
print FileInfo.to_json()

# convert the object into a dict
file_info_dict = file_info_instance.to_dict()
# create an instance of FileInfo from a dict
file_info_form_dict = file_info.from_dict(file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


