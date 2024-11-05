# ScanCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** |  | 

## Example

```python
from hiddenlayer.sdk.rest.models.scan_create_request import ScanCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScanCreateRequest from a JSON string
scan_create_request_instance = ScanCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ScanCreateRequest.to_json())

# convert the object into a dict
scan_create_request_dict = scan_create_request_instance.to_dict()
# create an instance of ScanCreateRequest from a dict
scan_create_request_from_dict = ScanCreateRequest.from_dict(scan_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


