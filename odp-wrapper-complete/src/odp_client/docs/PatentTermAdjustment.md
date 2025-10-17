# PatentTermAdjustment

Patent term adjustment data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_delay_quantity** | **int** | A delays quantity number of adjustments to the term of the patent based upon USPTO delays included in the PTA determination that is mailed as part of the ISSUE NOTIFICATION LETTER. | [optional] 
**adjustment_total_quantity** | **int** | Patent term adjustment total quantity number that is a summation of NONOVERLAPPING USPTO DELAYS (+/- PTO MANUAL ADJUSTMENTS) - APPLICANT DELAYS. | [optional] 
**applicant_day_delay_quantity** | **int** | Patent term adjustment applicant delays quantity number of the patent term due to the Applicant&#39;s failure to engage in reasonable efforts to conclude prosecution of the application for the cumulative period in excess of three | [optional] 
**b_delay_quantity** | **int** | B delays quantity number of adjustments to the term of the patent based upon the patent failing to issue within three years of the actual filing date of the application at the time that the issue notification letter is generated and an issue date has been established. | [optional] 
**c_delay_quantity** | **int** | C delays quantity number of adjustments to the term of the patent based upon USPTO delays caused by interference proceedings, secrecy orders, and successful appellate reviews. | [optional] 
**non_overlapping_day_quantity** | **float** | Patent term adjustment non overlapping days quantity number of overall summation of the USPTO delays minus any overlapping days. | [optional] 
**overlapping_day_quantity** | **float** | Patent term adjustment overlapping days quantity number that reflects the calculation of overlapping delays consistent with the federal circuit&#39;s interpretation. | [optional] 
**patent_term_adjustment_history_data_bag** | [**List[PatentTermAdjustmentPatentTermAdjustmentHistoryDataBagInner]**](PatentTermAdjustmentPatentTermAdjustmentHistoryDataBagInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.patent_term_adjustment import PatentTermAdjustment

# TODO update the JSON string below
json = "{}"
# create an instance of PatentTermAdjustment from a JSON string
patent_term_adjustment_instance = PatentTermAdjustment.from_json(json)
# print the JSON string representation of the object
print(PatentTermAdjustment.to_json())

# convert the object into a dict
patent_term_adjustment_dict = patent_term_adjustment_instance.to_dict()
# create an instance of PatentTermAdjustment from a dict
patent_term_adjustment_from_dict = PatentTermAdjustment.from_dict(patent_term_adjustment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


