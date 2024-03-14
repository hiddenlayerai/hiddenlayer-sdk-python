# ScanModelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** |  | 

## Example

```python
from hiddenlayer.rest.models.scan_model_request import ScanModelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScanModelRequest from a JSON string
scan_model_request_instance = ScanModelRequest.from_json(json)
# print the JSON string representation of the object
print ScanModelRequest.to_json()

# convert the object into a dict
scan_model_request_dict = scan_model_request_instance.to_dict()
# create an instance of ScanModelRequest from a dict
scan_model_request_form_dict = scan_model_request.from_dict(scan_model_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


