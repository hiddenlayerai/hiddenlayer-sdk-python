# hiddenlayer.rest.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submit_vectors**](DefaultApi.md#submit_vectors) | **POST** /api/v2/submit | Submit vectors


# **submit_vectors**
> SubmissionResponse submit_vectors(submission_v2)

Submit vectors

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import hiddenlayer.rest
from hiddenlayer.rest.models.submission_response import SubmissionResponse
from hiddenlayer.rest.models.submission_v2 import SubmissionV2
from hiddenlayer.rest.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = hiddenlayer.rest.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = hiddenlayer.rest.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hiddenlayer.rest.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hiddenlayer.rest.DefaultApi(api_client)
    submission_v2 = hiddenlayer.rest.SubmissionV2() # SubmissionV2 | 

    try:
        # Submit vectors
        api_response = api_instance.submit_vectors(submission_v2)
        print("The response of DefaultApi->submit_vectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->submit_vectors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_v2** | [**SubmissionV2**](SubmissionV2.md)|  | 

### Return type

[**SubmissionResponse**](SubmissionResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

