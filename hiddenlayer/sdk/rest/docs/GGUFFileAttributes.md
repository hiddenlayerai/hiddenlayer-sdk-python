# GGUFFileAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subtype** | **List[str]** |  | 

## Example

```python
from hiddenlayer.sdk.rest.models.gguf_file_attributes import GGUFFileAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of GGUFFileAttributes from a JSON string
gguf_file_attributes_instance = GGUFFileAttributes.from_json(json)
# print the JSON string representation of the object
print(GGUFFileAttributes.to_json())

# convert the object into a dict
gguf_file_attributes_dict = gguf_file_attributes_instance.to_dict()
# create an instance of GGUFFileAttributes from a dict
gguf_file_attributes_from_dict = GGUFFileAttributes.from_dict(gguf_file_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


