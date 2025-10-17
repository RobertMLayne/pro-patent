# ApplicationMetaDataEntityStatusData

Indicates the applicant's entity status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**small_entity_status_indicator** | **bool** | Indicates whether the applicant qualifies for small entity status | [optional] 
**business_entity_status_category** | **str** | Status of business entity being established for the purpose of paying a fee such as a filing fee and a maintenance fee | [optional] 

## Example

```python
from openapi_client.models.application_meta_data_entity_status_data import ApplicationMetaDataEntityStatusData

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationMetaDataEntityStatusData from a JSON string
application_meta_data_entity_status_data_instance = ApplicationMetaDataEntityStatusData.from_json(json)
# print the JSON string representation of the object
print(ApplicationMetaDataEntityStatusData.to_json())

# convert the object into a dict
application_meta_data_entity_status_data_dict = application_meta_data_entity_status_data_instance.to_dict()
# create an instance of ApplicationMetaDataEntityStatusData from a dict
application_meta_data_entity_status_data_from_dict = ApplicationMetaDataEntityStatusData.from_dict(application_meta_data_entity_status_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


