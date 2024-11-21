# CodeFlow

A set of threadFlows which together describe a pattern of code execution relevant to detecting a result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | [**Message**](Message.md) |  | [optional] 
**thread_flows** | [**List[ThreadFlow]**](ThreadFlow.md) | An array of one or more unique threadFlow objects, each of which describes the progress of a program through a thread of execution. | 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.code_flow import CodeFlow

# TODO update the JSON string below
json = "{}"
# create an instance of CodeFlow from a JSON string
code_flow_instance = CodeFlow.from_json(json)
# print the JSON string representation of the object
print(CodeFlow.to_json())

# convert the object into a dict
code_flow_dict = code_flow_instance.to_dict()
# create an instance of CodeFlow from a dict
code_flow_from_dict = CodeFlow.from_dict(code_flow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


