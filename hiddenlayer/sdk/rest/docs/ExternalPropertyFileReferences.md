# ExternalPropertyFileReferences

References to external property files that should be inlined with the content of a root log file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversion** | [**ExternalPropertyFileReference**](ExternalPropertyFileReference.md) |  | [optional] 
**graphs** | [**List[ExternalPropertyFileReference]**](ExternalPropertyFileReference.md) | An array of external property files containing a run.graphs object to be merged with the root log file. | [optional] [default to []]
**externalized_properties** | [**ExternalPropertyFileReference**](ExternalPropertyFileReference.md) |  | [optional] 
**artifacts** | [**List[ExternalPropertyFileReference]**](ExternalPropertyFileReference.md) | An array of external property files containing run.artifacts arrays to be merged with the root log file. | [optional] [default to []]
**invocations** | [**List[ExternalPropertyFileReference]**](ExternalPropertyFileReference.md) | An array of external property files containing run.invocations arrays to be merged with the root log file. | [optional] [default to []]
**logical_locations** | [**List[ExternalPropertyFileReference]**](ExternalPropertyFileReference.md) | An array of external property files containing run.logicalLocations arrays to be merged with the root log file. | [optional] [default to []]
**thread_flow_locations** | [**List[ExternalPropertyFileReference]**](ExternalPropertyFileReference.md) | An array of external property files containing run.threadFlowLocations arrays to be merged with the root log file. | [optional] [default to []]
**results** | [**List[ExternalPropertyFileReference]**](ExternalPropertyFileReference.md) | An array of external property files containing run.results arrays to be merged with the root log file. | [optional] [default to []]
**taxonomies** | [**List[ExternalPropertyFileReference]**](ExternalPropertyFileReference.md) | An array of external property files containing run.taxonomies arrays to be merged with the root log file. | [optional] [default to []]
**addresses** | [**List[ExternalPropertyFileReference]**](ExternalPropertyFileReference.md) | An array of external property files containing run.addresses arrays to be merged with the root log file. | [optional] [default to []]
**driver** | [**ExternalPropertyFileReference**](ExternalPropertyFileReference.md) |  | [optional] 
**extensions** | [**List[ExternalPropertyFileReference]**](ExternalPropertyFileReference.md) | An array of external property files containing run.extensions arrays to be merged with the root log file. | [optional] [default to []]
**policies** | [**List[ExternalPropertyFileReference]**](ExternalPropertyFileReference.md) | An array of external property files containing run.policies arrays to be merged with the root log file. | [optional] [default to []]
**translations** | [**List[ExternalPropertyFileReference]**](ExternalPropertyFileReference.md) | An array of external property files containing run.translations arrays to be merged with the root log file. | [optional] [default to []]
**web_requests** | [**List[ExternalPropertyFileReference]**](ExternalPropertyFileReference.md) | An array of external property files containing run.requests arrays to be merged with the root log file. | [optional] [default to []]
**web_responses** | [**List[ExternalPropertyFileReference]**](ExternalPropertyFileReference.md) | An array of external property files containing run.responses arrays to be merged with the root log file. | [optional] [default to []]
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.external_property_file_references import ExternalPropertyFileReferences

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalPropertyFileReferences from a JSON string
external_property_file_references_instance = ExternalPropertyFileReferences.from_json(json)
# print the JSON string representation of the object
print(ExternalPropertyFileReferences.to_json())

# convert the object into a dict
external_property_file_references_dict = external_property_file_references_instance.to_dict()
# create an instance of ExternalPropertyFileReferences from a dict
external_property_file_references_from_dict = ExternalPropertyFileReferences.from_dict(external_property_file_references_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


