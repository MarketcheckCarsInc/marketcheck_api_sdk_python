# marketcheck_api_sdk.InventoryApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dealer_active_inventory**](InventoryApi.md#get_dealer_active_inventory) | **GET** /dealer/{dealer_id}/active/inventory | Dealer inventory
[**get_dealer_historical_inventory**](InventoryApi.md#get_dealer_historical_inventory) | **GET** /dealer/{dealer_id}/historical/inventory | Dealer&#39;s historical inventory


# **get_dealer_active_inventory**
> BaseListing get_dealer_active_inventory(dealer_id, api_key=api_key, rows=rows, start=start)

Dealer inventory

Get a dealer's currently active inventory

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.InventoryApi()
dealer_id = 'dealer_id_example' # str | Id representing the dealer to fetch the active inventory for
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)
rows = 'rows_example' # str | Number of results to return. Default is 10. Max is 50 (optional)
start = 'start_example' # str | Page number to fetch the results for the given criteria. Default is 1. Pagination is allowed only till first 1000 results for the search and sort criteria. The page value can be only between 1 to 1000/rows (optional)

try:
    # Dealer inventory
    api_response = api_instance.get_dealer_active_inventory(dealer_id, api_key=api_key, rows=rows, start=start)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryApi->get_dealer_active_inventory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dealer_id** | **str**| Id representing the dealer to fetch the active inventory for | 
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **rows** | **str**| Number of results to return. Default is 10. Max is 50 | [optional] 
 **start** | **str**| Page number to fetch the results for the given criteria. Default is 1. Pagination is allowed only till first 1000 results for the search and sort criteria. The page value can be only between 1 to 1000/rows | [optional] 

### Return type

[**BaseListing**](BaseListing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dealer_historical_inventory**
> BaseListing get_dealer_historical_inventory(dealer_id)

Dealer's historical inventory

[v1 : Not Implemented Yet] - Get a dealer's historical inventory

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.InventoryApi()
dealer_id = 'dealer_id_example' # str | Id representing the dealer to fetch the active inventory for

try:
    # Dealer's historical inventory
    api_response = api_instance.get_dealer_historical_inventory(dealer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryApi->get_dealer_historical_inventory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dealer_id** | **str**| Id representing the dealer to fetch the active inventory for | 

### Return type

[**BaseListing**](BaseListing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

