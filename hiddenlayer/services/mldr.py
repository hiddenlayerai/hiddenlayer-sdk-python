import base64
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

import numpy as np

from hiddenlayer.rest.api import MldrApi
from hiddenlayer.rest.api_client import ApiClient
from hiddenlayer.rest.models import (
    SubmissionResponse,
    SubmissionV2,
)


class MLDRAPI:
    def __init__(self, api_client: ApiClient) -> None:
        self._mldr_api = MldrApi(api_client=api_client)

    def submit_vectors(
        self,
        *,
        model_id: str,
        input_vectors: Union[List[float], np.ndarray],
        output: Union[List[float], np.ndarray],
        predictions: Optional[List[float]] = None,
        requester_id: str = "PythonSDK",
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        event_time: Optional[str] = None,
    ) -> SubmissionResponse:
        """
        Submit feature vectors and model outputs via the HiddenLayer API.

        :param model_id: Model id.
        :param input_vectors: Feature vectors for your model.
        :param output: Output vectors directly from your model.
        :param predictions: If you ran `np.argmax` or `np.argmin` or provided custom logic onto the model output.
        :param requester_id: Custom identifier for the request.
            Generally used to identify where the request is coming from, defaults to PythonSDK.
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

        # Output vectors need to be at least 2d or MLDR will fail silently
        output = output.reshape(-1, 1) if len(output.shape) == 1 else output

        input_layer = base64.b64encode(input_vectors.tobytes()).decode()
        output_layer = base64.b64encode(output.tobytes()).decode()

        return self._mldr_api.submit_vectors(
            SubmissionV2(
                metadata=metadata if metadata else {},
                tags=tags if tags else [],
                sensor_id=model_id,
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
