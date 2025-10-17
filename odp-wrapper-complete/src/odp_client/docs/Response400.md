# Response400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **object** |  | [optional] 
**error** | **object** |  | [optional] 
**error_details** | **object** |  | [optional] 
**request_identifier** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.response400 import Response400

# TODO update the JSON string below
json = "{}"
# create an instance of Response400 from a JSON string
response400_instance = Response400.from_json(json)
# print the JSON string representation of the object
print(Response400.to_json())

# convert the object into a dict
response400_dict = response400_instance.to_dict()
# create an instance of Response400 from a dict
response400_from_dict = Response400.from_dict(response400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


