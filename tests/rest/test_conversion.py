# coding: utf-8

"""
    HiddenLayer-API

    HiddenLayer-API

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.conversion import Conversion

class TestConversion(unittest.TestCase):
    """Conversion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Conversion:
        """Test Conversion
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Conversion`
        """
        model = Conversion()
        if include_optional:
            return Conversion(
                tool = hiddenlayer.sdk.rest.models.tool.tool(
                    driver = hiddenlayer.sdk.rest.models.tool_component.toolComponent(
                        guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', 
                        name = '', 
                        organization = '', 
                        product = '', 
                        product_suite = '', 
                        short_description = hiddenlayer.sdk.rest.models.multiformat_message_string.multiformatMessageString(
                            text = '', 
                            markdown = '', 
                            properties = { }, ), 
                        full_description = hiddenlayer.sdk.rest.models.multiformat_message_string.multiformatMessageString(
                            text = '', 
                            markdown = '', ), 
                        full_name = '', 
                        version = '', 
                        semantic_version = '', 
                        dotted_quad_file_version = '4.072888001528021798096225500850762068629.39333975650685139102691291732729478601482026.0912727550417577019298162864882916633228770521', 
                        release_date_utc = '', 
                        download_uri = '', 
                        information_uri = '', 
                        global_message_strings = {
                            'key' : 
                            }, 
                        notifications = [
                            hiddenlayer.sdk.rest.models.reporting_descriptor.reportingDescriptor(
                                id = '', 
                                deprecated_ids = [
                                    ''
                                    ], 
                                guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', 
                                deprecated_guids = [
                                    '62ECB020-8429-10cc-81FF-CCfeEe150AC3'
                                    ], 
                                name = '', 
                                deprecated_names = [
                                    ''
                                    ], 
                                message_strings = {
                                    'key' : 
                                    }, 
                                default_configuration = hiddenlayer.sdk.rest.models.reporting_configuration.reportingConfiguration(
                                    enabled = True, 
                                    level = 'warning', 
                                    rank = -1, 
                                    parameters = { }, ), 
                                help_uri = '', 
                                help = , 
                                relationships = [
                                    hiddenlayer.sdk.rest.models.reporting_descriptor_relationship.reportingDescriptorRelationship(
                                        target = hiddenlayer.sdk.rest.models.reporting_descriptor_reference.reportingDescriptorReference(
                                            id = '', 
                                            index = -1, 
                                            guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', ), 
                                        kinds = [
                                            ''
                                            ], 
                                        description = hiddenlayer.sdk.rest.models.message.message(
                                            text = '', 
                                            markdown = '', 
                                            id = '', 
                                            arguments = [
                                                ''
                                                ], ), )
                                    ], )
                            ], 
                        rules = [
                            hiddenlayer.sdk.rest.models.reporting_descriptor.reportingDescriptor(
                                id = '', 
                                guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', 
                                name = '', 
                                help_uri = '', )
                            ], 
                        taxa = [
                            
                            ], 
                        locations = [
                            hiddenlayer.sdk.rest.models.artifact_location.artifactLocation(
                                uri = '', 
                                uri_base_id = '', 
                                index = -1, )
                            ], 
                        language = 'en-US', 
                        contents = [
                            'localizedData'
                            ], 
                        is_comprehensive = True, 
                        localized_data_semantic_version = '', 
                        minimum_required_localized_data_semantic_version = '', 
                        associated_component = hiddenlayer.sdk.rest.models.tool_component_reference.toolComponentReference(
                            name = '', 
                            index = -1, 
                            guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', ), 
                        translation_metadata = hiddenlayer.sdk.rest.models.translation_metadata.translationMetadata(
                            name = '', 
                            full_name = '', 
                            download_uri = '', 
                            information_uri = '', ), 
                        supported_taxonomies = [
                            hiddenlayer.sdk.rest.models.tool_component_reference.toolComponentReference(
                                name = '', 
                                index = -1, 
                                guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', )
                            ], 
                        properties = , ), 
                    extensions = [
                        hiddenlayer.sdk.rest.models.tool_component.toolComponent(
                            guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', 
                            name = '', 
                            organization = '', 
                            product = '', 
                            product_suite = '', 
                            full_name = '', 
                            version = '', 
                            semantic_version = '', 
                            dotted_quad_file_version = '4.072888001528021798096225500850762068629.39333975650685139102691291732729478601482026.0912727550417577019298162864882916633228770521', 
                            release_date_utc = '', 
                            download_uri = '', 
                            information_uri = '', 
                            language = 'en-US', 
                            is_comprehensive = True, 
                            localized_data_semantic_version = '', 
                            minimum_required_localized_data_semantic_version = '', )
                        ], 
                    properties = , ),
                invocation = hiddenlayer.sdk.rest.models.invocation.invocation(
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
                                parameters = , ), 
                            descriptor = hiddenlayer.sdk.rest.models.reporting_descriptor_reference.reportingDescriptorReference(
                                id = '', 
                                index = -1, 
                                guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', 
                                tool_component = hiddenlayer.sdk.rest.models.tool_component_reference.toolComponentReference(
                                    name = '', 
                                    index = -1, 
                                    guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', ), ), )
                        ], 
                    notification_configuration_overrides = [
                        hiddenlayer.sdk.rest.models.configuration_override.configurationOverride(
                            configuration = hiddenlayer.sdk.rest.models.reporting_configuration.reportingConfiguration(
                                enabled = True, 
                                level = 'warning', 
                                rank = -1, ), 
                            descriptor = hiddenlayer.sdk.rest.models.reporting_descriptor_reference.reportingDescriptorReference(
                                id = '', 
                                index = -1, 
                                guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', ), )
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
                                            parent_index = -1, ), 
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
                                            source_language = '', ), ), 
                                    logical_locations = [
                                        hiddenlayer.sdk.rest.models.logical_location.logicalLocation(
                                            name = '', 
                                            index = -1, 
                                            fully_qualified_name = '', 
                                            decorated_name = '', 
                                            parent_index = -1, 
                                            kind = '', )
                                        ], 
                                    annotations = [
                                        
                                        ], 
                                    relationships = [
                                        hiddenlayer.sdk.rest.models.location_relationship.locationRelationship(
                                            target = 0, 
                                            kinds = [
                                                ''
                                                ], )
                                        ], )
                                ], 
                            message = hiddenlayer.sdk.rest.models.message.message(
                                text = '', 
                                markdown = '', 
                                id = '', ), 
                            level = 'warning', 
                            thread_id = 56, 
                            time_utc = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            exception = hiddenlayer.sdk.rest.models.exception.exception(
                                kind = '', 
                                stack = hiddenlayer.sdk.rest.models.stack.stack(
                                    frames = [
                                        hiddenlayer.sdk.rest.models.stack_frame.stackFrame(
                                            module = '', 
                                            thread_id = 56, )
                                        ], ), 
                                inner_exceptions = [
                                    hiddenlayer.sdk.rest.models.exception.exception(
                                        kind = '', )
                                    ], ), 
                            associated_rule = , )
                        ], 
                    tool_configuration_notifications = [
                        hiddenlayer.sdk.rest.models.notification.notification(
                            message = , 
                            level = 'warning', 
                            thread_id = 56, 
                            time_utc = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
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
                        index = -1, ), 
                    working_directory = , 
                    environment_variables = {
                        'key' : ''
                        }, 
                    stdin = , 
                    stdout = , 
                    stderr = , 
                    stdout_stderr = , 
                    properties = , ),
                analysis_tool_log_files = [
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
                properties = { }
            )
        else:
            return Conversion(
                tool = hiddenlayer.sdk.rest.models.tool.tool(
                    driver = hiddenlayer.sdk.rest.models.tool_component.toolComponent(
                        guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', 
                        name = '', 
                        organization = '', 
                        product = '', 
                        product_suite = '', 
                        short_description = hiddenlayer.sdk.rest.models.multiformat_message_string.multiformatMessageString(
                            text = '', 
                            markdown = '', 
                            properties = { }, ), 
                        full_description = hiddenlayer.sdk.rest.models.multiformat_message_string.multiformatMessageString(
                            text = '', 
                            markdown = '', ), 
                        full_name = '', 
                        version = '', 
                        semantic_version = '', 
                        dotted_quad_file_version = '4.072888001528021798096225500850762068629.39333975650685139102691291732729478601482026.0912727550417577019298162864882916633228770521', 
                        release_date_utc = '', 
                        download_uri = '', 
                        information_uri = '', 
                        global_message_strings = {
                            'key' : 
                            }, 
                        notifications = [
                            hiddenlayer.sdk.rest.models.reporting_descriptor.reportingDescriptor(
                                id = '', 
                                deprecated_ids = [
                                    ''
                                    ], 
                                guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', 
                                deprecated_guids = [
                                    '62ECB020-8429-10cc-81FF-CCfeEe150AC3'
                                    ], 
                                name = '', 
                                deprecated_names = [
                                    ''
                                    ], 
                                message_strings = {
                                    'key' : 
                                    }, 
                                default_configuration = hiddenlayer.sdk.rest.models.reporting_configuration.reportingConfiguration(
                                    enabled = True, 
                                    level = 'warning', 
                                    rank = -1, 
                                    parameters = { }, ), 
                                help_uri = '', 
                                help = , 
                                relationships = [
                                    hiddenlayer.sdk.rest.models.reporting_descriptor_relationship.reportingDescriptorRelationship(
                                        target = hiddenlayer.sdk.rest.models.reporting_descriptor_reference.reportingDescriptorReference(
                                            id = '', 
                                            index = -1, 
                                            guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', ), 
                                        kinds = [
                                            ''
                                            ], 
                                        description = hiddenlayer.sdk.rest.models.message.message(
                                            text = '', 
                                            markdown = '', 
                                            id = '', 
                                            arguments = [
                                                ''
                                                ], ), )
                                    ], )
                            ], 
                        rules = [
                            hiddenlayer.sdk.rest.models.reporting_descriptor.reportingDescriptor(
                                id = '', 
                                guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', 
                                name = '', 
                                help_uri = '', )
                            ], 
                        taxa = [
                            
                            ], 
                        locations = [
                            hiddenlayer.sdk.rest.models.artifact_location.artifactLocation(
                                uri = '', 
                                uri_base_id = '', 
                                index = -1, )
                            ], 
                        language = 'en-US', 
                        contents = [
                            'localizedData'
                            ], 
                        is_comprehensive = True, 
                        localized_data_semantic_version = '', 
                        minimum_required_localized_data_semantic_version = '', 
                        associated_component = hiddenlayer.sdk.rest.models.tool_component_reference.toolComponentReference(
                            name = '', 
                            index = -1, 
                            guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', ), 
                        translation_metadata = hiddenlayer.sdk.rest.models.translation_metadata.translationMetadata(
                            name = '', 
                            full_name = '', 
                            download_uri = '', 
                            information_uri = '', ), 
                        supported_taxonomies = [
                            hiddenlayer.sdk.rest.models.tool_component_reference.toolComponentReference(
                                name = '', 
                                index = -1, 
                                guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', )
                            ], 
                        properties = , ), 
                    extensions = [
                        hiddenlayer.sdk.rest.models.tool_component.toolComponent(
                            guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', 
                            name = '', 
                            organization = '', 
                            product = '', 
                            product_suite = '', 
                            full_name = '', 
                            version = '', 
                            semantic_version = '', 
                            dotted_quad_file_version = '4.072888001528021798096225500850762068629.39333975650685139102691291732729478601482026.0912727550417577019298162864882916633228770521', 
                            release_date_utc = '', 
                            download_uri = '', 
                            information_uri = '', 
                            language = 'en-US', 
                            is_comprehensive = True, 
                            localized_data_semantic_version = '', 
                            minimum_required_localized_data_semantic_version = '', )
                        ], 
                    properties = , ),
        )
        """

    def testConversion(self):
        """Test Conversion"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
