# Rectangle

An area within an image.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top** | **float** | The Y coordinate of the top edge of the rectangle, measured in the image&#39;s natural units. | [optional] 
**left** | **float** | The X coordinate of the left edge of the rectangle, measured in the image&#39;s natural units. | [optional] 
**bottom** | **float** | The Y coordinate of the bottom edge of the rectangle, measured in the image&#39;s natural units. | [optional] 
**right** | **float** | The X coordinate of the right edge of the rectangle, measured in the image&#39;s natural units. | [optional] 
**message** | [**Message**](Message.md) |  | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.rectangle import Rectangle

# TODO update the JSON string below
json = "{}"
# create an instance of Rectangle from a JSON string
rectangle_instance = Rectangle.from_json(json)
# print the JSON string representation of the object
print(Rectangle.to_json())

# convert the object into a dict
rectangle_dict = rectangle_instance.to_dict()
# create an instance of Rectangle from a dict
rectangle_from_dict = Rectangle.from_dict(rectangle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


