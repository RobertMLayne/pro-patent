# StatusCodeSearchResponseStatusCodeBagInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_status_code** | **int** | Application status code | [optional] 
**application_status_description_text** | **str** | Application status code description | [optional] 

## Example

```python
from openapi_client.models.status_code_search_response_status_code_bag_inner import StatusCodeSearchResponseStatusCodeBagInner

# TODO update the JSON string below
json = "{}"
# create an instance of StatusCodeSearchResponseStatusCodeBagInner from a JSON string
status_code_search_response_status_code_bag_inner_instance = StatusCodeSearchResponseStatusCodeBagInner.from_json(json)
# print the JSON string representation of the object
print(StatusCodeSearchResponseStatusCodeBagInner.to_json())

# convert the object into a dict
status_code_search_response_status_code_bag_inner_dict = status_code_search_response_status_code_bag_inner_instance.to_dict()
# create an instance of StatusCodeSearchResponseStatusCodeBagInner from a dict
status_code_search_response_status_code_bag_inner_from_dict = StatusCodeSearchResponseStatusCodeBagInner.from_dict(status_code_search_response_status_code_bag_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


