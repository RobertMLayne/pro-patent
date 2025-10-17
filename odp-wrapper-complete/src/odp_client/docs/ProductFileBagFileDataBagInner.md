# ProductFileBagFileDataBagInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** |  | [optional] 
**file_size** | **float** |  | [optional] 
**file_data_from_date** | **date** |  | [optional] 
**file_data_to_date** | **date** |  | [optional] 
**file_type_text** | **str** |  | [optional] 
**file_download_uri** | **str** |  | [optional] 
**file_release_date** | **date** |  | [optional] 
**file_date** | **date** |  | [optional] 
**file_last_modified_date_time** | **date** |  | [optional] 

## Example

```python
from openapi_client.models.product_file_bag_file_data_bag_inner import ProductFileBagFileDataBagInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductFileBagFileDataBagInner from a JSON string
product_file_bag_file_data_bag_inner_instance = ProductFileBagFileDataBagInner.from_json(json)
# print the JSON string representation of the object
print(ProductFileBagFileDataBagInner.to_json())

# convert the object into a dict
product_file_bag_file_data_bag_inner_dict = product_file_bag_file_data_bag_inner_instance.to_dict()
# create an instance of ProductFileBagFileDataBagInner from a dict
product_file_bag_file_data_bag_inner_from_dict = ProductFileBagFileDataBagInner.from_dict(product_file_bag_file_data_bag_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


