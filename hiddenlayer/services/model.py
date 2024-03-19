from typing import Optional

from hiddenlayer.rest.api import SensorApi
from hiddenlayer.rest.api_client import ApiClient
from hiddenlayer.rest.models import (
    CreateSensorRequest,
    SensorSORItemResponse,
    SensorSORQueryFilter,
    SensorSORQueryRequest,
)


class ModelDoesNotExistError(Exception):
    pass


class ModelAPI:
    def __init__(self, api_client: ApiClient) -> None:
        self._sensor_api = SensorApi(api_client=api_client)

    def create(self, *, model_name: str) -> SensorSORItemResponse:
        """
        Creates a model in the HiddenLayer Platform.

        :params model_name: Name of the model

        :returns: HiddenLayer ModelID
        """
        return self._sensor_api.create_sensor(
            CreateSensorRequest(plaintext_name=model_name)
        )

    def get(
        self, *, model_name: str, version: Optional[int] = None
    ) -> SensorSORItemResponse:
        """
        Gets a HiddenLayer model object. If not version is supplied, the latest model is returned.

        :param model_name: Name of the model.
        :param version: Version of the model to get.

        :returns: HiddenLayer Model object
        """

        models = self._sensor_api.query_sensor(
            sensor_sor_query_request=SensorSORQueryRequest(
                filter=SensorSORQueryFilter(plaintext_name=model_name, version=version)
            )
        )

        if not models.results:
            msg = f"Model {model_name} does not exist"

            if version:
                msg = f"{msg} for version {version}."

            raise ModelDoesNotExistError(msg)

        if not version:
            models.results.sort(key=lambda x: x.version, reverse=True)

        return models.results[0]
