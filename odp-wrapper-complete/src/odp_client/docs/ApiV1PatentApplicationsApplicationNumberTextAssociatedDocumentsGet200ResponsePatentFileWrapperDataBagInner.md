# ApiV1PatentApplicationsApplicationNumberTextAssociatedDocumentsGet200ResponsePatentFileWrapperDataBagInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_number_text** | **str** | Free format of application number | [optional] 
**pgpub_document_meta_data** | [**PGPubFileMetaData**](PGPubFileMetaData.md) |  | [optional] 
**grant_document_meta_data** | [**GrantFileMetaData**](GrantFileMetaData.md) |  | [optional] 
**request_identifier** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.api_v1_patent_applications_application_number_text_associated_documents_get200_response_patent_file_wrapper_data_bag_inner import ApiV1PatentApplicationsApplicationNumberTextAssociatedDocumentsGet200ResponsePatentFileWrapperDataBagInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PatentApplicationsApplicationNumberTextAssociatedDocumentsGet200ResponsePatentFileWrapperDataBagInner from a JSON string
api_v1_patent_applications_application_number_text_associated_documents_get200_response_patent_file_wrapper_data_bag_inner_instance = ApiV1PatentApplicationsApplicationNumberTextAssociatedDocumentsGet200ResponsePatentFileWrapperDataBagInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1PatentApplicationsApplicationNumberTextAssociatedDocumentsGet200ResponsePatentFileWrapperDataBagInner.to_json())

# convert the object into a dict
api_v1_patent_applications_application_number_text_associated_documents_get200_response_patent_file_wrapper_data_bag_inner_dict = api_v1_patent_applications_application_number_text_associated_documents_get200_response_patent_file_wrapper_data_bag_inner_instance.to_dict()
# create an instance of ApiV1PatentApplicationsApplicationNumberTextAssociatedDocumentsGet200ResponsePatentFileWrapperDataBagInner from a dict
api_v1_patent_applications_application_number_text_associated_documents_get200_response_patent_file_wrapper_data_bag_inner_from_dict = ApiV1PatentApplicationsApplicationNumberTextAssociatedDocumentsGet200ResponsePatentFileWrapperDataBagInner.from_dict(api_v1_patent_applications_application_number_text_associated_documents_get200_response_patent_file_wrapper_data_bag_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


