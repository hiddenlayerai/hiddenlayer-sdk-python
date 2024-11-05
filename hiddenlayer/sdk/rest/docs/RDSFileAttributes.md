# RDSFileAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subtype** | **List[str]** |  | 
**rds_encoding** | **str** | encoding of the RDS file | 
**rds_min_reader_version** | **str** | minimum reader version for the RDS file | 
**rds_version** | **str** | version of the RDS file | 
**rds_writer_version** | **str** | version of the RDS writer | 

## Example

```python
from hiddenlayer.sdk.rest.models.rds_file_attributes import RDSFileAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of RDSFileAttributes from a JSON string
rds_file_attributes_instance = RDSFileAttributes.from_json(json)
# print the JSON string representation of the object
print(RDSFileAttributes.to_json())

# convert the object into a dict
rds_file_attributes_dict = rds_file_attributes_instance.to_dict()
# create an instance of RDSFileAttributes from a dict
rds_file_attributes_from_dict = RDSFileAttributes.from_dict(rds_file_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


