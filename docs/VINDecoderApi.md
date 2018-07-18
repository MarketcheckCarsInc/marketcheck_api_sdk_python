# marketcheck_api_sdk.VINDecoderApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**decode**](VINDecoderApi.md#decode) | **GET** /vin/{vin}/specs | VIN Decoder
[**get_economy**](VINDecoderApi.md#get_economy) | **GET** /economy | Get Economy based on environmental factors
[**get_efficiency**](VINDecoderApi.md#get_efficiency) | **GET** /fuel_efficiency | Get fuel effeciency
[**get_safety_rating**](VINDecoderApi.md#get_safety_rating) | **GET** /safety | Get Safety Rating


# **decode**
> Build decode(vin, api_key=api_key)

VIN Decoder

Get the basic information on specifications for a car identified by a valid VIN

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.VINDecoderApi()
vin = 'vin_example' # str | VIN to decode
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)

try:
    # VIN Decoder
    api_response = api_instance.decode(vin, api_key=api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VINDecoderApi->decode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vin** | **str**| VIN to decode | 
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 

### Return type

[**Build**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_economy**
> Economy get_economy(vin, api_key=api_key)

Get Economy based on environmental factors

[MOCK] Calculate Economy i.e. Environmental Friendliness

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.VINDecoderApi()
vin = 'vin_example' # str | VIN as a reference to the type of car for which Environmental Economy data is to be returned
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)

try:
    # Get Economy based on environmental factors
    api_response = api_instance.get_economy(vin, api_key=api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VINDecoderApi->get_economy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vin** | **str**| VIN as a reference to the type of car for which Environmental Economy data is to be returned | 
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 

### Return type

[**Economy**](Economy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_efficiency**
> FuelEfficiency get_efficiency(vin, api_key=api_key)

Get fuel effeciency

[MOCK] Calculate fuel efficiency from taxonomy db mileage values

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.VINDecoderApi()
vin = 'vin_example' # str | VIN as a reference to the type of car for which fuel data is to be returned
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)

try:
    # Get fuel effeciency
    api_response = api_instance.get_efficiency(vin, api_key=api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VINDecoderApi->get_efficiency: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vin** | **str**| VIN as a reference to the type of car for which fuel data is to be returned | 
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 

### Return type

[**FuelEfficiency**](FuelEfficiency.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_safety_rating**
> SafetyRating get_safety_rating(vin, api_key=api_key)

Get Safety Rating

[MOCK] Get Safety ratings from third party sources

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.VINDecoderApi()
vin = 'vin_example' # str | VIN to fetch the safety ratings
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)

try:
    # Get Safety Rating
    api_response = api_instance.get_safety_rating(vin, api_key=api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VINDecoderApi->get_safety_rating: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vin** | **str**| VIN to fetch the safety ratings | 
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 

### Return type

[**SafetyRating**](SafetyRating.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

