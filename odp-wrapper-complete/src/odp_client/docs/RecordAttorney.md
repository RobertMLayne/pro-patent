# RecordAttorney

An attorney selected by the applicant or owner of an intellectual property to represent them before the national office.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_number_correspondence_data** | [**List[RecordAttorneyCustomerNumberCorrespondenceDataInner]**](RecordAttorneyCustomerNumberCorrespondenceDataInner.md) | Correspondence address of the application inherited from the customer. | [optional] 
**power_of_attorney_bag** | [**List[RecordAttorneyPowerOfAttorneyBagInner]**](RecordAttorneyPowerOfAttorneyBagInner.md) |  | [optional] 
**attorney_bag** | [**List[RecordAttorneyAttorneyBagInner]**](RecordAttorneyAttorneyBagInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.record_attorney import RecordAttorney

# TODO update the JSON string below
json = "{}"
# create an instance of RecordAttorney from a JSON string
record_attorney_instance = RecordAttorney.from_json(json)
# print the JSON string representation of the object
print(RecordAttorney.to_json())

# convert the object into a dict
record_attorney_dict = record_attorney_instance.to_dict()
# create an instance of RecordAttorney from a dict
record_attorney_from_dict = RecordAttorney.from_dict(record_attorney_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


