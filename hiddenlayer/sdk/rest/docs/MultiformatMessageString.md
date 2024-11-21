# MultiformatMessageString

A message string or message format string rendered in multiple formats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | A plain text message string or format string. | 
**markdown** | **str** | A Markdown message string or format string. | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.multiformat_message_string import MultiformatMessageString

# TODO update the JSON string below
json = "{}"
# create an instance of MultiformatMessageString from a JSON string
multiformat_message_string_instance = MultiformatMessageString.from_json(json)
# print the JSON string representation of the object
print(MultiformatMessageString.to_json())

# convert the object into a dict
multiformat_message_string_dict = multiformat_message_string_instance.to_dict()
# create an instance of MultiformatMessageString from a dict
multiformat_message_string_from_dict = MultiformatMessageString.from_dict(multiformat_message_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


