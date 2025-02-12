# BeginMultipartFileUpload200ResponsePartsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**part_number** | **int** |  | [optional] 
**start_offset** | **int** |  | [optional] 
**stop_offset** | **int** |  | [optional] 
**upload_url** | **str** |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.begin_multipart_file_upload200_response_parts_inner import BeginMultipartFileUpload200ResponsePartsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BeginMultipartFileUpload200ResponsePartsInner from a JSON string
begin_multipart_file_upload200_response_parts_inner_instance = BeginMultipartFileUpload200ResponsePartsInner.from_json(json)
# print the JSON string representation of the object
print(BeginMultipartFileUpload200ResponsePartsInner.to_json())

# convert the object into a dict
begin_multipart_file_upload200_response_parts_inner_dict = begin_multipart_file_upload200_response_parts_inner_instance.to_dict()
# create an instance of BeginMultipartFileUpload200ResponsePartsInner from a dict
begin_multipart_file_upload200_response_parts_inner_from_dict = BeginMultipartFileUpload200ResponsePartsInner.from_dict(begin_multipart_file_upload200_response_parts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


