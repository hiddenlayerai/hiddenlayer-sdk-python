# ResultProvenance

Contains information about how and when a result was detected.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_detection_time_utc** | **datetime** | The Coordinated Universal Time (UTC) date and time at which the result was first detected. See \&quot;Date/time properties\&quot; in the SARIF spec for the required format. | [optional] 
**last_detection_time_utc** | **datetime** | The Coordinated Universal Time (UTC) date and time at which the result was most recently detected. See \&quot;Date/time properties\&quot; in the SARIF spec for the required format. | [optional] 
**first_detection_run_guid** | **str** | A GUID-valued string equal to the automationDetails.guid property of the run in which the result was first detected. | [optional] 
**last_detection_run_guid** | **str** | A GUID-valued string equal to the automationDetails.guid property of the run in which the result was most recently detected. | [optional] 
**invocation_index** | **int** | The index within the run.invocations array of the invocation object which describes the tool invocation that detected the result. | [optional] [default to -1]
**conversion_sources** | [**List[PhysicalLocation]**](PhysicalLocation.md) | An array of physicalLocation objects which specify the portions of an analysis tool&#39;s output that a converter transformed into the result. | [optional] [default to []]
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.result_provenance import ResultProvenance

# TODO update the JSON string below
json = "{}"
# create an instance of ResultProvenance from a JSON string
result_provenance_instance = ResultProvenance.from_json(json)
# print the JSON string representation of the object
print(ResultProvenance.to_json())

# convert the object into a dict
result_provenance_dict = result_provenance_instance.to_dict()
# create an instance of ResultProvenance from a dict
result_provenance_from_dict = ResultProvenance.from_dict(result_provenance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


