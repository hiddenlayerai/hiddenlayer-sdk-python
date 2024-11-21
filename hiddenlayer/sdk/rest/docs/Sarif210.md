# Sarif210

Static Analysis Results Format (SARIF) Version 2.1.0 JSON Schema: a standard format for the output of static analysis tools.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | The URI of the JSON schema corresponding to the version. | [optional] 
**version** | **object** | The SARIF format version of this log file. | 
**runs** | [**List[Run]**](Run.md) | The set of runs contained in this log file. | 
**inline_external_properties** | [**List[ExternalProperties]**](ExternalProperties.md) | References to external property files that share data between runs. | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.sarif210 import Sarif210

# TODO update the JSON string below
json = "{}"
# create an instance of Sarif210 from a JSON string
sarif210_instance = Sarif210.from_json(json)
# print the JSON string representation of the object
print(Sarif210.to_json())

# convert the object into a dict
sarif210_dict = sarif210_instance.to_dict()
# create an instance of Sarif210 from a dict
sarif210_from_dict = Sarif210.from_dict(sarif210_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


