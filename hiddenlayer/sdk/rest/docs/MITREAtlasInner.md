# MITREAtlasInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**technique** | **str** | MITRE Atlas Technique | [optional] 
**tactic** | **str** | MITRE Atlas Tactic | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.mitre_atlas_inner import MITREAtlasInner

# TODO update the JSON string below
json = "{}"
# create an instance of MITREAtlasInner from a JSON string
mitre_atlas_inner_instance = MITREAtlasInner.from_json(json)
# print the JSON string representation of the object
print(MITREAtlasInner.to_json())

# convert the object into a dict
mitre_atlas_inner_dict = mitre_atlas_inner_instance.to_dict()
# create an instance of MITREAtlasInner from a dict
mitre_atlas_inner_from_dict = MITREAtlasInner.from_dict(mitre_atlas_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


