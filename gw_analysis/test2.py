import datetime
import os
import pandas as pd 


dir_in = "R:\\40715-013 UKFPLOS\\Received_Data_Models"\
                "\\SWFWMD\\GroundwaterLevelData\\others"

os.chdir(dir_in)

shp = pd.read_csv("ukb_all_merged_wells_081122.csv")
swf = pd.read_csv("ukb_swf_GW_wells_ids.csv")

# print(shp)
# print(sf)

shp_dbkey = shp[(shp['layer'] == "ukb_swf_sa_ufa") | 
                        (shp['layer'] == "ukb_swf_wells_not_in_SHP")
                            ]['SITE_ID'].unique()

print(shp_dbkey, "\n")
print(len(shp_dbkey))


swfid = swf['sid'].astype(str).unique()

print(swfid, "\n")
print(len(swfid))


# shp_outlier = [x for x in shp_dbkey if x not in swfid]
# swf_outlier = [x for x in swfid if x not in shp_dbkey]

# print('swf_outlier')
# print(swf_outlier)
# print(len(swf_outlier))

# print('shp_outlier')
# print(shp_outlier)
# print(len(shp_outlier))

