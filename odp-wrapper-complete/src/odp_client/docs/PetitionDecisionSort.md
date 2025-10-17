# PetitionDecisionSort

Sort you search result by providing field to be sorted and sort order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**order** | **str** | Sort order. e.g. Asc, ASC, Desc, desc, DESC | [optional] 

## Example

```python
from openapi_client.models.petition_decision_sort import PetitionDecisionSort

# TODO update the JSON string below
json = "{}"
# create an instance of PetitionDecisionSort from a JSON string
petition_decision_sort_instance = PetitionDecisionSort.from_json(json)
# print the JSON string representation of the object
print(PetitionDecisionSort.to_json())

# convert the object into a dict
petition_decision_sort_dict = petition_decision_sort_instance.to_dict()
# create an instance of PetitionDecisionSort from a dict
petition_decision_sort_from_dict = PetitionDecisionSort.from_dict(petition_decision_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


