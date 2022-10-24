
"""  
Created on Fri Oct 21 15:39:00 2022

get validation metrics

@author: Michael Getachew Tadesse
"""
import os
import glob
import distfit
import logging
import datetime
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error

###############
# set year here
yr = "2017"
###############


dir_home = "D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\Hazen and Sawyer\\"\
                "MIKE_Modeling_Group - Documents\\BCB\\data\\Rainfall\\"\
                        "bk_nexrad_gage\\corrected_nexrad"
dir_out = "D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\Hazen and Sawyer\\"\
                "MIKE_Modeling_Group - Documents\\BCB\\data\\Rainfall\\"\
                        "bk_nexrad_gage"


os.chdir(dir_home)

# get list of stations
gageList = glob.glob('./*.csv')
print(gageList)


# create new dataframe
df = pd.DataFrame(columns = ['id','corr_org', 'corr_new', 'mse_org', 'mse_new'])

isFirst = True

for gg in gageList:
    print(gg)

    dat = pd.read_csv(gg)
#     print(dat)

#     print("correlation", dat['gage'].corr(dat['nexrad']), dat['gage'].corr(dat['corrected']))
#     print("mean_squared_error", mean_squared_error(dat['gage'], dat['nexrad']), 
#                                 mean_squared_error(dat['gage'], dat['corrected']))
    id = gg.split('.csv')[0].split('.\\')[1]
    corr_org = dat['gage'].corr(dat['nexrad'])
    mse_org = mean_squared_error(dat['gage'], dat['nexrad'])
    corr_new = dat['gage'].corr(dat['corrected'])
    mse_new = mean_squared_error(dat['gage'], dat['corrected'])


    print("\n")

    new_df = pd.DataFrame([id, corr_org, corr_new, mse_org, mse_new]).T
    new_df.columns = ['id','corr_org', 'corr_new', 'mse_org', 'mse_new']


    if isFirst:
        df = new_df 
        isFirst = False
    else: 
        df = pd.concat([df, new_df])


print(df)

os.chdir(dir_out)

df.to_csv("validation_metrics.csv")
