# coding: utf-8

"""
    HiddenLayer Sensor SOR

    HiddenLayer Sensor SOR API for operations to sensor data storage

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.scan_header_v3 import ScanHeaderV3

class TestScanHeaderV3(unittest.TestCase):
    """ScanHeaderV3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScanHeaderV3:
        """Test ScanHeaderV3
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScanHeaderV3`
        """
        model = ScanHeaderV3()
        if include_optional:
            return ScanHeaderV3(
                file_count = 56,
                files_with_detections_count = 56,
                detection_count = 56,
                detection_categories = [
                    ''
                    ],
                inventory = hiddenlayer.sdk.rest.models.model_inventory_info.Model Inventory Info(),
                version = '',
                scan_id = '',
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = 'pending',
                severity = 'low'
            )
        else:
            return ScanHeaderV3(
                file_count = 56,
                files_with_detections_count = 56,
                detection_count = 56,
                inventory = hiddenlayer.sdk.rest.models.model_inventory_info.Model Inventory Info(),
                version = '',
                scan_id = '',
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = 'pending',
        )
        """

    def testScanHeaderV3(self):
        """Test ScanHeaderV3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
