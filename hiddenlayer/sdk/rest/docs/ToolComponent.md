# ToolComponent

A component, such as a plug-in or the driver, of the analysis tool that was run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | A unique identifier for the tool component in the form of a GUID. | [optional] 
**name** | **str** | The name of the tool component. | 
**organization** | **str** | The organization or company that produced the tool component. | [optional] 
**product** | **str** | A product suite to which the tool component belongs. | [optional] 
**product_suite** | **str** | A localizable string containing the name of the suite of products to which the tool component belongs. | [optional] 
**short_description** | [**MultiformatMessageString**](MultiformatMessageString.md) |  | [optional] 
**full_description** | [**MultiformatMessageString**](MultiformatMessageString.md) |  | [optional] 
**full_name** | **str** | The name of the tool component along with its version and any other useful identifying information, such as its locale. | [optional] 
**version** | **str** | The tool component version, in whatever format the component natively provides. | [optional] 
**semantic_version** | **str** | The tool component version in the format specified by Semantic Versioning 2.0. | [optional] 
**dotted_quad_file_version** | **str** | The binary version of the tool component&#39;s primary executable file expressed as four non-negative integers separated by a period (for operating systems that express file versions in this way). | [optional] 
**release_date_utc** | **str** | A string specifying the UTC date (and optionally, the time) of the component&#39;s release. | [optional] 
**download_uri** | **str** | The absolute URI from which the tool component can be downloaded. | [optional] 
**information_uri** | **str** | The absolute URI at which information about this version of the tool component can be found. | [optional] 
**global_message_strings** | [**Dict[str, MultiformatMessageString]**](MultiformatMessageString.md) | A dictionary, each of whose keys is a resource identifier and each of whose values is a multiformatMessageString object, which holds message strings in plain text and (optionally) Markdown format. The strings can include placeholders, which can be used to construct a message in combination with an arbitrary number of additional string arguments. | [optional] 
**notifications** | [**List[ReportingDescriptor]**](ReportingDescriptor.md) | An array of reportingDescriptor objects relevant to the notifications related to the configuration and runtime execution of the tool component. | [optional] [default to []]
**rules** | [**List[ReportingDescriptor]**](ReportingDescriptor.md) | An array of reportingDescriptor objects relevant to the analysis performed by the tool component. | [optional] [default to []]
**taxa** | [**List[ReportingDescriptor]**](ReportingDescriptor.md) | An array of reportingDescriptor objects relevant to the definitions of both standalone and tool-defined taxonomies. | [optional] [default to []]
**locations** | [**List[ArtifactLocation]**](ArtifactLocation.md) | An array of the artifactLocation objects associated with the tool component. | [optional] [default to []]
**language** | **str** | The language of the messages emitted into the log file during this run (expressed as an ISO 639-1 two-letter lowercase language code) and an optional region (expressed as an ISO 3166-1 two-letter uppercase subculture code associated with a country or region). The casing is recommended but not required (in order for this data to conform to RFC5646). | [optional] [default to 'en-US']
**contents** | **List[str]** | The kinds of data contained in this object. | [optional] [default to ["localizedData","nonLocalizedData"]]
**is_comprehensive** | **bool** | Specifies whether this object contains a complete definition of the localizable and/or non-localizable data for this component, as opposed to including only data that is relevant to the results persisted to this log file. | [optional] [default to False]
**localized_data_semantic_version** | **str** | The semantic version of the localized strings defined in this component; maintained by components that provide translations. | [optional] 
**minimum_required_localized_data_semantic_version** | **str** | The minimum value of localizedDataSemanticVersion required in translations consumed by this component; used by components that consume translations. | [optional] 
**associated_component** | [**ToolComponentReference**](ToolComponentReference.md) |  | [optional] 
**translation_metadata** | [**TranslationMetadata**](TranslationMetadata.md) |  | [optional] 
**supported_taxonomies** | [**List[ToolComponentReference]**](ToolComponentReference.md) | An array of toolComponentReference objects to declare the taxonomies supported by the tool component. | [optional] [default to []]
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.tool_component import ToolComponent

# TODO update the JSON string below
json = "{}"
# create an instance of ToolComponent from a JSON string
tool_component_instance = ToolComponent.from_json(json)
# print the JSON string representation of the object
print(ToolComponent.to_json())

# convert the object into a dict
tool_component_dict = tool_component_instance.to_dict()
# create an instance of ToolComponent from a dict
tool_component_from_dict = ToolComponent.from_dict(tool_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


