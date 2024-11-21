# Exception

Describes a runtime exception encountered during the execution of an analysis tool.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | A string that identifies the kind of exception, for example, the fully qualified type name of an object that was thrown, or the symbolic name of a signal. | [optional] 
**message** | **str** | A message that describes the exception. | [optional] 
**stack** | [**Stack**](Stack.md) |  | [optional] 
**inner_exceptions** | [**List[Exception]**](Exception.md) | An array of exception objects each of which is considered a cause of this exception. | [optional] [default to []]
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.exception import Exception

# TODO update the JSON string below
json = "{}"
# create an instance of Exception from a JSON string
exception_instance = Exception.from_json(json)
# print the JSON string representation of the object
print(Exception.to_json())

# convert the object into a dict
exception_dict = exception_instance.to_dict()
# create an instance of Exception from a dict
exception_from_dict = Exception.from_dict(exception_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


