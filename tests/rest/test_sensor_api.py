# coding: utf-8

"""
    HiddenLayer ModelScan V2

    HiddenLayer ModelScan API for scanning of models

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

    def test_begin_multipart_upload(self) -> None:
        """Test case for begin_multipart_upload

        Begin Multipart Upload
        """
        pass

    def test_complete_multipart_upload(self) -> None:
        """Test case for complete_multipart_upload

        Complete Multipart Upload
        """
        pass

    def test_create_sensor(self) -> None:
        """Test case for create_sensor

        Create a Sensor
        """
        pass

    def test_delete_model(self) -> None:
        """Test case for delete_model

        Remove an Adhoc Sensor
        """
        pass

    def test_get_model(self) -> None:
        """Test case for get_model

        Get Model
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

    def test_upload_model_part(self) -> None:
        """Test case for upload_model_part

        Upload part
        """
        pass


if __name__ == '__main__':
    unittest.main()
