import base64
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

import numpy as np

from hiddenlayer.sdk.exceptions import SensorDoesNotExistError
from hiddenlayer.sdk.rest.api import AidrPredictiveApi
from hiddenlayer.sdk.rest.api.sensor_api import SensorApi
from hiddenlayer.sdk.rest.api_client import ApiClient
from hiddenlayer.sdk.rest.models import (
    SubmissionResponse,
    SubmissionV2,
)
from hiddenlayer.sdk.rest.models.create_sensor_request import CreateSensorRequest
from hiddenlayer.sdk.rest.models.sensor import Sensor
from hiddenlayer.sdk.rest.models.sensor_sor_query_filter import SensorSORQueryFilter
from hiddenlayer.sdk.rest.models.sensor_sor_query_request import SensorSORQueryRequest


class AIDRPredictive:
    def __init__(self, api_client: ApiClient) -> None:
        self._sensor_api = SensorApi(api_client=api_client)
        self._aidr_predictive = AidrPredictiveApi(api_client=api_client)

    def submit_vectors(
        self,
        *,
        sensor_id: str,
        requester_id: str,
        input_vectors: Union[List[float], np.ndarray],
        output: Union[List[float], np.ndarray],
        predictions: Optional[List[float]] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        event_time: Optional[str] = None,
    ) -> SubmissionResponse:
        """
        Submit feature vectors and model outputs via the HiddenLayer API.

        :param sensor_id: Sensor id.
        :param requester_id: Custom identifier for the inbound request. This should be a value that can be used to identify individual users interacting with the model.
        :param input_vectors: Feature vectors for your model.
        :param output: Output vectors directly from your model.
        :param predictions: If you ran `np.argmax` or `np.argmin` or provided custom logic onto the model output.
        :param tags: Custom tags attached to the request.
        :param metadata: Custom metadata attached to the request.
        :param event_time: Time when the features and outputs were created, defaults to now.

        :returns: Submission Response
        """

        input_vectors = (
            np.array(input_vectors)
            if isinstance(input_vectors, list)
            else input_vectors
        )
        output = np.array(output) if isinstance(output, list) else output

        # Output vectors need to be at least 2d or AIDR will fail silently
        output = output.reshape(-1, 1) if len(output.shape) == 1 else output

        input_layer = base64.b64encode(input_vectors.tobytes()).decode()
        output_layer = base64.b64encode(output.tobytes()).decode()

        return self._aidr_predictive.submit_vectors(
            SubmissionV2(
                metadata=metadata if metadata else {},
                tags=tags if tags else [],
                sensor_id=sensor_id,
                requester_id=requester_id,
                input_layer=input_layer,
                input_layer_dtype=str(input_vectors.dtype),
                input_layer_shape=list(input_vectors.shape),
                output_layer=output_layer,
                output_layer_dtype=str(output.dtype),
                output_layer_shape=list(output.shape),
                predictions=predictions,
                event_time=event_time
                if event_time
                else str(datetime.now().isoformat()),
            )
        )

    def create_sensor(self, *, sensor_name: str) -> Sensor:
        """
        Creates a sensor in the HiddenLayer Platform.

        :params sensor_name: Name of the sensor

        :returns: HiddenLayer Sensor
        """
        return self._sensor_api.create_sensor(
            CreateSensorRequest(plaintext_name=sensor_name)
        )

    def get_sensor(self, *, sensor_name: str) -> Sensor:
        """
        Gets a HiddenLayer sensor object.

        :params sensor_name: Name of the sensor

        :returns: HiddenLayer Sensor
        """

        return self._get_sensor_by_name(sensor_name=sensor_name)

    def _get_sensor_by_name(self, *, sensor_name: str) -> Sensor:
        """
        Gets a model sensor by name.

        :param sensor_name: Name of the model.

        :returns: HiddenLayer Model object
        """

        sensors = self._sensor_api.query_sensor(
            sensor_sor_query_request=SensorSORQueryRequest(
                filter=SensorSORQueryFilter(plaintext_name=sensor_name)
            )
        )

        if not sensors.results or len(sensors.results) == 0:
            msg = f"ModSensorel {sensor_name} does not exist"

            raise SensorDoesNotExistError(msg)

        sensors.results.sort(key=lambda x: x.version, reverse=True)

        return sensors.results[0]
