# MultipartUploadPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**part_number** | **float** |  | 
**start_offset** | **float** |  | 
**end_offset** | **float** |  | 

## Example

```python
from hiddenlayer.sdk.rest.models.multipart_upload_part import MultipartUploadPart

# TODO update the JSON string below
json = "{}"
# create an instance of MultipartUploadPart from a JSON string
multipart_upload_part_instance = MultipartUploadPart.from_json(json)
# print the JSON string representation of the object
print MultipartUploadPart.to_json()

# convert the object into a dict
multipart_upload_part_dict = multipart_upload_part_instance.to_dict()
# create an instance of MultipartUploadPart from a dict
multipart_upload_part_form_dict = multipart_upload_part.from_dict(multipart_upload_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


