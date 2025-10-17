# ApplicationMetaDataApplicantBagInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicant_name_text** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**preferred_name** | **str** |  | [optional] 
**name_prefix** | **str** |  | [optional] 
**name_suffix** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**correspondence_address_bag** | [**List[ApplicationMetaDataApplicantBagInnerCorrespondenceAddressBagInner]**](ApplicationMetaDataApplicantBagInnerCorrespondenceAddressBagInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.application_meta_data_applicant_bag_inner import ApplicationMetaDataApplicantBagInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationMetaDataApplicantBagInner from a JSON string
application_meta_data_applicant_bag_inner_instance = ApplicationMetaDataApplicantBagInner.from_json(json)
# print the JSON string representation of the object
print(ApplicationMetaDataApplicantBagInner.to_json())

# convert the object into a dict
application_meta_data_applicant_bag_inner_dict = application_meta_data_applicant_bag_inner_instance.to_dict()
# create an instance of ApplicationMetaDataApplicantBagInner from a dict
application_meta_data_applicant_bag_inner_from_dict = ApplicationMetaDataApplicantBagInner.from_dict(application_meta_data_applicant_bag_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


