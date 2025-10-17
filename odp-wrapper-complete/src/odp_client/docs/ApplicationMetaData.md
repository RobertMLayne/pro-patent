# ApplicationMetaData

Represents patent application meta data properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**national_stage_indicator** | **bool** | Indicates whether this application is a national application which entered the national stage from an international PCT application | [optional] 
**entity_status_data** | [**ApplicationMetaDataEntityStatusData**](ApplicationMetaDataEntityStatusData.md) |  | [optional] 
**publication_date_bag** | **List[str]** |  | [optional] 
**publication_sequence_number_bag** | **List[str]** |  | [optional] 
**publication_category_bag** | **List[str]** |  | [optional] 
**docket_number** | **str** |  | [optional] 
**first_inventor_to_file_indicator** | **str** |  | [optional] 
**first_applicant_name** | **str** |  | [optional] 
**first_inventor_name** | **str** |  | [optional] 
**application_confirmation_number** | **str** |  | [optional] 
**application_status_date** | **str** |  | [optional] 
**application_status_description_text** | **str** |  | [optional] 
**filing_date** | **str** | The date assigned by the Patent Office that identifies when an application meets certain criteria to qualify as having been filed. Refers to ST.9 INID Code 22. | [optional] 
**effective_filing_date** | **str** | The date according to PTO criteria that the patent case qualified as having been &#39;filed&#39;.  The effective filing date is the same or later than the Filing Date.  The filing date can be changed due to a subsequent action on an application patent case. | [optional] 
**grant_date** | **str** |  | [optional] 
**group_art_unit_number** | **str** | GAU Code | [optional] 
**application_type_code** | **str** | Code corresponding to Utility, Plant, Design, or Reissue | [optional] 
**application_type_label_name** | **str** |  | [optional] 
**application_type_category** | **str** |  | [optional] 
**invention_title** | **str** |  | [optional] 
**patent_number** | **str** |  | [optional] 
**application_status_code** | **int** |  | [optional] 
**earliest_publication_number** | **str** | Publication number corresponding to the earliest publication | [optional] 
**earliest_publication_date** | **str** |  | [optional] 
**pct_publication_number** | **str** | The unique identifier assigned to the publication of an international patent application in the PCT Gazette by the International Bureau (IB) of the World Intellectual Property Organization (WIPO). | [optional] 
**pct_publication_date** | **str** |  | [optional] 
**international_registration_publication_date** | **str** | The date that the IPR is published by the International Bureau | [optional] 
**international_registration_number** | **str** | The number assigned by the International Bureau to an international registration upon registering an industrial design, a trademark or other type of IPR in the International Register | [optional] 
**examiner_name_text** | **str** | Name of patent examiner | [optional] 
**var_class** | **str** | The first hierarchical level in the USPC classification schedule | [optional] 
**subclass** | **str** | The second highest hierarchical level  in the USP C classification schedule | [optional] 
**uspc_symbol_text** | **str** | The first hierarchical level in the USPC classification schedule/ The second highest hierarchical level in the USP C classification schedule | [optional] 
**customer_number** | **int** | Correspondence address of the application inherited from the customer. | [optional] 
**cpc_classification_bag** | **List[str]** | Collection of Classifications for CPC | [optional] 
**applicant_bag** | [**List[ApplicationMetaDataApplicantBagInner]**](ApplicationMetaDataApplicantBagInner.md) |  | [optional] 
**inventor_bag** | [**List[ApplicationMetaDataInventorBagInner]**](ApplicationMetaDataInventorBagInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.application_meta_data import ApplicationMetaData

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationMetaData from a JSON string
application_meta_data_instance = ApplicationMetaData.from_json(json)
# print the JSON string representation of the object
print(ApplicationMetaData.to_json())

# convert the object into a dict
application_meta_data_dict = application_meta_data_instance.to_dict()
# create an instance of ApplicationMetaData from a dict
application_meta_data_from_dict = ApplicationMetaData.from_dict(application_meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


