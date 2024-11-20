# FileScanReportV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_results** | [**List[FileResultsInner]**](FileResultsInner.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.file_scan_report_v3 import FileScanReportV3

# TODO update the JSON string below
json = "{}"
# create an instance of FileScanReportV3 from a JSON string
file_scan_report_v3_instance = FileScanReportV3.from_json(json)
# print the JSON string representation of the object
print(FileScanReportV3.to_json())

# convert the object into a dict
file_scan_report_v3_dict = file_scan_report_v3_instance.to_dict()
# create an instance of FileScanReportV3 from a dict
file_scan_report_v3_from_dict = FileScanReportV3.from_dict(file_scan_report_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


