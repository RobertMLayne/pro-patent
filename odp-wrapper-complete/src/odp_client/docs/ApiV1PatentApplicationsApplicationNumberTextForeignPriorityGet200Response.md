# ApiV1PatentApplicationsApplicationNumberTextForeignPriorityGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**patent_file_wrapper_data_bag** | [**List[ApiV1PatentApplicationsApplicationNumberTextForeignPriorityGet200ResponsePatentFileWrapperDataBagInner]**](ApiV1PatentApplicationsApplicationNumberTextForeignPriorityGet200ResponsePatentFileWrapperDataBagInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.api_v1_patent_applications_application_number_text_foreign_priority_get200_response import ApiV1PatentApplicationsApplicationNumberTextForeignPriorityGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PatentApplicationsApplicationNumberTextForeignPriorityGet200Response from a JSON string
api_v1_patent_applications_application_number_text_foreign_priority_get200_response_instance = ApiV1PatentApplicationsApplicationNumberTextForeignPriorityGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1PatentApplicationsApplicationNumberTextForeignPriorityGet200Response.to_json())

# convert the object into a dict
api_v1_patent_applications_application_number_text_foreign_priority_get200_response_dict = api_v1_patent_applications_application_number_text_foreign_priority_get200_response_instance.to_dict()
# create an instance of ApiV1PatentApplicationsApplicationNumberTextForeignPriorityGet200Response from a dict
api_v1_patent_applications_application_number_text_foreign_priority_get200_response_from_dict = ApiV1PatentApplicationsApplicationNumberTextForeignPriorityGet200Response.from_dict(api_v1_patent_applications_application_number_text_foreign_priority_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


