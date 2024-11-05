# FileTypeDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subtype** | **List[str]** |  | 
**keras_version** | **str** | version of the Keras file | [optional] 
**pickle_modules** | **List[str]** |  | 
**keras_class_name** | **str** |  | [optional] 
**keras_date_saved_at** | **str** |  | [optional] 
**keras_module** | **str** |  | [optional] 
**numpy_arrays** | **str** |  | 
**numpy_shape** | **List[str]** |  | 
**rds_encoding** | **str** | encoding of the RDS file | 
**rds_min_reader_version** | **str** | minimum reader version for the RDS file | 
**rds_version** | **str** | version of the RDS file | 
**rds_writer_version** | **str** | version of the RDS writer | 

## Example

```python
from hiddenlayer.sdk.rest.models.file_type_details import FileTypeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FileTypeDetails from a JSON string
file_type_details_instance = FileTypeDetails.from_json(json)
# print the JSON string representation of the object
print(FileTypeDetails.to_json())

# convert the object into a dict
file_type_details_dict = file_type_details_instance.to_dict()
# create an instance of FileTypeDetails from a dict
file_type_details_from_dict = FileTypeDetails.from_dict(file_type_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


