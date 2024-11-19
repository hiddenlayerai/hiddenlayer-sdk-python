# ModelInventoryInfo

information about model and version that this scan relates to

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_name** | **str** | name of the model | 
**model_version** | **str** | version of the model | 
**model_source** | **str** | source (provider) info | 
**requested_scan_location** | **str** | Location to be scanned | 
**requesting_entity** | **str** | Entity that requested the scan | [optional] 
**model_id** | **str** | Unique identifier for the model | 
**model_version_id** | **str** | unique identifier for the model version | 

## Example

```python
from hiddenlayer.sdk.rest.models.model_inventory_info import ModelInventoryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ModelInventoryInfo from a JSON string
model_inventory_info_instance = ModelInventoryInfo.from_json(json)
# print the JSON string representation of the object
print(ModelInventoryInfo.to_json())

# convert the object into a dict
model_inventory_info_dict = model_inventory_info_instance.to_dict()
# create an instance of ModelInventoryInfo from a dict
model_inventory_info_from_dict = ModelInventoryInfo.from_dict(model_inventory_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


