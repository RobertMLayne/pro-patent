# PetitionDecisionSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**q** | **str** | Search by field value or pass opensearch string query syntax | [optional] 
**filters** | [**List[PetitionDecisionFilter]**](PetitionDecisionFilter.md) |  | [optional] 
**range_filters** | [**List[PetitionDecisionRange]**](PetitionDecisionRange.md) |  | [optional] 
**sort** | [**List[PetitionDecisionSort]**](PetitionDecisionSort.md) |  | [optional] 
**fields** | **List[str]** |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**facets** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.petition_decision_search_request import PetitionDecisionSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PetitionDecisionSearchRequest from a JSON string
petition_decision_search_request_instance = PetitionDecisionSearchRequest.from_json(json)
# print the JSON string representation of the object
print(PetitionDecisionSearchRequest.to_json())

# convert the object into a dict
petition_decision_search_request_dict = petition_decision_search_request_instance.to_dict()
# create an instance of PetitionDecisionSearchRequest from a dict
petition_decision_search_request_from_dict = PetitionDecisionSearchRequest.from_dict(petition_decision_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


