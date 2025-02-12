# ScanResultsV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scan_id** | **str** |  | [optional] 
**start_time** | **int** |  | [optional] 
**end_time** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**inventory** | [**InventoryV3**](.md) |  | [optional] 
**file_results** | [**List[FileResultV3]**](FileResultV3.md) |  | 

## Example

```python
from hiddenlayer.sdk.rest.models.scan_results_v3 import ScanResultsV3

# TODO update the JSON string below
json = "{}"
# create an instance of ScanResultsV3 from a JSON string
scan_results_v3_instance = ScanResultsV3.from_json(json)
# print the JSON string representation of the object
print(ScanResultsV3.to_json())

# convert the object into a dict
scan_results_v3_dict = scan_results_v3_instance.to_dict()
# create an instance of ScanResultsV3 from a dict
scan_results_v3_from_dict = ScanResultsV3.from_dict(scan_results_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


