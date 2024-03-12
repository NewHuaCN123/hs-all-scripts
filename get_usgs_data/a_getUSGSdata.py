"""  
Created on Tue Mar 12 10:45:00 2024

Get USGS data from API

@author: Michael Getachew Tadesse

"""

import requests
import json
import os
import datetime
import pandas as pd
import seaborn as sns
from pprint import pprint 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import urllib.parse
import urllib.request 

## Method 1

usgs_water_api = "https://waterservices.usgs.gov/nwis/iv/?"\
                "format=json&sites=14128870&indent=on&siteStatus=all"
api_response = requests.get(usgs_water_api)

water_data = api_response.json()
pprint(water_data)

# site_name = water_data["value"]["timeSeries"][0]["sourceInfo"]["siteName"]
# date_time = water_data["value"]["timeSeries"][0]["values"][0]["value"][0]["dateTime"]
# station_id = water_data["value"]["timeSeries"][0]["sourceInfo"]["siteCode"][0]["value"]
# agency_code = water_data["value"]["timeSeries"][0]["sourceInfo"]["siteCode"][0]["agencyCode"]
# streamflow = water_data["value"]["timeSeries"][0]["values"][0]["value"][0]["value"]
# gage_height = water_data["value"]["timeSeries"][0]["values"][0]["value"][0]["value"]

# # Print the data
# # print(f"Site name: {site_name}")
# # print(f"Datetime: {date_time}")
# # print(f"Station ID: {station_id}")
# # print(f"Agency code: {agency_code}")
# # print(f"Streamflow (ft3/s): {streamflow}")
# # print(f"Gage height (ft): {gage_height}")



## Method 2

station_number = "05289800"
start_date = "2013-01-01"
end_date = "2024-03-01"


section1 = 'https://nwis.waterdata.usgs.gov/nwis/dv?referred_module=sw&search_site_no='
section2 = '&search_site_no_match_type=exact&site_tp_cd=OC&site_tp_cd=OC-CO&site_tp_cd=ES&site_tp_cd='\
'LK&site_tp_cd=ST&site_tp_cd=ST-CA&site_tp_cd=ST-DCH&site_tp_cd=ST-TS&index_pmcode_00060=1&group_key='\
'NONE&sitefile_output_format=html_table&column_name=agency_cd&column_name=site_no&column_name=station_nm&range_selection=date_range&begin_date='
section3 = '&end_date='
section4 = '&format=rdb&date_format=YYYY-MM-DD&rdb_compression=value&list_of_search_criteria=search_site_no%2Csite_tp_cd%2Crealtime_parameter_selection'


link = (section1 + station_number + section2 + start_date + section3 + end_date + section4)
print("Click here to see the generated USGS link: \n",link)

