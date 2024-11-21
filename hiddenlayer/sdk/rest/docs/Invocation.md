# Invocation

The runtime environment of the analysis tool run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command_line** | **str** | The command line used to invoke the tool. | [optional] 
**arguments** | **List[str]** | An array of strings, containing in order the command line arguments passed to the tool from the operating system. | [optional] 
**response_files** | [**List[ArtifactLocation]**](ArtifactLocation.md) | The locations of any response files specified on the tool&#39;s command line. | [optional] 
**start_time_utc** | **datetime** | The Coordinated Universal Time (UTC) date and time at which the invocation started. See \&quot;Date/time properties\&quot; in the SARIF spec for the required format. | [optional] 
**end_time_utc** | **datetime** | The Coordinated Universal Time (UTC) date and time at which the invocation ended. See \&quot;Date/time properties\&quot; in the SARIF spec for the required format. | [optional] 
**exit_code** | **int** | The process exit code. | [optional] 
**rule_configuration_overrides** | [**List[ConfigurationOverride]**](ConfigurationOverride.md) | An array of configurationOverride objects that describe rules related runtime overrides. | [optional] [default to []]
**notification_configuration_overrides** | [**List[ConfigurationOverride]**](ConfigurationOverride.md) | An array of configurationOverride objects that describe notifications related runtime overrides. | [optional] [default to []]
**tool_execution_notifications** | [**List[Notification]**](Notification.md) | A list of runtime conditions detected by the tool during the analysis. | [optional] [default to []]
**tool_configuration_notifications** | [**List[Notification]**](Notification.md) | A list of conditions detected by the tool that are relevant to the tool&#39;s configuration. | [optional] [default to []]
**exit_code_description** | **str** | The reason for the process exit. | [optional] 
**exit_signal_name** | **str** | The name of the signal that caused the process to exit. | [optional] 
**exit_signal_number** | **int** | The numeric value of the signal that caused the process to exit. | [optional] 
**process_start_failure_message** | **str** | The reason given by the operating system that the process failed to start. | [optional] 
**execution_successful** | **bool** | Specifies whether the tool&#39;s execution completed successfully. | 
**machine** | **str** | The machine on which the invocation occurred. | [optional] 
**account** | **str** | The account under which the invocation occurred. | [optional] 
**process_id** | **int** | The id of the process in which the invocation occurred. | [optional] 
**executable_location** | [**ArtifactLocation**](ArtifactLocation.md) |  | [optional] 
**working_directory** | [**ArtifactLocation**](ArtifactLocation.md) |  | [optional] 
**environment_variables** | **Dict[str, str]** | The environment variables associated with the analysis tool process, expressed as key/value pairs. | [optional] 
**stdin** | [**ArtifactLocation**](ArtifactLocation.md) |  | [optional] 
**stdout** | [**ArtifactLocation**](ArtifactLocation.md) |  | [optional] 
**stderr** | [**ArtifactLocation**](ArtifactLocation.md) |  | [optional] 
**stdout_stderr** | [**ArtifactLocation**](ArtifactLocation.md) |  | [optional] 
**properties** | [**PropertyBag**](PropertyBag.md) |  | [optional] 

## Example

```python
from hiddenlayer.sdk.rest.models.invocation import Invocation

# TODO update the JSON string below
json = "{}"
# create an instance of Invocation from a JSON string
invocation_instance = Invocation.from_json(json)
# print the JSON string representation of the object
print(Invocation.to_json())

# convert the object into a dict
invocation_dict = invocation_instance.to_dict()
# create an instance of Invocation from a dict
invocation_from_dict = Invocation.from_dict(invocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


