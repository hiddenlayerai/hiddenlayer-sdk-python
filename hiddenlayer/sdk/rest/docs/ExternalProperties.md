# ExternalProperties

The top-level element of an external property file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | The URI of the JSON schema corresponding to the version of the external property file format. | [optional] 
**version** | **str** | The SARIF format version of this external properties object. | [optional] 
**guid** | **str** | A stable, unique identifier for this external properties object, in the form of a GUID. | [optional] 
**run_guid** | **str** | A stable, unique identifier for the run associated with this external properties object, in the form of a GUID. | [optional] 
**conversion** | [**Conversion**](Conversion.md) |  | [optional] 
**graphs** | [**List[Graph]**](Graph.md) | An array of graph objects that will be merged with a separate run. | [optional] [default to []]
**externalized_properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 
**artifacts** | [**List[Artifact]**](Artifact.md) | An array of artifact objects that will be merged with a separate run. | [optional] 
**invocations** | [**List[Invocation]**](Invocation.md) | Describes the invocation of the analysis tool that will be merged with a separate run. | [optional] [default to []]
**logical_locations** | [**List[LogicalLocation]**](LogicalLocation.md) | An array of logical locations such as namespaces, types or functions that will be merged with a separate run. | [optional] [default to []]
**thread_flow_locations** | [**List[ThreadFlowLocation]**](ThreadFlowLocation.md) | An array of threadFlowLocation objects that will be merged with a separate run. | [optional] [default to []]
**results** | [**List[Result]**](Result.md) | An array of result objects that will be merged with a separate run. | [optional] [default to []]
**taxonomies** | [**List[ToolComponent]**](ToolComponent.md) | Tool taxonomies that will be merged with a separate run. | [optional] [default to []]
**driver** | [**ToolComponent**](ToolComponent.md) |  | [optional] 
**extensions** | [**List[ToolComponent]**](ToolComponent.md) | Tool extensions that will be merged with a separate run. | [optional] [default to []]
**policies** | [**List[ToolComponent]**](ToolComponent.md) | Tool policies that will be merged with a separate run. | [optional] [default to []]
**translations** | [**List[ToolComponent]**](ToolComponent.md) | Tool translations that will be merged with a separate run. | [optional] [default to []]
**addresses** | [**List[Address]**](Address.md) | Addresses that will be merged with a separate run. | [optional] [default to []]
**web_requests** | [**List[WebRequest]**](WebRequest.md) | Requests that will be merged with a separate run. | [optional] [default to []]
**web_responses** | [**List[WebResponse]**](WebResponse.md) | Responses that will be merged with a separate run. | [optional] [default to []]
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.external_properties import ExternalProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalProperties from a JSON string
external_properties_instance = ExternalProperties.from_json(json)
# print the JSON string representation of the object
print(ExternalProperties.to_json())

# convert the object into a dict
external_properties_dict = external_properties_instance.to_dict()
# create an instance of ExternalProperties from a dict
external_properties_from_dict = ExternalProperties.from_dict(external_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


