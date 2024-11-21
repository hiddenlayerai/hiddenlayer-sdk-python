# WebResponse

Describes the response to an HTTP request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | The index within the run.webResponses array of the response object associated with this result. | [optional] [default to -1]
**protocol** | **str** | The response protocol. Example: &#39;http&#39;. | [optional] 
**version** | **str** | The response version. Example: &#39;1.1&#39;. | [optional] 
**status_code** | **int** | The response status code. Example: 451. | [optional] 
**reason_phrase** | **str** | The response reason. Example: &#39;Not found&#39;. | [optional] 
**headers** | **Dict[str, str]** | The response headers. | [optional] 
**body** | [**ArtifactContent**](ArtifactContent.md) |  | [optional] 
**no_response_received** | **bool** | Specifies whether a response was received from the server. | [optional] [default to False]
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.web_response import WebResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebResponse from a JSON string
web_response_instance = WebResponse.from_json(json)
# print the JSON string representation of the object
print(WebResponse.to_json())

# convert the object into a dict
web_response_dict = web_response_instance.to_dict()
# create an instance of WebResponse from a dict
web_response_from_dict = WebResponse.from_dict(web_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


