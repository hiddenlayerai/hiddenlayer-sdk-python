# GetMultipartUploadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_id** | **str** |  | 
**parts** | [**List[MultipartUploadPart]**](MultipartUploadPart.md) |  | 

## Example

```python
from hiddenlayer.rest.models.get_multipart_upload_response import GetMultipartUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMultipartUploadResponse from a JSON string
get_multipart_upload_response_instance = GetMultipartUploadResponse.from_json(json)
# print the JSON string representation of the object
print GetMultipartUploadResponse.to_json()

# convert the object into a dict
get_multipart_upload_response_dict = get_multipart_upload_response_instance.to_dict()
# create an instance of GetMultipartUploadResponse from a dict
get_multipart_upload_response_form_dict = get_multipart_upload_response.from_dict(get_multipart_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


