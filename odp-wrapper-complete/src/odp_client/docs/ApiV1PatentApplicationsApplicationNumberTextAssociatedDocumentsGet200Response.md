# ApiV1PatentApplicationsApplicationNumberTextAssociatedDocumentsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**patent_file_wrapper_data_bag** | [**List[ApiV1PatentApplicationsApplicationNumberTextAssociatedDocumentsGet200ResponsePatentFileWrapperDataBagInner]**](ApiV1PatentApplicationsApplicationNumberTextAssociatedDocumentsGet200ResponsePatentFileWrapperDataBagInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.api_v1_patent_applications_application_number_text_associated_documents_get200_response import ApiV1PatentApplicationsApplicationNumberTextAssociatedDocumentsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PatentApplicationsApplicationNumberTextAssociatedDocumentsGet200Response from a JSON string
api_v1_patent_applications_application_number_text_associated_documents_get200_response_instance = ApiV1PatentApplicationsApplicationNumberTextAssociatedDocumentsGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1PatentApplicationsApplicationNumberTextAssociatedDocumentsGet200Response.to_json())

# convert the object into a dict
api_v1_patent_applications_application_number_text_associated_documents_get200_response_dict = api_v1_patent_applications_application_number_text_associated_documents_get200_response_instance.to_dict()
# create an instance of ApiV1PatentApplicationsApplicationNumberTextAssociatedDocumentsGet200Response from a dict
api_v1_patent_applications_application_number_text_associated_documents_get200_response_from_dict = ApiV1PatentApplicationsApplicationNumberTextAssociatedDocumentsGet200Response.from_dict(api_v1_patent_applications_application_number_text_associated_documents_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


