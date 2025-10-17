# PatentSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**q** | **str** | Search by field value or pass opensearch string query syntax | [optional] 
**filters** | [**List[Filter]**](Filter.md) |  | [optional] 
**range_filters** | [**List[Range]**](Range.md) |  | [optional] 
**sort** | [**List[Sort]**](Sort.md) |  | [optional] 
**fields** | **List[str]** |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**facets** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.patent_search_request import PatentSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatentSearchRequest from a JSON string
patent_search_request_instance = PatentSearchRequest.from_json(json)
# print the JSON string representation of the object
print(PatentSearchRequest.to_json())

# convert the object into a dict
patent_search_request_dict = patent_search_request_instance.to_dict()
# create an instance of PatentSearchRequest from a dict
patent_search_request_from_dict = PatentSearchRequest.from_dict(patent_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


