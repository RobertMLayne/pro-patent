# ApplicationMetaDataInventorBagInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**name_prefix** | **str** |  | [optional] 
**name_suffix** | **str** |  | [optional] 
**preferred_name** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**inventor_name_text** | **str** |  | [optional] 
**correspondence_address_bag** | [**List[ApplicationMetaDataInventorBagInnerCorrespondenceAddressBagInner]**](ApplicationMetaDataInventorBagInnerCorrespondenceAddressBagInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.application_meta_data_inventor_bag_inner import ApplicationMetaDataInventorBagInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationMetaDataInventorBagInner from a JSON string
application_meta_data_inventor_bag_inner_instance = ApplicationMetaDataInventorBagInner.from_json(json)
# print the JSON string representation of the object
print(ApplicationMetaDataInventorBagInner.to_json())

# convert the object into a dict
application_meta_data_inventor_bag_inner_dict = application_meta_data_inventor_bag_inner_instance.to_dict()
# create an instance of ApplicationMetaDataInventorBagInner from a dict
application_meta_data_inventor_bag_inner_from_dict = ApplicationMetaDataInventorBagInner.from_dict(application_meta_data_inventor_bag_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


