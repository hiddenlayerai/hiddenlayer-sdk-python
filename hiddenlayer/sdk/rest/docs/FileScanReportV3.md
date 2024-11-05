# FileScanReportV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_instance_id** | **str** | unique ID of the file | 
**file_location** | **str** | full file path | 
**start_time** | **datetime** | time the scan started | 
**end_time** | **datetime** | time the scan ended | 
**details** | [**FileDetailsV3**](.md) |  | 
**status** | **str** | status of the scan | 
**seen** | **datetime** | time the scan was seen at | 
**detections** | [**List[ScanDetectionV3]**](ScanDetectionV3.md) |  | 

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


