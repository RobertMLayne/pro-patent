# Status413


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**detailed_message** | **str** |  | [optional] 
**request_identifier** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.status413 import Status413

# TODO update the JSON string below
json = "{}"
# create an instance of Status413 from a JSON string
status413_instance = Status413.from_json(json)
# print the JSON string representation of the object
print(Status413.to_json())

# convert the object into a dict
status413_dict = status413_instance.to_dict()
# create an instance of Status413 from a dict
status413_from_dict = Status413.from_dict(status413_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


