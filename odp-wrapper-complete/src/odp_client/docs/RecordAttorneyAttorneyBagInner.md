# RecordAttorneyAttorneyBagInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**name_prefix** | **str** |  | [optional] 
**name_suffix** | **str** |  | [optional] 
**registration_number** | **str** |  | [optional] 
**active_indicator** | **str** |  | [optional] 
**registered_practitioner_category** | **str** |  | [optional] 
**attorney_address_bag** | [**List[RecordAttorneyAttorneyBagInnerAttorneyAddressBagInner]**](RecordAttorneyAttorneyBagInnerAttorneyAddressBagInner.md) |  | [optional] 
**telecommunication_address_bag** | [**List[RecordAttorneyPowerOfAttorneyBagInnerTelecommunicationAddressBagInner]**](RecordAttorneyPowerOfAttorneyBagInnerTelecommunicationAddressBagInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.record_attorney_attorney_bag_inner import RecordAttorneyAttorneyBagInner

# TODO update the JSON string below
json = "{}"
# create an instance of RecordAttorneyAttorneyBagInner from a JSON string
record_attorney_attorney_bag_inner_instance = RecordAttorneyAttorneyBagInner.from_json(json)
# print the JSON string representation of the object
print(RecordAttorneyAttorneyBagInner.to_json())

# convert the object into a dict
record_attorney_attorney_bag_inner_dict = record_attorney_attorney_bag_inner_instance.to_dict()
# create an instance of RecordAttorneyAttorneyBagInner from a dict
record_attorney_attorney_bag_inner_from_dict = RecordAttorneyAttorneyBagInner.from_dict(record_attorney_attorney_bag_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


