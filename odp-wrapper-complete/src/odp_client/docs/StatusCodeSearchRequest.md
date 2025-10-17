# StatusCodeSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**q** | **str** | Search by field value or pass opensearch string query syntax | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from openapi_client.models.status_code_search_request import StatusCodeSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StatusCodeSearchRequest from a JSON string
status_code_search_request_instance = StatusCodeSearchRequest.from_json(json)
# print the JSON string representation of the object
print(StatusCodeSearchRequest.to_json())

# convert the object into a dict
status_code_search_request_dict = status_code_search_request_instance.to_dict()
# create an instance of StatusCodeSearchRequest from a dict
status_code_search_request_from_dict = StatusCodeSearchRequest.from_dict(status_code_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


