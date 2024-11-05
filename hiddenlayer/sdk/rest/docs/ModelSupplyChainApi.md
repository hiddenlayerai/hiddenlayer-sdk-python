# hiddenlayer.sdk.rest.ModelSupplyChainApi

All URIs are relative to *https://api.hiddenlayer.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**model_scan_api_v3_scan_model_version_id_get**](ModelSupplyChainApi.md#model_scan_api_v3_scan_model_version_id_get) | **GET** /scan/v3/results/{scan_id} | Get Result of a Model Scan
[**model_scan_api_v3_scan_model_version_id_patch**](ModelSupplyChainApi.md#model_scan_api_v3_scan_model_version_id_patch) | **PATCH** /scan/v3/results/{scan_id} | Indicate part (file or files) of a model scan has completed
[**model_scan_api_v3_scan_model_version_id_post**](ModelSupplyChainApi.md#model_scan_api_v3_scan_model_version_id_post) | **POST** /scan/v3/results/{scan_id} | Indicate model scan has started
[**model_scan_api_v3_scan_query**](ModelSupplyChainApi.md#model_scan_api_v3_scan_query) | **GET** /scan/v3/results | Get condensed reports for a Model Scan
[**modelscan_api_v3_get_scan_results**](ModelSupplyChainApi.md#modelscan_api_v3_get_scan_results) | **GET** /scans/v3/results/{scan_id} | Retrieve Model Scan Results
[**modelscan_api_v3_post_scan_results**](ModelSupplyChainApi.md#modelscan_api_v3_post_scan_results) | **POST** /scans/v3/reports/{scan_id} | Engine Report Endpoint of Model Scan Results
[**modelscanner_api_v3_get_jobs**](ModelSupplyChainApi.md#modelscanner_api_v3_get_jobs) | **GET** /scans/v3/jobs | List all Model Scan Jobs
[**modelscanner_api_v3_health_check**](ModelSupplyChainApi.md#modelscanner_api_v3_health_check) | **GET** /scans/v3/health | Health check endpoint for Model Supply Chain Services
[**modelscanner_api_v3_post_request**](ModelSupplyChainApi.md#modelscanner_api_v3_post_request) | **POST** /scans/v3/jobs | Request a Model Scan Job
[**modelscanner_api_v3_readiness_check**](ModelSupplyChainApi.md#modelscanner_api_v3_readiness_check) | **GET** /scans/v3/readiness | Readiness check endpoint for Model Supply Chain Services


# **model_scan_api_v3_scan_model_version_id_get**
> ScanReportV3 model_scan_api_v3_scan_model_version_id_get(scan_id, x_correlation_id, x_tenant_id, has_detections=has_detections)

Get Result of a Model Scan

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
from hiddenlayer.sdk.rest.models.scan_report_v3 import ScanReportV3
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
    api_instance = hiddenlayer.sdk.rest.ModelSupplyChainApi(api_client)
    scan_id = '00000000-0000-0000-0000-000000000000' # str | 
    x_correlation_id = 'x_correlation_id_example' # str | The unique identifier for the request.
    x_tenant_id = 'x_tenant_id_example' # str | The unique identifier for the tenant.
    has_detections = True # bool | Filter file_results to only those that have detections (and parents) (optional)

    try:
        # Get Result of a Model Scan
        api_response = api_instance.model_scan_api_v3_scan_model_version_id_get(scan_id, x_correlation_id, x_tenant_id, has_detections=has_detections)
        print("The response of ModelSupplyChainApi->model_scan_api_v3_scan_model_version_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelSupplyChainApi->model_scan_api_v3_scan_model_version_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_id** | **str**|  | 
 **x_correlation_id** | **str**| The unique identifier for the request. | 
 **x_tenant_id** | **str**| The unique identifier for the tenant. | 
 **has_detections** | **bool**| Filter file_results to only those that have detections (and parents) | [optional] 

### Return type

[**ScanReportV3**](ScanReportV3.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | The request failed due to a client error, with one or more of the following possible causes: 1. The request required a tenant_id field, which was missing. 2. The request was malformed syntactically or semantically. |  -  |
**404** | The specified resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_scan_api_v3_scan_model_version_id_patch**
> ModelScanApiV3ScanModelVersionIdPatch200Response model_scan_api_v3_scan_model_version_id_patch(scan_id, x_correlation_id, x_tenant_id, scan_report_v3, has_detections=has_detections)

Indicate part (file or files) of a model scan has completed

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
from hiddenlayer.sdk.rest.models.model_scan_api_v3_scan_model_version_id_patch200_response import ModelScanApiV3ScanModelVersionIdPatch200Response
from hiddenlayer.sdk.rest.models.scan_report_v3 import ScanReportV3
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
    api_instance = hiddenlayer.sdk.rest.ModelSupplyChainApi(api_client)
    scan_id = '00000000-0000-0000-0000-000000000000' # str | 
    x_correlation_id = 'x_correlation_id_example' # str | The unique identifier for the request.
    x_tenant_id = 'x_tenant_id_example' # str | The unique identifier for the tenant.
    scan_report_v3 = hiddenlayer.sdk.rest.ScanReportV3() # ScanReportV3 | Request body for partial update
    has_detections = True # bool | Filter file_results to only those that have detections (and parents) (optional)

    try:
        # Indicate part (file or files) of a model scan has completed
        api_response = api_instance.model_scan_api_v3_scan_model_version_id_patch(scan_id, x_correlation_id, x_tenant_id, scan_report_v3, has_detections=has_detections)
        print("The response of ModelSupplyChainApi->model_scan_api_v3_scan_model_version_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelSupplyChainApi->model_scan_api_v3_scan_model_version_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_id** | **str**|  | 
 **x_correlation_id** | **str**| The unique identifier for the request. | 
 **x_tenant_id** | **str**| The unique identifier for the tenant. | 
 **scan_report_v3** | [**ScanReportV3**](ScanReportV3.md)| Request body for partial update | 
 **has_detections** | **bool**| Filter file_results to only those that have detections (and parents) | [optional] 

### Return type

[**ModelScanApiV3ScanModelVersionIdPatch200Response**](ModelScanApiV3ScanModelVersionIdPatch200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | The request failed due to a client error, with one or more of the following possible causes: 1. The request required a tenant_id field, which was missing. 2. The request was malformed syntactically or semantically. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_scan_api_v3_scan_model_version_id_post**
> model_scan_api_v3_scan_model_version_id_post(scan_id, x_correlation_id, x_tenant_id, scan_report_v3, has_detections=has_detections)

Indicate model scan has started

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
from hiddenlayer.sdk.rest.models.scan_report_v3 import ScanReportV3
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
    api_instance = hiddenlayer.sdk.rest.ModelSupplyChainApi(api_client)
    scan_id = '00000000-0000-0000-0000-000000000000' # str | 
    x_correlation_id = 'x_correlation_id_example' # str | The unique identifier for the request.
    x_tenant_id = 'x_tenant_id_example' # str | The unique identifier for the tenant.
    scan_report_v3 = hiddenlayer.sdk.rest.ScanReportV3() # ScanReportV3 | Request body for create
    has_detections = True # bool | Filter file_results to only those that have detections (and parents) (optional)

    try:
        # Indicate model scan has started
        api_instance.model_scan_api_v3_scan_model_version_id_post(scan_id, x_correlation_id, x_tenant_id, scan_report_v3, has_detections=has_detections)
    except Exception as e:
        print("Exception when calling ModelSupplyChainApi->model_scan_api_v3_scan_model_version_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_id** | **str**|  | 
 **x_correlation_id** | **str**| The unique identifier for the request. | 
 **x_tenant_id** | **str**| The unique identifier for the tenant. | 
 **scan_report_v3** | [**ScanReportV3**](ScanReportV3.md)| Request body for create | 
 **has_detections** | **bool**| Filter file_results to only those that have detections (and parents) | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The resource was successfully created. |  -  |
**400** | The request failed due to a client error, with one or more of the following possible causes: 1. The request required a tenant_id field, which was missing. 2. The request was malformed syntactically or semantically. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_scan_api_v3_scan_query**
> ModelScanApiV3ScanQuery200Response model_scan_api_v3_scan_query(x_correlation_id, x_tenant_id, model_version_ids=model_version_ids, model_ids=model_ids, start_time=start_time, end_time=end_time, severity=severity, status=status, limit=limit, offset=offset, sort=sort, latest_per_model_version_only=latest_per_model_version_only)

Get condensed reports for a Model Scan

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
from hiddenlayer.sdk.rest.models.model_scan_api_v3_scan_query200_response import ModelScanApiV3ScanQuery200Response
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
    api_instance = hiddenlayer.sdk.rest.ModelSupplyChainApi(api_client)
    x_correlation_id = 'x_correlation_id_example' # str | The unique identifier for the request.
    x_tenant_id = 'x_tenant_id_example' # str | The unique identifier for the tenant.
    model_version_ids = ['00fb9505-b9ac-4703-91a7-9d4859315a4b,0278fa73-4b08-47ca-bc23-33bc244719be'] # List[str] | Model Version ID (optional)
    model_ids = ['00fb9505-b9ac-4703-91a7-9d4859315a4b,2df09dc6-a0eb-4f67-9fe9-139ac3b75d11'] # List[str] | Model ID (optional)
    start_time = '2025-05-27T00:00:00Z' # datetime | Start Time (optional)
    end_time = '2025-05-27T23:59:59Z' # datetime | End Time (optional)
    severity = ['low,critical'] # List[str] | Severities (optional)
    status = ['done,failed'] # List[str] | Statuses (optional)
    limit = 25 # int |  (optional) (default to 25)
    offset = 0 # int |  (optional) (default to 0)
    sort = '-start_time' # str | allow sorting by status, severity or created at, ascending (+) or the default descending (-) (optional) (default to '-start_time')
    latest_per_model_version_only = False # bool | only return latest result per model version (optional) (default to False)

    try:
        # Get condensed reports for a Model Scan
        api_response = api_instance.model_scan_api_v3_scan_query(x_correlation_id, x_tenant_id, model_version_ids=model_version_ids, model_ids=model_ids, start_time=start_time, end_time=end_time, severity=severity, status=status, limit=limit, offset=offset, sort=sort, latest_per_model_version_only=latest_per_model_version_only)
        print("The response of ModelSupplyChainApi->model_scan_api_v3_scan_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelSupplyChainApi->model_scan_api_v3_scan_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_correlation_id** | **str**| The unique identifier for the request. | 
 **x_tenant_id** | **str**| The unique identifier for the tenant. | 
 **model_version_ids** | [**List[str]**](str.md)| Model Version ID | [optional] 
 **model_ids** | [**List[str]**](str.md)| Model ID | [optional] 
 **start_time** | **datetime**| Start Time | [optional] 
 **end_time** | **datetime**| End Time | [optional] 
 **severity** | [**List[str]**](str.md)| Severities | [optional] 
 **status** | [**List[str]**](str.md)| Statuses | [optional] 
 **limit** | **int**|  | [optional] [default to 25]
 **offset** | **int**|  | [optional] [default to 0]
 **sort** | **str**| allow sorting by status, severity or created at, ascending (+) or the default descending (-) | [optional] [default to &#39;-start_time&#39;]
 **latest_per_model_version_only** | **bool**| only return latest result per model version | [optional] [default to False]

### Return type

[**ModelScanApiV3ScanQuery200Response**](ModelScanApiV3ScanQuery200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | The request failed due to a client error, with one or more of the following possible causes: 1. The request required a tenant_id field, which was missing. 2. The request was malformed syntactically or semantically. |  -  |
**404** | The specified resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modelscan_api_v3_get_scan_results**
> List[ScanResultsV2] modelscan_api_v3_get_scan_results(scan_id=scan_id)

Retrieve Model Scan Results

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
from hiddenlayer.sdk.rest.models.scan_results_v2 import ScanResultsV2
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
    api_instance = hiddenlayer.sdk.rest.ModelSupplyChainApi(api_client)
    scan_id = 'scan_id_example' # str |  (optional)

    try:
        # Retrieve Model Scan Results
        api_response = api_instance.modelscan_api_v3_get_scan_results(scan_id=scan_id)
        print("The response of ModelSupplyChainApi->modelscan_api_v3_get_scan_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelSupplyChainApi->modelscan_api_v3_get_scan_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_id** | **str**|  | [optional] 

### Return type

[**List[ScanResultsV2]**](ScanResultsV2.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scan finished. Full results returned. |  -  |
**202** | Scan still in progress. Partial results returned. |  -  |
**400** | The request failed due to a client error, with one or more of the following possible causes: 1. The request required a tenant_id field, which was missing. 2. The request was malformed syntactically or semantically. |  -  |
**404** | The specified resource was not found. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modelscan_api_v3_post_scan_results**
> modelscan_api_v3_post_scan_results(scan_id, scan_create_request)

Engine Report Endpoint of Model Scan Results

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
from hiddenlayer.sdk.rest.models.scan_create_request import ScanCreateRequest
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
    api_instance = hiddenlayer.sdk.rest.ModelSupplyChainApi(api_client)
    scan_id = 'scan_id_example' # str | 
    scan_create_request = hiddenlayer.sdk.rest.ScanCreateRequest() # ScanCreateRequest | Request body for reporting a scan of one or more file results

    try:
        # Engine Report Endpoint of Model Scan Results
        api_instance.modelscan_api_v3_post_scan_results(scan_id, scan_create_request)
    except Exception as e:
        print("Exception when calling ModelSupplyChainApi->modelscan_api_v3_post_scan_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_id** | **str**|  | 
 **scan_create_request** | [**ScanCreateRequest**](ScanCreateRequest.md)| Request body for reporting a scan of one or more file results | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Report Successful |  -  |
**400** | The request failed due to a client error, with one or more of the following possible causes: 1. The request required a tenant_id field, which was missing. 2. The request was malformed syntactically or semantically. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modelscanner_api_v3_get_jobs**
> List[ScanJob] modelscanner_api_v3_get_jobs()

List all Model Scan Jobs

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
from hiddenlayer.sdk.rest.models.scan_job import ScanJob
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
    api_instance = hiddenlayer.sdk.rest.ModelSupplyChainApi(api_client)

    try:
        # List all Model Scan Jobs
        api_response = api_instance.modelscanner_api_v3_get_jobs()
        print("The response of ModelSupplyChainApi->modelscanner_api_v3_get_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelSupplyChainApi->modelscanner_api_v3_get_jobs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ScanJob]**](ScanJob.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | The request failed due to a client error, with one or more of the following possible causes: 1. The request required a tenant_id field, which was missing. 2. The request was malformed syntactically or semantically. |  -  |
**404** | The specified resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modelscanner_api_v3_health_check**
> modelscanner_api_v3_health_check()

Health check endpoint for Model Supply Chain Services

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
    api_instance = hiddenlayer.sdk.rest.ModelSupplyChainApi(api_client)

    try:
        # Health check endpoint for Model Supply Chain Services
        api_instance.modelscanner_api_v3_health_check()
    except Exception as e:
        print("Exception when calling ModelSupplyChainApi->modelscanner_api_v3_health_check: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | Healthy |  -  |
**503** | Not Ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modelscanner_api_v3_post_request**
> modelscanner_api_v3_post_request(scan_job)

Request a Model Scan Job

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
from hiddenlayer.sdk.rest.models.scan_job import ScanJob
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
    api_instance = hiddenlayer.sdk.rest.ModelSupplyChainApi(api_client)
    scan_job = hiddenlayer.sdk.rest.ScanJob() # ScanJob | Request body for create scan request

    try:
        # Request a Model Scan Job
        api_instance.modelscanner_api_v3_post_request(scan_job)
    except Exception as e:
        print("Exception when calling ModelSupplyChainApi->modelscanner_api_v3_post_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_job** | [**ScanJob**](ScanJob.md)| Request body for create scan request | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8, application/octet-stream
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The resource was successfully created. |  -  |
**400** | The request failed due to a client error, with one or more of the following possible causes: 1. The request required a tenant_id field, which was missing. 2. The request was malformed syntactically or semantically. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modelscanner_api_v3_readiness_check**
> modelscanner_api_v3_readiness_check()

Readiness check endpoint for Model Supply Chain Services

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
    api_instance = hiddenlayer.sdk.rest.ModelSupplyChainApi(api_client)

    try:
        # Readiness check endpoint for Model Supply Chain Services
        api_instance.modelscanner_api_v3_readiness_check()
    except Exception as e:
        print("Exception when calling ModelSupplyChainApi->modelscanner_api_v3_readiness_check: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | Ready |  -  |
**503** | Not Ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

