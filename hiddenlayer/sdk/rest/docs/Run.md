# Run

Describes a single run of an analysis tool, and contains the reported output of that run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool** | [**Tool**](Tool.md) |  | 
**invocations** | [**List[Invocation]**](Invocation.md) | Describes the invocation of the analysis tool. | [optional] [default to []]
**conversion** | [**Conversion**](Conversion.md) |  | [optional] 
**language** | **str** | The language of the messages emitted into the log file during this run (expressed as an ISO 639-1 two-letter lowercase culture code) and an optional region (expressed as an ISO 3166-1 two-letter uppercase subculture code associated with a country or region). The casing is recommended but not required (in order for this data to conform to RFC5646). | [optional] [default to 'en-US']
**version_control_provenance** | [**List[VersionControlDetails]**](VersionControlDetails.md) | Specifies the revision in version control of the artifacts that were scanned. | [optional] [default to []]
**original_uri_base_ids** | [**Dict[str, ArtifactLocation]**](ArtifactLocation.md) | The artifact location specified by each uriBaseId symbol on the machine where the tool originally ran. | [optional] 
**artifacts** | [**List[Artifact]**](Artifact.md) | An array of artifact objects relevant to the run. | [optional] 
**logical_locations** | [**List[LogicalLocation]**](LogicalLocation.md) | An array of logical locations such as namespaces, types or functions. | [optional] [default to []]
**graphs** | [**List[Graph]**](Graph.md) | An array of zero or more unique graph objects associated with the run. | [optional] [default to []]
**results** | [**List[Result]**](Result.md) | The set of results contained in an SARIF log. The results array can be omitted when a run is solely exporting rules metadata. It must be present (but may be empty) if a log file represents an actual scan. | [optional] 
**automation_details** | [**RunAutomationDetails**](RunAutomationDetails.md) |  | [optional] 
**run_aggregates** | [**List[RunAutomationDetails]**](RunAutomationDetails.md) | Automation details that describe the aggregate of runs to which this run belongs. | [optional] [default to []]
**baseline_guid** | **str** | The &#39;guid&#39; property of a previous SARIF &#39;run&#39; that comprises the baseline that was used to compute result &#39;baselineState&#39; properties for the run. | [optional] 
**redaction_tokens** | **List[str]** | An array of strings used to replace sensitive information in a redaction-aware property. | [optional] [default to []]
**default_encoding** | **str** | Specifies the default encoding for any artifact object that refers to a text file. | [optional] 
**default_source_language** | **str** | Specifies the default source language for any artifact object that refers to a text file that contains source code. | [optional] 
**newline_sequences** | **List[str]** | An ordered list of character sequences that were treated as line breaks when computing region information for the run. | [optional] [default to ["\r\n","\n"]]
**column_kind** | **str** | Specifies the unit in which the tool measures columns. | [optional] 
**external_property_file_references** | [**ExternalPropertyFileReferences**](ExternalPropertyFileReferences.md) |  | [optional] 
**thread_flow_locations** | [**List[ThreadFlowLocation]**](ThreadFlowLocation.md) | An array of threadFlowLocation objects cached at run level. | [optional] [default to []]
**taxonomies** | [**List[ToolComponent]**](ToolComponent.md) | An array of toolComponent objects relevant to a taxonomy in which results are categorized. | [optional] [default to []]
**addresses** | [**List[Address]**](Address.md) | Addresses associated with this run instance, if any. | [optional] [default to []]
**translations** | [**List[ToolComponent]**](ToolComponent.md) | The set of available translations of the localized data provided by the tool. | [optional] [default to []]
**policies** | [**List[ToolComponent]**](ToolComponent.md) | Contains configurations that may potentially override both reportingDescriptor.defaultConfiguration (the tool&#39;s default severities) and invocation.configurationOverrides (severities established at run-time from the command line). | [optional] [default to []]
**web_requests** | [**List[WebRequest]**](WebRequest.md) | An array of request objects cached at run level. | [optional] [default to []]
**web_responses** | [**List[WebResponse]**](WebResponse.md) | An array of response objects cached at run level. | [optional] [default to []]
**special_locations** | [**SpecialLocations**](SpecialLocations.md) |  | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.run import Run

# TODO update the JSON string below
json = "{}"
# create an instance of Run from a JSON string
run_instance = Run.from_json(json)
# print the JSON string representation of the object
print(Run.to_json())

# convert the object into a dict
run_dict = run_instance.to_dict()
# create an instance of Run from a dict
run_from_dict = Run.from_dict(run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


