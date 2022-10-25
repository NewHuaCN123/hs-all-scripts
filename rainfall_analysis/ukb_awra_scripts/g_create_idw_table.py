
"""  
Created on Thu Oct 25 11:15:00 2022

create a table with gage names and corresponding
values every 15 mins

this will be joined to the gages shapefile 

@author: Michael Getachew Tadesse
"""
import os
import glob
import logging
import datetime
import numpy
import pandas as pd
import seaborn as sns
import matplotlib.colors as mcolors
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

###############
# set year here
yr = "2011"
###############


dir_home = "R:\\40715-013 UKFPLOS\\Data\\Rainfall\\"\
                "NEXRAD_Gage_15min_comparison_correction_AWRA\\"\
                            "gage_bk_raw\\{}\\agg_15min".format(yr)

dir_out = "R:\\40715-013 UKFPLOS\\Data\\Rainfall\\"\
                "NEXRAD_Gage_15min_comparison_correction_AWRA\\"\
                            "gage_bk_raw\\{}".format(yr)

os.chdir(dir_out)
gInfo = pd.read_csv('{}_all_gages.csv'.format(yr))


os.chdir(dir_home)

gList = glob.glob('./*.csv')

print(gList)

isFirst = True

for gg in gList:
    print(gg)
    dat = pd.read_csv(gg)[['date', 'rain[in]']]

    col_name = gInfo[gInfo['DBKEY'] == gg.split('_')[0].split('.\\')[1]]['STATION'].values[0]
    print(col_name)

    dat.columns = ['date', col_name]
    # print(dat)

    if isFirst:
        df = dat
        isFirst = False
    else:
        df = pd.merge(df, dat, on = 'date', how = 'outer')
    

print(df)

os.chdir(dir_out)
new_df = df.T

# saving in parts
new_df.iloc[:, :500].to_csv('kriging_table_{}_1'.format(yr) + '.csv')
new_df.iloc[:, 500:1000].to_csv('kriging_table_{}_2'.format(yr) + '.csv')
new_df.iloc[:, 1000:1537].to_csv('kriging_table_{}_3'.format(yr) + '.csv')