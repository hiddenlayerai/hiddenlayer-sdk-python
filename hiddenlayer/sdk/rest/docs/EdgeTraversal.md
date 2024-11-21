# EdgeTraversal

Represents the traversal of a single edge during a graph traversal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edge_id** | **str** | Identifies the edge being traversed. | 
**message** | [**Message**](Message.md) |  | [optional] 
**final_state** | [**Dict[str, MultiformatMessageString]**](MultiformatMessageString.md) | The values of relevant expressions after the edge has been traversed. | [optional] 
**step_over_edge_count** | **int** | The number of edge traversals necessary to return from a nested graph. | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.edge_traversal import EdgeTraversal

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeTraversal from a JSON string
edge_traversal_instance = EdgeTraversal.from_json(json)
# print the JSON string representation of the object
print(EdgeTraversal.to_json())

# convert the object into a dict
edge_traversal_dict = edge_traversal_instance.to_dict()
# create an instance of EdgeTraversal from a dict
edge_traversal_from_dict = EdgeTraversal.from_dict(edge_traversal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


