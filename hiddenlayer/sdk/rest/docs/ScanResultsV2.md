# ScanResultsV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scan_id** | **str** |  | 
**status** | **str** |  | 
**start_time** | **int** |  | 
**end_time** | **int** |  | 
**results** | [**FileInfo**](FileInfo.md) |  | 
**detections** | **List[object]** |  | 

## Example

```python
from hiddenlayer.sdk.rest.models.scan_results_v2 import ScanResultsV2

# TODO update the JSON string below
json = "{}"
# create an instance of ScanResultsV2 from a JSON string
scan_results_v2_instance = ScanResultsV2.from_json(json)
# print the JSON string representation of the object
print(ScanResultsV2.to_json())

# convert the object into a dict
scan_results_v2_dict = scan_results_v2_instance.to_dict()
# create an instance of ScanResultsV2 from a dict
scan_results_v2_from_dict = ScanResultsV2.from_dict(scan_results_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


