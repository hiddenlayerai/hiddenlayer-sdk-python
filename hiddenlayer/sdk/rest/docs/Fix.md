# Fix

A proposed fix for the problem represented by a result object. A fix specifies a set of artifacts to modify. For each artifact, it specifies a set of bytes to remove, and provides a set of new bytes to replace them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**Message**](Message.md) |  | [optional] 
**artifact_changes** | [**List[ArtifactChange]**](ArtifactChange.md) | One or more artifact changes that comprise a fix for a result. | 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.fix import Fix

# TODO update the JSON string below
json = "{}"
# create an instance of Fix from a JSON string
fix_instance = Fix.from_json(json)
# print the JSON string representation of the object
print(Fix.to_json())

# convert the object into a dict
fix_dict = fix_instance.to_dict()
# create an instance of Fix from a dict
fix_from_dict = Fix.from_dict(fix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


