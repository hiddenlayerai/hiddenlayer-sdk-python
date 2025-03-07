# hiddenlayer.sdk.rest.ModelApi

All URIs are relative to *https://api.hiddenlayer.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_model**](ModelApi.md#delete_model) | **DELETE** /api/v2/models/{model_id} | Delete Adhoc Model
[**get_model**](ModelApi.md#get_model) | **GET** /api/v2/models/{model_id} | Get Model


# **delete_model**
> delete_model(model_id)

Delete Adhoc Model

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
    api_instance = hiddenlayer.sdk.rest.ModelApi(api_client)
    model_id = 'model_id_example' # str | 

    try:
        # Delete Adhoc Model
        api_instance.delete_model(model_id)
    except Exception as e:
        print("Exception when calling ModelApi->delete_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**|  | 

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
**204** | Successful (No Available Content) |  -  |
**400** | The request failed due to a client error, with one or more of the following possible causes: 1. The request required a tenant_id field, which was missing. 2. The request was malformed syntactically or semantically. |  -  |
**404** | The specified resource was not found. |  -  |
**409** | The specified resource is in an incompatible state |  -  |
**503** | The service is undergoing maintenance and is temporarily unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model**
> Model get_model(model_id)

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
    api_instance = hiddenlayer.sdk.rest.ModelApi(api_client)
    model_id = 'model_id_example' # str | 

    try:
        # Get Model
        api_response = api_instance.get_model(model_id)
        print("The response of ModelApi->get_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelApi->get_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**|  | 

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

