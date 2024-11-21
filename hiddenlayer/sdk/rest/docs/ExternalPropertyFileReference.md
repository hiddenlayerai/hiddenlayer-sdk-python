# ExternalPropertyFileReference

Contains information that enables a SARIF consumer to locate the external property file that contains the value of an externalized property associated with the run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | [**ArtifactLocation**](ArtifactLocation.md) |  | [optional] 
**guid** | **str** | A stable, unique identifier for the external property file in the form of a GUID. | [optional] 
**item_count** | **int** | A non-negative integer specifying the number of items contained in the external property file. | [optional] [default to -1]
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.external_property_file_reference import ExternalPropertyFileReference

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalPropertyFileReference from a JSON string
external_property_file_reference_instance = ExternalPropertyFileReference.from_json(json)
# print the JSON string representation of the object
print(ExternalPropertyFileReference.to_json())

# convert the object into a dict
external_property_file_reference_dict = external_property_file_reference_instance.to_dict()
# create an instance of ExternalPropertyFileReference from a dict
external_property_file_reference_from_dict = ExternalPropertyFileReference.from_dict(external_property_file_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


