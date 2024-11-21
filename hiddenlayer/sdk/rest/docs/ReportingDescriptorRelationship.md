# ReportingDescriptorRelationship

Information about the relation of one reporting descriptor to another.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | [**ReportingDescriptorReference**](ReportingDescriptorReference.md) |  | 
**kinds** | **List[str]** | A set of distinct strings that categorize the relationship. Well-known kinds include &#39;canPrecede&#39;, &#39;canFollow&#39;, &#39;willPrecede&#39;, &#39;willFollow&#39;, &#39;superset&#39;, &#39;subset&#39;, &#39;equal&#39;, &#39;disjoint&#39;, &#39;relevant&#39;, and &#39;incomparable&#39;. | [optional] [default to ["relevant"]]
**description** | [**Message**](Message.md) |  | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.reporting_descriptor_relationship import ReportingDescriptorRelationship

# TODO update the JSON string below
json = "{}"
# create an instance of ReportingDescriptorRelationship from a JSON string
reporting_descriptor_relationship_instance = ReportingDescriptorRelationship.from_json(json)
# print the JSON string representation of the object
print(ReportingDescriptorRelationship.to_json())

# convert the object into a dict
reporting_descriptor_relationship_dict = reporting_descriptor_relationship_instance.to_dict()
# create an instance of ReportingDescriptorRelationship from a dict
reporting_descriptor_relationship_from_dict = ReportingDescriptorRelationship.from_dict(reporting_descriptor_relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


