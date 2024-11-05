# ScanModelIdsV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **str** | Unique identifier for the model | 
**model_version_id** | **str** | unique identifier for the model version | 

## Example

```python
from hiddenlayer.sdk.rest.models.scan_model_ids_v3 import ScanModelIdsV3

# TODO update the JSON string below
json = "{}"
# create an instance of ScanModelIdsV3 from a JSON string
scan_model_ids_v3_instance = ScanModelIdsV3.from_json(json)
# print the JSON string representation of the object
print(ScanModelIdsV3.to_json())

# convert the object into a dict
scan_model_ids_v3_dict = scan_model_ids_v3_instance.to_dict()
# create an instance of ScanModelIdsV3 from a dict
scan_model_ids_v3_from_dict = ScanModelIdsV3.from_dict(scan_model_ids_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


