# ScanHeaderV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_count** | **int** | number of files scanned | 
**files_with_detections_count** | **int** | number of files with detections found | 
**detection_count** | **int** | number of detections found | 
**detection_categories** | **List[str]** | list of detection categories found | [optional] 
**inventory** | [**ModelInventoryInfo**](ModelInventoryInfo.md) |  | 
**version** | **str** | scanner version | 
**scan_id** | **str** | unique identifier for the scan | 
**start_time** | **datetime** | time the scan started | 
**end_time** | **datetime** | time the scan ended | [optional] 
**status** | **str** | status of the scan | 
**severity** | **str** | detection severity | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.scan_header_v3 import ScanHeaderV3

# TODO update the JSON string below
json = "{}"
# create an instance of ScanHeaderV3 from a JSON string
scan_header_v3_instance = ScanHeaderV3.from_json(json)
# print the JSON string representation of the object
print(ScanHeaderV3.to_json())

# convert the object into a dict
scan_header_v3_dict = scan_header_v3_instance.to_dict()
# create an instance of ScanHeaderV3 from a dict
scan_header_v3_from_dict = ScanHeaderV3.from_dict(scan_header_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


