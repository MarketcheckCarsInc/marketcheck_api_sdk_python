# marketcheck_api_sdk.FacetsApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_facets**](FacetsApi.md#get_facets) | **GET** /facets | Facets


# **get_facets**
> list[FacetItem] get_facets(fields, api_key=api_key, vin=vin, year=year, make=make, model=model, trim=trim)

Facets

[Merged with the /search API - Please check the 'facets' parameter to the Search API above] Get the facets for the given simple filter criteria (by given VIN's basic specification, Or by Year, Make, Model, Trim criteria) and facet fields

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.FacetsApi()
fields = 'fields_example' # str | Comma separated list of fields to generate facets for. Supported fields are - year, make, model, trim, exterior_color, interior_color, drivetrain, vehicle_type, car_type, body_style, body_subtype, doors
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)
vin = 'vin_example' # str | VIN as a reference to the type of car for which facets data is to be returned (optional)
year = 'year_example' # str | Year of the car (optional)
make = 'make_example' # str | Make of the car (optional)
model = 'model_example' # str | Model of the Car (optional)
trim = 'trim_example' # str | Trim of the Car (optional)

try:
    # Facets
    api_response = api_instance.get_facets(fields, api_key=api_key, vin=vin, year=year, make=make, model=model, trim=trim)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacetsApi->get_facets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma separated list of fields to generate facets for. Supported fields are - year, make, model, trim, exterior_color, interior_color, drivetrain, vehicle_type, car_type, body_style, body_subtype, doors | 
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **vin** | **str**| VIN as a reference to the type of car for which facets data is to be returned | [optional] 
 **year** | **str**| Year of the car | [optional] 
 **make** | **str**| Make of the car | [optional] 
 **model** | **str**| Model of the Car | [optional] 
 **trim** | **str**| Trim of the Car | [optional] 

### Return type

[**list[FacetItem]**](FacetItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

