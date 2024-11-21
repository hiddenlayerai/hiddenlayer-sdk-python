# ReportingConfiguration

Information about a rule or notification that can be configured at runtime.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Specifies whether the report may be produced during the scan. | [optional] [default to True]
**level** | **str** | Specifies the failure level for the report. | [optional] [default to 'warning']
**rank** | **float** | Specifies the relative priority of the report. Used for analysis output only. | [optional] [default to -1]
**parameters** | [**PropertyBag**](PropertyBag.md) |  | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.reporting_configuration import ReportingConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ReportingConfiguration from a JSON string
reporting_configuration_instance = ReportingConfiguration.from_json(json)
# print the JSON string representation of the object
print(ReportingConfiguration.to_json())

# convert the object into a dict
reporting_configuration_dict = reporting_configuration_instance.to_dict()
# create an instance of ReportingConfiguration from a dict
reporting_configuration_from_dict = ReportingConfiguration.from_dict(reporting_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


