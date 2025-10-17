# openapi_client.BulkDataSetsApi

All URIs are relative to *https://api.uspto.gov*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_datasets_products_product_identifier_get**](BulkDataSetsApi.md#api_v1_datasets_products_product_identifier_get) | **GET** /api/v1/datasets/products/{productIdentifier} | Bulk data- find a product by its identifier (shortName)
[**api_v1_datasets_products_search_get**](BulkDataSetsApi.md#api_v1_datasets_products_search_get) | **GET** /api/v1/datasets/products/search | Search bulk datasets products by supplying query parameters


# **api_v1_datasets_products_product_identifier_get**
> BdssResponseProductBag api_v1_datasets_products_product_identifier_get(product_identifier, file_data_from_date=file_data_from_date, file_data_to_date=file_data_to_date, offset=offset, limit=limit, include_files=include_files, latest=latest)

Bulk data- find a product by its identifier (shortName)

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.bdss_response_product_bag import BdssResponseProductBag
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
    api_instance = openapi_client.BulkDataSetsApi(api_client)
    product_identifier = 'product_identifier_example' # str | productIdentifier represents product Short name
    file_data_from_date = 'file_data_from_date_example' # str | fileDataFromDate (optional)
    file_data_to_date = 'file_data_to_date_example' # str | fileDataToDate (optional)
    offset = 56 # int | Number of product file records to skip (optional)
    limit = 56 # int | Number of product file records to collect (optional)
    include_files = 'include_files_example' # str | value true if product files should be included or false if they should be omitted from the response (optional)
    latest = 'latest_example' # str | value is true if only the latest product file should be returned for this specific product (optional)

    try:
        # Bulk data- find a product by its identifier (shortName)
        api_response = api_instance.api_v1_datasets_products_product_identifier_get(product_identifier, file_data_from_date=file_data_from_date, file_data_to_date=file_data_to_date, offset=offset, limit=limit, include_files=include_files, latest=latest)
        print("The response of BulkDataSetsApi->api_v1_datasets_products_product_identifier_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkDataSetsApi->api_v1_datasets_products_product_identifier_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_identifier** | **str**| productIdentifier represents product Short name | 
 **file_data_from_date** | **str**| fileDataFromDate | [optional] 
 **file_data_to_date** | **str**| fileDataToDate | [optional] 
 **offset** | **int**| Number of product file records to skip | [optional] 
 **limit** | **int**| Number of product file records to collect | [optional] 
 **include_files** | **str**| value true if product files should be included or false if they should be omitted from the response | [optional] 
 **latest** | **str**| value is true if only the latest product file should be returned for this specific product | [optional] 

### Return type

[**BdssResponseProductBag**](BdssResponseProductBag.md)

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

# **api_v1_datasets_products_search_get**
> BdssResponseBag api_v1_datasets_products_search_get(q=q, sort=sort, offset=offset, limit=limit, facets=facets, fields=fields, filters=filters, range_filters=range_filters)

Search bulk datasets products by supplying query parameters

Query parameters are optional. When no query parameters supplied, top 25 applications are returned

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.bdss_response_bag import BdssResponseBag
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
    api_instance = openapi_client.BulkDataSetsApi(api_client)
    q = 'q_example' # str | A search query string which accepts boolean operators (AND, OR, NOT), wildcards (*), and exact phrases (\"\"). (optional)
    sort = 'sort_example' # str | field to be sorted followed by sort order (optional)
    offset = 0 # int | Position in the dataset of a particular record (optional)
    limit = 25 # int | Limit the number of results returned (optional)
    facets = 'facets_example' # str | List of fields names to be faceted upon separated by comma (<b>,</b>) (optional)
    fields = 'fields_example' # str | Limits the response by specifying fields from dataset should be included. (optional)
    filters = 'filters_example' # str | Filter data by supplying filter parameter. Provide field name and its value (optional)
    range_filters = 'range_filters_example' # str | Filter the data by supplying range of values. Applicable for number and date type fields. (optional)

    try:
        # Search bulk datasets products by supplying query parameters
        api_response = api_instance.api_v1_datasets_products_search_get(q=q, sort=sort, offset=offset, limit=limit, facets=facets, fields=fields, filters=filters, range_filters=range_filters)
        print("The response of BulkDataSetsApi->api_v1_datasets_products_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkDataSetsApi->api_v1_datasets_products_search_get: %s\n" % e)
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

[**BdssResponseBag**](BdssResponseBag.md)

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

