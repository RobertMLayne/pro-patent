# PetitionDecisionResponseBag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**petition_decision_data_bag** | [**List[PetitionDecision]**](PetitionDecision.md) |  | [optional] 
**facets** | [**List[PetitionDecisionFacet]**](PetitionDecisionFacet.md) |  | [optional] 

## Example

```python
from openapi_client.models.petition_decision_response_bag import PetitionDecisionResponseBag

# TODO update the JSON string below
json = "{}"
# create an instance of PetitionDecisionResponseBag from a JSON string
petition_decision_response_bag_instance = PetitionDecisionResponseBag.from_json(json)
# print the JSON string representation of the object
print(PetitionDecisionResponseBag.to_json())

# convert the object into a dict
petition_decision_response_bag_dict = petition_decision_response_bag_instance.to_dict()
# create an instance of PetitionDecisionResponseBag from a dict
petition_decision_response_bag_from_dict = PetitionDecisionResponseBag.from_dict(petition_decision_response_bag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


