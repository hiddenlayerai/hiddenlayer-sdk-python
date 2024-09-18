# ValidationErrorModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loc** | [**List[ValidationErrorModelLocInner]**](ValidationErrorModelLocInner.md) |  | 
**msg** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from hiddenlayer.sdk.rest.models.validation_error_model import ValidationErrorModel

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationErrorModel from a JSON string
validation_error_model_instance = ValidationErrorModel.from_json(json)
# print the JSON string representation of the object
print(ValidationErrorModel.to_json())

# convert the object into a dict
validation_error_model_dict = validation_error_model_instance.to_dict()
# create an instance of ValidationErrorModel from a dict
validation_error_model_from_dict = ValidationErrorModel.from_dict(validation_error_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


