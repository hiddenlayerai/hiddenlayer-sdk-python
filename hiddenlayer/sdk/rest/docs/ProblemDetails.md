# ProblemDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | https://www.rfc-editor.org/rfc/rfc9457.html#name-type | [optional] 
**title** | **str** | https://www.rfc-editor.org/rfc/rfc9457.html#name-title | [optional] 
**detail** | **str** | https://www.rfc-editor.org/rfc/rfc9457.html#name-detail | [optional] 
**instance** | **str** | https://www.rfc-editor.org/rfc/rfc9457.html#name-instance | [optional] 
**errors** | [**List[ErrorsInner]**](ErrorsInner.md) | Error details | 

## Example

```python
from hiddenlayer.sdk.rest.models.problem_details import ProblemDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ProblemDetails from a JSON string
problem_details_instance = ProblemDetails.from_json(json)
# print the JSON string representation of the object
print(ProblemDetails.to_json())

# convert the object into a dict
problem_details_dict = problem_details_instance.to_dict()
# create an instance of ProblemDetails from a dict
problem_details_from_dict = ProblemDetails.from_dict(problem_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


