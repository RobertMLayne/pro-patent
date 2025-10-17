# BdssResponseProductBag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**bulk_data_product_bag** | **List[List[BulkDataProductBagInner]]** |  | [optional] 

## Example

```python
from openapi_client.models.bdss_response_product_bag import BdssResponseProductBag

# TODO update the JSON string below
json = "{}"
# create an instance of BdssResponseProductBag from a JSON string
bdss_response_product_bag_instance = BdssResponseProductBag.from_json(json)
# print the JSON string representation of the object
print(BdssResponseProductBag.to_json())

# convert the object into a dict
bdss_response_product_bag_dict = bdss_response_product_bag_instance.to_dict()
# create an instance of BdssResponseProductBag from a dict
bdss_response_product_bag_from_dict = BdssResponseProductBag.from_dict(bdss_response_product_bag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


