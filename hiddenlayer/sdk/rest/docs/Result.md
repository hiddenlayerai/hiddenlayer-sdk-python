# Result

A result produced by an analysis tool.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | The stable, unique identifier of the rule, if any, to which this result is relevant. | [optional] 
**rule_index** | **int** | The index within the tool component rules array of the rule object associated with this result. | [optional] [default to -1]
**rule** | [**ReportingDescriptorReference**](ReportingDescriptorReference.md) |  | [optional] 
**kind** | **str** | A value that categorizes results by evaluation state. | [optional] [default to 'fail']
**level** | **str** | A value specifying the severity level of the result. | [optional] [default to 'warning']
**message** | [**Message**](Message.md) |  | 
**analysis_target** | [**ArtifactLocation**](ArtifactLocation.md) |  | [optional] 
**locations** | [**List[Location]**](Location.md) | The set of locations where the result was detected. Specify only one location unless the problem indicated by the result can only be corrected by making a change at every specified location. | [optional] [default to []]
**guid** | **str** | A stable, unique identifier for the result in the form of a GUID. | [optional] 
**correlation_guid** | **str** | A stable, unique identifier for the equivalence class of logically identical results to which this result belongs, in the form of a GUID. | [optional] 
**occurrence_count** | **int** | A positive integer specifying the number of times this logically unique result was observed in this run. | [optional] 
**partial_fingerprints** | **Dict[str, str]** | A set of strings that contribute to the stable, unique identity of the result. | [optional] 
**fingerprints** | **Dict[str, str]** | A set of strings each of which individually defines a stable, unique identity for the result. | [optional] 
**stacks** | [**List[Stack]**](Stack.md) | An array of &#39;stack&#39; objects relevant to the result. | [optional] [default to []]
**code_flows** | [**List[CodeFlow]**](CodeFlow.md) | An array of &#39;codeFlow&#39; objects relevant to the result. | [optional] [default to []]
**graphs** | [**List[Graph]**](Graph.md) | An array of zero or more unique graph objects associated with the result. | [optional] [default to []]
**graph_traversals** | [**List[GraphTraversal]**](GraphTraversal.md) | An array of one or more unique &#39;graphTraversal&#39; objects. | [optional] [default to []]
**related_locations** | [**List[Location]**](Location.md) | A set of locations relevant to this result. | [optional] [default to []]
**suppressions** | [**List[Suppression]**](Suppression.md) | A set of suppressions relevant to this result. | [optional] 
**baseline_state** | **str** | The state of a result relative to a baseline of a previous run. | [optional] 
**rank** | **float** | A number representing the priority or importance of the result. | [optional] [default to -1]
**attachments** | [**List[Attachment]**](Attachment.md) | A set of artifacts relevant to the result. | [optional] [default to []]
**hosted_viewer_uri** | **str** | An absolute URI at which the result can be viewed. | [optional] 
**work_item_uris** | **List[str]** | The URIs of the work items associated with this result. | [optional] 
**provenance** | [**ResultProvenance**](ResultProvenance.md) |  | [optional] 
**fixes** | [**List[Fix]**](Fix.md) | An array of &#39;fix&#39; objects, each of which represents a proposed fix to the problem indicated by the result. | [optional] [default to []]
**taxa** | [**List[ReportingDescriptorReference]**](ReportingDescriptorReference.md) | An array of references to taxonomy reporting descriptors that are applicable to the result. | [optional] [default to []]
**web_request** | [**WebRequest**](WebRequest.md) |  | [optional] 
**web_response** | [**WebResponse**](WebResponse.md) |  | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.result import Result

# TODO update the JSON string below
json = "{}"
# create an instance of Result from a JSON string
result_instance = Result.from_json(json)
# print the JSON string representation of the object
print(Result.to_json())

# convert the object into a dict
result_dict = result_instance.to_dict()
# create an instance of Result from a dict
result_from_dict = Result.from_dict(result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


