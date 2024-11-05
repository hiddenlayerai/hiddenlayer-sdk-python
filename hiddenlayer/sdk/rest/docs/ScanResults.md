# ScanResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**md5** | **str** |  | [optional] 
**rds_encoding** | **str** |  | [optional] 
**rds_min_reader_version** | **str** |  | [optional] 
**rds_version** | **str** |  | [optional] 
**rds_writer_version** | **str** |  | [optional] 
**sha256** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**subtype** | **List[str]** |  | [optional] 
**tlsh** | **str** |  | [optional] 
**pickle_modules** | **List[str]** |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.scan_results import ScanResults

# TODO update the JSON string below
json = "{}"
# create an instance of ScanResults from a JSON string
scan_results_instance = ScanResults.from_json(json)
# print the JSON string representation of the object
print(ScanResults.to_json())

# convert the object into a dict
scan_results_dict = scan_results_instance.to_dict()
# create an instance of ScanResults from a dict
scan_results_from_dict = ScanResults.from_dict(scan_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


