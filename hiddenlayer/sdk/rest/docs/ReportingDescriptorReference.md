# ReportingDescriptorReference

Information about how to locate a relevant reporting descriptor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the descriptor. | [optional] 
**index** | **int** | The index into an array of descriptors in toolComponent.ruleDescriptors, toolComponent.notificationDescriptors, or toolComponent.taxonomyDescriptors, depending on context. | [optional] [default to -1]
**guid** | **str** | A guid that uniquely identifies the descriptor. | [optional] 
**tool_component** | [**ToolComponentReference**](ToolComponentReference.md) |  | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.reporting_descriptor_reference import ReportingDescriptorReference

# TODO update the JSON string below
json = "{}"
# create an instance of ReportingDescriptorReference from a JSON string
reporting_descriptor_reference_instance = ReportingDescriptorReference.from_json(json)
# print the JSON string representation of the object
print(ReportingDescriptorReference.to_json())

# convert the object into a dict
reporting_descriptor_reference_dict = reporting_descriptor_reference_instance.to_dict()
# create an instance of ReportingDescriptorReference from a dict
reporting_descriptor_reference_from_dict = ReportingDescriptorReference.from_dict(reporting_descriptor_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


