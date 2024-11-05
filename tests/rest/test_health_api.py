# coding: utf-8

"""
    HiddenLayer ModelScan V2

    HiddenLayer ModelScan API for scanning of models

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.api.health_api import HealthApi


class TestHealthApi(unittest.TestCase):
    """HealthApi unit test stubs"""

    def setUp(self) -> None:
        self.api = HealthApi()

    def tearDown(self) -> None:
        pass

    def test_modelscanner_api_v3_health_check(self) -> None:
        """Test case for modelscanner_api_v3_health_check

        Health check endpoint for Model Supply Chain Services
        """
        pass


if __name__ == '__main__':
    unittest.main()
