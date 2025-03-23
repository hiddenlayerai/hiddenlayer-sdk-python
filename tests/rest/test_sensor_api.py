# coding: utf-8

"""
    HiddenLayer Sensor SOR

    HiddenLayer Sensor SOR API for operations to sensor data storage

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hiddenlayer.sdk.rest.api.sensor_api import SensorApi


class TestSensorApi(unittest.TestCase):
    """SensorApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SensorApi()

    def tearDown(self) -> None:
        pass

    def test_create_sensor(self) -> None:
        """Test case for create_sensor

        Create a Sensor
        """
        pass

    def test_delete_sensor(self) -> None:
        """Test case for delete_sensor

        Delete Sensor
        """
        pass

    def test_get_sensor(self) -> None:
        """Test case for get_sensor

        Get Sensor
        """
        pass

    def test_query_sensor(self) -> None:
        """Test case for query_sensor

        Query a Sensor
        """
        pass

    def test_sensor_sor_api_v3_model_cards_query_get(self) -> None:
        """Test case for sensor_sor_api_v3_model_cards_query_get

        List Model Cards
        """
        pass


if __name__ == '__main__':
    unittest.main()
