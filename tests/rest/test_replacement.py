# coding: utf-8

"""
    HiddenLayer Sensor SOR

    HiddenLayer Sensor SOR API for operations to sensor data storage

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.replacement import Replacement

class TestReplacement(unittest.TestCase):
    """Replacement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Replacement:
        """Test Replacement
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Replacement`
        """
        model = Replacement()
        if include_optional:
            return Replacement(
                deleted_region = hiddenlayer.sdk.rest.models.region.region(
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
                            markdown = '', 
                            properties = { }, ), 
                        properties = { }, ), 
                    message = hiddenlayer.sdk.rest.models.message.message(
                        text = '', 
                        markdown = '', 
                        id = '', 
                        arguments = [
                            ''
                            ], ), 
                    source_language = '', 
                    properties = , ),
                inserted_content = hiddenlayer.sdk.rest.models.artifact_content.artifactContent(
                    text = '', 
                    binary = '', 
                    rendered = hiddenlayer.sdk.rest.models.multiformat_message_string.multiformatMessageString(
                        text = '', 
                        markdown = '', 
                        properties = { }, ), 
                    properties = { }, ),
                properties = { }
            )
        else:
            return Replacement(
                deleted_region = hiddenlayer.sdk.rest.models.region.region(
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
                            markdown = '', 
                            properties = { }, ), 
                        properties = { }, ), 
                    message = hiddenlayer.sdk.rest.models.message.message(
                        text = '', 
                        markdown = '', 
                        id = '', 
                        arguments = [
                            ''
                            ], ), 
                    source_language = '', 
                    properties = , ),
        )
        """

    def testReplacement(self):
        """Test Replacement"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
