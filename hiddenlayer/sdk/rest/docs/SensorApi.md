# hiddenlayer.sdk.rest.SensorApi

All URIs are relative to *https://api.hiddenlayer.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**begin_multipart_upload**](SensorApi.md#begin_multipart_upload) | **POST** /api/v2/sensors/{sensor_id}/upload/begin | Begin Multipart Upload
[**complete_multipart_upload**](SensorApi.md#complete_multipart_upload) | **POST** /api/v2/sensors/{sensor_id}/upload/{upload_id}/complete | Complete Multipart Upload
[**create_sensor**](SensorApi.md#create_sensor) | **POST** /api/v2/sensors/create | Create a Sensor
[**delete_model**](SensorApi.md#delete_model) | **DELETE** /api/v2/sensors/{sensor_id} | Remove an Adhoc Sensor
[**get_model**](SensorApi.md#get_model) | **GET** /api/v2/sensors/{sensor_id} | Get Model
[**query_sensor**](SensorApi.md#query_sensor) | **POST** /api/v2/sensors/query | Query a Sensor
[**sensor_sor_api_v3_model_cards_query_get**](SensorApi.md#sensor_sor_api_v3_model_cards_query_get) | **GET** /models/v3/cards | List Model Cards
[**upload_model_part**](SensorApi.md#upload_model_part) | **PUT** /api/v2/sensors/{sensor_id}/upload/{upload_id}/part/{part} | Upload part


# **begin_multipart_upload**
> GetMultipartUploadResponse begin_multipart_upload(sensor_id, x_content_length)

Begin Multipart Upload

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
from hiddenlayer.sdk.rest.models.get_multipart_upload_response import GetMultipartUploadResponse
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
    x_content_length = 56 # int | The total size of multipart upload.

    try:
        # Begin Multipart Upload
        api_response = api_instance.begin_multipart_upload(sensor_id, x_content_length)
        print("The response of SensorApi->begin_multipart_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SensorApi->begin_multipart_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_id** | **str**|  | 
 **x_content_length** | **int**| The total size of multipart upload. | 

### Return type

[**GetMultipartUploadResponse**](GetMultipartUploadResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | The request failed due to a client error, with one or more of the following possible causes: 1. The request required a tenant_id field, which was missing. 2. The request was malformed syntactically or semantically. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_multipart_upload**
> complete_multipart_upload(sensor_id, upload_id)

Complete Multipart Upload

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
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
    upload_id = 'upload_id_example' # str | 

    try:
        # Complete Multipart Upload
        api_instance.complete_multipart_upload(sensor_id, upload_id)
    except Exception as e:
        print("Exception when calling SensorApi->complete_multipart_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_id** | **str**|  | 
 **upload_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | The request failed due to a client error, with one or more of the following possible causes: 1. The request required a tenant_id field, which was missing. 2. The request was malformed syntactically or semantically. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sensor**
> Model create_sensor(create_sensor_request)

Create a Sensor

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
from hiddenlayer.sdk.rest.models.create_sensor_request import CreateSensorRequest
from hiddenlayer.sdk.rest.models.model import Model
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

[**Model**](Model.md)

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

# **delete_model**
> delete_model(sensor_id)

Remove an Adhoc Sensor

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
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
        # Remove an Adhoc Sensor
        api_instance.delete_model(sensor_id)
    except Exception as e:
        print("Exception when calling SensorApi->delete_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful response |  -  |
**400** | The request failed due to a client error, with one or more of the following possible causes: 1. The request required a tenant_id field, which was missing. 2. The request was malformed syntactically or semantically. |  -  |
**404** | The specified resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model**
> Model get_model(sensor_id)

Get Model

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
from hiddenlayer.sdk.rest.models.model import Model
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
        # Get Model
        api_response = api_instance.get_model(sensor_id)
        print("The response of SensorApi->get_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SensorApi->get_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_id** | **str**|  | 

### Return type

[**Model**](Model.md)

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
> ModelQueryResponse query_sensor(sensor_sor_query_request=sensor_sor_query_request)

Query a Sensor

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
from hiddenlayer.sdk.rest.models.model_query_response import ModelQueryResponse
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

[**ModelQueryResponse**](ModelQueryResponse.md)

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

# **upload_model_part**
> upload_model_part(sensor_id, upload_id, part, body)

Upload part

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
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
    upload_id = 'upload_id_example' # str | 
    part = 56 # int | 
    body = None # object | 

    try:
        # Upload part
        api_instance.upload_model_part(sensor_id, upload_id, part, body)
    except Exception as e:
        print("Exception when calling SensorApi->upload_model_part: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_id** | **str**|  | 
 **upload_id** | **str**|  | 
 **part** | **int**|  | 
 **body** | **object**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | The request failed due to a client error, with one or more of the following possible causes: 1. The request required a tenant_id field, which was missing. 2. The request was malformed syntactically or semantically. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

