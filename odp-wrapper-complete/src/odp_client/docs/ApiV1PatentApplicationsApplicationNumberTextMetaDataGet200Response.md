# ApiV1PatentApplicationsApplicationNumberTextMetaDataGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **object** |  | [optional] 
**patent_file_wrapper_data_bag** | [**List[ApiV1PatentApplicationsApplicationNumberTextMetaDataGet200ResponsePatentFileWrapperDataBagInner]**](ApiV1PatentApplicationsApplicationNumberTextMetaDataGet200ResponsePatentFileWrapperDataBagInner.md) |  | [optional] 
**request_identifier** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.api_v1_patent_applications_application_number_text_meta_data_get200_response import ApiV1PatentApplicationsApplicationNumberTextMetaDataGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PatentApplicationsApplicationNumberTextMetaDataGet200Response from a JSON string
api_v1_patent_applications_application_number_text_meta_data_get200_response_instance = ApiV1PatentApplicationsApplicationNumberTextMetaDataGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1PatentApplicationsApplicationNumberTextMetaDataGet200Response.to_json())

# convert the object into a dict
api_v1_patent_applications_application_number_text_meta_data_get200_response_dict = api_v1_patent_applications_application_number_text_meta_data_get200_response_instance.to_dict()
# create an instance of ApiV1PatentApplicationsApplicationNumberTextMetaDataGet200Response from a dict
api_v1_patent_applications_application_number_text_meta_data_get200_response_from_dict = ApiV1PatentApplicationsApplicationNumberTextMetaDataGet200Response.from_dict(api_v1_patent_applications_application_number_text_meta_data_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


