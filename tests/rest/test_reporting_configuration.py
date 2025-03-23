# coding: utf-8

"""
    HiddenLayer Sensor SOR

    HiddenLayer Sensor SOR API for operations to sensor data storage

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.reporting_configuration import ReportingConfiguration

class TestReportingConfiguration(unittest.TestCase):
    """ReportingConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReportingConfiguration:
        """Test ReportingConfiguration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReportingConfiguration`
        """
        model = ReportingConfiguration()
        if include_optional:
            return ReportingConfiguration(
                enabled = True,
                level = 'warning',
                rank = -1,
                parameters = { },
                properties = { }
            )
        else:
            return ReportingConfiguration(
        )
        """

    def testReportingConfiguration(self):
        """Test ReportingConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
