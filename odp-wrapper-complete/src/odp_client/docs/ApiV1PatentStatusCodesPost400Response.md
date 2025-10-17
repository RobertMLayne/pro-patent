# ApiV1PatentStatusCodesPost400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **object** |  | [optional] 
**error** | **object** |  | [optional] 
**error_details** | **object** |  | [optional] 
**request_identifier** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.api_v1_patent_status_codes_post400_response import ApiV1PatentStatusCodesPost400Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PatentStatusCodesPost400Response from a JSON string
api_v1_patent_status_codes_post400_response_instance = ApiV1PatentStatusCodesPost400Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1PatentStatusCodesPost400Response.to_json())

# convert the object into a dict
api_v1_patent_status_codes_post400_response_dict = api_v1_patent_status_codes_post400_response_instance.to_dict()
# create an instance of ApiV1PatentStatusCodesPost400Response from a dict
api_v1_patent_status_codes_post400_response_from_dict = ApiV1PatentStatusCodesPost400Response.from_dict(api_v1_patent_status_codes_post400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


