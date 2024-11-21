# ConfigurationOverride

Information about how a specific rule or notification was reconfigured at runtime.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**ReportingConfiguration**](ReportingConfiguration.md) |  | 
**descriptor** | [**ReportingDescriptorReference**](ReportingDescriptorReference.md) |  | 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.configuration_override import ConfigurationOverride

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationOverride from a JSON string
configuration_override_instance = ConfigurationOverride.from_json(json)
# print the JSON string representation of the object
print(ConfigurationOverride.to_json())

# convert the object into a dict
configuration_override_dict = configuration_override_instance.to_dict()
# create an instance of ConfigurationOverride from a dict
configuration_override_from_dict = ConfigurationOverride.from_dict(configuration_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


