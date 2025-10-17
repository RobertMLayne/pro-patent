# PetitionDecision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**petition_decision_record_identifier** | **str** |  | [optional] 
**application_number_text** | **str** |  | [optional] 
**business_entity_status_category** | **str** |  | [optional] 
**customer_number** | **int** |  | [optional] 
**decision_date** | **str** |  | [optional] 
**decision_petition_type_code** | **int** |  | [optional] 
**decision_type_code** | **str** |  | [optional] 
**decision_petition_type_code_description_text** | **str** |  | [optional] 
**final_deciding_office_name** | **str** |  | [optional] 
**first_applicant_name** | **str** |  | [optional] 
**first_inventor_to_file_indicator** | **bool** |  | [optional] 
**group_art_unit_number** | **str** |  | [optional] 
**technology_center** | **str** |  | [optional] 
**invention_title** | **str** |  | [optional] 
**inventor_bag** | **List[str]** |  | [optional] 
**action_taken_by_court_name** | **str** |  | [optional] 
**court_action_indicator** | **bool** |  | [optional] 
**last_ingestion_date_time** | **str** |  | [optional] 
**patent_number** | **str** |  | [optional] 
**petition_issue_considered_text_bag** | **List[object]** |  | [optional] 
**petition_mail_date** | **str** |  | [optional] 
**prosecution_status_code** | **str** |  | [optional] 
**prosecution_status_code_description_text** | **str** |  | [optional] 
**rule_bag** | **List[str]** |  | [optional] 
**statute_bag** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.petition_decision import PetitionDecision

# TODO update the JSON string below
json = "{}"
# create an instance of PetitionDecision from a JSON string
petition_decision_instance = PetitionDecision.from_json(json)
# print the JSON string representation of the object
print(PetitionDecision.to_json())

# convert the object into a dict
petition_decision_dict = petition_decision_instance.to_dict()
# create an instance of PetitionDecision from a dict
petition_decision_from_dict = PetitionDecision.from_dict(petition_decision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


