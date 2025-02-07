# ModelScanApiV3UploadModelAddFileScanIdPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_id** | **str** | UploadId for the current file | 
**parts** | [**List[ModelScanApiV3UploadModelAddFileScanIdPost200ResponsePartsInner]**](ModelScanApiV3UploadModelAddFileScanIdPost200ResponsePartsInner.md) |  | 

## Example

```python
from hiddenlayer.sdk.rest.models.model_scan_api_v3_upload_model_add_file_scan_id_post200_response import ModelScanApiV3UploadModelAddFileScanIdPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ModelScanApiV3UploadModelAddFileScanIdPost200Response from a JSON string
model_scan_api_v3_upload_model_add_file_scan_id_post200_response_instance = ModelScanApiV3UploadModelAddFileScanIdPost200Response.from_json(json)
# print the JSON string representation of the object
print(ModelScanApiV3UploadModelAddFileScanIdPost200Response.to_json())

# convert the object into a dict
model_scan_api_v3_upload_model_add_file_scan_id_post200_response_dict = model_scan_api_v3_upload_model_add_file_scan_id_post200_response_instance.to_dict()
# create an instance of ModelScanApiV3UploadModelAddFileScanIdPost200Response from a dict
model_scan_api_v3_upload_model_add_file_scan_id_post200_response_from_dict = ModelScanApiV3UploadModelAddFileScanIdPost200Response.from_dict(model_scan_api_v3_upload_model_add_file_scan_id_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


