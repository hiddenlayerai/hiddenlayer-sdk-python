# coding: utf-8

"""
    HiddenLayer-API

    HiddenLayer-API

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.scan_model_ids_v3 import ScanModelIdsV3

class TestScanModelIdsV3(unittest.TestCase):
    """ScanModelIdsV3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScanModelIdsV3:
        """Test ScanModelIdsV3
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScanModelIdsV3`
        """
        model = ScanModelIdsV3()
        if include_optional:
            return ScanModelIdsV3(
                model_id = '00000000-0000-0000-0000-000000000000',
                model_version_id = '00000000-0000-0000-0000-000000000000'
            )
        else:
            return ScanModelIdsV3(
                model_id = '00000000-0000-0000-0000-000000000000',
                model_version_id = '00000000-0000-0000-0000-000000000000',
        )
        """

    def testScanModelIdsV3(self):
        """Test ScanModelIdsV3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
