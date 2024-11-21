# GraphTraversal

Represents a path through a graph.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_graph_index** | **int** | The index within the run.graphs to be associated with the result. | [optional] [default to -1]
**result_graph_index** | **int** | The index within the result.graphs to be associated with the result. | [optional] [default to -1]
**description** | [**Message**](Message.md) |  | [optional] 
**initial_state** | [**Dict[str, MultiformatMessageString]**](MultiformatMessageString.md) | Values of relevant expressions at the start of the graph traversal that may change during graph traversal. | [optional] 
**immutable_state** | [**Dict[str, MultiformatMessageString]**](MultiformatMessageString.md) | Values of relevant expressions at the start of the graph traversal that remain constant for the graph traversal. | [optional] 
**edge_traversals** | [**List[EdgeTraversal]**](EdgeTraversal.md) | The sequences of edges traversed by this graph traversal. | [optional] [default to []]
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.graph_traversal import GraphTraversal

# TODO update the JSON string below
json = "{}"
# create an instance of GraphTraversal from a JSON string
graph_traversal_instance = GraphTraversal.from_json(json)
# print the JSON string representation of the object
print(GraphTraversal.to_json())

# convert the object into a dict
graph_traversal_dict = graph_traversal_instance.to_dict()
# create an instance of GraphTraversal from a dict
graph_traversal_from_dict = GraphTraversal.from_dict(graph_traversal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


