# MultiFileUploadRequestV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_version** | **str** | Model version | 
**model_name** | **str** | Model name | 
**requesting_entity** | **str** | Requesting entity | 
**location_alias** | **str** | Requested location alias | [optional] 
**request_source** | **str** | Identifies the system that requested the scan | [optional] 
**origin** | **str** | Specifies the platform or service where the model originated before being scanned | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.multi_file_upload_request_v3 import MultiFileUploadRequestV3

# TODO update the JSON string below
json = "{}"
# create an instance of MultiFileUploadRequestV3 from a JSON string
multi_file_upload_request_v3_instance = MultiFileUploadRequestV3.from_json(json)
# print the JSON string representation of the object
print(MultiFileUploadRequestV3.to_json())

# convert the object into a dict
multi_file_upload_request_v3_dict = multi_file_upload_request_v3_instance.to_dict()
# create an instance of MultiFileUploadRequestV3 from a dict
multi_file_upload_request_v3_from_dict = MultiFileUploadRequestV3.from_dict(multi_file_upload_request_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


