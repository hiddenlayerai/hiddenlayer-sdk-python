# coding: utf-8

"""
    HiddenLayer-API

    HiddenLayer-API

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.models.security_posture import SecurityPosture

class TestSecurityPosture(unittest.TestCase):
    """SecurityPosture unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SecurityPosture:
        """Test SecurityPosture
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SecurityPosture`
        """
        model = SecurityPosture()
        if include_optional:
            return SecurityPosture(
                model_scan = True,
                attack_monitoring = True
            )
        else:
            return SecurityPosture(
        )
        """

    def testSecurityPosture(self):
        """Test SecurityPosture"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
