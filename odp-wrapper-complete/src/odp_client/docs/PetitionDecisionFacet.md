# PetitionDecisionFacet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**technology_center** | [**List[PetitionDecisionFacetEntity]**](PetitionDecisionFacetEntity.md) |  | [optional] 
**final_deciding_office_name** | [**List[PetitionDecisionFacetEntity]**](PetitionDecisionFacetEntity.md) |  | [optional] 
**first_inventor_to_file_indicator** | [**List[PetitionDecisionFacetEntity]**](PetitionDecisionFacetEntity.md) |  | [optional] 
**decision_petition_type_code** | [**List[PetitionDecisionFacetEntity]**](PetitionDecisionFacetEntity.md) |  | [optional] 
**decision_type_code_description_text** | [**List[PetitionDecisionFacetEntity]**](PetitionDecisionFacetEntity.md) |  | [optional] 
**prosecution_status_code_description_text** | [**List[PetitionDecisionFacetEntity]**](PetitionDecisionFacetEntity.md) |  | [optional] 
**petition_issue_considered_text_bag** | [**List[PetitionDecisionFacetEntity]**](PetitionDecisionFacetEntity.md) |  | [optional] 
**statute_bag** | [**List[PetitionDecisionFacetEntity]**](PetitionDecisionFacetEntity.md) |  | [optional] 
**rule_bag** | [**List[PetitionDecisionFacetEntity]**](PetitionDecisionFacetEntity.md) |  | [optional] 
**action_taken_by_court_name** | [**List[PetitionDecisionFacetEntity]**](PetitionDecisionFacetEntity.md) |  | [optional] 
**court_action_indicator** | [**List[PetitionDecisionFacetEntity]**](PetitionDecisionFacetEntity.md) |  | [optional] 
**business_entity_status_category** | [**List[PetitionDecisionFacetEntity]**](PetitionDecisionFacetEntity.md) |  | [optional] 

## Example

```python
from openapi_client.models.petition_decision_facet import PetitionDecisionFacet

# TODO update the JSON string below
json = "{}"
# create an instance of PetitionDecisionFacet from a JSON string
petition_decision_facet_instance = PetitionDecisionFacet.from_json(json)
# print the JSON string representation of the object
print(PetitionDecisionFacet.to_json())

# convert the object into a dict
petition_decision_facet_dict = petition_decision_facet_instance.to_dict()
# create an instance of PetitionDecisionFacet from a dict
petition_decision_facet_from_dict = PetitionDecisionFacet.from_dict(petition_decision_facet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


