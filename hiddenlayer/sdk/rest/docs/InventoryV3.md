# InventoryV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_scan_location** | **str** |  | [optional] 
**model_name** | **str** |  | [optional] 
**model_source** | **str** |  | [optional] 
**model_version** | **str** |  | [optional] 
**model_version_id** | **str** |  | [optional] 
**requesting_entity** | **str** |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.inventory_v3 import InventoryV3

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryV3 from a JSON string
inventory_v3_instance = InventoryV3.from_json(json)
# print the JSON string representation of the object
print(InventoryV3.to_json())

# convert the object into a dict
inventory_v3_dict = inventory_v3_instance.to_dict()
# create an instance of InventoryV3 from a dict
inventory_v3_from_dict = InventoryV3.from_dict(inventory_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


