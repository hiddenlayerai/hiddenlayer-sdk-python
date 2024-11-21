# Graph

A network of nodes and directed edges that describes some aspect of the structure of the code (for example, a call graph).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**Message**](Message.md) |  | [optional] 
**nodes** | [**List[Node]**](Node.md) | An array of node objects representing the nodes of the graph. | [optional] [default to []]
**edges** | [**List[Edge]**](Edge.md) | An array of edge objects representing the edges of the graph. | [optional] [default to []]
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.graph import Graph

# TODO update the JSON string below
json = "{}"
# create an instance of Graph from a JSON string
graph_instance = Graph.from_json(json)
# print the JSON string representation of the object
print(Graph.to_json())

# convert the object into a dict
graph_dict = graph_instance.to_dict()
# create an instance of Graph from a dict
graph_from_dict = Graph.from_dict(graph_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


