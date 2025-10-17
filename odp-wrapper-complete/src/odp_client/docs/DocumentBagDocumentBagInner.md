# DocumentBagDocumentBagInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_number_text** | **str** |  | [optional] 
**official_date** | **str** |  | [optional] 
**document_identifier** | **str** |  | [optional] 
**document_code** | **str** |  | [optional] 
**document_code_description_text** | **str** |  | [optional] 
**document_direction_category** | **str** |  | [optional] 
**download_option_bag** | [**List[DocumentBagDocumentBagInnerDownloadOptionBagInner]**](DocumentBagDocumentBagInnerDownloadOptionBagInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.document_bag_document_bag_inner import DocumentBagDocumentBagInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentBagDocumentBagInner from a JSON string
document_bag_document_bag_inner_instance = DocumentBagDocumentBagInner.from_json(json)
# print the JSON string representation of the object
print(DocumentBagDocumentBagInner.to_json())

# convert the object into a dict
document_bag_document_bag_inner_dict = document_bag_document_bag_inner_instance.to_dict()
# create an instance of DocumentBagDocumentBagInner from a dict
document_bag_document_bag_inner_from_dict = DocumentBagDocumentBagInner.from_dict(document_bag_document_bag_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


