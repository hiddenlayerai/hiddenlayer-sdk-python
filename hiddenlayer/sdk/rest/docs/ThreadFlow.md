# ThreadFlow

Describes a sequence of code locations that specify a path through a single thread of execution such as an operating system or fiber.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An string that uniquely identifies the threadFlow within the codeFlow in which it occurs. | [optional] 
**message** | [**Message**](Message.md) |  | [optional] 
**initial_state** | [**Dict[str, MultiformatMessageString]**](MultiformatMessageString.md) | Values of relevant expressions at the start of the thread flow that may change during thread flow execution. | [optional] 
**immutable_state** | [**Dict[str, MultiformatMessageString]**](MultiformatMessageString.md) | Values of relevant expressions at the start of the thread flow that remain constant. | [optional] 
**locations** | [**List[ThreadFlowLocation]**](ThreadFlowLocation.md) | A temporally ordered array of &#39;threadFlowLocation&#39; objects, each of which describes a location visited by the tool while producing the result. | 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.thread_flow import ThreadFlow

# TODO update the JSON string below
json = "{}"
# create an instance of ThreadFlow from a JSON string
thread_flow_instance = ThreadFlow.from_json(json)
# print the JSON string representation of the object
print(ThreadFlow.to_json())

# convert the object into a dict
thread_flow_dict = thread_flow_instance.to_dict()
# create an instance of ThreadFlow from a dict
thread_flow_from_dict = ThreadFlow.from_dict(thread_flow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


