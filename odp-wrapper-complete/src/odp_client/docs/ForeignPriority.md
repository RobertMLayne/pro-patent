# ForeignPriority


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_office_name** | **str** |  | [optional] 
**filing_date** | **str** |  | [optional] 
**application_number_text** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.foreign_priority import ForeignPriority

# TODO update the JSON string below
json = "{}"
# create an instance of ForeignPriority from a JSON string
foreign_priority_instance = ForeignPriority.from_json(json)
# print the JSON string representation of the object
print(ForeignPriority.to_json())

# convert the object into a dict
foreign_priority_dict = foreign_priority_instance.to_dict()
# create an instance of ForeignPriority from a dict
foreign_priority_from_dict = ForeignPriority.from_dict(foreign_priority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


