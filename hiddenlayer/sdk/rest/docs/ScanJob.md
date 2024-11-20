# ScanJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scan_id** | **str** | unique identifier for the scan | [optional] [readonly] 
**status** | **str** | Status of the scan | [optional] [readonly] 
**inventory** | [**ScanJobInventory**](ScanJobInventory.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.scan_job import ScanJob

# TODO update the JSON string below
json = "{}"
# create an instance of ScanJob from a JSON string
scan_job_instance = ScanJob.from_json(json)
# print the JSON string representation of the object
print(ScanJob.to_json())

# convert the object into a dict
scan_job_dict = scan_job_instance.to_dict()
# create an instance of ScanJob from a dict
scan_job_from_dict = ScanJob.from_dict(scan_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


