# coding: utf-8

"""
    HiddenLayer ModelScan V2

    HiddenLayer ModelScan API for scanning of models

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.scan_job import ScanJob

class TestScanJob(unittest.TestCase):
    """ScanJob unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScanJob:
        """Test ScanJob
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScanJob`
        """
        model = ScanJob()
        if include_optional:
            return ScanJob(
                scan_id = '00000000-0000-0000-0000-000000000000',
                status = 'pending',
                inventory = hiddenlayer.sdk.rest.models.scan_job_inventory.ScanJob_inventory(
                    requested_scan_location = 's3://bucket-name/folder-name/file-name.ext', )
            )
        else:
            return ScanJob(
        )
        """

    def testScanJob(self):
        """Test ScanJob"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()