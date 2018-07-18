# marketcheck_api_sdk.CRMApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crm_check**](CRMApi.md#crm_check) | **GET** /crm_check/{vin} | CRM check of a particular vin


# **crm_check**
> CRMResponse crm_check(vin, sale_date, api_key=api_key)

CRM check of a particular vin

Check whether particular vin has had a listing after stipulated date or not

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.CRMApi()
vin = 'vin_example' # str | vin for which CRM check needs to be done
sale_date = 'sale_date_example' # str | sale date after which listing has appeared or not
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)

try:
    # CRM check of a particular vin
    api_response = api_instance.crm_check(vin, sale_date, api_key=api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CRMApi->crm_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vin** | **str**| vin for which CRM check needs to be done | 
 **sale_date** | **str**| sale date after which listing has appeared or not | 
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 

### Return type

[**CRMResponse**](CRMResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

