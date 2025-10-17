# ChildContinuityData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_application_status_code** | **float** |  | [optional] 
**parent_application_number_text** | **str** |  | [optional] 
**child_application_number_text** | **str** | Application number of the child application, which is the unique value assigned by the USPTO to a patent application upon receipt | [optional] 
**child_application_status_description_text** | **str** |  | [optional] 
**child_application_filing_date** | **str** |  | [optional] 
**first_inventor_to_file_indicator** | **bool** |  | [optional] 
**child_patent_number** | **str** |  | [optional] 
**claim_parentage_type_code** | **str** |  | [optional] 
**claim_parentage_type_code_description_text** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.child_continuity_data import ChildContinuityData

# TODO update the JSON string below
json = "{}"
# create an instance of ChildContinuityData from a JSON string
child_continuity_data_instance = ChildContinuityData.from_json(json)
# print the JSON string representation of the object
print(ChildContinuityData.to_json())

# convert the object into a dict
child_continuity_data_dict = child_continuity_data_instance.to_dict()
# create an instance of ChildContinuityData from a dict
child_continuity_data_from_dict = ChildContinuityData.from_dict(child_continuity_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


