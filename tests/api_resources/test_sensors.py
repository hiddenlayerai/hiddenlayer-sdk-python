# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hiddenlayer import HiddenLayer, AsyncHiddenLayer
from tests.utils import assert_matches_type
from hiddenlayer.types import (
    SensorQueryResponse,
    SensorCreateResponse,
    SensorUpdateResponse,
    SensorRetrieveResponse,
)
from hiddenlayer._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSensors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HiddenLayer) -> None:
        sensor = client.sensors.create(
            plaintext_name="plaintext_name",
        )
        assert_matches_type(SensorCreateResponse, sensor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HiddenLayer) -> None:
        sensor = client.sensors.create(
            plaintext_name="plaintext_name",
            active=True,
            adhoc=True,
            tags={"foo": "bar"},
            version=0,
        )
        assert_matches_type(SensorCreateResponse, sensor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HiddenLayer) -> None:
        response = client.sensors.with_raw_response.create(
            plaintext_name="plaintext_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = response.parse()
        assert_matches_type(SensorCreateResponse, sensor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HiddenLayer) -> None:
        with client.sensors.with_streaming_response.create(
            plaintext_name="plaintext_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = response.parse()
            assert_matches_type(SensorCreateResponse, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: HiddenLayer) -> None:
        sensor = client.sensors.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SensorRetrieveResponse, sensor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: HiddenLayer) -> None:
        response = client.sensors.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = response.parse()
        assert_matches_type(SensorRetrieveResponse, sensor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: HiddenLayer) -> None:
        with client.sensors.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = response.parse()
            assert_matches_type(SensorRetrieveResponse, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: HiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sensor_id` but received ''"):
            client.sensors.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HiddenLayer) -> None:
        sensor = client.sensors.update(
            sensor_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SensorUpdateResponse, sensor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HiddenLayer) -> None:
        sensor = client.sensors.update(
            sensor_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            active=True,
            plaintext_name="plaintext_name",
            tags={"foo": "bar"},
        )
        assert_matches_type(SensorUpdateResponse, sensor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HiddenLayer) -> None:
        response = client.sensors.with_raw_response.update(
            sensor_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = response.parse()
        assert_matches_type(SensorUpdateResponse, sensor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HiddenLayer) -> None:
        with client.sensors.with_streaming_response.update(
            sensor_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = response.parse()
            assert_matches_type(SensorUpdateResponse, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sensor_id` but received ''"):
            client.sensors.with_raw_response.update(
                sensor_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HiddenLayer) -> None:
        sensor = client.sensors.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert sensor is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HiddenLayer) -> None:
        response = client.sensors.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = response.parse()
        assert sensor is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HiddenLayer) -> None:
        with client.sensors.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = response.parse()
            assert sensor is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sensor_id` but received ''"):
            client.sensors.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_query(self, client: HiddenLayer) -> None:
        sensor = client.sensors.query()
        assert_matches_type(SensorQueryResponse, sensor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_query_with_all_params(self, client: HiddenLayer) -> None:
        sensor = client.sensors.query(
            filter={
                "active": True,
                "created_at_start": parse_datetime("2019-12-27T18:11:19.117Z"),
                "created_at_stop": parse_datetime("2019-12-27T18:11:19.117Z"),
                "plaintext_name": "plaintext_name",
                "source": "adhoc",
                "version": 0,
            },
            order_by="order_by",
            order_dir="asc",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(SensorQueryResponse, sensor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_query(self, client: HiddenLayer) -> None:
        response = client.sensors.with_raw_response.query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = response.parse()
        assert_matches_type(SensorQueryResponse, sensor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_query(self, client: HiddenLayer) -> None:
        with client.sensors.with_streaming_response.query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = response.parse()
            assert_matches_type(SensorQueryResponse, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSensors:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHiddenLayer) -> None:
        sensor = await async_client.sensors.create(
            plaintext_name="plaintext_name",
        )
        assert_matches_type(SensorCreateResponse, sensor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHiddenLayer) -> None:
        sensor = await async_client.sensors.create(
            plaintext_name="plaintext_name",
            active=True,
            adhoc=True,
            tags={"foo": "bar"},
            version=0,
        )
        assert_matches_type(SensorCreateResponse, sensor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.sensors.with_raw_response.create(
            plaintext_name="plaintext_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = await response.parse()
        assert_matches_type(SensorCreateResponse, sensor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.sensors.with_streaming_response.create(
            plaintext_name="plaintext_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = await response.parse()
            assert_matches_type(SensorCreateResponse, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHiddenLayer) -> None:
        sensor = await async_client.sensors.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SensorRetrieveResponse, sensor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.sensors.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = await response.parse()
        assert_matches_type(SensorRetrieveResponse, sensor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.sensors.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = await response.parse()
            assert_matches_type(SensorRetrieveResponse, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sensor_id` but received ''"):
            await async_client.sensors.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHiddenLayer) -> None:
        sensor = await async_client.sensors.update(
            sensor_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SensorUpdateResponse, sensor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHiddenLayer) -> None:
        sensor = await async_client.sensors.update(
            sensor_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            active=True,
            plaintext_name="plaintext_name",
            tags={"foo": "bar"},
        )
        assert_matches_type(SensorUpdateResponse, sensor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.sensors.with_raw_response.update(
            sensor_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = await response.parse()
        assert_matches_type(SensorUpdateResponse, sensor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.sensors.with_streaming_response.update(
            sensor_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = await response.parse()
            assert_matches_type(SensorUpdateResponse, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sensor_id` but received ''"):
            await async_client.sensors.with_raw_response.update(
                sensor_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHiddenLayer) -> None:
        sensor = await async_client.sensors.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert sensor is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.sensors.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = await response.parse()
        assert sensor is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.sensors.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = await response.parse()
            assert sensor is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHiddenLayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sensor_id` but received ''"):
            await async_client.sensors.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_query(self, async_client: AsyncHiddenLayer) -> None:
        sensor = await async_client.sensors.query()
        assert_matches_type(SensorQueryResponse, sensor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncHiddenLayer) -> None:
        sensor = await async_client.sensors.query(
            filter={
                "active": True,
                "created_at_start": parse_datetime("2019-12-27T18:11:19.117Z"),
                "created_at_stop": parse_datetime("2019-12-27T18:11:19.117Z"),
                "plaintext_name": "plaintext_name",
                "source": "adhoc",
                "version": 0,
            },
            order_by="order_by",
            order_dir="asc",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(SensorQueryResponse, sensor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_query(self, async_client: AsyncHiddenLayer) -> None:
        response = await async_client.sensors.with_raw_response.query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = await response.parse()
        assert_matches_type(SensorQueryResponse, sensor, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncHiddenLayer) -> None:
        async with async_client.sensors.with_streaming_response.query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = await response.parse()
            assert_matches_type(SensorQueryResponse, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True
