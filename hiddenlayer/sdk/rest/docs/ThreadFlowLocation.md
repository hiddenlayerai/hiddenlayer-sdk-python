# ThreadFlowLocation

A location visited by an analysis tool while simulating or monitoring the execution of a program.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | The index within the run threadFlowLocations array. | [optional] [default to -1]
**location** | [**Location**](Location.md) |  | [optional] 
**stack** | [**Stack**](Stack.md) |  | [optional] 
**kinds** | **List[str]** | A set of distinct strings that categorize the thread flow location. Well-known kinds include &#39;acquire&#39;, &#39;release&#39;, &#39;enter&#39;, &#39;exit&#39;, &#39;call&#39;, &#39;return&#39;, &#39;branch&#39;, &#39;implicit&#39;, &#39;false&#39;, &#39;true&#39;, &#39;caution&#39;, &#39;danger&#39;, &#39;unknown&#39;, &#39;unreachable&#39;, &#39;taint&#39;, &#39;function&#39;, &#39;handler&#39;, &#39;lock&#39;, &#39;memory&#39;, &#39;resource&#39;, &#39;scope&#39; and &#39;value&#39;. | [optional] [default to []]
**taxa** | [**List[ReportingDescriptorReference]**](ReportingDescriptorReference.md) | An array of references to rule or taxonomy reporting descriptors that are applicable to the thread flow location. | [optional] [default to []]
**module** | **str** | The name of the module that contains the code that is executing. | [optional] 
**state** | [**Dict[str, MultiformatMessageString]**](MultiformatMessageString.md) | A dictionary, each of whose keys specifies a variable or expression, the associated value of which represents the variable or expression value. For an annotation of kind &#39;continuation&#39;, for example, this dictionary might hold the current assumed values of a set of global variables. | [optional] 
**nesting_level** | **int** | An integer representing a containment hierarchy within the thread flow. | [optional] 
**execution_order** | **int** | An integer representing the temporal order in which execution reached this location. | [optional] [default to -1]
**execution_time_utc** | **datetime** | The Coordinated Universal Time (UTC) date and time at which this location was executed. | [optional] 
**importance** | **str** | Specifies the importance of this location in understanding the code flow in which it occurs. The order from most to least important is \&quot;essential\&quot;, \&quot;important\&quot;, \&quot;unimportant\&quot;. Default: \&quot;important\&quot;. | [optional] [default to 'important']
**web_request** | [**WebRequest**](WebRequest.md) |  | [optional] 
**web_response** | [**WebResponse**](WebResponse.md) |  | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.thread_flow_location import ThreadFlowLocation

# TODO update the JSON string below
json = "{}"
# create an instance of ThreadFlowLocation from a JSON string
thread_flow_location_instance = ThreadFlowLocation.from_json(json)
# print the JSON string representation of the object
print(ThreadFlowLocation.to_json())

# convert the object into a dict
thread_flow_location_dict = thread_flow_location_instance.to_dict()
# create an instance of ThreadFlowLocation from a dict
thread_flow_location_from_dict = ThreadFlowLocation.from_dict(thread_flow_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


