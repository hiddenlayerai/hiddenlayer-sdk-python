# coding: utf-8

"""
    HiddenLayer-API

    HiddenLayer-API

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.begin_multipart_file_upload200_response import BeginMultipartFileUpload200Response

class TestBeginMultipartFileUpload200Response(unittest.TestCase):
    """BeginMultipartFileUpload200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BeginMultipartFileUpload200Response:
        """Test BeginMultipartFileUpload200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BeginMultipartFileUpload200Response`
        """
        model = BeginMultipartFileUpload200Response()
        if include_optional:
            return BeginMultipartFileUpload200Response(
                upload_id = '',
                parts = [
                    hiddenlayer.sdk.rest.models.begin_multipart_file_upload_200_response_parts_inner.begin_multipart_file_upload_200_response_parts_inner(
                        part_number = 0, 
                        start_offset = 56, 
                        end_offset = 56, 
                        upload_url = '', )
                    ]
            )
        else:
            return BeginMultipartFileUpload200Response(
                upload_id = '',
                parts = [
                    hiddenlayer.sdk.rest.models.begin_multipart_file_upload_200_response_parts_inner.begin_multipart_file_upload_200_response_parts_inner(
                        part_number = 0, 
                        start_offset = 56, 
                        end_offset = 56, 
                        upload_url = '', )
                    ],
        )
        """

    def testBeginMultipartFileUpload200Response(self):
        """Test BeginMultipartFileUpload200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
