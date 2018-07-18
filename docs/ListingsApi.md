# marketcheck_api_sdk.ListingsApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_listing**](ListingsApi.md#get_listing) | **GET** /listing/{id} | Listing by id
[**get_listing_extra**](ListingsApi.md#get_listing_extra) | **GET** /listing/{id}/extra | Long text Listings attributes for Listing with the given id
[**get_listing_media**](ListingsApi.md#get_listing_media) | **GET** /listing/{id}/media | Listing media by id
[**get_listing_vdp**](ListingsApi.md#get_listing_vdp) | **GET** /listing/{id}/vdp | Get listing HTML
[**get_summary_report**](ListingsApi.md#get_summary_report) | **GET** /vin_report_summary | Get Summary Report
[**search**](ListingsApi.md#search) | **GET** /search | Gets active car listings for the given search criteria


# **get_listing**
> Listing get_listing(id, api_key=api_key)

Listing by id

Get a particular listing by its id

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.ListingsApi()
id = 'id_example' # str | Listing id to get all the listing attributes
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)

try:
    # Listing by id
    api_response = api_instance.get_listing(id, api_key=api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListingsApi->get_listing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Listing id to get all the listing attributes | 
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 

### Return type

[**Listing**](Listing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listing_extra**
> ListingExtraAttributes get_listing_extra(id, api_key=api_key)

Long text Listings attributes for Listing with the given id

Get listing options, features, seller comments

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.ListingsApi()
id = 'id_example' # str | Listing id to get all the long text listing attributes
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)

try:
    # Long text Listings attributes for Listing with the given id
    api_response = api_instance.get_listing_extra(id, api_key=api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListingsApi->get_listing_extra: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Listing id to get all the long text listing attributes | 
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 

### Return type

[**ListingExtraAttributes**](ListingExtraAttributes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listing_media**
> ListingMedia get_listing_media(id, api_key=api_key)

Listing media by id

Get listing media (photo, photos) by id

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.ListingsApi()
id = 'id_example' # str | Listing id to get all the listing attributes
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)

try:
    # Listing media by id
    api_response = api_instance.get_listing_media(id, api_key=api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListingsApi->get_listing_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Listing id to get all the listing attributes | 
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 

### Return type

[**ListingMedia**](ListingMedia.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listing_vdp**
> ListingVDP get_listing_vdp(id, api_key=api_key, html=html)

Get listing HTML

Cached HTML of the Vehicle Details Page (VDP) for the listing. The HTML is cached only for 7 days for all listings. So this API could be used to get HTML of mostly active listings and that have recently expired

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.ListingsApi()
id = 'id_example' # str | Listing id to get the vehicle details page (VDP) HTML
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)
html = 'html_example' # str | Get only HTML for given listings VDP page (optional)

try:
    # Get listing HTML
    api_response = api_instance.get_listing_vdp(id, api_key=api_key, html=html)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListingsApi->get_listing_vdp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Listing id to get the vehicle details page (VDP) HTML | 
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **html** | **str**| Get only HTML for given listings VDP page | [optional] 

### Return type

[**ListingVDP**](ListingVDP.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary_report**
> list[VinReport] get_summary_report(vin, api_key=api_key)

Get Summary Report

[MOCK] Generate Summary report

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.ListingsApi()
vin = 'vin_example' # str | VIN as a reference to the type of car for which Summary data is to be returned
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)

try:
    # Get Summary Report
    api_response = api_instance.get_summary_report(vin, api_key=api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListingsApi->get_summary_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vin** | **str**| VIN as a reference to the type of car for which Summary data is to be returned | 
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 

### Return type

[**list[VinReport]**](VinReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> SearchResponse search(api_key=api_key, latitude=latitude, longitude=longitude, radius=radius, zip=zip, include_lease=include_lease, include_finance=include_finance, lease_term=lease_term, lease_down_payment=lease_down_payment, lease_emp=lease_emp, finance_loan_term=finance_loan_term, finance_loan_apr=finance_loan_apr, finance_emp=finance_emp, finance_down_payment=finance_down_payment, finance_down_payment_per=finance_down_payment_per, car_type=car_type, seller_type=seller_type, carfax_1_owner=carfax_1_owner, carfax_clean_title=carfax_clean_title, year=year, make=make, model=model, trim=trim, dealer_id=dealer_id, vin=vin, source=source, body_type=body_type, body_subtype=body_subtype, vehicle_type=vehicle_type, vins=vins, taxonomy_vins=taxonomy_vins, ymmt=ymmt, match=match, cylinders=cylinders, transmission=transmission, speeds=speeds, doors=doors, drivetrain=drivetrain, exterior_color=exterior_color, interior_color=interior_color, engine=engine, engine_type=engine_type, engine_aspiration=engine_aspiration, engine_block=engine_block, miles_range=miles_range, price_range=price_range, dom_range=dom_range, sort_by=sort_by, sort_order=sort_order, rows=rows, start=start, facets=facets, stats=stats, country=country, plot=plot, nodedup=nodedup, state=state, city=city, dealer_name=dealer_name, trim_o=trim_o, trim_r=trim_r, dom_active_range=dom_active_range, dom_180_range=dom_180_range, options=options, features=features, exclude_certified=exclude_certified)

Gets active car listings for the given search criteria

This endpoint is the meat of the API and serves many purposes. This API produces a list of currently active cars from the market for the given search criteria. The API results are limited to allow pagination upto 1000 rows.   The search API facilitates the following use cases -  1. Search Cars around a given geo-point within a given radius  2. Search cars for a specific year / make / model or combination of these  3. Search cars matching multiple year, make, model combinatins in the same search request 4. Filter results by most car specification attributes 5. Search for similar cars by VIN or Taxonomy VIN  6. Filter cars within a given price / miles / days on market (dom) range 7. Specify a sort order for the results on price / miles / dom / listed date  8. Search cars for a given City / State combination  9. Get Facets to build the search drill downs  10. Get Market averages for price/miles/dom/msrp for your search

### Example
```python
from __future__ import print_function
import time
import marketcheck_api_sdk
from marketcheck_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = marketcheck_api_sdk.ListingsApi()
api_key = 'api_key_example' # str | The API Authentication Key. Mandatory with all API calls. (optional)
latitude = 1.2 # float | Latitude component of location (optional)
longitude = 1.2 # float | Longitude component of location (optional)
radius = 56 # int | Radius around the search location (optional)
zip = 'zip_example' # str | car search bases on zipcode (optional)
include_lease = true # bool | Boolean param to search for listings that include leasing options in them (optional)
include_finance = true # bool | Boolean param to search for listings that include finance options in them (optional)
lease_term = 'lease_term_example' # str | Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term=30-60 (optional)
lease_down_payment = 'lease_down_payment_example' # str | Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment=30-60 (optional)
lease_emp = 'lease_emp_example' # str | Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp=30-60 (optional)
finance_loan_term = 'finance_loan_term_example' # str | Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term=30-60 (optional)
finance_loan_apr = 'finance_loan_apr_example' # str | Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr=30-60 (optional)
finance_emp = 'finance_emp_example' # str | Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp=30-60 (optional)
finance_down_payment = 'finance_down_payment_example' # str | Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment=30-60 (optional)
finance_down_payment_per = 'finance_down_payment_per_example' # str | Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per=30-60 (optional)
car_type = 'car_type_example' # str | Car type. Allowed values are - new / used / certified (optional)
seller_type = 'seller_type_example' # str | Seller type to filter cars on. Valid filter values are those that our Search facets API returns for unique seller types. You can pass in multiple seller type values comma separated. (optional)
carfax_1_owner = 'carfax_1_owner_example' # str | Indicates whether car has had only one owner or not (optional)
carfax_clean_title = 'carfax_clean_title_example' # str | Indicates whether car has clean ownership records (optional)
year = 'year_example' # str | Car year - 1980 onwards. Valid filter values are those that our Search facets API returns for unique years. You can pass in multiple year values comma separated. (optional)
make = 'make_example' # str | Car Make - should be a standard OEM Make name. Valid filter values are those that our Search facets API returns for unique make. You can pass in multiple make values separated by comma. e.g. ford,audi (optional)
model = 'model_example' # str | Car model to search. Valid filter values are those that our Search facets API returns for unique model. You can pass in multiple model values comma separated for e.g f-150,Mustang. (optional)
trim = 'trim_example' # str | Car trim to search. Valid filter values are those that our Search facets API returns for unique trim. You can pass in multiple trim values comma separated (optional)
dealer_id = 'dealer_id_example' # str | Dealer id to filter the cars. (optional)
vin = 'vin_example' # str | Car vin to search (optional)
source = 'source_example' # str | Source to search cars. Valid filter values are those that our Search facets API returns for unique source. You can pass in multiple source values comma separated (optional)
body_type = 'body_type_example' # str | Body type to filter the cars on. Valid filter values are those that our Search facets API returns for unique body types. You can pass in multiple body types comma separated. (optional)
body_subtype = 'body_subtype_example' # str | Body subtype to filter the cars on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated (optional)
vehicle_type = 'vehicle_type_example' # str | Vehicle type to filter the cars on. Valid filter values are those that our Search facets API returns for unique vehicle types. You can pass in multiple vehicle type values comma separated (optional)
vins = 'vins_example' # str | Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc (optional)
taxonomy_vins = 'taxonomy_vins_example' # str | Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API. (optional)
ymmt = 'ymmt_example' # str | Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe '|' character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - 'year|make||' or 'year|make|model' or '|make|model|' combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the 'vins' or 'taxonomy_vins' parameter to the search api instead the year|make|model|trim combinations. (optional)
match = 'match_example' # str | Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match (optional)
cylinders = 'cylinders_example' # str | Cylinders to filter the cars on. Valid filter values are those that our Search facets API returns for unique cylinder values. You can pass in multiple cylinder values comma separated (optional)
transmission = 'transmission_example' # str | Transmission to filter the cars on. [a = Automatic, m = Manual]. Valid filter values are those that our Search facets API returns for unique transmission. You can pass in multiple transmission values comma separated (optional)
speeds = 'speeds_example' # str | Speeds to filter the cars on. Valid filter values are those that our Search facets API returns for unique speeds. You can pass in multiple speeds values comma separated (optional)
doors = 'doors_example' # str | Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated (optional)
drivetrain = 'drivetrain_example' # str | Drivetrain to filter the cars on. Valid filter values are those that our Search facets API returns for unique drivetrains. You can pass in multiple drivetrain values comma separated (optional)
exterior_color = 'exterior_color_example' # str | Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated (optional)
interior_color = 'interior_color_example' # str | Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated (optional)
engine = 'engine_example' # str | Filter listings on engine (optional)
engine_type = 'engine_type_example' # str | Engine Type to match. Valid filter values are those that our Search facets API returns for unique engine types. You can pass in multiple engine type values comma separated (optional)
engine_aspiration = 'engine_aspiration_example' # str | Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated (optional)
engine_block = 'engine_block_example' # str | Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated (optional)
miles_range = 'miles_range_example' # str | Miles range to filter cars with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000 (optional)
price_range = 'price_range_example' # str | Price range to filter cars with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000 (optional)
dom_range = 'dom_range_example' # str | Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 (optional)
sort_by = 'sort_by_example' # str | Sort by field - allowed fields are distance|price|miles|dom|age|posted_at|year. Default sort field is distance from the given point (optional)
sort_order = 'sort_order_example' # str | Sort order - asc or desc. Default sort order is distance from a point. (optional)
rows = 'rows_example' # str | Number of results to return. Default is 10. Max is 50 (optional)
start = 'start_example' # str | Page number to fetch the results for the given criteria. Default is 1. Pagination is allowed only till first 1000 results for the search and sort criteria. The page value can be only between 1 to 1000/rows (optional)
facets = 'facets_example' # str | The comma separated list of fields for which facets are requested. Supported fields are - year, make, model, trim, vehicle_type, car_type, body_type, body_subtype, drivetrain, cylinders, transmission, exterior_color, interior_color, doors, engine_type, engine_aspiration, engine_block. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. (optional)
stats = 'stats_example' # str | The list of fields for which stats need to be generated based on the matching listings for the search criteria. Allowed fields are - price, miles, msrp, dom The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond. (optional)
country = 'country_example' # str | Filter on Country, by default US. Search available on US (United States) and CA (Canada) (optional)
plot = 'plot_example' # str | If plot has value true results in around 25k coordinates with limited fields to plot respective graph (optional)
nodedup = true # bool | If nodedup is set to true then will give results without is_searchable i.e multiple listings for single vin (optional)
state = 'state_example' # str | Filter listsings on State (optional)
city = 'city_example' # str | Filter listings on city (optional)
dealer_name = 'dealer_name_example' # str | Filter listings on dealer_name (optional)
trim_o = 'trim_o_example' # str | Filter listings on web scraped trim (optional)
trim_r = 'trim_r_example' # str | Filter trim on custom possible matches (optional)
dom_active_range = 'dom_active_range_example' # str | Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 (optional)
dom_180_range = 'dom_180_range_example' # str | Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 (optional)
options = 'options_example' # str | Tokenizer search on options for multiple options use | as seperator (optional)
features = 'features_example' # str | Tokenizer search on features for multiple options use | as seperator (optional)
exclude_certified = true # bool | Boolean param to exclude certified cars from search results (optional)

try:
    # Gets active car listings for the given search criteria
    api_response = api_instance.search(api_key=api_key, latitude=latitude, longitude=longitude, radius=radius, zip=zip, include_lease=include_lease, include_finance=include_finance, lease_term=lease_term, lease_down_payment=lease_down_payment, lease_emp=lease_emp, finance_loan_term=finance_loan_term, finance_loan_apr=finance_loan_apr, finance_emp=finance_emp, finance_down_payment=finance_down_payment, finance_down_payment_per=finance_down_payment_per, car_type=car_type, seller_type=seller_type, carfax_1_owner=carfax_1_owner, carfax_clean_title=carfax_clean_title, year=year, make=make, model=model, trim=trim, dealer_id=dealer_id, vin=vin, source=source, body_type=body_type, body_subtype=body_subtype, vehicle_type=vehicle_type, vins=vins, taxonomy_vins=taxonomy_vins, ymmt=ymmt, match=match, cylinders=cylinders, transmission=transmission, speeds=speeds, doors=doors, drivetrain=drivetrain, exterior_color=exterior_color, interior_color=interior_color, engine=engine, engine_type=engine_type, engine_aspiration=engine_aspiration, engine_block=engine_block, miles_range=miles_range, price_range=price_range, dom_range=dom_range, sort_by=sort_by, sort_order=sort_order, rows=rows, start=start, facets=facets, stats=stats, country=country, plot=plot, nodedup=nodedup, state=state, city=city, dealer_name=dealer_name, trim_o=trim_o, trim_r=trim_r, dom_active_range=dom_active_range, dom_180_range=dom_180_range, options=options, features=features, exclude_certified=exclude_certified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListingsApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **latitude** | **float**| Latitude component of location | [optional] 
 **longitude** | **float**| Longitude component of location | [optional] 
 **radius** | **int**| Radius around the search location | [optional] 
 **zip** | **str**| car search bases on zipcode | [optional] 
 **include_lease** | **bool**| Boolean param to search for listings that include leasing options in them | [optional] 
 **include_finance** | **bool**| Boolean param to search for listings that include finance options in them | [optional] 
 **lease_term** | **str**| Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term&#x3D;30-60 | [optional] 
 **lease_down_payment** | **str**| Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment&#x3D;30-60 | [optional] 
 **lease_emp** | **str**| Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp&#x3D;30-60 | [optional] 
 **finance_loan_term** | **str**| Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term&#x3D;30-60 | [optional] 
 **finance_loan_apr** | **str**| Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr&#x3D;30-60 | [optional] 
 **finance_emp** | **str**| Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp&#x3D;30-60 | [optional] 
 **finance_down_payment** | **str**| Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment&#x3D;30-60 | [optional] 
 **finance_down_payment_per** | **str**| Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per&#x3D;30-60 | [optional] 
 **car_type** | **str**| Car type. Allowed values are - new / used / certified | [optional] 
 **seller_type** | **str**| Seller type to filter cars on. Valid filter values are those that our Search facets API returns for unique seller types. You can pass in multiple seller type values comma separated. | [optional] 
 **carfax_1_owner** | **str**| Indicates whether car has had only one owner or not | [optional] 
 **carfax_clean_title** | **str**| Indicates whether car has clean ownership records | [optional] 
 **year** | **str**| Car year - 1980 onwards. Valid filter values are those that our Search facets API returns for unique years. You can pass in multiple year values comma separated. | [optional] 
 **make** | **str**| Car Make - should be a standard OEM Make name. Valid filter values are those that our Search facets API returns for unique make. You can pass in multiple make values separated by comma. e.g. ford,audi | [optional] 
 **model** | **str**| Car model to search. Valid filter values are those that our Search facets API returns for unique model. You can pass in multiple model values comma separated for e.g f-150,Mustang. | [optional] 
 **trim** | **str**| Car trim to search. Valid filter values are those that our Search facets API returns for unique trim. You can pass in multiple trim values comma separated | [optional] 
 **dealer_id** | **str**| Dealer id to filter the cars. | [optional] 
 **vin** | **str**| Car vin to search | [optional] 
 **source** | **str**| Source to search cars. Valid filter values are those that our Search facets API returns for unique source. You can pass in multiple source values comma separated | [optional] 
 **body_type** | **str**| Body type to filter the cars on. Valid filter values are those that our Search facets API returns for unique body types. You can pass in multiple body types comma separated. | [optional] 
 **body_subtype** | **str**| Body subtype to filter the cars on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated | [optional] 
 **vehicle_type** | **str**| Vehicle type to filter the cars on. Valid filter values are those that our Search facets API returns for unique vehicle types. You can pass in multiple vehicle type values comma separated | [optional] 
 **vins** | **str**| Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc | [optional] 
 **taxonomy_vins** | **str**| Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API. | [optional] 
 **ymmt** | **str**| Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe &#39;|&#39; character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - &#39;year|make||&#39; or &#39;year|make|model&#39; or &#39;|make|model|&#39; combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the &#39;vins&#39; or &#39;taxonomy_vins&#39; parameter to the search api instead the year|make|model|trim combinations. | [optional] 
 **match** | **str**| Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match | [optional] 
 **cylinders** | **str**| Cylinders to filter the cars on. Valid filter values are those that our Search facets API returns for unique cylinder values. You can pass in multiple cylinder values comma separated | [optional] 
 **transmission** | **str**| Transmission to filter the cars on. [a &#x3D; Automatic, m &#x3D; Manual]. Valid filter values are those that our Search facets API returns for unique transmission. You can pass in multiple transmission values comma separated | [optional] 
 **speeds** | **str**| Speeds to filter the cars on. Valid filter values are those that our Search facets API returns for unique speeds. You can pass in multiple speeds values comma separated | [optional] 
 **doors** | **str**| Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated | [optional] 
 **drivetrain** | **str**| Drivetrain to filter the cars on. Valid filter values are those that our Search facets API returns for unique drivetrains. You can pass in multiple drivetrain values comma separated | [optional] 
 **exterior_color** | **str**| Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated | [optional] 
 **interior_color** | **str**| Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated | [optional] 
 **engine** | **str**| Filter listings on engine | [optional] 
 **engine_type** | **str**| Engine Type to match. Valid filter values are those that our Search facets API returns for unique engine types. You can pass in multiple engine type values comma separated | [optional] 
 **engine_aspiration** | **str**| Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated | [optional] 
 **engine_block** | **str**| Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated | [optional] 
 **miles_range** | **str**| Miles range to filter cars with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **price_range** | **str**| Price range to filter cars with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **dom_range** | **str**| Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **sort_by** | **str**| Sort by field - allowed fields are distance|price|miles|dom|age|posted_at|year. Default sort field is distance from the given point | [optional] 
 **sort_order** | **str**| Sort order - asc or desc. Default sort order is distance from a point. | [optional] 
 **rows** | **str**| Number of results to return. Default is 10. Max is 50 | [optional] 
 **start** | **str**| Page number to fetch the results for the given criteria. Default is 1. Pagination is allowed only till first 1000 results for the search and sort criteria. The page value can be only between 1 to 1000/rows | [optional] 
 **facets** | **str**| The comma separated list of fields for which facets are requested. Supported fields are - year, make, model, trim, vehicle_type, car_type, body_type, body_subtype, drivetrain, cylinders, transmission, exterior_color, interior_color, doors, engine_type, engine_aspiration, engine_block. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] 
 **stats** | **str**| The list of fields for which stats need to be generated based on the matching listings for the search criteria. Allowed fields are - price, miles, msrp, dom The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond. | [optional] 
 **country** | **str**| Filter on Country, by default US. Search available on US (United States) and CA (Canada) | [optional] 
 **plot** | **str**| If plot has value true results in around 25k coordinates with limited fields to plot respective graph | [optional] 
 **nodedup** | **bool**| If nodedup is set to true then will give results without is_searchable i.e multiple listings for single vin | [optional] 
 **state** | **str**| Filter listsings on State | [optional] 
 **city** | **str**| Filter listings on city | [optional] 
 **dealer_name** | **str**| Filter listings on dealer_name | [optional] 
 **trim_o** | **str**| Filter listings on web scraped trim | [optional] 
 **trim_r** | **str**| Filter trim on custom possible matches | [optional] 
 **dom_active_range** | **str**| Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **dom_180_range** | **str**| Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **options** | **str**| Tokenizer search on options for multiple options use | as seperator | [optional] 
 **features** | **str**| Tokenizer search on features for multiple options use | as seperator | [optional] 
 **exclude_certified** | **bool**| Boolean param to exclude certified cars from search results | [optional] 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

