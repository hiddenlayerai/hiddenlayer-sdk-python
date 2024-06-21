"""
This file is created because the Enterprise and SaaS APIs are not in sync.

When they are in sync, this file and related references can be deleted.  
"""
from typing import Dict, Optional

from hiddenlayer.sdk.rest.api_client import ApiClient
from hiddenlayer.sdk.rest.models.scan_results_v2 import ScanResultsV2


class EnterpriseModelScanApi:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    def scan_model(self, sensor_id: str, data: Optional[bytes] = None, post_params: Optional[dict] = None):
        _response_types_map: Dict[str, Optional[str]] = {
            '201': "ScanResultsV2",
            '400': None,
            '422': "ValidationErrorModel",
        }
        resource_path = f"/api/v2/create/{sensor_id}"

        response_data = self.api_client.call_api(
           "POST",
           self.api_client.configuration.host + resource_path,
           body=data,
           post_params=post_params,
           header_params={"Content-Type": "octet-binary"}
        )
        response_data.read()
       
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map
        ).data

    def scan_status(self, sensor_id: str) -> ScanResultsV2:
        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ScanResultsV2",
            '400': None,
            '404': None,
        }
        resource_path = f"/api/v2/status/{sensor_id}"

        response_data = self.api_client.call_api(
            "GET",
            self.api_client.configuration.host + resource_path,
        )
        response_data.read()

        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map
        ).data
