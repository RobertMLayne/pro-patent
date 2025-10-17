# PatentDataResponsePatentFileWrapperDataBagInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_number_text** | **str** | Free format of application number | [optional] 
**application_meta_data** | [**ApplicationMetaData**](ApplicationMetaData.md) |  | [optional] 
**correspondence_address_bag** | [**List[PatentDataResponsePatentFileWrapperDataBagInnerCorrespondenceAddressBagInner]**](PatentDataResponsePatentFileWrapperDataBagInnerCorrespondenceAddressBagInner.md) | Collection of correspondences | [optional] 
**assignment_bag** | [**List[Assignment]**](Assignment.md) |  | [optional] 
**record_attorney** | [**RecordAttorney**](RecordAttorney.md) |  | [optional] 
**foreign_priority_bag** | [**List[ForeignPriority]**](ForeignPriority.md) |  | [optional] 
**parent_continuity_bag** | [**List[ParentContinuityData]**](ParentContinuityData.md) |  | [optional] 
**child_continuity_bag** | [**List[ChildContinuityData]**](ChildContinuityData.md) |  | [optional] 
**patent_term_adjustment_data** | [**PatentTermAdjustment**](PatentTermAdjustment.md) |  | [optional] 
**event_data_bag** | [**List[EventData]**](EventData.md) |  | [optional] 
**pgpub_document_meta_data** | [**PGPubFileMetaData**](PGPubFileMetaData.md) |  | [optional] 
**grant_document_meta_data** | [**GrantFileMetaData**](GrantFileMetaData.md) |  | [optional] 
**last_ingestion_date_time** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.patent_data_response_patent_file_wrapper_data_bag_inner import PatentDataResponsePatentFileWrapperDataBagInner

# TODO update the JSON string below
json = "{}"
# create an instance of PatentDataResponsePatentFileWrapperDataBagInner from a JSON string
patent_data_response_patent_file_wrapper_data_bag_inner_instance = PatentDataResponsePatentFileWrapperDataBagInner.from_json(json)
# print the JSON string representation of the object
print(PatentDataResponsePatentFileWrapperDataBagInner.to_json())

# convert the object into a dict
patent_data_response_patent_file_wrapper_data_bag_inner_dict = patent_data_response_patent_file_wrapper_data_bag_inner_instance.to_dict()
# create an instance of PatentDataResponsePatentFileWrapperDataBagInner from a dict
patent_data_response_patent_file_wrapper_data_bag_inner_from_dict = PatentDataResponsePatentFileWrapperDataBagInner.from_dict(patent_data_response_patent_file_wrapper_data_bag_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


