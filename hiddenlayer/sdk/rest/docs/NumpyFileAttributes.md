# NumpyFileAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subtype** | **List[str]** |  | 
**numpy_arrays** | **str** |  | 
**numpy_shape** | **List[str]** |  | 

## Example

```python
from hiddenlayer.sdk.rest.models.numpy_file_attributes import NumpyFileAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of NumpyFileAttributes from a JSON string
numpy_file_attributes_instance = NumpyFileAttributes.from_json(json)
# print the JSON string representation of the object
print(NumpyFileAttributes.to_json())

# convert the object into a dict
numpy_file_attributes_dict = numpy_file_attributes_instance.to_dict()
# create an instance of NumpyFileAttributes from a dict
numpy_file_attributes_from_dict = NumpyFileAttributes.from_dict(numpy_file_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


