# TranslationMetadata

Provides additional metadata related to translation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name associated with the translation metadata. | 
**full_name** | **str** | The full name associated with the translation metadata. | [optional] 
**short_description** | [**MultiformatMessageString**](MultiformatMessageString.md) |  | [optional] 
**full_description** | [**MultiformatMessageString**](MultiformatMessageString.md) |  | [optional] 
**download_uri** | **str** | The absolute URI from which the translation metadata can be downloaded. | [optional] 
**information_uri** | **str** | The absolute URI from which information related to the translation metadata can be downloaded. | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.translation_metadata import TranslationMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationMetadata from a JSON string
translation_metadata_instance = TranslationMetadata.from_json(json)
# print the JSON string representation of the object
print(TranslationMetadata.to_json())

# convert the object into a dict
translation_metadata_dict = translation_metadata_instance.to_dict()
# create an instance of TranslationMetadata from a dict
translation_metadata_from_dict = TranslationMetadata.from_dict(translation_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


