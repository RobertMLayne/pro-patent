# StatusCodeSearchResponse

This json structure represents data fields for status codes search API

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**status_code_bag** | [**List[StatusCodeSearchResponseStatusCodeBagInner]**](StatusCodeSearchResponseStatusCodeBagInner.md) |  | [optional] 
**request_identifier** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.status_code_search_response import StatusCodeSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StatusCodeSearchResponse from a JSON string
status_code_search_response_instance = StatusCodeSearchResponse.from_json(json)
# print the JSON string representation of the object
print(StatusCodeSearchResponse.to_json())

# convert the object into a dict
status_code_search_response_dict = status_code_search_response_instance.to_dict()
# create an instance of StatusCodeSearchResponse from a dict
status_code_search_response_from_dict = StatusCodeSearchResponse.from_dict(status_code_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


