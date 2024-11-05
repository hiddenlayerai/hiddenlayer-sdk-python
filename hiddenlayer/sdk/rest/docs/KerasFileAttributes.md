# KerasFileAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subtype** | **List[str]** |  | 
**keras_version** | **str** | version of the Keras file | [optional] 
**pickle_modules** | **List[str]** |  | 
**keras_class_name** | **str** |  | [optional] 
**keras_date_saved_at** | **str** |  | [optional] 
**keras_module** | **str** |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.keras_file_attributes import KerasFileAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of KerasFileAttributes from a JSON string
keras_file_attributes_instance = KerasFileAttributes.from_json(json)
# print the JSON string representation of the object
print(KerasFileAttributes.to_json())

# convert the object into a dict
keras_file_attributes_dict = keras_file_attributes_instance.to_dict()
# create an instance of KerasFileAttributes from a dict
keras_file_attributes_from_dict = KerasFileAttributes.from_dict(keras_file_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


