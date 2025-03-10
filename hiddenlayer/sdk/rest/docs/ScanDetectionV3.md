# ScanDetectionV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | detection description | 
**risk** | **str** | detection risk | [optional] 
**severity** | **str** | detection severity | 
**detection_id** | **str** | unique identifier for the detection | 
**impact** | **str** | detection impact | [optional] 
**likelihood** | **str** | detection likelihood | [optional] 
**rule_details** | [**List[RuleDetailsInner]**](RuleDetailsInner.md) |  | [optional] 
**rule_id** | **str** | unique identifier for the rule that sourced the detection | 
**category** | **str** | Vulnerability category for the detection | 
**mitre_atlas** | [**List[MITREAtlasInner]**](MITREAtlasInner.md) |  | 
**owasp** | **List[str]** |  | 
**cve** | **List[str]** |  | [optional] 
**cwe** | **str** |  | [optional] 
**cwe_href** | **str** | CWE URL for the detection | [optional] 
**technical_blog_href** | **str** | Hiddenlayer Technical Blog URL for the detection | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.scan_detection_v3 import ScanDetectionV3

# TODO update the JSON string below
json = "{}"
# create an instance of ScanDetectionV3 from a JSON string
scan_detection_v3_instance = ScanDetectionV3.from_json(json)
# print the JSON string representation of the object
print(ScanDetectionV3.to_json())

# convert the object into a dict
scan_detection_v3_dict = scan_detection_v3_instance.to_dict()
# create an instance of ScanDetectionV3 from a dict
scan_detection_v3_from_dict = ScanDetectionV3.from_dict(scan_detection_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


