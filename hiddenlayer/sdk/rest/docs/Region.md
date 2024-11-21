# Region

A region within an artifact where a result was detected.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_line** | **int** | The line number of the first character in the region. | [optional] 
**start_column** | **int** | The column number of the first character in the region. | [optional] 
**end_line** | **int** | The line number of the last character in the region. | [optional] 
**end_column** | **int** | The column number of the character following the end of the region. | [optional] 
**char_offset** | **int** | The zero-based offset from the beginning of the artifact of the first character in the region. | [optional] [default to -1]
**char_length** | **int** | The length of the region in characters. | [optional] 
**byte_offset** | **int** | The zero-based offset from the beginning of the artifact of the first byte in the region. | [optional] [default to -1]
**byte_length** | **int** | The length of the region in bytes. | [optional] 
**snippet** | [**ArtifactContent**](ArtifactContent.md) |  | [optional] 
**message** | [**Message**](Message.md) |  | [optional] 
**source_language** | **str** | Specifies the source language, if any, of the portion of the artifact specified by the region object. | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.region import Region

# TODO update the JSON string below
json = "{}"
# create an instance of Region from a JSON string
region_instance = Region.from_json(json)
# print the JSON string representation of the object
print(Region.to_json())

# convert the object into a dict
region_dict = region_instance.to_dict()
# create an instance of Region from a dict
region_from_dict = Region.from_dict(region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


