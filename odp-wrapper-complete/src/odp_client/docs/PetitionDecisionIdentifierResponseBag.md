# PetitionDecisionIdentifierResponseBag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**petition_decision_data_bag** | [**List[PetitionDecisionAndDocuments]**](PetitionDecisionAndDocuments.md) |  | [optional] 

## Example

```python
from openapi_client.models.petition_decision_identifier_response_bag import PetitionDecisionIdentifierResponseBag

# TODO update the JSON string below
json = "{}"
# create an instance of PetitionDecisionIdentifierResponseBag from a JSON string
petition_decision_identifier_response_bag_instance = PetitionDecisionIdentifierResponseBag.from_json(json)
# print the JSON string representation of the object
print(PetitionDecisionIdentifierResponseBag.to_json())

# convert the object into a dict
petition_decision_identifier_response_bag_dict = petition_decision_identifier_response_bag_instance.to_dict()
# create an instance of PetitionDecisionIdentifierResponseBag from a dict
petition_decision_identifier_response_bag_from_dict = PetitionDecisionIdentifierResponseBag.from_dict(petition_decision_identifier_response_bag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


