# Assignment

The collection of national assignments related to a patent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reel_number** | **str** | 1-6 digit number identifies the reel number to be used to locate the assignment on microfilm. | [optional] 
**frame_number** | **str** | 1-4 digit number that identifies the frame number to be used to locate the first image(page) of the assignment on microfilm. | [optional] 
**reel_and_frame_number** | **str** |  | [optional] 
**page_total_quantity** | **int** |  | [optional] 
**assignment_document_location_uri** | **str** |  | [optional] 
**assignment_received_date** | **str** |  | [optional] 
**assignment_recorded_date** | **str** |  | [optional] 
**assignment_mailed_date** | **str** | The date an assignment request was mailed to the office or received by the office | [optional] 
**conveyance_text** | **str** | A description of the nature of the interest conveyed or transaction to be recorded in an assignment. Examples of the types of descriptions &#x60;include:&#x60; assignment, security agreement, merger, change of name, license, foreclosure, lien, | [optional] 
**assignor_bag** | [**List[AssignmentAssignorBagInner]**](AssignmentAssignorBagInner.md) |  | [optional] 
**assignee_bag** | [**List[AssignmentAssigneeBagInner]**](AssignmentAssigneeBagInner.md) |  | [optional] 
**correspondence_address_bag** | [**List[AssignmentCorrespondenceAddressBagInner]**](AssignmentCorrespondenceAddressBagInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.assignment import Assignment

# TODO update the JSON string below
json = "{}"
# create an instance of Assignment from a JSON string
assignment_instance = Assignment.from_json(json)
# print the JSON string representation of the object
print(Assignment.to_json())

# convert the object into a dict
assignment_dict = assignment_instance.to_dict()
# create an instance of Assignment from a dict
assignment_from_dict = Assignment.from_dict(assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


