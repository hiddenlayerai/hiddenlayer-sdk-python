# RuleDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | status | [optional] 
**status_at** | **datetime** | date-time when the details entry was created | [optional] 
**description** | **str** | description of the deprecation | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.rule_details_inner import RuleDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RuleDetailsInner from a JSON string
rule_details_inner_instance = RuleDetailsInner.from_json(json)
# print the JSON string representation of the object
print(RuleDetailsInner.to_json())

# convert the object into a dict
rule_details_inner_dict = rule_details_inner_instance.to_dict()
# create an instance of RuleDetailsInner from a dict
rule_details_inner_from_dict = RuleDetailsInner.from_dict(rule_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


