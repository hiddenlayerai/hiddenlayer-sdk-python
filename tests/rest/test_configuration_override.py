# coding: utf-8

"""
    HiddenLayer-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.configuration_override import ConfigurationOverride

class TestConfigurationOverride(unittest.TestCase):
    """ConfigurationOverride unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigurationOverride:
        """Test ConfigurationOverride
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigurationOverride`
        """
        model = ConfigurationOverride()
        if include_optional:
            return ConfigurationOverride(
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
                        guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', 
                        properties = { }, ), 
                    properties = { }, ),
                properties = { }
            )
        else:
            return ConfigurationOverride(
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
                        guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3', 
                        properties = { }, ), 
                    properties = { }, ),
        )
        """

    def testConfigurationOverride(self):
        """Test ConfigurationOverride"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
