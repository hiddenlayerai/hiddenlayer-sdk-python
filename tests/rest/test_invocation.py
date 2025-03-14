# coding: utf-8

"""
    HiddenLayer-API

    HiddenLayer-API

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.invocation import Invocation

class TestInvocation(unittest.TestCase):
    """Invocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Invocation:
        """Test Invocation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Invocation`
        """
        model = Invocation()
        if include_optional:
            return Invocation(
                command_line = '',
                arguments = [
                    ''
                    ],
                response_files = [
                    hiddenlayer.sdk.rest.models.artifact_location.artifactLocation(
                        uri = '', 
                        uri_base_id = '', 
                        index = -1, 
                        description = hiddenlayer.sdk.rest.models.message.message(
                            text = '', 
                            markdown = '', 
                            id = '', 
                            arguments = [
                                ''
                                ], 
                            properties = { }, ), 
                        properties = { }, )
                    ],
                start_time_utc = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                end_time_utc = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                exit_code = 56,
                rule_configuration_overrides = [
                    hiddenlayer.sdk.rest.models.configuration_override.configurationOverride(
                        configuration = hiddenlayer.sdk.rest.models.reporting_configuration.reportingConfiguration(
                            enabled = True, 
                            level = 'warning', 
                            rank = -1, 
                            parameters = { }, 
                            properties = { }, ), 
                        descriptor = hiddenlayer.sdk.rest.models.reporting_descriptor_reference.reportingDescriptorReference(
                            id = '', 
                            index = -1, 
                            guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', 
                            tool_component = hiddenlayer.sdk.rest.models.tool_component_reference.toolComponentReference(
                                name = '', 
                                index = -1, 
                                guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', ), ), 
                        properties = , )
                    ],
                notification_configuration_overrides = [
                    hiddenlayer.sdk.rest.models.configuration_override.configurationOverride(
                        configuration = hiddenlayer.sdk.rest.models.reporting_configuration.reportingConfiguration(
                            enabled = True, 
                            level = 'warning', 
                            rank = -1, 
                            parameters = { }, 
                            properties = { }, ), 
                        descriptor = hiddenlayer.sdk.rest.models.reporting_descriptor_reference.reportingDescriptorReference(
                            id = '', 
                            index = -1, 
                            guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', 
                            tool_component = hiddenlayer.sdk.rest.models.tool_component_reference.toolComponentReference(
                                name = '', 
                                index = -1, 
                                guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', ), ), 
                        properties = , )
                    ],
                tool_execution_notifications = [
                    hiddenlayer.sdk.rest.models.notification.notification(
                        locations = [
                            hiddenlayer.sdk.rest.models.location.location(
                                id = -1, 
                                physical_location = hiddenlayer.sdk.rest.models.physical_location.physicalLocation(
                                    address = hiddenlayer.sdk.rest.models.address.address(
                                        absolute_address = -1, 
                                        relative_address = 56, 
                                        length = 56, 
                                        kind = '', 
                                        name = '', 
                                        fully_qualified_name = '', 
                                        offset_from_parent = 56, 
                                        index = -1, 
                                        parent_index = -1, 
                                        properties = { }, ), 
                                    artifact_location = hiddenlayer.sdk.rest.models.artifact_location.artifactLocation(
                                        uri = '', 
                                        uri_base_id = '', 
                                        index = -1, 
                                        description = hiddenlayer.sdk.rest.models.message.message(
                                            text = '', 
                                            markdown = '', 
                                            id = '', 
                                            arguments = [
                                                ''
                                                ], ), ), 
                                    region = hiddenlayer.sdk.rest.models.region.region(
                                        start_line = 1, 
                                        start_column = 1, 
                                        end_line = 1, 
                                        end_column = 1, 
                                        char_offset = -1, 
                                        char_length = 0, 
                                        byte_offset = -1, 
                                        byte_length = 0, 
                                        snippet = hiddenlayer.sdk.rest.models.artifact_content.artifactContent(
                                            text = '', 
                                            binary = '', 
                                            rendered = hiddenlayer.sdk.rest.models.multiformat_message_string.multiformatMessageString(
                                                text = '', 
                                                markdown = '', ), ), 
                                        source_language = '', ), 
                                    context_region = hiddenlayer.sdk.rest.models.region.region(
                                        start_line = 1, 
                                        start_column = 1, 
                                        end_line = 1, 
                                        end_column = 1, 
                                        char_offset = -1, 
                                        char_length = 0, 
                                        byte_offset = -1, 
                                        byte_length = 0, 
                                        source_language = '', ), 
                                    properties = { }, ), 
                                logical_locations = [
                                    hiddenlayer.sdk.rest.models.logical_location.logicalLocation(
                                        name = '', 
                                        index = -1, 
                                        fully_qualified_name = '', 
                                        decorated_name = '', 
                                        parent_index = -1, 
                                        kind = '', )
                                    ], 
                                message = hiddenlayer.sdk.rest.models.message.message(
                                    text = '', 
                                    markdown = '', 
                                    id = '', ), 
                                annotations = [
                                    
                                    ], 
                                relationships = [
                                    hiddenlayer.sdk.rest.models.location_relationship.locationRelationship(
                                        target = 0, 
                                        kinds = [
                                            ''
                                            ], )
                                    ], 
                                properties = , )
                            ], 
                        message = , 
                        level = 'warning', 
                        thread_id = 56, 
                        time_utc = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        exception = hiddenlayer.sdk.rest.models.exception.exception(
                            kind = '', 
                            stack = hiddenlayer.sdk.rest.models.stack.stack(
                                frames = [
                                    hiddenlayer.sdk.rest.models.stack_frame.stackFrame(
                                        module = '', 
                                        thread_id = 56, 
                                        parameters = [
                                            ''
                                            ], )
                                    ], ), 
                            inner_exceptions = [
                                hiddenlayer.sdk.rest.models.exception.exception(
                                    kind = '', )
                                ], ), 
                        descriptor = hiddenlayer.sdk.rest.models.reporting_descriptor_reference.reportingDescriptorReference(
                            id = '', 
                            index = -1, 
                            guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', 
                            tool_component = hiddenlayer.sdk.rest.models.tool_component_reference.toolComponentReference(
                                name = '', 
                                index = -1, 
                                guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', ), ), 
                        associated_rule = hiddenlayer.sdk.rest.models.reporting_descriptor_reference.reportingDescriptorReference(
                            id = '', 
                            index = -1, 
                            guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', ), 
                        properties = , )
                    ],
                tool_configuration_notifications = [
                    hiddenlayer.sdk.rest.models.notification.notification(
                        locations = [
                            hiddenlayer.sdk.rest.models.location.location(
                                id = -1, 
                                physical_location = hiddenlayer.sdk.rest.models.physical_location.physicalLocation(
                                    address = hiddenlayer.sdk.rest.models.address.address(
                                        absolute_address = -1, 
                                        relative_address = 56, 
                                        length = 56, 
                                        kind = '', 
                                        name = '', 
                                        fully_qualified_name = '', 
                                        offset_from_parent = 56, 
                                        index = -1, 
                                        parent_index = -1, 
                                        properties = { }, ), 
                                    artifact_location = hiddenlayer.sdk.rest.models.artifact_location.artifactLocation(
                                        uri = '', 
                                        uri_base_id = '', 
                                        index = -1, 
                                        description = hiddenlayer.sdk.rest.models.message.message(
                                            text = '', 
                                            markdown = '', 
                                            id = '', 
                                            arguments = [
                                                ''
                                                ], ), ), 
                                    region = hiddenlayer.sdk.rest.models.region.region(
                                        start_line = 1, 
                                        start_column = 1, 
                                        end_line = 1, 
                                        end_column = 1, 
                                        char_offset = -1, 
                                        char_length = 0, 
                                        byte_offset = -1, 
                                        byte_length = 0, 
                                        snippet = hiddenlayer.sdk.rest.models.artifact_content.artifactContent(
                                            text = '', 
                                            binary = '', 
                                            rendered = hiddenlayer.sdk.rest.models.multiformat_message_string.multiformatMessageString(
                                                text = '', 
                                                markdown = '', ), ), 
                                        source_language = '', ), 
                                    context_region = hiddenlayer.sdk.rest.models.region.region(
                                        start_line = 1, 
                                        start_column = 1, 
                                        end_line = 1, 
                                        end_column = 1, 
                                        char_offset = -1, 
                                        char_length = 0, 
                                        byte_offset = -1, 
                                        byte_length = 0, 
                                        source_language = '', ), 
                                    properties = { }, ), 
                                logical_locations = [
                                    hiddenlayer.sdk.rest.models.logical_location.logicalLocation(
                                        name = '', 
                                        index = -1, 
                                        fully_qualified_name = '', 
                                        decorated_name = '', 
                                        parent_index = -1, 
                                        kind = '', )
                                    ], 
                                message = hiddenlayer.sdk.rest.models.message.message(
                                    text = '', 
                                    markdown = '', 
                                    id = '', ), 
                                annotations = [
                                    
                                    ], 
                                relationships = [
                                    hiddenlayer.sdk.rest.models.location_relationship.locationRelationship(
                                        target = 0, 
                                        kinds = [
                                            ''
                                            ], )
                                    ], 
                                properties = , )
                            ], 
                        message = , 
                        level = 'warning', 
                        thread_id = 56, 
                        time_utc = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        exception = hiddenlayer.sdk.rest.models.exception.exception(
                            kind = '', 
                            stack = hiddenlayer.sdk.rest.models.stack.stack(
                                frames = [
                                    hiddenlayer.sdk.rest.models.stack_frame.stackFrame(
                                        module = '', 
                                        thread_id = 56, 
                                        parameters = [
                                            ''
                                            ], )
                                    ], ), 
                            inner_exceptions = [
                                hiddenlayer.sdk.rest.models.exception.exception(
                                    kind = '', )
                                ], ), 
                        descriptor = hiddenlayer.sdk.rest.models.reporting_descriptor_reference.reportingDescriptorReference(
                            id = '', 
                            index = -1, 
                            guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', 
                            tool_component = hiddenlayer.sdk.rest.models.tool_component_reference.toolComponentReference(
                                name = '', 
                                index = -1, 
                                guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', ), ), 
                        associated_rule = hiddenlayer.sdk.rest.models.reporting_descriptor_reference.reportingDescriptorReference(
                            id = '', 
                            index = -1, 
                            guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', ), 
                        properties = , )
                    ],
                exit_code_description = '',
                exit_signal_name = '',
                exit_signal_number = 56,
                process_start_failure_message = '',
                execution_successful = True,
                machine = '',
                account = '',
                process_id = 56,
                executable_location = hiddenlayer.sdk.rest.models.artifact_location.artifactLocation(
                    uri = '', 
                    uri_base_id = '', 
                    index = -1, 
                    description = hiddenlayer.sdk.rest.models.message.message(
                        text = '', 
                        markdown = '', 
                        id = '', 
                        arguments = [
                            ''
                            ], 
                        properties = { }, ), 
                    properties = { }, ),
                working_directory = hiddenlayer.sdk.rest.models.artifact_location.artifactLocation(
                    uri = '', 
                    uri_base_id = '', 
                    index = -1, 
                    description = hiddenlayer.sdk.rest.models.message.message(
                        text = '', 
                        markdown = '', 
                        id = '', 
                        arguments = [
                            ''
                            ], 
                        properties = { }, ), 
                    properties = { }, ),
                environment_variables = {
                    'key' : ''
                    },
                stdin = hiddenlayer.sdk.rest.models.artifact_location.artifactLocation(
                    uri = '', 
                    uri_base_id = '', 
                    index = -1, 
                    description = hiddenlayer.sdk.rest.models.message.message(
                        text = '', 
                        markdown = '', 
                        id = '', 
                        arguments = [
                            ''
                            ], 
                        properties = { }, ), 
                    properties = { }, ),
                stdout = hiddenlayer.sdk.rest.models.artifact_location.artifactLocation(
                    uri = '', 
                    uri_base_id = '', 
                    index = -1, 
                    description = hiddenlayer.sdk.rest.models.message.message(
                        text = '', 
                        markdown = '', 
                        id = '', 
                        arguments = [
                            ''
                            ], 
                        properties = { }, ), 
                    properties = { }, ),
                stderr = hiddenlayer.sdk.rest.models.artifact_location.artifactLocation(
                    uri = '', 
                    uri_base_id = '', 
                    index = -1, 
                    description = hiddenlayer.sdk.rest.models.message.message(
                        text = '', 
                        markdown = '', 
                        id = '', 
                        arguments = [
                            ''
                            ], 
                        properties = { }, ), 
                    properties = { }, ),
                stdout_stderr = hiddenlayer.sdk.rest.models.artifact_location.artifactLocation(
                    uri = '', 
                    uri_base_id = '', 
                    index = -1, 
                    description = hiddenlayer.sdk.rest.models.message.message(
                        text = '', 
                        markdown = '', 
                        id = '', 
                        arguments = [
                            ''
                            ], 
                        properties = { }, ), 
                    properties = { }, ),
                properties = { }
            )
        else:
            return Invocation(
                execution_successful = True,
        )
        """

    def testInvocation(self):
        """Test Invocation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
