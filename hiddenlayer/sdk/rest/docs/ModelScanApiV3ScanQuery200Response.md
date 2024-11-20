# ModelScanApiV3ScanQuery200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ScanReportV3]**](ScanReportV3.md) |  | [optional] 
**total** | **float** | Total number of items available based on the query criteria. | 
**limit** | **int** | Maximum number of items to return | [default to 25]
**offset** | **int** | Begin returning the results from this offset | [default to 0]

## Example

```python
from hiddenlayer.sdk.rest.models.model_scan_api_v3_scan_query200_response import ModelScanApiV3ScanQuery200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ModelScanApiV3ScanQuery200Response from a JSON string
model_scan_api_v3_scan_query200_response_instance = ModelScanApiV3ScanQuery200Response.from_json(json)
# print the JSON string representation of the object
print(ModelScanApiV3ScanQuery200Response.to_json())

# convert the object into a dict
model_scan_api_v3_scan_query200_response_dict = model_scan_api_v3_scan_query200_response_instance.to_dict()
# create an instance of ModelScanApiV3ScanQuery200Response from a dict
model_scan_api_v3_scan_query200_response_from_dict = ModelScanApiV3ScanQuery200Response.from_dict(model_scan_api_v3_scan_query200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


