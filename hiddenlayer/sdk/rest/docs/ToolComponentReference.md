# ToolComponentReference

Identifies a particular toolComponent object, either the driver or an extension.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The &#39;name&#39; property of the referenced toolComponent. | [optional] 
**index** | **int** | An index into the referenced toolComponent in tool.extensions. | [optional] [default to -1]
**guid** | **str** | The &#39;guid&#39; property of the referenced toolComponent. | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.tool_component_reference import ToolComponentReference

# TODO update the JSON string below
json = "{}"
# create an instance of ToolComponentReference from a JSON string
tool_component_reference_instance = ToolComponentReference.from_json(json)
# print the JSON string representation of the object
print(ToolComponentReference.to_json())

# convert the object into a dict
tool_component_reference_dict = tool_component_reference_instance.to_dict()
# create an instance of ToolComponentReference from a dict
tool_component_reference_from_dict = ToolComponentReference.from_dict(tool_component_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


