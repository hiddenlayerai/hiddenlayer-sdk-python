# Artifact

A single artifact. In some cases, this artifact might be nested within another artifact.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**Message**](Message.md) |  | [optional] 
**location** | [**ArtifactLocation**](ArtifactLocation.md) |  | [optional] 
**parent_index** | **int** | Identifies the index of the immediate parent of the artifact, if this artifact is nested. | [optional] [default to -1]
**offset** | **int** | The offset in bytes of the artifact within its containing artifact. | [optional] 
**length** | **int** | The length of the artifact in bytes. | [optional] [default to -1]
**roles** | **List[str]** | The role or roles played by the artifact in the analysis. | [optional] [default to []]
**mime_type** | **str** | The MIME type (RFC 2045) of the artifact. | [optional] 
**contents** | [**ArtifactContent**](ArtifactContent.md) |  | [optional] 
**encoding** | **str** | Specifies the encoding for an artifact object that refers to a text file. | [optional] 
**source_language** | **str** | Specifies the source language for any artifact object that refers to a text file that contains source code. | [optional] 
**hashes** | **Dict[str, str]** | A dictionary, each of whose keys is the name of a hash function and each of whose values is the hashed value of the artifact produced by the specified hash function. | [optional] 
**last_modified_time_utc** | **datetime** | The Coordinated Universal Time (UTC) date and time at which the artifact was most recently modified. See \&quot;Date/time properties\&quot; in the SARIF spec for the required format. | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.artifact import Artifact

# TODO update the JSON string below
json = "{}"
# create an instance of Artifact from a JSON string
artifact_instance = Artifact.from_json(json)
# print the JSON string representation of the object
print(Artifact.to_json())

# convert the object into a dict
artifact_dict = artifact_instance.to_dict()
# create an instance of Artifact from a dict
artifact_from_dict = Artifact.from_dict(artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


