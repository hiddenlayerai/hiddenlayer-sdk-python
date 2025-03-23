# coding: utf-8

"""
    HiddenLayer Sensor SOR

    HiddenLayer Sensor SOR API for operations to sensor data storage

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.logical_location import LogicalLocation

class TestLogicalLocation(unittest.TestCase):
    """LogicalLocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LogicalLocation:
        """Test LogicalLocation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LogicalLocation`
        """
        model = LogicalLocation()
        if include_optional:
            return LogicalLocation(
                name = '',
                index = -1,
                fully_qualified_name = '',
                decorated_name = '',
                parent_index = -1,
                kind = '',
                properties = { }
            )
        else:
            return LogicalLocation(
        )
        """

    def testLogicalLocation(self):
        """Test LogicalLocation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
