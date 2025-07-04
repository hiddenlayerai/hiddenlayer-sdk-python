# coding: utf-8

"""
    HiddenLayer-API

    HiddenLayer-API

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.scan_model_details_v31 import ScanModelDetailsV31

class TestScanModelDetailsV31(unittest.TestCase):
    """ScanModelDetailsV31 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScanModelDetailsV31:
        """Test ScanModelDetailsV31
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScanModelDetailsV31`
        """
        model = ScanModelDetailsV31()
        if include_optional:
            return ScanModelDetailsV31(
                model_name = 'keras-tf-2025-05-27',
                model_version = '1.0.0',
                requested_scan_location = '/files-to-scan',
                requesting_entity = '',
                request_source = 'API Upload',
                origin = 'Hugging Face'
            )
        else:
            return ScanModelDetailsV31(
                model_name = 'keras-tf-2025-05-27',
                model_version = '1.0.0',
                requested_scan_location = '/files-to-scan',
                requesting_entity = '',
        )
        """

    def testScanModelDetailsV31(self):
        """Test ScanModelDetailsV31"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
