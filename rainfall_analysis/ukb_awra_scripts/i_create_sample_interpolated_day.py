
"""  
Created on Thu Oct 26 08:37:00 2022

create a day of interpolated rain gage data
for plotting purposes

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

###############
# set date here
dt = "2017-09-10 10:30:00"
###############


dir_home = "R:\\40715-013 UKFPLOS\\Data\\Rainfall\\"\
                "NEXRAD_Gage_15min_comparison_correction_AWRA\\"\
                            "gage_interpolated_pixels\\{}".format(yr)

dir_out = "R:\\40715-013 UKFPLOS\\Data\\Rainfall\\"\
                "NEXRAD_Gage_15min_comparison_correction_AWRA\\"\
                        "gage_interpolated_pixels\\interpolated_4_figure"

os.chdir(dir_home)

pList = os.listdir()

isFirst = True
for pp in pList:
    print(pp)

    dat = pd.read_csv(pp)
    # print(dat)

    df = dat[dat['date'] == dt]
    df.reset_index(inplace = True)
    # print(df)

    # print(pp.split('.csv')[0])

    new_df = pd.DataFrame([pp.split('.csv')[0], df['value'].values[0]]).T
    new_df.columns = ['pixel', 'value']

    if isFirst:
        df_final = new_df
        isFirst = False
    else:
        df_final = pd.concat([df_final, new_df], axis = 0)
    
print(df_final)


os.chdir(dir_out)
df_final.to_csv("interp_201709101030.csv")

