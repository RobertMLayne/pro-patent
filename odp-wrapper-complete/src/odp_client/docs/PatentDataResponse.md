# PatentDataResponse

This json structure represents all data fields possible for a patent application. Not all fields mentioned here will be returned in API response, only fields that have data should present in the response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**patent_file_wrapper_data_bag** | [**List[PatentDataResponsePatentFileWrapperDataBagInner]**](PatentDataResponsePatentFileWrapperDataBagInner.md) |  | [optional] 
**facets** | [**List[PatentDataResponseFacetsInner]**](PatentDataResponseFacetsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.patent_data_response import PatentDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PatentDataResponse from a JSON string
patent_data_response_instance = PatentDataResponse.from_json(json)
# print the JSON string representation of the object
print(PatentDataResponse.to_json())

# convert the object into a dict
patent_data_response_dict = patent_data_response_instance.to_dict()
# create an instance of PatentDataResponse from a dict
patent_data_response_from_dict = PatentDataResponse.from_dict(patent_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


