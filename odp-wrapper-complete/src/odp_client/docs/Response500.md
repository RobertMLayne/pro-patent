# Response500

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **object** |  | [optional]
**error** | **object** |  | [optional]
**error_details** | **object** |  | [optional]
**request_identifier** | **object** |  | [optional]

## Example

```python
from openapi_client.models.response500 import Response500

# TODO update the JSON string below
json = "{}"
# create an instance of Response500 from a JSON string
response500_instance = Response500.from_json(json)
# print the JSON string representation of the object
print(Response500.to_json())

# convert the object into a dict
response500_dict = response500_instance.to_dict()
# create an instance of Response500 from a dict
response500_from_dict = Response500.from_dict(response500_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
