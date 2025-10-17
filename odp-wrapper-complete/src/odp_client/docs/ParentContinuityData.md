# ParentContinuityData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_inventor_to_file_indicator** | **bool** | Indicates first inventor to file. | [optional] 
**parent_application_status_code** | **int** |  | [optional] 
**parent_patent_number** | **str** |  | [optional] 
**parent_application_status_description_text** | **str** |  | [optional] 
**parent_application_filing_date** | **str** |  | [optional] 
**parent_application_number_text** | **str** |  | [optional] 
**child_application_number_text** | **str** |  | [optional] 
**claim_parentage_type_code** | **str** |  | [optional] 
**claim_parentage_type_code_description_text** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.parent_continuity_data import ParentContinuityData

# TODO update the JSON string below
json = "{}"
# create an instance of ParentContinuityData from a JSON string
parent_continuity_data_instance = ParentContinuityData.from_json(json)
# print the JSON string representation of the object
print(ParentContinuityData.to_json())

# convert the object into a dict
parent_continuity_data_dict = parent_continuity_data_instance.to_dict()
# create an instance of ParentContinuityData from a dict
parent_continuity_data_from_dict = ParentContinuityData.from_dict(parent_continuity_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


