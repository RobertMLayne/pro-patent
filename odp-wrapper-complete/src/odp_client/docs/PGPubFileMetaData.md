# PGPubFileMetaData

Contains pgpub zip and xml file meta data for an application

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
from openapi_client.models.pg_pub_file_meta_data import PGPubFileMetaData

# TODO update the JSON string below
json = "{}"
# create an instance of PGPubFileMetaData from a JSON string
pg_pub_file_meta_data_instance = PGPubFileMetaData.from_json(json)
# print the JSON string representation of the object
print(PGPubFileMetaData.to_json())

# convert the object into a dict
pg_pub_file_meta_data_dict = pg_pub_file_meta_data_instance.to_dict()
# create an instance of PGPubFileMetaData from a dict
pg_pub_file_meta_data_from_dict = PGPubFileMetaData.from_dict(pg_pub_file_meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


