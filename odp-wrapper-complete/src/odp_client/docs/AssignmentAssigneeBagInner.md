# AssignmentAssigneeBagInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignee_name_text** | **str** |  | [optional] 
**assignee_address** | [**AssignmentAssigneeBagInnerAssigneeAddress**](AssignmentAssigneeBagInnerAssigneeAddress.md) |  | [optional] 

## Example

```python
from openapi_client.models.assignment_assignee_bag_inner import AssignmentAssigneeBagInner

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentAssigneeBagInner from a JSON string
assignment_assignee_bag_inner_instance = AssignmentAssigneeBagInner.from_json(json)
# print the JSON string representation of the object
print(AssignmentAssigneeBagInner.to_json())

# convert the object into a dict
assignment_assignee_bag_inner_dict = assignment_assignee_bag_inner_instance.to_dict()
# create an instance of AssignmentAssigneeBagInner from a dict
assignment_assignee_bag_inner_from_dict = AssignmentAssigneeBagInner.from_dict(assignment_assignee_bag_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


