# RecordAttorneyCustomerNumberCorrespondenceDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patron_identifier** | **float** |  | [optional] 
**organization_standard_name** | **str** |  | [optional] 
**power_of_attorney_address_bag** | [**List[RecordAttorneyCustomerNumberCorrespondenceDataInnerPowerOfAttorneyAddressBagInner]**](RecordAttorneyCustomerNumberCorrespondenceDataInnerPowerOfAttorneyAddressBagInner.md) |  | [optional] 
**telecommunication_address_bag** | [**List[RecordAttorneyCustomerNumberCorrespondenceDataInnerTelecommunicationAddressBagInner]**](RecordAttorneyCustomerNumberCorrespondenceDataInnerTelecommunicationAddressBagInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.record_attorney_customer_number_correspondence_data_inner import RecordAttorneyCustomerNumberCorrespondenceDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of RecordAttorneyCustomerNumberCorrespondenceDataInner from a JSON string
record_attorney_customer_number_correspondence_data_inner_instance = RecordAttorneyCustomerNumberCorrespondenceDataInner.from_json(json)
# print the JSON string representation of the object
print(RecordAttorneyCustomerNumberCorrespondenceDataInner.to_json())

# convert the object into a dict
record_attorney_customer_number_correspondence_data_inner_dict = record_attorney_customer_number_correspondence_data_inner_instance.to_dict()
# create an instance of RecordAttorneyCustomerNumberCorrespondenceDataInner from a dict
record_attorney_customer_number_correspondence_data_inner_from_dict = RecordAttorneyCustomerNumberCorrespondenceDataInner.from_dict(record_attorney_customer_number_correspondence_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


