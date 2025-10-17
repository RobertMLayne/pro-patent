# PetitionDecisionDocumentDownloadOptionBagInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mime_type_identifier** | **str** |  | [optional] 
**document_uri** | **str** |  | [optional] 
**page_total_quantity** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.petition_decision_document_download_option_bag_inner import PetitionDecisionDocumentDownloadOptionBagInner

# TODO update the JSON string below
json = "{}"
# create an instance of PetitionDecisionDocumentDownloadOptionBagInner from a JSON string
petition_decision_document_download_option_bag_inner_instance = PetitionDecisionDocumentDownloadOptionBagInner.from_json(json)
# print the JSON string representation of the object
print(PetitionDecisionDocumentDownloadOptionBagInner.to_json())

# convert the object into a dict
petition_decision_document_download_option_bag_inner_dict = petition_decision_document_download_option_bag_inner_instance.to_dict()
# create an instance of PetitionDecisionDocumentDownloadOptionBagInner from a dict
petition_decision_document_download_option_bag_inner_from_dict = PetitionDecisionDocumentDownloadOptionBagInner.from_dict(petition_decision_document_download_option_bag_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


