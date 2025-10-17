# Response404


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **object** |  | [optional] 
**error** | **object** |  | [optional] 
**error_details** | **object** |  | [optional] 
**request_identifier** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.response404 import Response404

# TODO update the JSON string below
json = "{}"
# create an instance of Response404 from a JSON string
response404_instance = Response404.from_json(json)
# print the JSON string representation of the object
print(Response404.to_json())

# convert the object into a dict
response404_dict = response404_instance.to_dict()
# create an instance of Response404 from a dict
response404_from_dict = Response404.from_dict(response404_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


