# Address

A physical or virtual address, or a range of addresses, in an 'addressable region' (memory or a binary file).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absolute_address** | **int** | The address expressed as a byte offset from the start of the addressable region. | [optional] [default to -1]
**relative_address** | **int** | The address expressed as a byte offset from the absolute address of the top-most parent object. | [optional] 
**length** | **int** | The number of bytes in this range of addresses. | [optional] 
**kind** | **str** | An open-ended string that identifies the address kind. &#39;data&#39;, &#39;function&#39;, &#39;header&#39;,&#39;instruction&#39;, &#39;module&#39;, &#39;page&#39;, &#39;section&#39;, &#39;segment&#39;, &#39;stack&#39;, &#39;stackFrame&#39;, &#39;table&#39; are well-known values. | [optional] 
**name** | **str** | A name that is associated with the address, e.g., &#39;.text&#39;. | [optional] 
**fully_qualified_name** | **str** | A human-readable fully qualified name that is associated with the address. | [optional] 
**offset_from_parent** | **int** | The byte offset of this address from the absolute or relative address of the parent object. | [optional] 
**index** | **int** | The index within run.addresses of the cached object for this address. | [optional] [default to -1]
**parent_index** | **int** | The index within run.addresses of the parent object. | [optional] [default to -1]
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print(Address.to_json())

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_from_dict = Address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


