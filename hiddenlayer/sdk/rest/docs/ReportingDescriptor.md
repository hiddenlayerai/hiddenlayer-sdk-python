# ReportingDescriptor

Metadata that describes a specific report produced by the tool, as part of the analysis it provides or its runtime reporting.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A stable, opaque identifier for the report. | 
**deprecated_ids** | **List[str]** | An array of stable, opaque identifiers by which this report was known in some previous version of the analysis tool. | [optional] 
**guid** | **str** | A unique identifier for the reporting descriptor in the form of a GUID. | [optional] 
**deprecated_guids** | **List[str]** | An array of unique identifies in the form of a GUID by which this report was known in some previous version of the analysis tool. | [optional] 
**name** | **str** | A report identifier that is understandable to an end user. | [optional] 
**deprecated_names** | **List[str]** | An array of readable identifiers by which this report was known in some previous version of the analysis tool. | [optional] 
**short_description** | [**MultiformatMessageString**](MultiformatMessageString.md) |  | [optional] 
**full_description** | [**MultiformatMessageString**](MultiformatMessageString.md) |  | [optional] 
**message_strings** | [**Dict[str, MultiformatMessageString]**](MultiformatMessageString.md) | A set of name/value pairs with arbitrary names. Each value is a multiformatMessageString object, which holds message strings in plain text and (optionally) Markdown format. The strings can include placeholders, which can be used to construct a message in combination with an arbitrary number of additional string arguments. | [optional] 
**default_configuration** | [**ReportingConfiguration**](ReportingConfiguration.md) |  | [optional] 
**help_uri** | **str** | A URI where the primary documentation for the report can be found. | [optional] 
**help** | [**MultiformatMessageString**](MultiformatMessageString.md) |  | [optional] 
**relationships** | [**List[ReportingDescriptorRelationship]**](ReportingDescriptorRelationship.md) | An array of objects that describe relationships between this reporting descriptor and others. | [optional] [default to []]
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.reporting_descriptor import ReportingDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of ReportingDescriptor from a JSON string
reporting_descriptor_instance = ReportingDescriptor.from_json(json)
# print the JSON string representation of the object
print(ReportingDescriptor.to_json())

# convert the object into a dict
reporting_descriptor_dict = reporting_descriptor_instance.to_dict()
# create an instance of ReportingDescriptor from a dict
reporting_descriptor_from_dict = ReportingDescriptor.from_dict(reporting_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


