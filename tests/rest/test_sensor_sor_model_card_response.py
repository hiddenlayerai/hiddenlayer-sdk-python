# coding: utf-8

"""
    HiddenLayer-API

    HiddenLayer-API

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.sensor_sor_model_card_response import SensorSORModelCardResponse

class TestSensorSORModelCardResponse(unittest.TestCase):
    """SensorSORModelCardResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SensorSORModelCardResponse:
        """Test SensorSORModelCardResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SensorSORModelCardResponse`
        """
        model = SensorSORModelCardResponse()
        if include_optional:
            return SensorSORModelCardResponse(
                model_id = '',
                created_at = 56,
                plaintext_name = 'Resnet-50',
                active_versions = [
                    56
                    ],
                source = 'azure:datascience-workspace',
                tags = { },
                model_scan_threat_level = 'safe',
                attack_monitoring_threat_level = 'safe',
                security_posture = hiddenlayer.sdk.rest.models.security_posture.SecurityPosture(
                    model_scan = True, 
                    attack_monitoring = True, )
            )
        else:
            return SensorSORModelCardResponse(
                model_id = '',
                created_at = 56,
                plaintext_name = 'Resnet-50',
                active_versions = [
                    56
                    ],
                source = 'azure:datascience-workspace',
        )
        """

    def testSensorSORModelCardResponse(self):
        """Test SensorSORModelCardResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
