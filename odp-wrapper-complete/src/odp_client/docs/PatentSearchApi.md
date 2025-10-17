# openapi_client.PatentSearchApi

All URIs are relative to *https://api.uspto.gov*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_patent_applications_application_number_text_adjustment_get**](PatentSearchApi.md#api_v1_patent_applications_application_number_text_adjustment_get) | **GET** /api/v1/patent/applications/{applicationNumberText}/adjustment | Get patent term adjustment data for an application number
[**api_v1_patent_applications_application_number_text_assignment_get**](PatentSearchApi.md#api_v1_patent_applications_application_number_text_assignment_get) | **GET** /api/v1/patent/applications/{applicationNumberText}/assignment | Get patent assignment data for an application number
[**api_v1_patent_applications_application_number_text_associated_documents_get**](PatentSearchApi.md#api_v1_patent_applications_application_number_text_associated_documents_get) | **GET** /api/v1/patent/applications/{applicationNumberText}/associated-documents | Associated (pgpub, grant) documents meta-data for an application
[**api_v1_patent_applications_application_number_text_attorney_get**](PatentSearchApi.md#api_v1_patent_applications_application_number_text_attorney_get) | **GET** /api/v1/patent/applications/{applicationNumberText}/attorney | Get attorney/agent data for an application number
[**api_v1_patent_applications_application_number_text_continuity_get**](PatentSearchApi.md#api_v1_patent_applications_application_number_text_continuity_get) | **GET** /api/v1/patent/applications/{applicationNumberText}/continuity | Get continuity data for an application number
[**api_v1_patent_applications_application_number_text_documents_get**](PatentSearchApi.md#api_v1_patent_applications_application_number_text_documents_get) | **GET** /api/v1/patent/applications/{applicationNumberText}/documents | Documents details for an application number
[**api_v1_patent_applications_application_number_text_foreign_priority_get**](PatentSearchApi.md#api_v1_patent_applications_application_number_text_foreign_priority_get) | **GET** /api/v1/patent/applications/{applicationNumberText}/foreign-priority | Get foreign-priority data for an application number
[**api_v1_patent_applications_application_number_text_get**](PatentSearchApi.md#api_v1_patent_applications_application_number_text_get) | **GET** /api/v1/patent/applications/{applicationNumberText} | Patent application data for a provided application number
[**api_v1_patent_applications_application_number_text_meta_data_get**](PatentSearchApi.md#api_v1_patent_applications_application_number_text_meta_data_get) | **GET** /api/v1/patent/applications/{applicationNumberText}/meta-data | Get patent application meta data
[**api_v1_patent_applications_application_number_text_transactions_get**](PatentSearchApi.md#api_v1_patent_applications_application_number_text_transactions_get) | **GET** /api/v1/patent/applications/{applicationNumberText}/transactions | Get transaction data for an application number
[**api_v1_patent_applications_search_download_get**](PatentSearchApi.md#api_v1_patent_applications_search_download_get) | **GET** /api/v1/patent/applications/search/download | Patent application search by supplying query parameters
[**api_v1_patent_applications_search_download_post**](PatentSearchApi.md#api_v1_patent_applications_search_download_post) | **POST** /api/v1/patent/applications/search/download | Download patent data by supplying json payload
[**api_v1_patent_applications_search_get**](PatentSearchApi.md#api_v1_patent_applications_search_get) | **GET** /api/v1/patent/applications/search | Patent application search by supplying query parameters
[**api_v1_patent_applications_search_post**](PatentSearchApi.md#api_v1_patent_applications_search_post) | **POST** /api/v1/patent/applications/search | Search patent applications by supplying json payload
[**api_v1_patent_status_codes_get**](PatentSearchApi.md#api_v1_patent_status_codes_get) | **GET** /api/v1/patent/status-codes | Search patent application status codes and status code description
[**api_v1_patent_status_codes_post**](PatentSearchApi.md#api_v1_patent_status_codes_post) | **POST** /api/v1/patent/status-codes | Search patent application status codes and status code description


# **api_v1_patent_applications_application_number_text_adjustment_get**
> ApiV1PatentApplicationsApplicationNumberTextAdjustmentGet200Response api_v1_patent_applications_application_number_text_adjustment_get(application_number_text)

Get patent term adjustment data for an application number

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_v1_patent_applications_application_number_text_adjustment_get200_response import ApiV1PatentApplicationsApplicationNumberTextAdjustmentGet200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.uspto.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.uspto.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PatentSearchApi(api_client)
    application_number_text = 'application_number_text_example' # str | Patent application number

    try:
        # Get patent term adjustment data for an application number
        api_response = api_instance.api_v1_patent_applications_application_number_text_adjustment_get(application_number_text)
        print("The response of PatentSearchApi->api_v1_patent_applications_application_number_text_adjustment_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatentSearchApi->api_v1_patent_applications_application_number_text_adjustment_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_number_text** | **str**| Patent application number | 

### Return type

[**ApiV1PatentApplicationsApplicationNumberTextAdjustmentGet200Response**](ApiV1PatentApplicationsApplicationNumberTextAdjustmentGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_patent_applications_application_number_text_assignment_get**
> ApiV1PatentApplicationsApplicationNumberTextAssignmentGet200Response api_v1_patent_applications_application_number_text_assignment_get(application_number_text)

Get patent assignment data for an application number

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_v1_patent_applications_application_number_text_assignment_get200_response import ApiV1PatentApplicationsApplicationNumberTextAssignmentGet200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.uspto.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.uspto.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PatentSearchApi(api_client)
    application_number_text = 'application_number_text_example' # str | Patent application number

    try:
        # Get patent assignment data for an application number
        api_response = api_instance.api_v1_patent_applications_application_number_text_assignment_get(application_number_text)
        print("The response of PatentSearchApi->api_v1_patent_applications_application_number_text_assignment_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatentSearchApi->api_v1_patent_applications_application_number_text_assignment_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_number_text** | **str**| Patent application number | 

### Return type

[**ApiV1PatentApplicationsApplicationNumberTextAssignmentGet200Response**](ApiV1PatentApplicationsApplicationNumberTextAssignmentGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_patent_applications_application_number_text_associated_documents_get**
> ApiV1PatentApplicationsApplicationNumberTextAssociatedDocumentsGet200Response api_v1_patent_applications_application_number_text_associated_documents_get(application_number_text)

Associated (pgpub, grant) documents meta-data for an application

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_v1_patent_applications_application_number_text_associated_documents_get200_response import ApiV1PatentApplicationsApplicationNumberTextAssociatedDocumentsGet200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.uspto.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.uspto.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PatentSearchApi(api_client)
    application_number_text = '16330077' # str | application number

    try:
        # Associated (pgpub, grant) documents meta-data for an application
        api_response = api_instance.api_v1_patent_applications_application_number_text_associated_documents_get(application_number_text)
        print("The response of PatentSearchApi->api_v1_patent_applications_application_number_text_associated_documents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatentSearchApi->api_v1_patent_applications_application_number_text_associated_documents_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_number_text** | **str**| application number | 

### Return type

[**ApiV1PatentApplicationsApplicationNumberTextAssociatedDocumentsGet200Response**](ApiV1PatentApplicationsApplicationNumberTextAssociatedDocumentsGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_patent_applications_application_number_text_attorney_get**
> ApiV1PatentApplicationsApplicationNumberTextAttorneyGet200Response api_v1_patent_applications_application_number_text_attorney_get(application_number_text)

Get attorney/agent data for an application number

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_v1_patent_applications_application_number_text_attorney_get200_response import ApiV1PatentApplicationsApplicationNumberTextAttorneyGet200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.uspto.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.uspto.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PatentSearchApi(api_client)
    application_number_text = 'application_number_text_example' # str | Patent application number

    try:
        # Get attorney/agent data for an application number
        api_response = api_instance.api_v1_patent_applications_application_number_text_attorney_get(application_number_text)
        print("The response of PatentSearchApi->api_v1_patent_applications_application_number_text_attorney_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatentSearchApi->api_v1_patent_applications_application_number_text_attorney_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_number_text** | **str**| Patent application number | 

### Return type

[**ApiV1PatentApplicationsApplicationNumberTextAttorneyGet200Response**](ApiV1PatentApplicationsApplicationNumberTextAttorneyGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_patent_applications_application_number_text_continuity_get**
> ApiV1PatentApplicationsApplicationNumberTextContinuityGet200Response api_v1_patent_applications_application_number_text_continuity_get(application_number_text)

Get continuity data for an application number

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_v1_patent_applications_application_number_text_continuity_get200_response import ApiV1PatentApplicationsApplicationNumberTextContinuityGet200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.uspto.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.uspto.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PatentSearchApi(api_client)
    application_number_text = 'application_number_text_example' # str | Patent application number

    try:
        # Get continuity data for an application number
        api_response = api_instance.api_v1_patent_applications_application_number_text_continuity_get(application_number_text)
        print("The response of PatentSearchApi->api_v1_patent_applications_application_number_text_continuity_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatentSearchApi->api_v1_patent_applications_application_number_text_continuity_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_number_text** | **str**| Patent application number | 

### Return type

[**ApiV1PatentApplicationsApplicationNumberTextContinuityGet200Response**](ApiV1PatentApplicationsApplicationNumberTextContinuityGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_patent_applications_application_number_text_documents_get**
> DocumentBag api_v1_patent_applications_application_number_text_documents_get(application_number_text, document_codes=document_codes, official_date_from=official_date_from, official_date_to=official_date_to)

Documents details for an application number

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.document_bag import DocumentBag
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.uspto.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.uspto.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PatentSearchApi(api_client)
    application_number_text = '16330077' # str | application number
    document_codes = 'document_codes_example' # str | single or multiple comma separated document codes (optional)
    official_date_from = 'official_date_from_example' # str | Search by document official date from (optional)
    official_date_to = 'official_date_to_example' # str | Search by document official date to (optional)

    try:
        # Documents details for an application number
        api_response = api_instance.api_v1_patent_applications_application_number_text_documents_get(application_number_text, document_codes=document_codes, official_date_from=official_date_from, official_date_to=official_date_to)
        print("The response of PatentSearchApi->api_v1_patent_applications_application_number_text_documents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatentSearchApi->api_v1_patent_applications_application_number_text_documents_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_number_text** | **str**| application number | 
 **document_codes** | **str**| single or multiple comma separated document codes | [optional] 
 **official_date_from** | **str**| Search by document official date from | [optional] 
 **official_date_to** | **str**| Search by document official date to | [optional] 

### Return type

[**DocumentBag**](DocumentBag.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_patent_applications_application_number_text_foreign_priority_get**
> ApiV1PatentApplicationsApplicationNumberTextForeignPriorityGet200Response api_v1_patent_applications_application_number_text_foreign_priority_get(application_number_text)

Get foreign-priority data for an application number

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_v1_patent_applications_application_number_text_foreign_priority_get200_response import ApiV1PatentApplicationsApplicationNumberTextForeignPriorityGet200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.uspto.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.uspto.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PatentSearchApi(api_client)
    application_number_text = 'application_number_text_example' # str | Patent application number

    try:
        # Get foreign-priority data for an application number
        api_response = api_instance.api_v1_patent_applications_application_number_text_foreign_priority_get(application_number_text)
        print("The response of PatentSearchApi->api_v1_patent_applications_application_number_text_foreign_priority_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatentSearchApi->api_v1_patent_applications_application_number_text_foreign_priority_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_number_text** | **str**| Patent application number | 

### Return type

[**ApiV1PatentApplicationsApplicationNumberTextForeignPriorityGet200Response**](ApiV1PatentApplicationsApplicationNumberTextForeignPriorityGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_patent_applications_application_number_text_get**
> PatentDataResponse api_v1_patent_applications_application_number_text_get(application_number_text)

Patent application data for a provided application number

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.patent_data_response import PatentDataResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.uspto.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.uspto.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PatentSearchApi(api_client)
    application_number_text = '14412875' # str | Patent application number. <b>Note</b>:Application number having special character e.g PCT/BR00/000001 must be encoded with UTF-8 character encoding standard

    try:
        # Patent application data for a provided application number
        api_response = api_instance.api_v1_patent_applications_application_number_text_get(application_number_text)
        print("The response of PatentSearchApi->api_v1_patent_applications_application_number_text_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatentSearchApi->api_v1_patent_applications_application_number_text_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_number_text** | **str**| Patent application number. &lt;b&gt;Note&lt;/b&gt;:Application number having special character e.g PCT/BR00/000001 must be encoded with UTF-8 character encoding standard | 

### Return type

[**PatentDataResponse**](PatentDataResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_patent_applications_application_number_text_meta_data_get**
> ApiV1PatentApplicationsApplicationNumberTextMetaDataGet200Response api_v1_patent_applications_application_number_text_meta_data_get(application_number_text)

Get patent application meta data

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_v1_patent_applications_application_number_text_meta_data_get200_response import ApiV1PatentApplicationsApplicationNumberTextMetaDataGet200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.uspto.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.uspto.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PatentSearchApi(api_client)
    application_number_text = '16330077' # str | Patent application number

    try:
        # Get patent application meta data
        api_response = api_instance.api_v1_patent_applications_application_number_text_meta_data_get(application_number_text)
        print("The response of PatentSearchApi->api_v1_patent_applications_application_number_text_meta_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatentSearchApi->api_v1_patent_applications_application_number_text_meta_data_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_number_text** | **str**| Patent application number | 

### Return type

[**ApiV1PatentApplicationsApplicationNumberTextMetaDataGet200Response**](ApiV1PatentApplicationsApplicationNumberTextMetaDataGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application meta data section |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_patent_applications_application_number_text_transactions_get**
> ApiV1PatentApplicationsApplicationNumberTextTransactionsGet200Response api_v1_patent_applications_application_number_text_transactions_get(application_number_text)

Get transaction data for an application number

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_v1_patent_applications_application_number_text_transactions_get200_response import ApiV1PatentApplicationsApplicationNumberTextTransactionsGet200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.uspto.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.uspto.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PatentSearchApi(api_client)
    application_number_text = 'application_number_text_example' # str | Patent application number

    try:
        # Get transaction data for an application number
        api_response = api_instance.api_v1_patent_applications_application_number_text_transactions_get(application_number_text)
        print("The response of PatentSearchApi->api_v1_patent_applications_application_number_text_transactions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatentSearchApi->api_v1_patent_applications_application_number_text_transactions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_number_text** | **str**| Patent application number | 

### Return type

[**ApiV1PatentApplicationsApplicationNumberTextTransactionsGet200Response**](ApiV1PatentApplicationsApplicationNumberTextTransactionsGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_patent_applications_search_download_get**
> PatentDataResponse api_v1_patent_applications_search_download_get(q=q, sort=sort, offset=offset, limit=limit, fields=fields, filters=filters, range_filters=range_filters, format=format)

Patent application search by supplying query parameters

Query parameters are optional. When no query parameters supplied, top 25 applications are returned

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.patent_data_response import PatentDataResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.uspto.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.uspto.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PatentSearchApi(api_client)
    q = 'q_example' # str | A search query string which accepts boolean operators (AND, OR, NOT), wildcards (*), and exact phrases (\"\"). (optional)
    sort = 'sort_example' # str | field to be sorted followed by sort order (optional)
    offset = 0 # int | Page number to begin with (optional)
    limit = 25 # int | Limit the number of results returned (optional)
    fields = 'fields_example' # str | Limits the response by specifying fields from dataset should be included. (optional)
    filters = 'filters_example' # str | Filter data by supplying filter parameter. Provide field name and its value (optional)
    range_filters = 'range_filters_example' # str | Filter the data by supplying range of values. Applicable for number and date type fields. (optional)
    format = 'json' # str | Download Format (optional)

    try:
        # Patent application search by supplying query parameters
        api_response = api_instance.api_v1_patent_applications_search_download_get(q=q, sort=sort, offset=offset, limit=limit, fields=fields, filters=filters, range_filters=range_filters, format=format)
        print("The response of PatentSearchApi->api_v1_patent_applications_search_download_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatentSearchApi->api_v1_patent_applications_search_download_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| A search query string which accepts boolean operators (AND, OR, NOT), wildcards (*), and exact phrases (\&quot;\&quot;). | [optional] 
 **sort** | **str**| field to be sorted followed by sort order | [optional] 
 **offset** | **int**| Page number to begin with | [optional] 
 **limit** | **int**| Limit the number of results returned | [optional] 
 **fields** | **str**| Limits the response by specifying fields from dataset should be included. | [optional] 
 **filters** | **str**| Filter data by supplying filter parameter. Provide field name and its value | [optional] 
 **range_filters** | **str**| Filter the data by supplying range of values. Applicable for number and date type fields. | [optional] 
 **format** | **str**| Download Format | [optional] 

### Return type

[**PatentDataResponse**](PatentDataResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_patent_applications_search_download_post**
> PatentDataResponse api_v1_patent_applications_search_download_post(patent_download_request=patent_download_request)

Download patent data by supplying json payload

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.patent_data_response import PatentDataResponse
from openapi_client.models.patent_download_request import PatentDownloadRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.uspto.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.uspto.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PatentSearchApi(api_client)
    patent_download_request = openapi_client.PatentDownloadRequest() # PatentDownloadRequest | Patent data search request json payload. Fields in the request is optional (optional)

    try:
        # Download patent data by supplying json payload
        api_response = api_instance.api_v1_patent_applications_search_download_post(patent_download_request=patent_download_request)
        print("The response of PatentSearchApi->api_v1_patent_applications_search_download_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatentSearchApi->api_v1_patent_applications_search_download_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patent_download_request** | [**PatentDownloadRequest**](PatentDownloadRequest.md)| Patent data search request json payload. Fields in the request is optional | [optional] 

### Return type

[**PatentDataResponse**](PatentDataResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_patent_applications_search_get**
> PatentDataResponse api_v1_patent_applications_search_get(q=q, sort=sort, offset=offset, limit=limit, facets=facets, fields=fields, filters=filters, range_filters=range_filters)

Patent application search by supplying query parameters

Query parameters are optional. When no query parameters supplied, top 25 applications are returned

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.patent_data_response import PatentDataResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.uspto.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.uspto.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PatentSearchApi(api_client)
    q = 'q_example' # str | A search query string which accepts boolean operators (AND, OR, NOT), wildcards (*), and exact phrases (\"\"). (optional)
    sort = 'sort_example' # str | Field to be sorted followed by sort order (optional)
    offset = 0 # int | Position in the dataset of a particular record (optional)
    limit = 25 # int | Limit the number of results returned (optional)
    facets = 'facets_example' # str | List of fields names to be faceted upon separated by comma (<b>,</b>) (optional)
    fields = 'fields_example' # str | Limits the response by specifying which fields from dataset should be included. (optional)
    filters = 'filters_example' # str | Filter data by supplying filter parameter. Provide field name and its value. (optional)
    range_filters = 'range_filters_example' # str | Filter the data by supplying range of values. Applicable for number and date type fields. (optional)

    try:
        # Patent application search by supplying query parameters
        api_response = api_instance.api_v1_patent_applications_search_get(q=q, sort=sort, offset=offset, limit=limit, facets=facets, fields=fields, filters=filters, range_filters=range_filters)
        print("The response of PatentSearchApi->api_v1_patent_applications_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatentSearchApi->api_v1_patent_applications_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| A search query string which accepts boolean operators (AND, OR, NOT), wildcards (*), and exact phrases (\&quot;\&quot;). | [optional] 
 **sort** | **str**| Field to be sorted followed by sort order | [optional] 
 **offset** | **int**| Position in the dataset of a particular record | [optional] 
 **limit** | **int**| Limit the number of results returned | [optional] 
 **facets** | **str**| List of fields names to be faceted upon separated by comma (&lt;b&gt;,&lt;/b&gt;) | [optional] 
 **fields** | **str**| Limits the response by specifying which fields from dataset should be included. | [optional] 
 **filters** | **str**| Filter data by supplying filter parameter. Provide field name and its value. | [optional] 
 **range_filters** | **str**| Filter the data by supplying range of values. Applicable for number and date type fields. | [optional] 

### Return type

[**PatentDataResponse**](PatentDataResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**413** | Payload Too Large |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_patent_applications_search_post**
> PatentDataResponse api_v1_patent_applications_search_post(patent_search_request=patent_search_request)

Search patent applications by supplying json payload

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.patent_data_response import PatentDataResponse
from openapi_client.models.patent_search_request import PatentSearchRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.uspto.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.uspto.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PatentSearchApi(api_client)
    patent_search_request = openapi_client.PatentSearchRequest() # PatentSearchRequest | Patent data search request json payload. Fields in the request is optional (optional)

    try:
        # Search patent applications by supplying json payload
        api_response = api_instance.api_v1_patent_applications_search_post(patent_search_request=patent_search_request)
        print("The response of PatentSearchApi->api_v1_patent_applications_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatentSearchApi->api_v1_patent_applications_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patent_search_request** | [**PatentSearchRequest**](PatentSearchRequest.md)| Patent data search request json payload. Fields in the request is optional | [optional] 

### Return type

[**PatentDataResponse**](PatentDataResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**413** | Payload Too Large |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_patent_status_codes_get**
> StatusCodeSearchResponse api_v1_patent_status_codes_get(q=q, offset=offset, limit=limit)

Search patent application status codes and status code description

Query parameters are optional.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.status_code_search_response import StatusCodeSearchResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.uspto.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.uspto.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PatentSearchApi(api_client)
    q = 'q_example' # str | A search query string which accepts boolean operators (AND, OR, NOT), wildcards (*), and exact phrases (\"\"). (optional)
    offset = 0 # int | Position in the dataset of a particular record (optional)
    limit = 25 # int | Limit the number of results returned (optional)

    try:
        # Search patent application status codes and status code description
        api_response = api_instance.api_v1_patent_status_codes_get(q=q, offset=offset, limit=limit)
        print("The response of PatentSearchApi->api_v1_patent_status_codes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatentSearchApi->api_v1_patent_status_codes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| A search query string which accepts boolean operators (AND, OR, NOT), wildcards (*), and exact phrases (\&quot;\&quot;). | [optional] 
 **offset** | **int**| Position in the dataset of a particular record | [optional] 
 **limit** | **int**| Limit the number of results returned | [optional] 

### Return type

[**StatusCodeSearchResponse**](StatusCodeSearchResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_patent_status_codes_post**
> StatusCodeSearchResponse api_v1_patent_status_codes_post(status_code_search_request=status_code_search_request)

Search patent application status codes and status code description

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.status_code_search_request import StatusCodeSearchRequest
from openapi_client.models.status_code_search_response import StatusCodeSearchResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.uspto.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.uspto.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PatentSearchApi(api_client)
    status_code_search_request = openapi_client.StatusCodeSearchRequest() # StatusCodeSearchRequest | Patent status code search request json payload. All fields in the request are optional (optional)

    try:
        # Search patent application status codes and status code description
        api_response = api_instance.api_v1_patent_status_codes_post(status_code_search_request=status_code_search_request)
        print("The response of PatentSearchApi->api_v1_patent_status_codes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PatentSearchApi->api_v1_patent_status_codes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_code_search_request** | [**StatusCodeSearchRequest**](StatusCodeSearchRequest.md)| Patent status code search request json payload. All fields in the request are optional | [optional] 

### Return type

[**StatusCodeSearchResponse**](StatusCodeSearchResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

