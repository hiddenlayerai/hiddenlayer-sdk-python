# hiddenlayer.sdk.rest.SensorApi

All URIs are relative to *https://api.hiddenlayer.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sensor**](SensorApi.md#create_sensor) | **POST** /api/v2/sensors/create | Create a Sensor
[**get_sensor**](SensorApi.md#get_sensor) | **GET** /api/v2/sensors/{sensor_id} | Get Sensor
[**query_sensor**](SensorApi.md#query_sensor) | **POST** /api/v2/sensors/query | Query a Sensor
[**sensor_sor_api_v3_model_cards_query_get**](SensorApi.md#sensor_sor_api_v3_model_cards_query_get) | **GET** /models/v3/cards | List Model Cards


# **create_sensor**
> Sensor create_sensor(create_sensor_request)

Create a Sensor

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
from hiddenlayer.sdk.rest.models.create_sensor_request import CreateSensorRequest
from hiddenlayer.sdk.rest.models.sensor import Sensor
from hiddenlayer.sdk.rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.hiddenlayer.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = hiddenlayer.sdk.rest.Configuration(
    host = "https://api.hiddenlayer.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = hiddenlayer.sdk.rest.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hiddenlayer.sdk.rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hiddenlayer.sdk.rest.SensorApi(api_client)
    create_sensor_request = hiddenlayer.sdk.rest.CreateSensorRequest() # CreateSensorRequest | Request body for create

    try:
        # Create a Sensor
        api_response = api_instance.create_sensor(create_sensor_request)
        print("The response of SensorApi->create_sensor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SensorApi->create_sensor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_sensor_request** | [**CreateSensorRequest**](CreateSensorRequest.md)| Request body for create | 

### Return type

[**Sensor**](Sensor.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**400** | The request failed due to a client error, with one or more of the following possible causes: 1. The request required a tenant_id field, which was missing. 2. The request was malformed syntactically or semantically. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sensor**
> Sensor get_sensor(sensor_id)

Get Sensor

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
from hiddenlayer.sdk.rest.models.sensor import Sensor
from hiddenlayer.sdk.rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.hiddenlayer.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = hiddenlayer.sdk.rest.Configuration(
    host = "https://api.hiddenlayer.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = hiddenlayer.sdk.rest.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hiddenlayer.sdk.rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hiddenlayer.sdk.rest.SensorApi(api_client)
    sensor_id = 'sensor_id_example' # str | 

    try:
        # Get Sensor
        api_response = api_instance.get_sensor(sensor_id)
        print("The response of SensorApi->get_sensor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SensorApi->get_sensor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_id** | **str**|  | 

### Return type

[**Sensor**](Sensor.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | The request failed due to a client error, with one or more of the following possible causes: 1. The request required a tenant_id field, which was missing. 2. The request was malformed syntactically or semantically. |  -  |
**404** | The specified resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_sensor**
> SensorQueryResponse query_sensor(sensor_sor_query_request=sensor_sor_query_request)

Query a Sensor

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
from hiddenlayer.sdk.rest.models.sensor_query_response import SensorQueryResponse
from hiddenlayer.sdk.rest.models.sensor_sor_query_request import SensorSORQueryRequest
from hiddenlayer.sdk.rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.hiddenlayer.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = hiddenlayer.sdk.rest.Configuration(
    host = "https://api.hiddenlayer.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = hiddenlayer.sdk.rest.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hiddenlayer.sdk.rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hiddenlayer.sdk.rest.SensorApi(api_client)
    sensor_sor_query_request = hiddenlayer.sdk.rest.SensorSORQueryRequest() # SensorSORQueryRequest | Request body for create (optional)

    try:
        # Query a Sensor
        api_response = api_instance.query_sensor(sensor_sor_query_request=sensor_sor_query_request)
        print("The response of SensorApi->query_sensor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SensorApi->query_sensor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_sor_query_request** | [**SensorSORQueryRequest**](SensorSORQueryRequest.md)| Request body for create | [optional] 

### Return type

[**SensorQueryResponse**](SensorQueryResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | The request failed due to a client error, with one or more of the following possible causes: 1. The request required a tenant_id field, which was missing. 2. The request was malformed syntactically or semantically. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensor_sor_api_v3_model_cards_query_get**
> SensorSORModelCardQueryResponse sensor_sor_api_v3_model_cards_query_get(model_name_eq=model_name_eq, model_name_contains=model_name_contains, limit=limit, offset=offset, sort=sort)

List Model Cards

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
from hiddenlayer.sdk.rest.models.sensor_sor_model_card_query_response import SensorSORModelCardQueryResponse
from hiddenlayer.sdk.rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.hiddenlayer.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = hiddenlayer.sdk.rest.Configuration(
    host = "https://api.hiddenlayer.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = hiddenlayer.sdk.rest.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hiddenlayer.sdk.rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hiddenlayer.sdk.rest.SensorApi(api_client)
    model_name_eq = 'model_name_eq_example' # str | substring match on model name (optional)
    model_name_contains = 'model_name_contains_example' # str | substring match on model name (optional)
    limit = 25 # int |  (optional) (default to 25)
    offset = 0 # int |  (optional) (default to 0)
    sort = '-created_at' # str | allow sorting by model name or created at timestamp, ascending (+) or the default descending (-) (optional) (default to '-created_at')

    try:
        # List Model Cards
        api_response = api_instance.sensor_sor_api_v3_model_cards_query_get(model_name_eq=model_name_eq, model_name_contains=model_name_contains, limit=limit, offset=offset, sort=sort)
        print("The response of SensorApi->sensor_sor_api_v3_model_cards_query_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SensorApi->sensor_sor_api_v3_model_cards_query_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_name_eq** | **str**| substring match on model name | [optional] 
 **model_name_contains** | **str**| substring match on model name | [optional] 
 **limit** | **int**|  | [optional] [default to 25]
 **offset** | **int**|  | [optional] [default to 0]
 **sort** | **str**| allow sorting by model name or created at timestamp, ascending (+) or the default descending (-) | [optional] [default to &#39;-created_at&#39;]

### Return type

[**SensorSORModelCardQueryResponse**](SensorSORModelCardQueryResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | The request failed due to a client error, with one or more of the following possible causes: 1. The request required a tenant_id field, which was missing. 2. The request was malformed syntactically or semantically. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

