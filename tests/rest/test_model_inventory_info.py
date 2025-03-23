# coding: utf-8

"""
    HiddenLayer Sensor SOR

    HiddenLayer Sensor SOR API for operations to sensor data storage

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.model_inventory_info import ModelInventoryInfo

class TestModelInventoryInfo(unittest.TestCase):
    """ModelInventoryInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModelInventoryInfo:
        """Test ModelInventoryInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModelInventoryInfo`
        """
        model = ModelInventoryInfo()
        if include_optional:
            return ModelInventoryInfo(
                model_name = 'keras-tf-2025-05-27',
                model_version = '1.0.0',
                model_source = 'adhoc',
                requested_scan_location = '/files-to-scan',
                requesting_entity = '',
                model_id = '00000000-0000-0000-0000-000000000000',
                model_version_id = '00000000-0000-0000-0000-000000000000'
            )
        else:
            return ModelInventoryInfo(
                model_name = 'keras-tf-2025-05-27',
                model_version = '1.0.0',
                requested_scan_location = '/files-to-scan',
                model_id = '00000000-0000-0000-0000-000000000000',
                model_version_id = '00000000-0000-0000-0000-000000000000',
        )
        """

    def testModelInventoryInfo(self):
        """Test ModelInventoryInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
