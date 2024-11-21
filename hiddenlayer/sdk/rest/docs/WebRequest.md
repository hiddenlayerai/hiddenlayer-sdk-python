# WebRequest

Describes an HTTP request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | The index within the run.webRequests array of the request object associated with this result. | [optional] [default to -1]
**protocol** | **str** | The request protocol. Example: &#39;http&#39;. | [optional] 
**version** | **str** | The request version. Example: &#39;1.1&#39;. | [optional] 
**target** | **str** | The target of the request. | [optional] 
**method** | **str** | The HTTP method. Well-known values are &#39;GET&#39;, &#39;PUT&#39;, &#39;POST&#39;, &#39;DELETE&#39;, &#39;PATCH&#39;, &#39;HEAD&#39;, &#39;OPTIONS&#39;, &#39;TRACE&#39;, &#39;CONNECT&#39;. | [optional] 
**headers** | **Dict[str, str]** | The request headers. | [optional] 
**parameters** | **Dict[str, str]** | The request parameters. | [optional] 
**body** | [**ArtifactContent**](ArtifactContent.md) |  | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.web_request import WebRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebRequest from a JSON string
web_request_instance = WebRequest.from_json(json)
# print the JSON string representation of the object
print(WebRequest.to_json())

# convert the object into a dict
web_request_dict = web_request_instance.to_dict()
# create an instance of WebRequest from a dict
web_request_from_dict = WebRequest.from_dict(web_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


