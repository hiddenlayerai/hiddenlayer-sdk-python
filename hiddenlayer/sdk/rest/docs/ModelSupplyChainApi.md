# hiddenlayer.sdk.rest.ModelSupplyChainApi

All URIs are relative to *https://api.hiddenlayer.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**begin_multi_file_upload**](ModelSupplyChainApi.md#begin_multi_file_upload) | **POST** /scan/v3/upload | Start V3 Upload
[**begin_multipart_file_upload**](ModelSupplyChainApi.md#begin_multipart_file_upload) | **POST** /scan/v3/upload/{scan_id}/file | Add file to V3 Upload
[**complete_multi_file_upload**](ModelSupplyChainApi.md#complete_multi_file_upload) | **PATCH** /scan/v3/upload/{scan_id} | Indicate All files are uploaded and start the scan
[**complete_multipart_file_upload**](ModelSupplyChainApi.md#complete_multipart_file_upload) | **PATCH** /scan/v3/upload/{scan_id}/file/{file_id} | Indicate that upload is completed for {file_id}
[**create_scan_job**](ModelSupplyChainApi.md#create_scan_job) | **POST** /scan/v3/jobs | Request a Model Scan Job
[**get_condensed_model_scan_reports**](ModelSupplyChainApi.md#get_condensed_model_scan_reports) | **GET** /scan/v3/results | Get condensed reports for a Model Scan
[**get_scan_jobs**](ModelSupplyChainApi.md#get_scan_jobs) | **GET** /scan/v3/jobs | List all Model Scan Jobs
[**get_scan_results**](ModelSupplyChainApi.md#get_scan_results) | **GET** /scan/v3/results/{scan_id} | Get Result of a Model Scan
[**get_scan_results1**](ModelSupplyChainApi.md#get_scan_results1) | **GET** /scans/v3/results/{scan_id} | Retrieve Model Scan Results
[**modelscanner_api_v3_health_check**](ModelSupplyChainApi.md#modelscanner_api_v3_health_check) | **GET** /scans/v3/health | Health check endpoint for Model Supply Chain Services
[**modelscanner_api_v3_readiness_check**](ModelSupplyChainApi.md#modelscanner_api_v3_readiness_check) | **GET** /scans/v3/readiness | Readiness check endpoint for Model Supply Chain Services
[**notify_model_scan_completed**](ModelSupplyChainApi.md#notify_model_scan_completed) | **PATCH** /scan/v3/results/{scan_id} | Indicate part (file or files) of a model scan has completed
[**notify_model_scan_started**](ModelSupplyChainApi.md#notify_model_scan_started) | **POST** /scan/v3/results/{scan_id} | Indicate model scan has started
[**report_scan_results**](ModelSupplyChainApi.md#report_scan_results) | **POST** /scans/v3/reports/{scan_id} | Engine Report Endpoint of Model Scan Results


# **begin_multi_file_upload**
> BeginMultiFileUpload200Response begin_multi_file_upload(multi_file_upload_request_v3)

Start V3 Upload

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
from hiddenlayer.sdk.rest.models.begin_multi_file_upload200_response import BeginMultiFileUpload200Response
from hiddenlayer.sdk.rest.models.multi_file_upload_request_v3 import MultiFileUploadRequestV3
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
    multi_file_upload_request_v3 = hiddenlayer.sdk.rest.MultiFileUploadRequestV3() # MultiFileUploadRequestV3 | Request body for create

    try:
        # Start V3 Upload
        api_response = api_instance.begin_multi_file_upload(multi_file_upload_request_v3)
        print("The response of ModelSupplyChainApi->begin_multi_file_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelSupplyChainApi->begin_multi_file_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multi_file_upload_request_v3** | [**MultiFileUploadRequestV3**](MultiFileUploadRequestV3.md)| Request body for create | 

### Return type

[**BeginMultiFileUpload200Response**](BeginMultiFileUpload200Response.md)

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

# **begin_multipart_file_upload**
> BeginMultipartFileUpload200Response begin_multipart_file_upload(file_content_length, file_name, scan_id)

Add file to V3 Upload

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
from hiddenlayer.sdk.rest.models.begin_multipart_file_upload200_response import BeginMultipartFileUpload200Response
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
    file_content_length = 12345 # int | Added file size in bytes
    file_name = 'exampleFile.txt' # str | Added file name
    scan_id = 'scan_id_example' # str | 

    try:
        # Add file to V3 Upload
        api_response = api_instance.begin_multipart_file_upload(file_content_length, file_name, scan_id)
        print("The response of ModelSupplyChainApi->begin_multipart_file_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelSupplyChainApi->begin_multipart_file_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_content_length** | **int**| Added file size in bytes | 
 **file_name** | **str**| Added file name | 
 **scan_id** | **str**|  | 

### Return type

[**BeginMultipartFileUpload200Response**](BeginMultipartFileUpload200Response.md)

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_multi_file_upload**
> BeginMultiFileUpload200Response complete_multi_file_upload(scan_id)

Indicate All files are uploaded and start the scan

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
from hiddenlayer.sdk.rest.models.begin_multi_file_upload200_response import BeginMultiFileUpload200Response
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

    try:
        # Indicate All files are uploaded and start the scan
        api_response = api_instance.complete_multi_file_upload(scan_id)
        print("The response of ModelSupplyChainApi->complete_multi_file_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelSupplyChainApi->complete_multi_file_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_id** | **str**|  | 

### Return type

[**BeginMultiFileUpload200Response**](BeginMultiFileUpload200Response.md)

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_multipart_file_upload**
> BeginMultiFileUpload200Response complete_multipart_file_upload(scan_id, file_id)

Indicate that upload is completed for {file_id}

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
from hiddenlayer.sdk.rest.models.begin_multi_file_upload200_response import BeginMultiFileUpload200Response
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
    file_id = 'file_id_example' # str | 

    try:
        # Indicate that upload is completed for {file_id}
        api_response = api_instance.complete_multipart_file_upload(scan_id, file_id)
        print("The response of ModelSupplyChainApi->complete_multipart_file_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelSupplyChainApi->complete_multipart_file_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_id** | **str**|  | 
 **file_id** | **str**|  | 

### Return type

[**BeginMultiFileUpload200Response**](BeginMultiFileUpload200Response.md)

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_scan_job**
> ScanReportV3 create_scan_job(scan_job)

Request a Model Scan Job

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
from hiddenlayer.sdk.rest.models.scan_job import ScanJob
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
    scan_job = {"access":{"source":"HUGGING_FACE"},"inventory":{"model_name":"some-model","model_version":"main","requested_scan_location":"owner/repo","requesting_entity":"some-user@example.com"}} # ScanJob | Request body for create scan request

    try:
        # Request a Model Scan Job
        api_response = api_instance.create_scan_job(scan_job)
        print("The response of ModelSupplyChainApi->create_scan_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelSupplyChainApi->create_scan_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_job** | [**ScanJob**](ScanJob.md)| Request body for create scan request | 

### Return type

[**ScanReportV3**](ScanReportV3.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8, application/octet-stream
 - **Accept**: application/json; charset=utf-8, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Scan Job Created |  -  |
**400** | The request failed due to a client error, with one or more of the following possible causes: 1. The request required a tenant_id field, which was missing. 2. The request was malformed syntactically or semantically. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_condensed_model_scan_reports**
> GetCondensedModelScanReports200Response get_condensed_model_scan_reports(model_version_ids=model_version_ids, model_ids=model_ids, start_time=start_time, end_time=end_time, severity=severity, status=status, limit=limit, offset=offset, sort=sort, latest_per_model_version_only=latest_per_model_version_only)

Get condensed reports for a Model Scan

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
from hiddenlayer.sdk.rest.models.get_condensed_model_scan_reports200_response import GetCondensedModelScanReports200Response
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
        api_response = api_instance.get_condensed_model_scan_reports(model_version_ids=model_version_ids, model_ids=model_ids, start_time=start_time, end_time=end_time, severity=severity, status=status, limit=limit, offset=offset, sort=sort, latest_per_model_version_only=latest_per_model_version_only)
        print("The response of ModelSupplyChainApi->get_condensed_model_scan_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelSupplyChainApi->get_condensed_model_scan_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

[**GetCondensedModelScanReports200Response**](GetCondensedModelScanReports200Response.md)

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

# **get_scan_jobs**
> ScanJob get_scan_jobs()

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
        api_response = api_instance.get_scan_jobs()
        print("The response of ModelSupplyChainApi->get_scan_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelSupplyChainApi->get_scan_jobs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ScanJob**](ScanJob.md)

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

# **get_scan_results**
> ScanReportV3 get_scan_results(scan_id, has_detections=has_detections)

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
    has_detections = True # bool | Filter file_results to only those that have detections (and parents) (optional)

    try:
        # Get Result of a Model Scan
        api_response = api_instance.get_scan_results(scan_id, has_detections=has_detections)
        print("The response of ModelSupplyChainApi->get_scan_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelSupplyChainApi->get_scan_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_id** | **str**|  | 
 **has_detections** | **bool**| Filter file_results to only those that have detections (and parents) | [optional] 

### Return type

[**ScanReportV3**](ScanReportV3.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, application/sarif+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | The request failed due to a client error, with one or more of the following possible causes: 1. The request required a tenant_id field, which was missing. 2. The request was malformed syntactically or semantically. |  -  |
**404** | The specified resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scan_results1**
> List[ScanResultsMapV3] get_scan_results1(scan_id=scan_id, cursor=cursor, page_size=page_size)

Retrieve Model Scan Results

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
from hiddenlayer.sdk.rest.models.scan_results_map_v3 import ScanResultsMapV3
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
    cursor = 'cursor_example' # str |  (optional)
    page_size = 25 # int |  (optional) (default to 25)

    try:
        # Retrieve Model Scan Results
        api_response = api_instance.get_scan_results1(scan_id=scan_id, cursor=cursor, page_size=page_size)
        print("The response of ModelSupplyChainApi->get_scan_results1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelSupplyChainApi->get_scan_results1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_id** | **str**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] [default to 25]

### Return type

[**List[ScanResultsMapV3]**](ScanResultsMapV3.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scan finished. Full results returned. |  -  |
**400** | The request failed due to a client error, with one or more of the following possible causes: 1. The request required a tenant_id field, which was missing. 2. The request was malformed syntactically or semantically. |  -  |
**404** | The specified resource was not found. |  -  |
**405** | The specified method is not allowed. |  -  |

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

# **notify_model_scan_completed**
> NotifyModelScanCompleted200Response notify_model_scan_completed(scan_id, scan_report_v3, has_detections=has_detections)

Indicate part (file or files) of a model scan has completed

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.sdk.rest
from hiddenlayer.sdk.rest.models.notify_model_scan_completed200_response import NotifyModelScanCompleted200Response
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
    scan_report_v3 = hiddenlayer.sdk.rest.ScanReportV3() # ScanReportV3 | Request body for partial update
    has_detections = True # bool | Filter file_results to only those that have detections (and parents) (optional)

    try:
        # Indicate part (file or files) of a model scan has completed
        api_response = api_instance.notify_model_scan_completed(scan_id, scan_report_v3, has_detections=has_detections)
        print("The response of ModelSupplyChainApi->notify_model_scan_completed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelSupplyChainApi->notify_model_scan_completed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_id** | **str**|  | 
 **scan_report_v3** | [**ScanReportV3**](ScanReportV3.md)| Request body for partial update | 
 **has_detections** | **bool**| Filter file_results to only those that have detections (and parents) | [optional] 

### Return type

[**NotifyModelScanCompleted200Response**](NotifyModelScanCompleted200Response.md)

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

# **notify_model_scan_started**
> notify_model_scan_started(scan_id, scan_report_v3, has_detections=has_detections)

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
    scan_report_v3 = hiddenlayer.sdk.rest.ScanReportV3() # ScanReportV3 | Request body for create
    has_detections = True # bool | Filter file_results to only those that have detections (and parents) (optional)

    try:
        # Indicate model scan has started
        api_instance.notify_model_scan_started(scan_id, scan_report_v3, has_detections=has_detections)
    except Exception as e:
        print("Exception when calling ModelSupplyChainApi->notify_model_scan_started: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_id** | **str**|  | 
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

# **report_scan_results**
> report_scan_results(scan_id, scan_create_request)

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
        api_instance.report_scan_results(scan_id, scan_create_request)
    except Exception as e:
        print("Exception when calling ModelSupplyChainApi->report_scan_results: %s\n" % e)
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

