import json
from typing import Optional

from hiddenlayer.sdk.constants import ApiErrors
from hiddenlayer.sdk.exceptions import (
    HiddenlayerConflictError,
    IncompatibleModelError,
    ModelDoesNotExistError,
)
from hiddenlayer.sdk.rest.api import SensorApi
from hiddenlayer.sdk.rest.api_client import ApiClient
from hiddenlayer.sdk.rest.exceptions import ApiException
from hiddenlayer.sdk.rest.models import (
    CreateSensorRequest,
    Model,
    SensorSORQueryFilter,
    SensorSORQueryRequest,
)


class ModelAPI:
    def __init__(self, api_client: ApiClient) -> None:
        self._sensor_api = SensorApi(api_client=api_client)

    def create(self, *, model_name: str) -> Model:
        """
        Creates a model in the HiddenLayer Platform.

        :params model_name: Name of the model

        :returns: HiddenLayer ModelID
        """
        return self._sensor_api.create_sensor(
            CreateSensorRequest(plaintext_name=model_name, adhoc=True)
        )

    def get(self, *, model_name: str, version: Optional[int] = None) -> Model:
        """
        Gets a HiddenLayer model object. If not version is supplied, the latest model is returned.

        :param model_name: Name of the model.
        :param version: Version of the model to get.

        :returns: HiddenLayer Model object
        """

        return self._get_model_by_name(model_name=model_name, version=version)

    def delete(self, *, model_name: str) -> None:
        """
        Delete a model.

        :param model_name: Name of the model.
        """

        model = self._get_model_by_name(model_name=model_name, version=None)

        try:
            self._sensor_api.delete_model(sensor_id=model.sensor_id)
        except ApiException as e:
            reason = json.loads(str(e.body))["detail"]

            if reason == ApiErrors.NON_ADHOC_SENSOR_DELETE:
                raise IncompatibleModelError(
                    "This type of model is unable to be deleted."
                )
            else:
                raise HiddenlayerConflictError(reason)
        except Exception as e:
            raise e

    def _get_model_by_name(
        self, *, model_name: str, version: Optional[int] = None
    ) -> Model:
        """
        Gets a model object by name. If version is not supplied, get the latest.

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
