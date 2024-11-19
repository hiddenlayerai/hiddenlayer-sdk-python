# coding: utf-8

"""
    HiddenLayer ModelScan V2

    HiddenLayer ModelScan API for scanning of models

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.sensor_sor_model_card_query_response import SensorSORModelCardQueryResponse

class TestSensorSORModelCardQueryResponse(unittest.TestCase):
    """SensorSORModelCardQueryResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SensorSORModelCardQueryResponse:
        """Test SensorSORModelCardQueryResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SensorSORModelCardQueryResponse`
        """
        model = SensorSORModelCardQueryResponse()
        if include_optional:
            return SensorSORModelCardQueryResponse(
                total_count = 56,
                page_size = 56,
                page_number = 56,
                results = [
                    null
                    ]
            )
        else:
            return SensorSORModelCardQueryResponse(
                total_count = 56,
                page_size = 56,
                page_number = 56,
                results = [
                    null
                    ],
        )
        """

    def testSensorSORModelCardQueryResponse(self):
        """Test SensorSORModelCardQueryResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()