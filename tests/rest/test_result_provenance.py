# coding: utf-8

"""
    HiddenLayer-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.result_provenance import ResultProvenance

class TestResultProvenance(unittest.TestCase):
    """ResultProvenance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResultProvenance:
        """Test ResultProvenance
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResultProvenance`
        """
        model = ResultProvenance()
        if include_optional:
            return ResultProvenance(
                first_detection_time_utc = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_detection_time_utc = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                first_detection_run_guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3',
                last_detection_run_guid = '62ECB020-8429-10cc-81FF-CCfeEe150AC3',
                invocation_index = -1,
                conversion_sources = [
                    hiddenlayer.sdk.rest.models.physical_location.physicalLocation(
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
                        properties = { }, )
                    ],
                properties = { }
            )
        else:
            return ResultProvenance(
        )
        """

    def testResultProvenance(self):
        """Test ResultProvenance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
