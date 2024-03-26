# Model


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sensor_id** | **str** |  | 
**created_at** | **datetime** |  | 
**tenant_id** | **str** |  | 
**plaintext_name** | **str** |  | 
**active** | **bool** |  | 
**version** | **int** |  | 
**tags** | **Dict[str, object]** |  | [optional] 

## Example

```python
from hiddenlayer.rest.models.model import Model

# TODO update the JSON string below
json = "{}"
# create an instance of Model from a JSON string
model_instance = Model.from_json(json)
# print the JSON string representation of the object
print Model.to_json()

# convert the object into a dict
model_dict = model_instance.to_dict()
# create an instance of Model from a dict
model_form_dict = model.from_dict(model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


