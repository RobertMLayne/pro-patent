# Facets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_label_array_text** | [**List[FacetsProductLabelArrayTextInner]**](FacetsProductLabelArrayTextInner.md) |  | [optional] 
**product_data_set_array_text** | [**List[FacetsProductDataSetArrayTextInner]**](FacetsProductDataSetArrayTextInner.md) |  | [optional] 
**product_category_array_text** | [**List[FacetsProductCategoryArrayTextInner]**](FacetsProductCategoryArrayTextInner.md) |  | [optional] 
**mime_type_identifier_array_text** | [**List[FacetsMimeTypeIdentifierArrayTextInner]**](FacetsMimeTypeIdentifierArrayTextInner.md) |  | [optional] 
**product_frequency_array_text** | [**List[FacetsProductFrequencyArrayTextInner]**](FacetsProductFrequencyArrayTextInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.facets import Facets

# TODO update the JSON string below
json = "{}"
# create an instance of Facets from a JSON string
facets_instance = Facets.from_json(json)
# print the JSON string representation of the object
print(Facets.to_json())

# convert the object into a dict
facets_dict = facets_instance.to_dict()
# create an instance of Facets from a dict
facets_from_dict = Facets.from_dict(facets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


