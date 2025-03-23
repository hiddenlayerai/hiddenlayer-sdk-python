# ScanModelDetailsV31


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_name** | **str** | Name of the model | 
**model_version** | **str** | If you do not provide a version, one will be generated for you. | 
**requested_scan_location** | **str** | Location to be scanned | 
**requesting_entity** | **str** | Entity that requested the scan | 

## Example

```python
from hiddenlayer.sdk.rest.models.scan_model_details_v31 import ScanModelDetailsV31

# TODO update the JSON string below
json = "{}"
# create an instance of ScanModelDetailsV31 from a JSON string
scan_model_details_v31_instance = ScanModelDetailsV31.from_json(json)
# print the JSON string representation of the object
print(ScanModelDetailsV31.to_json())

# convert the object into a dict
scan_model_details_v31_dict = scan_model_details_v31_instance.to_dict()
# create an instance of ScanModelDetailsV31 from a dict
scan_model_details_v31_from_dict = ScanModelDetailsV31.from_dict(scan_model_details_v31_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


