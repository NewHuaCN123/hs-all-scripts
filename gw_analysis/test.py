

import pandas as pd
import os

os.chdir("R:\\40715-013 UKFPLOS\\Data\\CFWI\\GW")

dat = pd.read_csv("Groundwater Sites (SFWMD) as of December 2021.csv")


os.chdir("R:\\40715-013 UKFPLOS\\Received_Data_Models\\FromSFWMD\\GW")

df = pd.read_csv("ukb_sf_GW_wells_sites_zshift_v4.csv")


print(dat)
print(dat.columns)
dat.columns = ['SITE ID', 'station_name', 'TOTAL DEPTH', 'CASING DEPTH',
       'CASING DIAMETER', 'LAND SURFACE ELEV', 'RECORDER TYPE', 'LATITUDE DMS',
       'LONGITUDE DMS', 'HYPERLINK', 'SITE STATUS DESC', 'WL COLLECTION START',
       'WL COLLECTION END', 'WQ COLLECTION START', 'WQ COLLECTION END',        
       'COLLECTION AGENCY', 'AQUIFER', 'HAS LITHO', 'HAS GEO', 'HAS APT',      
       'FGS NUMBER', 'USGS SITE NUMBER', 'UPDATE DATE', 'DMIT WORK PLAN SITE', 
       'x', 'y']
print(df)
print(df.columns) 

df.columns = ['DBKEY', 'station_name', 'TYPE', 'UNITS', 'FQ', 'STAT', 'STRATA', 'OPNUM',
       'RCDR', 'AGENCY', 'START', 'END', 'CNTY', 'Lat', 'Long', 'Aquifer',
       'zshift1']


dat_merged = pd.merge(dat, df, on = 'station_name', how = 'inner')

print(dat_merged)