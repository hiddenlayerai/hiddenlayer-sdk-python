# ScanResultsMapV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**List[PaginationV3]**](PaginationV3.md) |  | 
**items** | [**List[ScanResultsV3]**](ScanResultsV3.md) |  | 

## Example

```python
from hiddenlayer.sdk.rest.models.scan_results_map_v3 import ScanResultsMapV3

# TODO update the JSON string below
json = "{}"
# create an instance of ScanResultsMapV3 from a JSON string
scan_results_map_v3_instance = ScanResultsMapV3.from_json(json)
# print the JSON string representation of the object
print(ScanResultsMapV3.to_json())

# convert the object into a dict
scan_results_map_v3_dict = scan_results_map_v3_instance.to_dict()
# create an instance of ScanResultsMapV3 from a dict
scan_results_map_v3_from_dict = ScanResultsMapV3.from_dict(scan_results_map_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


