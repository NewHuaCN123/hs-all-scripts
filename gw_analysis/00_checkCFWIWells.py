import pandas as pd
import os


home = "R:\\40715-013 UKFPLOS\\Data\\CFWI"
os.chdir(home)

cfwi = pd.read_csv("ukb_cfwi_sa_ufa_merged.csv")
cfwi.columns = ['SITE_ID', 'site_name', 'TOTAL_DEPT', 'CASING_DEP', 'CASING_DIA',       
       'LAND_SURFA', 'RECORDER_T', 'lat', 'lon', 'HYPERLINK', 'SITE_STATU',    
       'WL_COLLECT', 'WL_COLLE_1', 'WQ_COLLECT', 'WQ_COLLE_1', 'COLLECTION',   
       'AQUIFER', 'HAS_LITHO', 'HAS_GEO', 'HAS_APT', 'FGS_NUMBER', 'USGS_SITE',
       'UPDATE_DAT', 'DMIT_WORK', 'OBJECTID', 'LATITUDE_D', 'LONGITUDE_',      
       'layer', 'path']
# print(cfwi.columns)

sf = pd.read_csv("ukb_sf_GW_sites_sa_ufa.csv")
sf.columns = ['DBKEY', 'site_name', 'TYPE', 'UNITS', 'FQ', 'STAT', 'STRATA', 'OPNUM',  
       'RCDR', 'AGENCY', 'START', 'END', 'CNTY', 'Lat', 'Long', 'Aquifer',    
       'zshift1']
# print(sf.columns)

swf = pd.read_csv("ukb_swf_sa_ufa.csv")
swf.columns = ['OBJECTID', 'SITE_ID', 'site_name', 'SITE_TYPE_', 'SITE_PRIMA',        
       'GIS_UPDATE', 'USGS_SITE_', 'LAND_SURFA', 'UTME', 'UTMN', 'SPFWE',     
       'SPFWN', 'LATITUDE', 'LONGITUDE', 'TOTAL_DEPT', 'CASING_DEP',
       'CASING_DIA', 'WELL_CASIN', 'WELL_TYPE_', 'WM_AQUIFER', 'DCS_SITE_S',  
       'EDPEXTERNA', 'SHAPE_1']
# print(swf.columns)

sjr = pd.read_csv("ukb_sjr_sa_int_ufa.csv")
sjr.columns = ['SITE_ID', 'site_name', 'STN_NM', 'LONG_NM', 'STATUS', 'STN_TYPE',       
       'LATITUDE', 'LONGITUDE', 'EVENT', 'FREQUENCY', 'HYDRON_NO',
       'COLL_AGNCY', 'PROJ_NM', 'MAJOR_BSN', 'MINOR_BSN', 'COUNTY', 'SOURCE']
# print(sjr.columns)


# print(cfwi)

# print(sf)

# print(swf)

# print(sjr)

cfwi_sf = pd.merge(cfwi, sf, on = 'site_name', how = 'inner')
cfwi_sf.to_csv('cfwi_sf.csv')
cfwi_swf = pd.merge(cfwi, swf, on = 'site_name', how = 'inner')
cfwi_swf.to_csv('cfwi_swf.csv')
cfwi_sjr = pd.merge(cfwi, sjr, on = 'site_name', how = 'inner')
cfwi_sjr.to_csv('cfwi_sjr.csv')

print(cfwi_sf)

print(cfwi_swf)
print(cfwi_sjr)