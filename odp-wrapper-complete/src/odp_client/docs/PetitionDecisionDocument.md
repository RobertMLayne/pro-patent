# PetitionDecisionDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_number_text** | **str** |  | [optional] 
**official_date** | **str** |  | [optional] 
**document_identifier** | **str** |  | [optional] 
**document_code** | **str** |  | [optional] 
**document_code_description_text** | **str** |  | [optional] 
**document_direction_category** | **str** |  | [optional] 
**download_option_bag** | [**List[PetitionDecisionDocumentDownloadOptionBagInner]**](PetitionDecisionDocumentDownloadOptionBagInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.petition_decision_document import PetitionDecisionDocument

# TODO update the JSON string below
json = "{}"
# create an instance of PetitionDecisionDocument from a JSON string
petition_decision_document_instance = PetitionDecisionDocument.from_json(json)
# print the JSON string representation of the object
print(PetitionDecisionDocument.to_json())

# convert the object into a dict
petition_decision_document_dict = petition_decision_document_instance.to_dict()
# create an instance of PetitionDecisionDocument from a dict
petition_decision_document_from_dict = PetitionDecisionDocument.from_dict(petition_decision_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


