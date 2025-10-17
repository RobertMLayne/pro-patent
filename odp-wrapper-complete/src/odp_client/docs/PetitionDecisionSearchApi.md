# openapi_client.PetitionDecisionSearchApi

All URIs are relative to *https://api.uspto.gov*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_petition_decisions_petition_decision_record_identifier_get**](PetitionDecisionSearchApi.md#api_v1_petition_decisions_petition_decision_record_identifier_get) | **GET** /api/v1/petition/decisions/{petitionDecisionRecordIdentifier} | Petition decision application data for a provided application number
[**api_v1_petition_decisions_search_download_get**](PetitionDecisionSearchApi.md#api_v1_petition_decisions_search_download_get) | **GET** /api/v1/petition/decisions/search/download | Petition decision application search by supplying query parameters
[**api_v1_petition_decisions_search_download_post**](PetitionDecisionSearchApi.md#api_v1_petition_decisions_search_download_post) | **POST** /api/v1/petition/decisions/search/download | Download petition decision data by supplying json payload
[**api_v1_petition_decisions_search_get**](PetitionDecisionSearchApi.md#api_v1_petition_decisions_search_get) | **GET** /api/v1/petition/decisions/search | Petition decision application search by supplying query parameters
[**api_v1_petition_decisions_search_post**](PetitionDecisionSearchApi.md#api_v1_petition_decisions_search_post) | **POST** /api/v1/petition/decisions/search | Search petition decision applications by supplying json payload


# **api_v1_petition_decisions_petition_decision_record_identifier_get**
> PetitionDecisionIdentifierResponseBag api_v1_petition_decisions_petition_decision_record_identifier_get(petition_decision_record_identifier, include_documents=include_documents)

Petition decision application data for a provided application number

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.petition_decision_identifier_response_bag import PetitionDecisionIdentifierResponseBag
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
    api_instance = openapi_client.PetitionDecisionSearchApi(api_client)
    petition_decision_record_identifier = '6779f1be-0f3b-5775-b9d3-dcfdb83171c3' # str | Petition Decision number
    include_documents = true # bool | This is a true or false...yes to include petition decision documents in the response and no to omit the petition decision documents from the response (optional)

    try:
        # Petition decision application data for a provided application number
        api_response = api_instance.api_v1_petition_decisions_petition_decision_record_identifier_get(petition_decision_record_identifier, include_documents=include_documents)
        print("The response of PetitionDecisionSearchApi->api_v1_petition_decisions_petition_decision_record_identifier_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PetitionDecisionSearchApi->api_v1_petition_decisions_petition_decision_record_identifier_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **petition_decision_record_identifier** | **str**| Petition Decision number | 
 **include_documents** | **bool**| This is a true or false...yes to include petition decision documents in the response and no to omit the petition decision documents from the response | [optional] 

### Return type

[**PetitionDecisionIdentifierResponseBag**](PetitionDecisionIdentifierResponseBag.md)

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

# **api_v1_petition_decisions_search_download_get**
> PetitionDecisionResponseBag api_v1_petition_decisions_search_download_get(q=q, sort=sort, offset=offset, limit=limit, fields=fields, filters=filters, range_filters=range_filters, format=format)

Petition decision application search by supplying query parameters

Query parameters are optional. When no query parameters supplied, top 25 petition decisions are returned

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.petition_decision_response_bag import PetitionDecisionResponseBag
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
    api_instance = openapi_client.PetitionDecisionSearchApi(api_client)
    q = 'q_example' # str | A search query string which accepts boolean operators (AND, OR, NOT), wildcards (*), and exact phrases (\"\"). (optional)
    sort = 'sort_example' # str | field to be sorted followed by sort order (optional)
    offset = 0 # int | Position in the dataset of a particular record (optional)
    limit = 25 # int | Limit the number of results returned (optional)
    fields = 'fields_example' # str | Limits the response by specifying fields from dataset should be included. (optional)
    filters = 'filters_example' # str | Filter data by supplying filter parameter. Provide field name and its value (optional)
    range_filters = 'range_filters_example' # str | Filter the data by supplying range of values. Applicable for number and date type fields. (optional)
    format = 'json' # str | Download Format (optional)

    try:
        # Petition decision application search by supplying query parameters
        api_response = api_instance.api_v1_petition_decisions_search_download_get(q=q, sort=sort, offset=offset, limit=limit, fields=fields, filters=filters, range_filters=range_filters, format=format)
        print("The response of PetitionDecisionSearchApi->api_v1_petition_decisions_search_download_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PetitionDecisionSearchApi->api_v1_petition_decisions_search_download_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| A search query string which accepts boolean operators (AND, OR, NOT), wildcards (*), and exact phrases (\&quot;\&quot;). | [optional] 
 **sort** | **str**| field to be sorted followed by sort order | [optional] 
 **offset** | **int**| Position in the dataset of a particular record | [optional] 
 **limit** | **int**| Limit the number of results returned | [optional] 
 **fields** | **str**| Limits the response by specifying fields from dataset should be included. | [optional] 
 **filters** | **str**| Filter data by supplying filter parameter. Provide field name and its value | [optional] 
 **range_filters** | **str**| Filter the data by supplying range of values. Applicable for number and date type fields. | [optional] 
 **format** | **str**| Download Format | [optional] 

### Return type

[**PetitionDecisionResponseBag**](PetitionDecisionResponseBag.md)

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

# **api_v1_petition_decisions_search_download_post**
> PetitionDecisionResponseBag api_v1_petition_decisions_search_download_post(petition_decision_download_request=petition_decision_download_request)

Download petition decision data by supplying json payload

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.petition_decision_download_request import PetitionDecisionDownloadRequest
from openapi_client.models.petition_decision_response_bag import PetitionDecisionResponseBag
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
    api_instance = openapi_client.PetitionDecisionSearchApi(api_client)
    petition_decision_download_request = openapi_client.PetitionDecisionDownloadRequest() # PetitionDecisionDownloadRequest | Petition decision data search request json payload. Fields in the request is optional (optional)

    try:
        # Download petition decision data by supplying json payload
        api_response = api_instance.api_v1_petition_decisions_search_download_post(petition_decision_download_request=petition_decision_download_request)
        print("The response of PetitionDecisionSearchApi->api_v1_petition_decisions_search_download_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PetitionDecisionSearchApi->api_v1_petition_decisions_search_download_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **petition_decision_download_request** | [**PetitionDecisionDownloadRequest**](PetitionDecisionDownloadRequest.md)| Petition decision data search request json payload. Fields in the request is optional | [optional] 

### Return type

[**PetitionDecisionResponseBag**](PetitionDecisionResponseBag.md)

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

# **api_v1_petition_decisions_search_get**
> PetitionDecisionResponseBag api_v1_petition_decisions_search_get(q=q, sort=sort, offset=offset, limit=limit, facets=facets, fields=fields, filters=filters, range_filters=range_filters)

Petition decision application search by supplying query parameters

Query parameters are optional. When no query parameters supplied, top 25 petition decisions are returned

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.petition_decision_response_bag import PetitionDecisionResponseBag
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
    api_instance = openapi_client.PetitionDecisionSearchApi(api_client)
    q = 'q_example' # str | A search query string which accepts boolean operators (AND, OR, NOT), wildcards (*), and exact phrases (\"\"). (optional)
    sort = 'sort_example' # str | field to be sorted followed by sort order (optional)
    offset = 0 # int | Position in the dataset of a particular record (optional)
    limit = 25 # int | Limit the number of results returned (optional)
    facets = 'facets_example' # str | List of fields names to be faceted upon separated by comma (<b>,</b>) (optional)
    fields = 'fields_example' # str | Limits the response by specifying fields from dataset should be included. (optional)
    filters = 'filters_example' # str | Filter data by supplying filter parameter. Provide field name and its value (optional)
    range_filters = 'range_filters_example' # str | Filter the data by supplying range of values. Applicable for number and date type fields. (optional)

    try:
        # Petition decision application search by supplying query parameters
        api_response = api_instance.api_v1_petition_decisions_search_get(q=q, sort=sort, offset=offset, limit=limit, facets=facets, fields=fields, filters=filters, range_filters=range_filters)
        print("The response of PetitionDecisionSearchApi->api_v1_petition_decisions_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PetitionDecisionSearchApi->api_v1_petition_decisions_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| A search query string which accepts boolean operators (AND, OR, NOT), wildcards (*), and exact phrases (\&quot;\&quot;). | [optional] 
 **sort** | **str**| field to be sorted followed by sort order | [optional] 
 **offset** | **int**| Position in the dataset of a particular record | [optional] 
 **limit** | **int**| Limit the number of results returned | [optional] 
 **facets** | **str**| List of fields names to be faceted upon separated by comma (&lt;b&gt;,&lt;/b&gt;) | [optional] 
 **fields** | **str**| Limits the response by specifying fields from dataset should be included. | [optional] 
 **filters** | **str**| Filter data by supplying filter parameter. Provide field name and its value | [optional] 
 **range_filters** | **str**| Filter the data by supplying range of values. Applicable for number and date type fields. | [optional] 

### Return type

[**PetitionDecisionResponseBag**](PetitionDecisionResponseBag.md)

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

# **api_v1_petition_decisions_search_post**
> PetitionDecisionResponseBag api_v1_petition_decisions_search_post(petition_decision_search_request=petition_decision_search_request)

Search petition decision applications by supplying json payload

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.petition_decision_response_bag import PetitionDecisionResponseBag
from openapi_client.models.petition_decision_search_request import PetitionDecisionSearchRequest
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
    api_instance = openapi_client.PetitionDecisionSearchApi(api_client)
    petition_decision_search_request = openapi_client.PetitionDecisionSearchRequest() # PetitionDecisionSearchRequest | Petition Decision data search request json payload. Fields in the request is optional (optional)

    try:
        # Search petition decision applications by supplying json payload
        api_response = api_instance.api_v1_petition_decisions_search_post(petition_decision_search_request=petition_decision_search_request)
        print("The response of PetitionDecisionSearchApi->api_v1_petition_decisions_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PetitionDecisionSearchApi->api_v1_petition_decisions_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **petition_decision_search_request** | [**PetitionDecisionSearchRequest**](PetitionDecisionSearchRequest.md)| Petition Decision data search request json payload. Fields in the request is optional | [optional] 

### Return type

[**PetitionDecisionResponseBag**](PetitionDecisionResponseBag.md)

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

