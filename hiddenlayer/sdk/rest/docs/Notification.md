# Notification

Describes a condition relevant to the tool itself, as opposed to being relevant to a target being analyzed by the tool.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locations** | [**List[Location]**](Location.md) | The locations relevant to this notification. | [optional] [default to []]
**message** | [**Message**](Message.md) |  | 
**level** | **str** | A value specifying the severity level of the notification. | [optional] [default to 'warning']
**thread_id** | **int** | The thread identifier of the code that generated the notification. | [optional] 
**time_utc** | **datetime** | The Coordinated Universal Time (UTC) date and time at which the analysis tool generated the notification. | [optional] 
**exception** | [**Exception**](Exception.md) |  | [optional] 
**descriptor** | [**ReportingDescriptorReference**](ReportingDescriptorReference.md) |  | [optional] 
**associated_rule** | [**ReportingDescriptorReference**](ReportingDescriptorReference.md) |  | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.notification import Notification

# TODO update the JSON string below
json = "{}"
# create an instance of Notification from a JSON string
notification_instance = Notification.from_json(json)
# print the JSON string representation of the object
print(Notification.to_json())

# convert the object into a dict
notification_dict = notification_instance.to_dict()
# create an instance of Notification from a dict
notification_from_dict = Notification.from_dict(notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


