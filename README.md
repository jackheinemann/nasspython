# nasspython
A wrapper for the NASS Quickstats API for Python, modeled off of the R package documented here: https://github.com/rdinter/usdarnass

You can find the database here: https://quickstats.nass.usda.gov/
<hr>

## Functions provided:
### nass_count

#### Description
Checks the number of observations that will be returned in a data request. All queries to the QuickStats are limited to 50,000 observations. This is a helpful function in determining how to structurea data request to fit within the 50,000 limit.<br>

#### Arguments
* Inital argument is your API key for NASS Quickstats
* <b>source_desc</b>: "Program" - Source of data ("CENSUS" or "SURVEY").  Census program in-cludes the Census of Ag as well as follow up projects. Survey program includesnational, state, and county surveys.
* <b>sector_desc</b>: "Sector"  -  Five  high  level,  broad  categories  useful  to  narrow  down  choices.("ANIMALS & PRODUCTS", "CROPS", "DEMOGRAPHICS", "ECONOMICS",or "ENVIRONMENTAL")
* <b>group_desc</b>: "Group" - Subsets within sector (e.g., under sector_desc = "CROPS", the groupsare "FIELD CROPS", "FRUIT & TREE NUTS", "HORTICULTURE", and "VEG-ETABLES").
* <b>commodity_desc</b>: "Commodity"  -  The  primary  subject  of  interest  (e.g.,  "CORN",  "CATTLE","LABOR", "TRACTORS", "OPERATORS").
* <b>short_desc</b>: "Data Item" - A concatenation of six columns:  commodity_desc,  class_desc,prodn_practice_desc, util_practice_desc, statisticcat_desc, and unit_desc.
* <b>domain_desc</b>: "Domain" - Generally another characteristic of operations that produce a partic-ular commodity (e.g., "ECONOMIC CLASS", "AREA OPERATED", "NAICSCLASSIFICATION",  "SALES").   For  chemical  usage  data,  the  domain  de-scribes  the  type  of  chemical  applied  to  the  commodity.   The  domain_desc  ="TOTAL" will have no further breakouts; i.e., the data value pertains completelyto the short_desc.
* <b>domaincat_desc</b>: "Domain Category" - Categories or partitions within a domain (e.g., under do-main_desc = "SALES", domain categories include $1,000 TO $9,999, $10,000TO $19,999, etc).
* <b>agg_level_desc</b>: "Geographic Level" - Aggregation level or geographic granularity of the data.("AGRICULTURAL  DISTRICT",  "COUNTY",  "INTERNATIONAL",  "NA-TIONAL", "REGION : MULTI-STATE", "REGION : SUB-STATE", "STATE","WATERSHED", or "ZIP CODE")
* <b>statisticcat_desc</b>: "Category" - The aspect of a commodity being measured (e.g., "AREA HAR-VESTED", "PRICE RECEIVED", "INVENTORY", "SALES").
* <b>state_name</b>: "State" - State full name.
* <b>asd_desc</b>: "Ag District" - Ag statistics district name.
* <b>county_name</b>: "County" - County name.
* <b>region_desc</b>: "Region" - NASS defined geographic entities not readily defined by other stan-dard geographic levels.  A region can be a less than a state (SUB-STATE) or agroup of states (MULTI-STATE), and may be specific to a commodity.
* <b>zip_5</b>: "Zip Code" - US Postal Service 5-digit zip code.
* <b>watershed_desc</b>: "Watershed" - Name assigned to the HUC.
* <b>year</b>: "Year" - The numeric year of the data and can be either a character or numericvector.
* <b>freq_desc</b>: "Period Type" - Length of time covered ("ANNUAL", "SEASON", "MONTHLY","WEEKLY", "POINT IN TIME").  "MONTHLY" often covers more than onemonth. "POINT IN TIME" is as of a particular day.
* <b>reference_period_desc</b>: "Period" - The specific time frame, within a freq_desc.

#### Return Value
Number of observations.

#### Examples
Return count of all observations in NASS:<br>
` nass_count(<your api key>) `<br><br>
Find the number of observations for Wake County in North Carolina:<br>
` nass_count(<your api key>, state_name = "NORTH CAROLINA", county_name = "WAKE") `

<hr>

### nass_data
#### Description
Sends query to Quick Stats API from given parameter values. Data request is limited to 50,000 records per the API. Use <em>nass_count</em> to determine number of records in query.<br>

#### Arguments
* Inital argument is your API key for NASS Quickstats
* <b>source_desc</b>: "Program" - Source of data ("CENSUS" or "SURVEY").  Census program in-cludes the Census of Ag as well as follow up projects. Survey program includesnational, state, and county surveys.
* <b>sector_desc</b>: "Sector"  -  Five  high  level,  broad  categories  useful  to  narrow  down  choices.("ANIMALS & PRODUCTS", "CROPS", "DEMOGRAPHICS", "ECONOMICS",or "ENVIRONMENTAL")
* <b>group_desc</b>: "Group" - Subsets within sector (e.g., under sector_desc = "CROPS", the groupsare "FIELD CROPS", "FRUIT & TREE NUTS", "HORTICULTURE", and "VEG-ETABLES").
* <b>commodity_desc</b>: "Commodity"  -  The  primary  subject  of  interest  (e.g.,  "CORN",  "CATTLE","LABOR", "TRACTORS", "OPERATORS").
* <b>short_desc</b>: "Data Item" - A concatenation of six columns:  commodity_desc,  class_desc,prodn_practice_desc, util_practice_desc, statisticcat_desc, and unit_desc.
* <b>domain_desc</b>: "Domain" - Generally another characteristic of operations that produce a partic-ular commodity (e.g., "ECONOMIC CLASS", "AREA OPERATED", "NAICSCLASSIFICATION",  "SALES").   For  chemical  usage  data,  the  domain  de-scribes  the  type  of  chemical  applied  to  the  commodity.   The  domain_desc  ="TOTAL" will have no further breakouts; i.e., the data value pertains completelyto the short_desc.
* <b>domaincat_desc</b>: "Domain Category" - Categories or partitions within a domain (e.g., under do-main_desc = "SALES", domain categories include $1,000 TO $9,999, $10,000TO $19,999, etc).
* <b>agg_level_desc</b>: "Geographic Level" - Aggregation level or geographic granularity of the data.("AGRICULTURAL  DISTRICT",  "COUNTY",  "INTERNATIONAL",  "NA-TIONAL", "REGION : MULTI-STATE", "REGION : SUB-STATE", "STATE","WATERSHED", or "ZIP CODE")
* <b>statisticcat_desc</b>: "Category" - The aspect of a commodity being measured (e.g., "AREA HAR-VESTED", "PRICE RECEIVED", "INVENTORY", "SALES").
* <b>state_name</b>: "State" - State full name.
* <b>asd_desc</b>: "Ag District" - Ag statistics district name.
* <b>county_name</b>: "County" - County name.
* <b>region_desc</b>: "Region" - NASS defined geographic entities not readily defined by other stan-dard geographic levels.  A region can be a less than a state (SUB-STATE) or agroup of states (MULTI-STATE), and may be specific to a commodity.
* <b>zip_5</b>: "Zip Code" - US Postal Service 5-digit zip code.
* <b>watershed_desc</b>: "Watershed" - Name assigned to the HUC.
* <b>year</b>: "Year" - The numeric year of the data and can be either a character or numericvector.
* <b>freq_desc</b>: "Period Type" - Length of time covered ("ANNUAL", "SEASON", "MONTHLY","WEEKLY", "POINT IN TIME").  "MONTHLY" often covers more than onemonth. "POINT IN TIME" is as of a particular day.
* <b>reference_period_desc</b>: "Period" - The specific time frame, within a freq_desc.
* <b>format</b>: Output format from API call.   Defaults to CSV as it is typically the smallestsized call.  Other options are JSON and XML but these are not recommended. 
* <b>numeric_vals</b>: Optional to convert the year, value, and coefficient of variation (CV %) to numerics as opposed to defaulted character values.  Default is to FALSE as some values have a suppression code. Converting to numeric will result in suppressed values to be NA. 

#### Return Value 
JSON object of query results

#### Examples
Get state values in 2012 for all of the values of agricultural land:<br>
` nass_data(<your API key>, agg_level_desc = "STATE", year = "2012",commodity_desc = "AG LAND", domain_desc = "VALUE") `<br><br>
Get county level values in 2012 for the specific data item:<br>
` nass_data(<your API key>, year = 2012, agg_level_desc = "COUNTY",short_desc = "AG LAND, INCL BUILDINGS - ASSET VALUE, MEASURED IN $") `

<hr>

### nass_param

#### Description
All possible values of a parameter for a given query. Helps to break down possible results from <em>nass_data</em>.<br>

#### Arguments
* Inital argument is your API key for NASS Quickstats
* <b>param</b>: A valid parameter value. Available names are: source_desc, sector_desc, group_desc,commodity_desc,  short_desc,  domain_desc,  domaincat_desc,  agg_level_desc,statisticcat_desc, state_name, asd_desc, county_name, region_desc, zip_5, wa-tershed_desc, year, freq_desc, and reference_period_desc.
* <b>source_desc</b>: "Program" - Source of data ("CENSUS" or "SURVEY").  Census program in-cludes the Census of Ag as well as follow up projects. Survey program includesnational, state, and county surveys.
* <b>sector_desc</b>: "Sector"  -  Five  high  level,  broad  categories  useful  to  narrow  down  choices.("ANIMALS & PRODUCTS", "CROPS", "DEMOGRAPHICS", "ECONOMICS",or "ENVIRONMENTAL")
* <b>group_desc</b>: "Group" - Subsets within sector (e.g., under sector_desc = "CROPS", the groupsare "FIELD CROPS", "FRUIT & TREE NUTS", "HORTICULTURE", and "VEG-ETABLES").
* <b>commodity_desc</b>: "Commodity"  -  The  primary  subject  of  interest  (e.g.,  "CORN",  "CATTLE","LABOR", "TRACTORS", "OPERATORS").
* <b>short_desc</b>: "Data Item" - A concatenation of six columns:  commodity_desc,  class_desc,prodn_practice_desc, util_practice_desc, statisticcat_desc, and unit_desc.
* <b>domain_desc</b>: "Domain" - Generally another characteristic of operations that produce a partic-ular commodity (e.g., "ECONOMIC CLASS", "AREA OPERATED", "NAICSCLASSIFICATION",  "SALES").   For  chemical  usage  data,  the  domain  de-scribes  the  type  of  chemical  applied  to  the  commodity.   The  domain_desc  ="TOTAL" will have no further breakouts; i.e., the data value pertains completelyto the short_desc.
* <b>domaincat_desc</b>: "Domain Category" - Categories or partitions within a domain (e.g., under do-main_desc = "SALES", domain categories include $1,000 TO $9,999, $10,000TO $19,999, etc).
* <b>agg_level_desc</b>: "Geographic Level" - Aggregation level or geographic granularity of the data.("AGRICULTURAL  DISTRICT",  "COUNTY",  "INTERNATIONAL",  "NA-TIONAL", "REGION : MULTI-STATE", "REGION : SUB-STATE", "STATE","WATERSHED", or "ZIP CODE")
* <b>statisticcat_desc</b>: "Category" - The aspect of a commodity being measured (e.g., "AREA HAR-VESTED", "PRICE RECEIVED", "INVENTORY", "SALES").
* <b>state_name</b>: "State" - State full name.
* <b>asd_desc</b>: "Ag District" - Ag statistics district name.
* <b>county_name</b>: "County" - County name.
* <b>region_desc</b>: "Region" - NASS defined geographic entities not readily defined by other stan-dard geographic levels.  A region can be a less than a state (SUB-STATE) or agroup of states (MULTI-STATE), and may be specific to a commodity.
* <b>zip_5</b>: "Zip Code" - US Postal Service 5-digit zip code.
* <b>watershed_desc</b>: "Watershed" - Name assigned to the HUC.
* <b>year</b>: "Year" - The numeric year of the data and can be either a character or numericvector.
* <b>freq_desc</b>: "Period Type" - Length of time covered ("ANNUAL", "SEASON", "MONTHLY","WEEKLY", "POINT IN TIME").  "MONTHLY" often covers more than onemonth. "POINT IN TIME" is as of a particular day.
* <b>reference_period_desc</b>: "Period" - The specific time frame, within a freq_desc.

#### Return Value
JSON object of all possible parameter values

#### Examples
Return the program sources for data:<br>
` nass_param(<your API key>, "source_desc") `<br><br>
Return the group categories available in the CROPS sector:<br>
` nass_param(<your API key>, param = "group_desc", sector_desc = "CROPS") `

<hr>
