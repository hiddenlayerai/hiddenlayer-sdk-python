# coding: utf-8

"""
    HiddenLayer-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.tool_component import ToolComponent

class TestToolComponent(unittest.TestCase):
    """ToolComponent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ToolComponent:
        """Test ToolComponent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ToolComponent`
        """
        model = ToolComponent()
        if include_optional:
            return ToolComponent(
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
                    markdown = '', 
                    properties = { }, ),
                full_name = '',
                version = '',
                semantic_version = '',
                dotted_quad_file_version = '4.072888001528021798096225500850762068629.39333975650685139102691291732729478601482026.0912727550417577019298162864882916633228770521',
                release_date_utc = '',
                download_uri = '',
                information_uri = '',
                global_message_strings = {
                    'key' : hiddenlayer.sdk.rest.models.multiformat_message_string.multiformatMessageString(
                        text = '', 
                        markdown = '', 
                        properties = { }, )
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
                        short_description = hiddenlayer.sdk.rest.models.multiformat_message_string.multiformatMessageString(
                            text = '', 
                            markdown = '', 
                            properties = { }, ), 
                        full_description = hiddenlayer.sdk.rest.models.multiformat_message_string.multiformatMessageString(
                            text = '', 
                            markdown = '', ), 
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
                                    guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', 
                                    tool_component = hiddenlayer.sdk.rest.models.tool_component_reference.toolComponentReference(
                                        name = '', 
                                        index = -1, 
                                        guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', ), ), 
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
                            ], 
                        properties = , )
                    ],
                rules = [
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
                        short_description = hiddenlayer.sdk.rest.models.multiformat_message_string.multiformatMessageString(
                            text = '', 
                            markdown = '', 
                            properties = { }, ), 
                        full_description = hiddenlayer.sdk.rest.models.multiformat_message_string.multiformatMessageString(
                            text = '', 
                            markdown = '', ), 
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
                                    guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', 
                                    tool_component = hiddenlayer.sdk.rest.models.tool_component_reference.toolComponentReference(
                                        name = '', 
                                        index = -1, 
                                        guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', ), ), 
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
                            ], 
                        properties = , )
                    ],
                taxa = [
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
                        short_description = hiddenlayer.sdk.rest.models.multiformat_message_string.multiformatMessageString(
                            text = '', 
                            markdown = '', 
                            properties = { }, ), 
                        full_description = hiddenlayer.sdk.rest.models.multiformat_message_string.multiformatMessageString(
                            text = '', 
                            markdown = '', ), 
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
                                    guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', 
                                    tool_component = hiddenlayer.sdk.rest.models.tool_component_reference.toolComponentReference(
                                        name = '', 
                                        index = -1, 
                                        guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', ), ), 
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
                            ], 
                        properties = , )
                    ],
                locations = [
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
                    guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', 
                    properties = { }, ),
                translation_metadata = hiddenlayer.sdk.rest.models.translation_metadata.translationMetadata(
                    name = '', 
                    full_name = '', 
                    short_description = hiddenlayer.sdk.rest.models.multiformat_message_string.multiformatMessageString(
                        text = '', 
                        markdown = '', 
                        properties = { }, ), 
                    full_description = hiddenlayer.sdk.rest.models.multiformat_message_string.multiformatMessageString(
                        text = '', 
                        markdown = '', ), 
                    download_uri = '', 
                    information_uri = '', 
                    properties = { }, ),
                supported_taxonomies = [
                    hiddenlayer.sdk.rest.models.tool_component_reference.toolComponentReference(
                        name = '', 
                        index = -1, 
                        guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', 
                        properties = { }, )
                    ],
                properties = { }
            )
        else:
            return ToolComponent(
                name = '',
        )
        """

    def testToolComponent(self):
        """Test ToolComponent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
