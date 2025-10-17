# PetitionDecisionRange

Range filter. Provide field from dataset and valueFrom and valueTo. If range filter is for date field, date must be in “yyyy-MM-dd” format

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**value_from** | **str** |  | [optional] 
**value_to** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.petition_decision_range import PetitionDecisionRange

# TODO update the JSON string below
json = "{}"
# create an instance of PetitionDecisionRange from a JSON string
petition_decision_range_instance = PetitionDecisionRange.from_json(json)
# print the JSON string representation of the object
print(PetitionDecisionRange.to_json())

# convert the object into a dict
petition_decision_range_dict = petition_decision_range_instance.to_dict()
# create an instance of PetitionDecisionRange from a dict
petition_decision_range_from_dict = PetitionDecisionRange.from_dict(petition_decision_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


