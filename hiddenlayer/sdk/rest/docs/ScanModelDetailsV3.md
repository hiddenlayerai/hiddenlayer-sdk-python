# ScanModelDetailsV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_name** | **str** | name of the model | 
**model_version** | **str** | version of the model | 
**model_source** | **str** | source (provider) info | 
**requested_scan_location** | **str** | Location to be scanned | 
**requesting_entity** | **str** | Entity that requested the scan | 

## Example

```python
from hiddenlayer.sdk.rest.models.scan_model_details_v3 import ScanModelDetailsV3

# TODO update the JSON string below
json = "{}"
# create an instance of ScanModelDetailsV3 from a JSON string
scan_model_details_v3_instance = ScanModelDetailsV3.from_json(json)
# print the JSON string representation of the object
print(ScanModelDetailsV3.to_json())

# convert the object into a dict
scan_model_details_v3_dict = scan_model_details_v3_instance.to_dict()
# create an instance of ScanModelDetailsV3 from a dict
scan_model_details_v3_from_dict = ScanModelDetailsV3.from_dict(scan_model_details_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


