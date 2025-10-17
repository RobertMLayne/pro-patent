# BulkDataProductBagInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_identifier** | **str** |  | [optional] 
**product_description_text** | **str** |  | [optional] 
**product_title_text** | **str** |  | [optional] 
**product_frequency_text** | **str** |  | [optional] 
**days_of_week_text** | **str** |  | [optional] 
**product_label_array_text** | **List[str]** |  | [optional] 
**product_data_set_array_text** | **List[str]** |  | [optional] 
**product_data_set_category_array_text** | **List[str]** |  | [optional] 
**product_from_date** | **date** |  | [optional] 
**product_to_date** | **date** |  | [optional] 
**product_total_file_size** | **float** |  | [optional] 
**product_file_total_quantity** | **float** |  | [optional] 
**last_modified_date_time** | **str** |  | [optional] 
**mime_type_identifier_array_text** | **List[str]** |  | [optional] 
**product_file_bag** | [**ProductFileBag**](ProductFileBag.md) |  | [optional] 

## Example

```python
from openapi_client.models.bulk_data_product_bag_inner import BulkDataProductBagInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDataProductBagInner from a JSON string
bulk_data_product_bag_inner_instance = BulkDataProductBagInner.from_json(json)
# print the JSON string representation of the object
print(BulkDataProductBagInner.to_json())

# convert the object into a dict
bulk_data_product_bag_inner_dict = bulk_data_product_bag_inner_instance.to_dict()
# create an instance of BulkDataProductBagInner from a dict
bulk_data_product_bag_inner_from_dict = BulkDataProductBagInner.from_dict(bulk_data_product_bag_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


