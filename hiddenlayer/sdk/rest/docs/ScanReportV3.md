# ScanReportV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_count** | **int** | number of files scanned | 
**files_with_detections_count** | **int** | number of files with detections found | 
**detection_count** | **int** | number of detections found | 
**detection_categories** | **List[str]** | list of detection categories found | 
**inventory** | [**ModelInventoryInfo**](ModelInventoryInfo.md) |  | 
**version** | **str** | scanner version | 
**scan_id** | **str** | unique identifier for the scan | 
**start_time** | **datetime** | time the scan started | 
**end_time** | **datetime** | time the scan ended | 
**status** | **str** | status of the scan | 
**severity** | **str** | detection severity | 
**file_results** | [**List[FileScanReportV3]**](FileScanReportV3.md) |  | 

## Example

```python
from hiddenlayer.sdk.rest.models.scan_report_v3 import ScanReportV3

# TODO update the JSON string below
json = "{}"
# create an instance of ScanReportV3 from a JSON string
scan_report_v3_instance = ScanReportV3.from_json(json)
# print the JSON string representation of the object
print(ScanReportV3.to_json())

# convert the object into a dict
scan_report_v3_dict = scan_report_v3_instance.to_dict()
# create an instance of ScanReportV3 from a dict
scan_report_v3_from_dict = ScanReportV3.from_dict(scan_report_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


