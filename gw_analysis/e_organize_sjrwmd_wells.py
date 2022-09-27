"""  
Created on Wed Aug 11 07:53:00 2022

morganize sjrwmd wells


@author: Michael Getachew Tadesse
"""

import os
import datetime
import pandas as pd 


dir_in = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\"\
            "FromSJRWMD\\GroundWaterData\\from_seth_barr_sjrwmd"
os.chdir(dir_in)

dat = pd.read_csv("R.Rani.welldata_cleaned.CSV")
selected_wells = pd.read_csv("ukb_sjr_wells_seth_barr.csv")

# format the column
getStr = lambda x: x.split('.0')[0]
selected_wells['HYDRON_NO'] = selected_wells['HYDRON_NO'].astype(str)
selected_wells['HYDRON_NO'] = pd.DataFrame(list(map(getStr, selected_wells['HYDRON_NO'])))
print(selected_wells['HYDRON_NO'])

# convert selected wells to list
sjr_wells = selected_wells['HYDRON_NO'].tolist()
# print(sjr_wells)

# remove "unnamed" columns
col_names = dat.columns
col_unnamed = [x for x in col_names if "Unnamed:" in x]

dat = dat.drop(col_unnamed, axis = 1)

dat_sjr = dat[sjr_wells]

# print(dat)
# print(dat_sjr)

dat_sjr = pd.concat([dat['date'], dat_sjr], axis = 1)

print(dat_sjr)

# subset from 2011 to 2017
dat_sjr['date'] = pd.to_datetime(dat_sjr['date'])
print(dat_sjr)
dat_sjr_subset = dat_sjr[(dat_sjr['date'] >= '2011-01-01') & 
                            (dat_sjr['date'] <= '2017-12-31')]
print(dat_sjr_subset)

dat_sjr_subset.to_csv("sjrwmd_wells_GW_navd88.csv")