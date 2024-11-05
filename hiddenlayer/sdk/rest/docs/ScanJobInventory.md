# ScanJobInventory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_scan_location** | **str** | Location to be scanned | [optional] 
**model_name** | **str** | name of the model | 
**model_version** | **str** | version of the model | 
**model_source** | **str** | source (provider) info | 
**requesting_entity** | **str** | Entity that requested the scan | 
**model_id** | **str** | Unique identifier for the model | 
**model_version_id** | **str** | unique identifier for the model version | 

## Example

```python
from hiddenlayer.sdk.rest.models.scan_job_inventory import ScanJobInventory

# TODO update the JSON string below
json = "{}"
# create an instance of ScanJobInventory from a JSON string
scan_job_inventory_instance = ScanJobInventory.from_json(json)
# print the JSON string representation of the object
print(ScanJobInventory.to_json())

# convert the object into a dict
scan_job_inventory_dict = scan_job_inventory_instance.to_dict()
# create an instance of ScanJobInventory from a dict
scan_job_inventory_from_dict = ScanJobInventory.from_dict(scan_job_inventory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


