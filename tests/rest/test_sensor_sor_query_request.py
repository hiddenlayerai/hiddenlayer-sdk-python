# coding: utf-8

"""
    HiddenLayer-API

    HiddenLayer-API

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.sensor_sor_query_request import SensorSORQueryRequest

class TestSensorSORQueryRequest(unittest.TestCase):
    """SensorSORQueryRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SensorSORQueryRequest:
        """Test SensorSORQueryRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SensorSORQueryRequest`
        """
        model = SensorSORQueryRequest()
        if include_optional:
            return SensorSORQueryRequest(
                filter = hiddenlayer.sdk.rest.models.sensor_sor_query_filter.SensorSORQueryFilter(
                    plaintext_name = '', 
                    active = True, 
                    version = 56, 
                    created_at_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created_at_stop = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    source = 'adhoc', ),
                order_by = 'created_at',
                order_dir = 'asc',
                page_size = 56,
                page_number = 56
            )
        else:
            return SensorSORQueryRequest(
        )
        """

    def testSensorSORQueryRequest(self):
        """Test SensorSORQueryRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
