# RunAutomationDetails

Information that describes a run's identity and role within an engineering system process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**Message**](Message.md) |  | [optional] 
**id** | **str** | A hierarchical string that uniquely identifies this object&#39;s containing run object. | [optional] 
**guid** | **str** | A stable, unique identifier for this object&#39;s containing run object in the form of a GUID. | [optional] 
**correlation_guid** | **str** | A stable, unique identifier for the equivalence class of runs to which this object&#39;s containing run object belongs in the form of a GUID. | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.run_automation_details import RunAutomationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RunAutomationDetails from a JSON string
run_automation_details_instance = RunAutomationDetails.from_json(json)
# print the JSON string representation of the object
print(RunAutomationDetails.to_json())

# convert the object into a dict
run_automation_details_dict = run_automation_details_instance.to_dict()
# create an instance of RunAutomationDetails from a dict
run_automation_details_from_dict = RunAutomationDetails.from_dict(run_automation_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


