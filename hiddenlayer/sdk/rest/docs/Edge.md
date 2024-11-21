# Edge

Represents a directed edge in a graph.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A string that uniquely identifies the edge within its graph. | 
**label** | [**Message**](Message.md) |  | [optional] 
**source_node_id** | **str** | Identifies the source node (the node at which the edge starts). | 
**target_node_id** | **str** | Identifies the target node (the node at which the edge ends). | 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.edge import Edge

# TODO update the JSON string below
json = "{}"
# create an instance of Edge from a JSON string
edge_instance = Edge.from_json(json)
# print the JSON string representation of the object
print(Edge.to_json())

# convert the object into a dict
edge_dict = edge_instance.to_dict()
# create an instance of Edge from a dict
edge_from_dict = Edge.from_dict(edge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


