# Tool

The analysis tool that was run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver** | [**ToolComponent**](ToolComponent.md) |  | 
**extensions** | [**List[ToolComponent]**](ToolComponent.md) | Tool extensions that contributed to or reconfigured the analysis tool that was run. | [optional] [default to []]
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.tool import Tool

# TODO update the JSON string below
json = "{}"
# create an instance of Tool from a JSON string
tool_instance = Tool.from_json(json)
# print the JSON string representation of the object
print(Tool.to_json())

# convert the object into a dict
tool_dict = tool_instance.to_dict()
# create an instance of Tool from a dict
tool_from_dict = Tool.from_dict(tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


