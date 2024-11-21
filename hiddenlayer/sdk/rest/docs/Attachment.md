# Attachment

An artifact relevant to a result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**Message**](Message.md) |  | [optional] 
**artifact_location** | [**ArtifactLocation**](ArtifactLocation.md) |  | 
**regions** | [**List[Region]**](Region.md) | An array of regions of interest within the attachment. | [optional] [default to []]
**rectangles** | [**List[Rectangle]**](Rectangle.md) | An array of rectangles specifying areas of interest within the image. | [optional] [default to []]
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.attachment import Attachment

# TODO update the JSON string below
json = "{}"
# create an instance of Attachment from a JSON string
attachment_instance = Attachment.from_json(json)
# print the JSON string representation of the object
print(Attachment.to_json())

# convert the object into a dict
attachment_dict = attachment_instance.to_dict()
# create an instance of Attachment from a dict
attachment_from_dict = Attachment.from_dict(attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


