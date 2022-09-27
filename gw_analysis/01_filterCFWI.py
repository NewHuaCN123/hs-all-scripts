import pandas as pd
import os


home = "R:\\40715-013 UKFPLOS\\Data\\CFWI\\cfwi_merged_ukb"
dir_cfwi = "R:\\40715-013 UKFPLOS\\Data\\CFWI"
os.chdir(home)

match = pd.read_csv("cfwi_matched_with_ukb.csv") # station names that matched with UKB

os.chdir(dir_cfwi)

cfwi = pd.read_csv("ukb_cfwi_sa_ufa_merged.csv")

cfwi.columns = ['SITE_ID', 'site_name', 'TOTAL_DEPT', 'CASING_DEP', 'CASING_DIA',       
       'LAND_SURFA', 'RECORDER_T', 'lat', 'lon', 'HYPERLINK', 'SITE_STATU',    
       'WL_COLLECT', 'WL_COLLE_1', 'WQ_COLLECT', 'WQ_COLLE_1', 'COLLECTION',   
       'AQUIFER', 'HAS_LITHO', 'HAS_GEO', 'HAS_APT', 'FGS_NUMBER', 'USGS_SITE',
       'UPDATE_DAT', 'DMIT_WORK', 'OBJECTID', 'LATITUDE_D', 'LONGITUDE_',      
       'layer', 'path']

print(match)

print(cfwi)


cfwi_matched = pd.merge(cfwi, match, on = 'site_name', how = 'outer')

os.chdir(home)
cfwi_matched.to_csv("cfwi_matched_unmatched.csv")