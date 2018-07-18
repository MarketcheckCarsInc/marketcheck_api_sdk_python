# marketcheck_api_sdk.HistoryApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**history**](HistoryApi.md#history) | **GET** /history/{vin} | Get a cars online listing history


# **history**
> list[HistoricalListing] history(vin, api_key=api_key, fields=fields, page=page)

Get a cars online listing history

The history API returns online listing history for a car identified by its VIN. History listings are sorted in the descending order of the listing date / last seen date

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.HistoryApi()
vin = 'vin_example' # str | The VIN to identify the car to fetch the listing history. Must be a valid 17 char VIN
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)
fields = 'fields_example' # str | List of fields to fetch, in case the default fields list in the response is to be trimmed down (optional)
page = 8.14 # float | Page number to fetch the results for the given criteria. Default is 1. (optional)

try:
    # Get a cars online listing history
    api_response = api_instance.history(vin, api_key=api_key, fields=fields, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HistoryApi->history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vin** | **str**| The VIN to identify the car to fetch the listing history. Must be a valid 17 char VIN | 
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **fields** | **str**| List of fields to fetch, in case the default fields list in the response is to be trimmed down | [optional] 
 **page** | **float**| Page number to fetch the results for the given criteria. Default is 1. | [optional] 

### Return type

[**list[HistoricalListing]**](HistoricalListing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

