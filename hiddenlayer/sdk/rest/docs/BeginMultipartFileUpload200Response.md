# BeginMultipartFileUpload200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_id** | **str** | UploadId for the current file | 
**parts** | [**List[BeginMultipartFileUpload200ResponsePartsInner]**](BeginMultipartFileUpload200ResponsePartsInner.md) |  | 

## Example

```python
from hiddenlayer.sdk.rest.models.begin_multipart_file_upload200_response import BeginMultipartFileUpload200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BeginMultipartFileUpload200Response from a JSON string
begin_multipart_file_upload200_response_instance = BeginMultipartFileUpload200Response.from_json(json)
# print the JSON string representation of the object
print(BeginMultipartFileUpload200Response.to_json())

# convert the object into a dict
begin_multipart_file_upload200_response_dict = begin_multipart_file_upload200_response_instance.to_dict()
# create an instance of BeginMultipartFileUpload200Response from a dict
begin_multipart_file_upload200_response_from_dict = BeginMultipartFileUpload200Response.from_dict(begin_multipart_file_upload200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


