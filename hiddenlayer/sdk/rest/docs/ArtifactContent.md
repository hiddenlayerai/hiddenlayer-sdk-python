# ArtifactContent

Represents the contents of an artifact.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | UTF-8-encoded content from a text artifact. | [optional] 
**binary** | **str** | MIME Base64-encoded content from a binary artifact, or from a text artifact in its original encoding. | [optional] 
**rendered** | [**MultiformatMessageString**](MultiformatMessageString.md) |  | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.artifact_content import ArtifactContent

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactContent from a JSON string
artifact_content_instance = ArtifactContent.from_json(json)
# print the JSON string representation of the object
print(ArtifactContent.to_json())

# convert the object into a dict
artifact_content_dict = artifact_content_instance.to_dict()
# create an instance of ArtifactContent from a dict
artifact_content_from_dict = ArtifactContent.from_dict(artifact_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


