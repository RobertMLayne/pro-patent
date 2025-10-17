# PatentDataResponseFacetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_status_code** | [**List[PatentDataResponseFacetsInnerApplicationStatusCodeInner]**](PatentDataResponseFacetsInnerApplicationStatusCodeInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.patent_data_response_facets_inner import PatentDataResponseFacetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PatentDataResponseFacetsInner from a JSON string
patent_data_response_facets_inner_instance = PatentDataResponseFacetsInner.from_json(json)
# print the JSON string representation of the object
print(PatentDataResponseFacetsInner.to_json())

# convert the object into a dict
patent_data_response_facets_inner_dict = patent_data_response_facets_inner_instance.to_dict()
# create an instance of PatentDataResponseFacetsInner from a dict
patent_data_response_facets_inner_from_dict = PatentDataResponseFacetsInner.from_dict(patent_data_response_facets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


