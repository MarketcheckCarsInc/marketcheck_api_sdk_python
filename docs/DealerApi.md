# marketcheck_api_sdk.DealerApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dealer_search**](DealerApi.md#dealer_search) | **GET** /dealers | Find car dealers around
[**get_dealer**](DealerApi.md#get_dealer) | **GET** /dealer/{dealer_id} | Dealer by id
[**get_dealer_active_inventory**](DealerApi.md#get_dealer_active_inventory) | **GET** /dealer/{dealer_id}/active/inventory | Dealer inventory
[**get_dealer_historical_inventory**](DealerApi.md#get_dealer_historical_inventory) | **GET** /dealer/{dealer_id}/historical/inventory | Dealer&#39;s historical inventory
[**get_dealer_landing_page**](DealerApi.md#get_dealer_landing_page) | **GET** /dealer/{dealer_id}/landing | Experimental: Get cached version of dealer landing page by dealer id
[**get_dealer_ratings**](DealerApi.md#get_dealer_ratings) | **GET** /dealer/{dealer_id}/ratings | Dealer&#39;s Rating
[**get_dealer_reviews**](DealerApi.md#get_dealer_reviews) | **GET** /dealer/{dealer_id}/reviews | Dealer&#39;s Review


# **dealer_search**
> DealersResponse dealer_search(latitude, longitude, radius, api_key=api_key, rows=rows, start=start)

Find car dealers around

The dealers API returns a list of dealers around a given point and radius.

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.DealerApi()
latitude = 1.2 # float | Latitude component of location
longitude = 1.2 # float | Longitude component of location
radius = 56 # int | Radius around the search location
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)
rows = 8.14 # float | Number of results to return. Default is 10. Max is 50 (optional)
start = 8.14 # float | Offset for the search results. Default is 1. (optional)

try:
    # Find car dealers around
    api_response = api_instance.dealer_search(latitude, longitude, radius, api_key=api_key, rows=rows, start=start)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DealerApi->dealer_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latitude** | **float**| Latitude component of location | 
 **longitude** | **float**| Longitude component of location | 
 **radius** | **int**| Radius around the search location | 
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **rows** | **float**| Number of results to return. Default is 10. Max is 50 | [optional] 
 **start** | **float**| Offset for the search results. Default is 1. | [optional] 

### Return type

[**DealersResponse**](DealersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dealer**
> Dealer get_dealer(dealer_id, api_key=api_key)

Dealer by id

Get a particular dealer's information by its id

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.DealerApi()
dealer_id = 'dealer_id_example' # str | Dealer id to get all the dealer info attributes
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)

try:
    # Dealer by id
    api_response = api_instance.get_dealer(dealer_id, api_key=api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DealerApi->get_dealer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dealer_id** | **str**| Dealer id to get all the dealer info attributes | 
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 

### Return type

[**Dealer**](Dealer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = marketcheck_api_sdk.DealerApi()
dealer_id = 'dealer_id_example' # str | Id representing the dealer to fetch the active inventory for
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)
rows = 'rows_example' # str | Number of results to return. Default is 10. Max is 50 (optional)
start = 'start_example' # str | Page number to fetch the results for the given criteria. Default is 1. Pagination is allowed only till first 1000 results for the search and sort criteria. The page value can be only between 1 to 1000/rows (optional)

try:
    # Dealer inventory
    api_response = api_instance.get_dealer_active_inventory(dealer_id, api_key=api_key, rows=rows, start=start)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DealerApi->get_dealer_active_inventory: %s\n" % e)
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
api_instance = marketcheck_api_sdk.DealerApi()
dealer_id = 'dealer_id_example' # str | Id representing the dealer to fetch the active inventory for

try:
    # Dealer's historical inventory
    api_response = api_instance.get_dealer_historical_inventory(dealer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DealerApi->get_dealer_historical_inventory: %s\n" % e)
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

# **get_dealer_landing_page**
> DealerLandingPage get_dealer_landing_page(dealer_id, api_key=api_key)

Experimental: Get cached version of dealer landing page by dealer id

Experimental: Get cached version of dealer landing page by dealer id

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.DealerApi()
dealer_id = 'dealer_id_example' # str | Robot id to get the landing page html for
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)

try:
    # Experimental: Get cached version of dealer landing page by dealer id
    api_response = api_instance.get_dealer_landing_page(dealer_id, api_key=api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DealerApi->get_dealer_landing_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dealer_id** | **str**| Robot id to get the landing page html for | 
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 

### Return type

[**DealerLandingPage**](DealerLandingPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dealer_ratings**
> DealerRating get_dealer_ratings(dealer_id)

Dealer's Rating

[MOCK] Get a dealer's Rating

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.DealerApi()
dealer_id = 'dealer_id_example' # str | Id representing the dealer to fetch the ratings for

try:
    # Dealer's Rating
    api_response = api_instance.get_dealer_ratings(dealer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DealerApi->get_dealer_ratings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dealer_id** | **str**| Id representing the dealer to fetch the ratings for | 

### Return type

[**DealerRating**](DealerRating.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dealer_reviews**
> DealerReview get_dealer_reviews(dealer_id)

Dealer's Review

[MOCK] Get a dealer's Review

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.DealerApi()
dealer_id = 'dealer_id_example' # str | Id representing the dealer to fetch the ratings for

try:
    # Dealer's Review
    api_response = api_instance.get_dealer_reviews(dealer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DealerApi->get_dealer_reviews: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dealer_id** | **str**| Id representing the dealer to fetch the ratings for | 

### Return type

[**DealerReview**](DealerReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

