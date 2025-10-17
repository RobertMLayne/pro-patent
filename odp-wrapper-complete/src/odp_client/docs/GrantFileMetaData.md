# GrantFileMetaData

Contains patent grant zip and xml file meta data for an application

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zip_file_name** | **str** |  | [optional] 
**product_identifier** | **str** |  | [optional] 
**file_location_uri** | **str** |  | [optional] 
**file_create_date_time** | **str** |  | [optional] 
**xml_file_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.grant_file_meta_data import GrantFileMetaData

# TODO update the JSON string below
json = "{}"
# create an instance of GrantFileMetaData from a JSON string
grant_file_meta_data_instance = GrantFileMetaData.from_json(json)
# print the JSON string representation of the object
print(GrantFileMetaData.to_json())

# convert the object into a dict
grant_file_meta_data_dict = grant_file_meta_data_instance.to_dict()
# create an instance of GrantFileMetaData from a dict
grant_file_meta_data_from_dict = GrantFileMetaData.from_dict(grant_file_meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


