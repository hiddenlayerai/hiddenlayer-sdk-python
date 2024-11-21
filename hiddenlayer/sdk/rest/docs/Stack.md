# Stack

A call stack that is relevant to a result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | [**Message**](Message.md) |  | [optional] 
**frames** | [**List[StackFrame]**](StackFrame.md) | An array of stack frames that represents a sequence of calls, rendered in reverse chronological order, that comprise the call stack. | 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.stack import Stack

# TODO update the JSON string below
json = "{}"
# create an instance of Stack from a JSON string
stack_instance = Stack.from_json(json)
# print the JSON string representation of the object
print(Stack.to_json())

# convert the object into a dict
stack_dict = stack_instance.to_dict()
# create an instance of Stack from a dict
stack_from_dict = Stack.from_dict(stack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


