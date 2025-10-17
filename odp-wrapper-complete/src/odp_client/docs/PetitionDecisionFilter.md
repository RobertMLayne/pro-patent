# PetitionDecisionFilter

Add filters to your search request by providing filter name and filter value where name in filter request some field in data set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.petition_decision_filter import PetitionDecisionFilter

# TODO update the JSON string below
json = "{}"
# create an instance of PetitionDecisionFilter from a JSON string
petition_decision_filter_instance = PetitionDecisionFilter.from_json(json)
# print the JSON string representation of the object
print(PetitionDecisionFilter.to_json())

# convert the object into a dict
petition_decision_filter_dict = petition_decision_filter_instance.to_dict()
# create an instance of PetitionDecisionFilter from a dict
petition_decision_filter_from_dict = PetitionDecisionFilter.from_dict(petition_decision_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


