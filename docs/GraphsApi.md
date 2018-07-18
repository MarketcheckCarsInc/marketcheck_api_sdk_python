# marketcheck_api_sdk.GraphsApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_price_miles_plot_data**](GraphsApi.md#get_price_miles_plot_data) | **GET** /plots | Price, Miles plots data for given criteria


# **get_price_miles_plot_data**
> list[PlotPoint] get_price_miles_plot_data(car_type, api_key=api_key, vin=vin, year=year, make=make, model=model, trim=trim, rows=rows)

Price, Miles plots data for given criteria

[DEPRECIATED Please check this in /search API using plot=true]Get price, miles plot data for active cars matching the given VIN's basic specification or Year, Make, Model, Trim (Optional) criteria

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.GraphsApi()
car_type = 'car_type_example' # str | Car type to get the scatter plot data for
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)
vin = 'vin_example' # str | VIN as a reference to the type of car for which plot data is to be returned (optional)
year = 'year_example' # str | Year of the car (optional)
make = 'make_example' # str | Make of the car (optional)
model = 'model_example' # str | Model of the Car (optional)
trim = 'trim_example' # str | Trim of the Car (optional)
rows = 'rows_example' # str | Number of results to return. Default is 1000. Max is 10000 (optional)

try:
    # Price, Miles plots data for given criteria
    api_response = api_instance.get_price_miles_plot_data(car_type, api_key=api_key, vin=vin, year=year, make=make, model=model, trim=trim, rows=rows)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphsApi->get_price_miles_plot_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_type** | **str**| Car type to get the scatter plot data for | 
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **vin** | **str**| VIN as a reference to the type of car for which plot data is to be returned | [optional] 
 **year** | **str**| Year of the car | [optional] 
 **make** | **str**| Make of the car | [optional] 
 **model** | **str**| Model of the Car | [optional] 
 **trim** | **str**| Trim of the Car | [optional] 
 **rows** | **str**| Number of results to return. Default is 1000. Max is 10000 | [optional] 

### Return type

[**list[PlotPoint]**](PlotPoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

