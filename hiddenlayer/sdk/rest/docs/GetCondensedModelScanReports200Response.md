# GetCondensedModelScanReports200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ScanReportV3]**](ScanReportV3.md) |  | [optional] 
**total** | **int** | Total number of items available based on the query criteria. | 
**limit** | **int** | Maximum number of items to return | [default to 25]
**offset** | **int** | Begin returning the results from this offset | [default to 0]

## Example

```python
from hiddenlayer.sdk.rest.models.get_condensed_model_scan_reports200_response import GetCondensedModelScanReports200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCondensedModelScanReports200Response from a JSON string
get_condensed_model_scan_reports200_response_instance = GetCondensedModelScanReports200Response.from_json(json)
# print the JSON string representation of the object
print(GetCondensedModelScanReports200Response.to_json())

# convert the object into a dict
get_condensed_model_scan_reports200_response_dict = get_condensed_model_scan_reports200_response_instance.to_dict()
# create an instance of GetCondensedModelScanReports200Response from a dict
get_condensed_model_scan_reports200_response_from_dict = GetCondensedModelScanReports200Response.from_dict(get_condensed_model_scan_reports200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


