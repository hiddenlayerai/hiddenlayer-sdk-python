# StackFrame

A function call within a stack trace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | [**Location**](Location.md) |  | [optional] 
**module** | **str** | The name of the module that contains the code of this stack frame. | [optional] 
**thread_id** | **int** | The thread identifier of the stack frame. | [optional] 
**parameters** | **List[str]** | The parameters of the call that is executing. | [optional] [default to []]
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.stack_frame import StackFrame

# TODO update the JSON string below
json = "{}"
# create an instance of StackFrame from a JSON string
stack_frame_instance = StackFrame.from_json(json)
# print the JSON string representation of the object
print(StackFrame.to_json())

# convert the object into a dict
stack_frame_dict = stack_frame_instance.to_dict()
# create an instance of StackFrame from a dict
stack_frame_from_dict = StackFrame.from_dict(stack_frame_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


