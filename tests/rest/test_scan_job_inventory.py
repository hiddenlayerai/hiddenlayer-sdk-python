# coding: utf-8

"""
    HiddenLayer ModelScan V2

    HiddenLayer ModelScan API for scanning of models

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.scan_job_inventory import ScanJobInventory

class TestScanJobInventory(unittest.TestCase):
    """ScanJobInventory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScanJobInventory:
        """Test ScanJobInventory
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScanJobInventory`
        """
        model = ScanJobInventory()
        if include_optional:
            return ScanJobInventory(
                requested_scan_location = 's3://bucket-name/folder-name/file-name.ext',
                model_name = 'keras-tf-2025-05-27',
                model_version = '1.0.0',
                model_source = 'adhoc',
                requesting_entity = '',
                model_id = '00000000-0000-0000-0000-000000000000',
                model_version_id = '00000000-0000-0000-0000-000000000000'
            )
        else:
            return ScanJobInventory(
                model_name = 'keras-tf-2025-05-27',
                model_version = '1.0.0',
                model_source = 'adhoc',
                model_id = '00000000-0000-0000-0000-000000000000',
                model_version_id = '00000000-0000-0000-0000-000000000000',
        )
        """

    def testScanJobInventory(self):
        """Test ScanJobInventory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()