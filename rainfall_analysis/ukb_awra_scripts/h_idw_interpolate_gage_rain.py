
"""  
Created on Thu Oct 25 15:17:00 2022

interpolate the rain gage data using IDW

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
yr = "2017"
###############


dir_info = "R:\\40715-013 UKFPLOS\\Data\\Rainfall\\"\
                    "NEXRAD_Gage_15min_comparison_correction_AWRA\\gage_bk_raw"

dir_gage = "R:\\40715-013 UKFPLOS\\Data\\Rainfall\\"\
                    "NEXRAD_Gage_15min_comparison_correction_AWRA\\gage_bk_raw\\"\
                                    "{}\\agg_15min".format(yr)

dir_out = "R:\\40715-013 UKFPLOS\\Data\\Rainfall\\"\
                "NEXRAD_Gage_15min_comparison_correction_AWRA\\"\
                            "gage_interpolated_pixels\\{}".format(yr)



os.chdir(dir_info)
gInfo = pd.read_csv('ukb_nexrad_weights.csv')

print(gInfo)


# get all the gages data first
os.chdir(dir_gage)

gList = glob.glob('./*.csv')
print(gList)

isFirst = True
for gg in gList:
    print(gg)
    
    col_name = gg.split('.\\')[1].split("_")[0]
    dat = pd.read_csv(gg)[['date', 'rain[in]']]
    dat.columns = ['date', col_name]


    if isFirst:
        df = dat
        isFirst = False
    else:
        df = pd.merge(df, dat, on = 'date', how = 'outer')
print(df)


# get the columns of the gages names
col_unq = df.columns[1:]
print(col_unq)

for pp in gInfo['pixel']:

    new_df = gInfo[gInfo['pixel'] == pp]
    # print(new_df)

    # get a copy of the rain gage data (concatenated in one dataframe)
    df_modified = df.copy()


    # check if pixel lies in the same location as gage
    # in this case assign the gage rain to it
    if new_df['sum'].values[0] == "#DIV/0!":

        # find the column that is causing error
        col_nan = new_df.columns[new_df.eq("#DIV/0!").any()][0]

        # assign the gage rain to the pixel
        df_final = pd.concat([df_modified['date'], df[col_nan]], axis = 1)
        df_final.columns = ['date', 'value']
        print(df_final)
        
        os.chdir(dir_out)
        df_final.to_csv(str(pp) + '.csv')
        
        continue


    for cc in col_unq:
        print(pp, cc)
        
        factor = float(new_df[cc].values[0])
            

        df_modified[cc] = df_modified[cc] * factor
        denominator = 1/(float(new_df['sum'].values[0]))

    df_final = pd.concat([df_modified['date'], 
                    denominator*df_modified.iloc[:,1:].sum(axis = 1)], axis = 1)
    df_final.columns = ['date', 'value']

    print(df_final)

    # save interpolated gage value
    os.chdir(dir_out)

    df_final.to_csv(str(pp) + '.csv')


