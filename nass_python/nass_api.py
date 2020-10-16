import requests


nass_url = "http://quickstats.nass.usda.gov/api/"

def nass_count(api_key, source_desc=None, sector_desc=None, group_desc=None, commodity_desc=None, short_desc=None, domain_desc=None, agg_level_desc=None, domaincat_desc=None, statisticcat_desc=None, state_name=None, asd_desc=None, county_name=None, region_desc=None, zip_5=None, watershed_desc=None, year=None, freq_desc=None, reference_period_desc=None):
    
    # get dict of paramaters
    inputs = vars()
    inputs.pop('api_key') # get rid of api_key in dict for building url, as it is hardcoded below

    # set up the url with api key
    base_url = nass_url + 'get_counts/get?key=' + api_key

    # filter dict for non-None values and add actual values to the request
    for item in list(inputs):
        if inputs[item] == None:
            inputs.pop(item)
        else:
            # make sure the desc inputs are all uppercase, and strings
            if item != 'format' and item != 'numeric_vals':
                inputs[item] = str((inputs[item])).upper()
            
            # add on the url parameters
            base_url += '&' + item + '=' + requests.utils.quote(inputs[item]) #encodes unsafe / reserved chars in the user input (such as in ANIMALS & PRODUCTS)
    
    # make the request
    r = requests.get(base_url)
    print(r.content)

def nass_data(api_key, source_desc=None, sector_desc=None, group_desc=None, commodity_desc=None, short_desc=None, domain_desc=None, agg_level_desc=None, domaincat_desc=None, statisticcat_desc=None, state_name=None, asd_desc=None, county_name=None, region_desc=None, zip_5=None, watershed_desc=None, year=None, freq_desc=None, reference_period_desc=None, format=None, numeric_vals=None):
    
    # get dict of paramaters
    inputs = vars()
    inputs.pop('api_key') # get rid of api_key in dict for building url, as it is hardcoded below

    # set up the url with api key
    base_url = nass_url + 'api_GET?key=' + api_key

    # filter dict for non-None values and add actual values to the request
    for item in list(inputs):
        if inputs[item] == None:
            inputs.pop(item)
        else:
            # make sure the desc inputs are all uppercase, and strings
            if item != 'format' and item != 'numeric_vals':
                inputs[item] = str((inputs[item])).upper()
            
            # add on the url parameters
            base_url += '&' + item + '=' + requests.utils.quote(inputs[item]) #encodes unsafe / reserved chars in the user input (such as in ANIMALS & PRODUCTS)
    
    # make the request
    print(base_url)
    r = requests.get(base_url)
    print(r.content)
    return r




def nass_param(api_key, param=None, source_desc=None, sector_desc=None, group_desc=None, commodity_desc=None, short_desc=None, domain_desc=None, agg_level_desc=None, domaincat_desc=None, statisticcat_desc=None, state_name=None, asd_desc=None, county_name=None, region_desc=None, zip_5=None, watershed_desc=None, year=None, freq_desc=None, reference_period_desc=None):
    
    # get dict of paramaters
    inputs = vars()
    inputs.pop('api_key') # get rid of api_key in dict for building url, as it is hardcoded below

    # set up the url with api key
    base_url = nass_url + 'get_param_values/' + 'get?key=' + api_key

    # filter dict for non-None values and add actual values to the request
    for item in list(inputs):
        if inputs[item] == None:
            inputs.pop(item)
        else:
            # make sure the desc inputs are all uppercase, and strings
            if item != 'param':
                inputs[item] = str((inputs[item])).upper()
            
            # add on the url parameters
            base_url += '&' + item + '=' + requests.utils.quote(inputs[item]) #encodes unsafe / reserved chars in the user input (such as in ANIMALS & PRODUCTS)

    # make the request
    print(base_url)
    r = requests.get(base_url)
    print(r.content)
    return r


#nass_param('31F43E8A-05B2-3383-81B1-8E8811AE700D', year=2018, commodity_desc='Cattle', param='state_name')

nass_count('31F43E8A-05B2-3383-81B1-8E8811AE700D')