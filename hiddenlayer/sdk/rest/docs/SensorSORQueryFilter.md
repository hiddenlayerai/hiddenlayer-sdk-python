# SensorSORQueryFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plaintext_name** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**version** | **int** |  | [optional] 
**created_at_start** | **datetime** |  | [optional] 
**created_at_stop** | **datetime** |  | [optional] 
**source** | **str** |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.sensor_sor_query_filter import SensorSORQueryFilter

# TODO update the JSON string below
json = "{}"
# create an instance of SensorSORQueryFilter from a JSON string
sensor_sor_query_filter_instance = SensorSORQueryFilter.from_json(json)
# print the JSON string representation of the object
print(SensorSORQueryFilter.to_json())

# convert the object into a dict
sensor_sor_query_filter_dict = sensor_sor_query_filter_instance.to_dict()
# create an instance of SensorSORQueryFilter from a dict
sensor_sor_query_filter_from_dict = SensorSORQueryFilter.from_dict(sensor_sor_query_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


