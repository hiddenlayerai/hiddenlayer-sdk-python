# coding: utf-8

"""
    HiddenLayer Sensor SOR

    HiddenLayer Sensor SOR API for operations to sensor data storage

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.begin_multipart_file_upload200_response_parts_inner import BeginMultipartFileUpload200ResponsePartsInner

class TestBeginMultipartFileUpload200ResponsePartsInner(unittest.TestCase):
    """BeginMultipartFileUpload200ResponsePartsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BeginMultipartFileUpload200ResponsePartsInner:
        """Test BeginMultipartFileUpload200ResponsePartsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BeginMultipartFileUpload200ResponsePartsInner`
        """
        model = BeginMultipartFileUpload200ResponsePartsInner()
        if include_optional:
            return BeginMultipartFileUpload200ResponsePartsInner(
                part_number = 0,
                start_offset = 56,
                end_offset = 56,
                upload_url = ''
            )
        else:
            return BeginMultipartFileUpload200ResponsePartsInner(
        )
        """

    def testBeginMultipartFileUpload200ResponsePartsInner(self):
        """Test BeginMultipartFileUpload200ResponsePartsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
