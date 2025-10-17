# PatentDownloadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**q** | **str** | Search by field value or pass opensearch string query syntax | [optional] 
**filters** | [**List[Filter]**](Filter.md) |  | [optional] 
**range_filters** | [**List[Range]**](Range.md) |  | [optional] 
**sort** | [**List[Sort]**](Sort.md) |  | [optional] 
**fields** | **List[str]** |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**format** | **str** | Download format. csv or json | [optional] 

## Example

```python
from openapi_client.models.patent_download_request import PatentDownloadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatentDownloadRequest from a JSON string
patent_download_request_instance = PatentDownloadRequest.from_json(json)
# print the JSON string representation of the object
print(PatentDownloadRequest.to_json())

# convert the object into a dict
patent_download_request_dict = patent_download_request_instance.to_dict()
# create an instance of PatentDownloadRequest from a dict
patent_download_request_from_dict = PatentDownloadRequest.from_dict(patent_download_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


