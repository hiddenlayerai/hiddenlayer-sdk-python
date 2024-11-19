# coding: utf-8

"""
    HiddenLayer ModelScan V2

    HiddenLayer ModelScan API for scanning of models

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.model_scan_api_v3_scan_model_version_id_patch200_response import ModelScanApiV3ScanModelVersionIdPatch200Response

class TestModelScanApiV3ScanModelVersionIdPatch200Response(unittest.TestCase):
    """ModelScanApiV3ScanModelVersionIdPatch200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModelScanApiV3ScanModelVersionIdPatch200Response:
        """Test ModelScanApiV3ScanModelVersionIdPatch200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModelScanApiV3ScanModelVersionIdPatch200Response`
        """
        model = ModelScanApiV3ScanModelVersionIdPatch200Response()
        if include_optional:
            return ModelScanApiV3ScanModelVersionIdPatch200Response(
                message = ''
            )
        else:
            return ModelScanApiV3ScanModelVersionIdPatch200Response(
                message = '',
        )
        """

    def testModelScanApiV3ScanModelVersionIdPatch200Response(self):
        """Test ModelScanApiV3ScanModelVersionIdPatch200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()