# ProductFileBag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**file_data_bag** | [**List[ProductFileBagFileDataBagInner]**](ProductFileBagFileDataBagInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.product_file_bag import ProductFileBag

# TODO update the JSON string below
json = "{}"
# create an instance of ProductFileBag from a JSON string
product_file_bag_instance = ProductFileBag.from_json(json)
# print the JSON string representation of the object
print(ProductFileBag.to_json())

# convert the object into a dict
product_file_bag_dict = product_file_bag_instance.to_dict()
# create an instance of ProductFileBag from a dict
product_file_bag_from_dict = ProductFileBag.from_dict(product_file_bag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


