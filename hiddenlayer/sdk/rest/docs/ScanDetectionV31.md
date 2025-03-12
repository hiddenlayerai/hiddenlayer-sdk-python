# ScanDetectionV31


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detection_id** | **str** | unique identifier for the detection | 
**rule_id** | **str** | unique identifier for the rule that sourced the detection | 
**risk** | **str** | detection risk | [optional] 
**category** | **str** | Vulnerability category for the detection | 
**description** | **str** | detection description | 
**likelihood** | **str** | detection likelihood | 
**impact** | **str** | detection impact | 
**severity** | **str** | detection severity | 
**rule_details** | [**List[RuleDetailsInner]**](RuleDetailsInner.md) |  | [optional] 
**mitre_atlas** | [**List[MITREAtlasInner]**](MITREAtlasInner.md) |  | 
**owasp** | **List[str]** |  | 
**cve** | **List[str]** |  | 
**cwe** | **str** |  | 
**cwe_href** | **str** | CWE URL for the detection | 
**technical_blog_hrefs** | **List[str]** | Hiddenlayer Technical Blog URLs for the detection | [optional] 
**technical_blog_href** | **str** | Hiddenlayer Technical Blog URL for the detection | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.scan_detection_v31 import ScanDetectionV31

# TODO update the JSON string below
json = "{}"
# create an instance of ScanDetectionV31 from a JSON string
scan_detection_v31_instance = ScanDetectionV31.from_json(json)
# print the JSON string representation of the object
print(ScanDetectionV31.to_json())

# convert the object into a dict
scan_detection_v31_dict = scan_detection_v31_instance.to_dict()
# create an instance of ScanDetectionV31 from a dict
scan_detection_v31_from_dict = ScanDetectionV31.from_dict(scan_detection_v31_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


