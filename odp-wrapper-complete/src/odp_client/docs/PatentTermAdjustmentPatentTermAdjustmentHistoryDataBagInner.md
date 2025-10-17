# PatentTermAdjustmentPatentTermAdjustmentHistoryDataBagInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_date** | **str** | The date that the symbol was assigned to the patent document | [optional] 
**applicant_day_delay_quantity** | **int** |  | [optional] 
**event_description_text** | **str** |  | [optional] 
**event_sequence_number** | **float** |  | [optional] 
**ip_office_day_delay_quantity** | **int** | Number of days the UPSTO personnel adjusting the calculation to increase or decrease the patent term adjustment based upon a request for reconsideration of the patent term adjustment. | [optional] 
**originating_event_sequence_number** | **float** |  | [optional] 
**pta_pte_code** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.patent_term_adjustment_patent_term_adjustment_history_data_bag_inner import PatentTermAdjustmentPatentTermAdjustmentHistoryDataBagInner

# TODO update the JSON string below
json = "{}"
# create an instance of PatentTermAdjustmentPatentTermAdjustmentHistoryDataBagInner from a JSON string
patent_term_adjustment_patent_term_adjustment_history_data_bag_inner_instance = PatentTermAdjustmentPatentTermAdjustmentHistoryDataBagInner.from_json(json)
# print the JSON string representation of the object
print(PatentTermAdjustmentPatentTermAdjustmentHistoryDataBagInner.to_json())

# convert the object into a dict
patent_term_adjustment_patent_term_adjustment_history_data_bag_inner_dict = patent_term_adjustment_patent_term_adjustment_history_data_bag_inner_instance.to_dict()
# create an instance of PatentTermAdjustmentPatentTermAdjustmentHistoryDataBagInner from a dict
patent_term_adjustment_patent_term_adjustment_history_data_bag_inner_from_dict = PatentTermAdjustmentPatentTermAdjustmentHistoryDataBagInner.from_dict(patent_term_adjustment_patent_term_adjustment_history_data_bag_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


