# AssignmentAssigneeBagInnerAssigneeAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line_one_text** | **str** |  | [optional] 
**address_line_two_text** | **str** |  | [optional] 
**city_name** | **str** |  | [optional] 
**geographic_region_name** | **str** |  | [optional] 
**geographic_region_code** | **str** |  | [optional] 
**country_name** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.assignment_assignee_bag_inner_assignee_address import AssignmentAssigneeBagInnerAssigneeAddress

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentAssigneeBagInnerAssigneeAddress from a JSON string
assignment_assignee_bag_inner_assignee_address_instance = AssignmentAssigneeBagInnerAssigneeAddress.from_json(json)
# print the JSON string representation of the object
print(AssignmentAssigneeBagInnerAssigneeAddress.to_json())

# convert the object into a dict
assignment_assignee_bag_inner_assignee_address_dict = assignment_assignee_bag_inner_assignee_address_instance.to_dict()
# create an instance of AssignmentAssigneeBagInnerAssigneeAddress from a dict
assignment_assignee_bag_inner_assignee_address_from_dict = AssignmentAssigneeBagInnerAssigneeAddress.from_dict(assignment_assignee_bag_inner_assignee_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


