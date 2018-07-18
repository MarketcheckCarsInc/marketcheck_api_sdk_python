# marketcheck_api_sdk.MarketApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_averages**](MarketApi.md#get_averages) | **GET** /averages | [MOCK] Get Averages for YMM
[**get_comparison**](MarketApi.md#get_comparison) | **GET** /comparison | Compare market
[**get_competition**](MarketApi.md#get_competition) | **GET** /competition | Competitors
[**get_depreciation**](MarketApi.md#get_depreciation) | **GET** /depreciation | Depreciation
[**get_mds**](MarketApi.md#get_mds) | **GET** /mds | Market Days Supply
[**get_popularity**](MarketApi.md#get_popularity) | **GET** /popularity | Popularity
[**get_sales_count**](MarketApi.md#get_sales_count) | **GET** /sales | Get sales count by make, model, year, trim or taxonomy vin
[**get_trends**](MarketApi.md#get_trends) | **GET** /trends | Get Trends for criteria


# **get_averages**
> Averages get_averages(vin, api_key=api_key, year=year, make=make, model=model, trim=trim, fields=fields)

[MOCK] Get Averages for YMM

[Merged with the /search API - Please check the 'stats' parameter to the Search API above] Get market averages for price / miles / msrp / dom (days on market) fields for active cars matching the given reference VIN's basic specification or Year, Make, Model, Trim (Optional) criteria

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.MarketApi()
vin = 'vin_example' # str | VIN as a reference to the type of car for which averages data is to be returned
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)
year = 'year_example' # str | Year of the car (optional)
make = 'make_example' # str | Make of the car (optional)
model = 'model_example' # str | Model of the Car (optional)
trim = 'trim_example' # str | Trim of the Car (optional)
fields = 'fields_example' # str | Comma separated list of fields to generate stats for. Allowed fields in the list are - price, miles, msrp, dom (days on market) (optional)

try:
    # [MOCK] Get Averages for YMM
    api_response = api_instance.get_averages(vin, api_key=api_key, year=year, make=make, model=model, trim=trim, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->get_averages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vin** | **str**| VIN as a reference to the type of car for which averages data is to be returned | 
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **year** | **str**| Year of the car | [optional] 
 **make** | **str**| Make of the car | [optional] 
 **model** | **str**| Model of the Car | [optional] 
 **trim** | **str**| Trim of the Car | [optional] 
 **fields** | **str**| Comma separated list of fields to generate stats for. Allowed fields in the list are - price, miles, msrp, dom (days on market) | [optional] 

### Return type

[**Averages**](Averages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comparison**
> ComparisonPoint get_comparison(vin, api_key=api_key)

Compare market

[MOCK] Get historical market trends for cars matching the given VIN's basic specification or Year, Make, Model, Trim (Optional) criteria

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.MarketApi()
vin = 'vin_example' # str | VIN as a reference to the type of car for which comparison data is to be returned
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)

try:
    # Compare market
    api_response = api_instance.get_comparison(vin, api_key=api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->get_comparison: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vin** | **str**| VIN as a reference to the type of car for which comparison data is to be returned | 
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 

### Return type

[**ComparisonPoint**](ComparisonPoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_competition**
> CompetitorsPoint get_competition(vin, api_key=api_key)

Competitors

[MOCK] Competitor cars in market for current vin

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.MarketApi()
vin = 'vin_example' # str | VIN as a reference to the type of car for which competitors data is to be returned
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)

try:
    # Competitors
    api_response = api_instance.get_competition(vin, api_key=api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->get_competition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vin** | **str**| VIN as a reference to the type of car for which competitors data is to be returned | 
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 

### Return type

[**CompetitorsPoint**](CompetitorsPoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_depreciation**
> DepreciationPoint get_depreciation(vin, api_key=api_key)

Depreciation

[MOCK] Model resale value based on depreciation

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.MarketApi()
vin = 'vin_example' # str | VIN as a reference to the type of car for which Depreciation stats is to be returned
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)

try:
    # Depreciation
    api_response = api_instance.get_depreciation(vin, api_key=api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->get_depreciation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vin** | **str**| VIN as a reference to the type of car for which Depreciation stats is to be returned | 
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 

### Return type

[**DepreciationPoint**](DepreciationPoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mds**
> Mds get_mds(vin, api_key=api_key, exact=exact, latitude=latitude, longitude=longitude, radius=radius, debug=debug, include_sold=include_sold)

Market Days Supply

Get the basic information on specifications for a car identified by a valid VIN

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.MarketApi()
vin = 'vin_example' # str | VIN to decode
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)
exact = false # bool | Exact parameter (optional) (default to false)
latitude = 1.2 # float | Latitude component of location (optional)
longitude = 1.2 # float | Longitude component of location (optional)
radius = 56 # int | Radius around the search location (optional)
debug = 0 # int | Debug parameter (optional) (default to 0)
include_sold = false # bool | To fetch sold vins (optional) (default to false)

try:
    # Market Days Supply
    api_response = api_instance.get_mds(vin, api_key=api_key, exact=exact, latitude=latitude, longitude=longitude, radius=radius, debug=debug, include_sold=include_sold)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->get_mds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vin** | **str**| VIN to decode | 
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **exact** | **bool**| Exact parameter | [optional] [default to false]
 **latitude** | **float**| Latitude component of location | [optional] 
 **longitude** | **float**| Longitude component of location | [optional] 
 **radius** | **int**| Radius around the search location | [optional] 
 **debug** | **int**| Debug parameter | [optional] [default to 0]
 **include_sold** | **bool**| To fetch sold vins | [optional] [default to false]

### Return type

[**Mds**](Mds.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_popularity**
> list[PopularityItem] get_popularity(year, make, model, trim, body_type, api_key=api_key, stats=stats)

Popularity

[MOCK] [Merged with the /search API - Please check the 'popularity' parameter to the Search API above] Get the Popularity for the given simple filter criteria (by given Year, Make, Model, Trim criteria)

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.MarketApi()
year = 'year_example' # str | Year of the car
make = 'make_example' # str | Make of the car
model = 'model_example' # str | Model of the Car
trim = 'trim_example' # str | Trim of the Car
body_type = 'body_type_example' # str | Body type to filter the cars on. Valid values are the ones returned by body_type facets API call
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)
stats = 'stats_example' # str | The list of fields for which stats need to be generated based on the matching listings for the search criteria. Allowed fields are - price, miles, msrp, dom The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond. (optional)

try:
    # Popularity
    api_response = api_instance.get_popularity(year, make, model, trim, body_type, api_key=api_key, stats=stats)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->get_popularity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **str**| Year of the car | 
 **make** | **str**| Make of the car | 
 **model** | **str**| Model of the Car | 
 **trim** | **str**| Trim of the Car | 
 **body_type** | **str**| Body type to filter the cars on. Valid values are the ones returned by body_type facets API call | 
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **stats** | **str**| The list of fields for which stats need to be generated based on the matching listings for the search criteria. Allowed fields are - price, miles, msrp, dom The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond. | [optional] 

### Return type

[**list[PopularityItem]**](PopularityItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_count**
> Sales get_sales_count(api_key=api_key, car_type=car_type, make=make, mm=mm, ymm=ymm, ymmt=ymmt, taxonomy_vin=taxonomy_vin, state=state, city_state=city_state, stats=stats)

Get sales count by make, model, year, trim or taxonomy vin

Get a sales count for city, state or national level by make, model, year, trim or taxonomy vin

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.MarketApi()
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)
car_type = 'used' # str | Inventory type for which sales count is to be searched, default is used (optional) (default to used)
make = 'make_example' # str | Make for which sales count is to be searched (optional)
mm = 'mm_example' # str | Make-Model for which sales count is to be searched, pipe seperated like mm=ford|f-150 (optional)
ymm = 'ymm_example' # str | Year-Make-Model for which sales count is to be searched, pipe seperated like ymm=2015|ford|f-150 (optional)
ymmt = 'ymmt_example' # str | Year-Make-Model-Trim for which sales count is to be searched, pipe seperated like ymmt=2015|ford|f-150|platinum (optional)
taxonomy_vin = 'taxonomy_vin_example' # str | taxonomy_vin for which sales count is to be searched (optional)
state = 'state_example' # str | State level sales count (optional)
city_state = 'city_state_example' # str | City level sales count, pipe seperated like city_state=jacksonville|FL (optional)
stats = 'stats_example' # str | Comma separated list of fields to generate stats for. Allowed fields in the list are - price, miles, dom (days on market) OR all (optional)

try:
    # Get sales count by make, model, year, trim or taxonomy vin
    api_response = api_instance.get_sales_count(api_key=api_key, car_type=car_type, make=make, mm=mm, ymm=ymm, ymmt=ymmt, taxonomy_vin=taxonomy_vin, state=state, city_state=city_state, stats=stats)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->get_sales_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **car_type** | **str**| Inventory type for which sales count is to be searched, default is used | [optional] [default to used]
 **make** | **str**| Make for which sales count is to be searched | [optional] 
 **mm** | **str**| Make-Model for which sales count is to be searched, pipe seperated like mm&#x3D;ford|f-150 | [optional] 
 **ymm** | **str**| Year-Make-Model for which sales count is to be searched, pipe seperated like ymm&#x3D;2015|ford|f-150 | [optional] 
 **ymmt** | **str**| Year-Make-Model-Trim for which sales count is to be searched, pipe seperated like ymmt&#x3D;2015|ford|f-150|platinum | [optional] 
 **taxonomy_vin** | **str**| taxonomy_vin for which sales count is to be searched | [optional] 
 **state** | **str**| State level sales count | [optional] 
 **city_state** | **str**| City level sales count, pipe seperated like city_state&#x3D;jacksonville|FL | [optional] 
 **stats** | **str**| Comma separated list of fields to generate stats for. Allowed fields in the list are - price, miles, dom (days on market) OR all | [optional] 

### Return type

[**Sales**](Sales.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trends**
> list[TrendPoint] get_trends(vin, car_type, api_key=api_key, year=year, make=make, model=model, trim=trim)

Get Trends for criteria

Get historical market trends for cars matching the given VIN's basic specification or Year, Make, Model, Trim (Optional) criteria

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.MarketApi()
vin = 'vin_example' # str | VIN as a reference to the type of car for which trend data is to be returned
car_type = 'car_type_example' # str | Car type. Allowed values are - new / used / certified
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)
year = 'year_example' # str | Year of the car (optional)
make = 'make_example' # str | Make of the car (optional)
model = 'model_example' # str | Model of the Car (optional)
trim = 'trim_example' # str | Trim of the Car (optional)

try:
    # Get Trends for criteria
    api_response = api_instance.get_trends(vin, car_type, api_key=api_key, year=year, make=make, model=model, trim=trim)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->get_trends: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vin** | **str**| VIN as a reference to the type of car for which trend data is to be returned | 
 **car_type** | **str**| Car type. Allowed values are - new / used / certified | 
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **year** | **str**| Year of the car | [optional] 
 **make** | **str**| Make of the car | [optional] 
 **model** | **str**| Model of the Car | [optional] 
 **trim** | **str**| Trim of the Car | [optional] 

### Return type

[**list[TrendPoint]**](TrendPoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

