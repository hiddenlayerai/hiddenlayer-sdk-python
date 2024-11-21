# Conversion

Describes how a converter transformed the output of a static analysis tool from the analysis tool's native output format into the SARIF format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool** | [**Tool**](Tool.md) |  | 
**invocation** | [**Invocation**](Invocation.md) |  | [optional] 
**analysis_tool_log_files** | [**List[ArtifactLocation]**](ArtifactLocation.md) | The locations of the analysis tool&#39;s per-run log files. | [optional] [default to []]
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.conversion import Conversion

# TODO update the JSON string below
json = "{}"
# create an instance of Conversion from a JSON string
conversion_instance = Conversion.from_json(json)
# print the JSON string representation of the object
print(Conversion.to_json())

# convert the object into a dict
conversion_dict = conversion_instance.to_dict()
# create an instance of Conversion from a dict
conversion_from_dict = Conversion.from_dict(conversion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


