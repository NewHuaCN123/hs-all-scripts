"""  
Created on Wed Aug 10 17:33:00 2022

merge all swfwmd wells


@author: Michael Getachew Tadesse
"""

import os
import datetime
import pandas as pd 


dir_in = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\"\
                "SWFWMD\\GroundwaterLevelData\\ufa_081222\\parsed"
os.chdir(dir_in)

gList = os.listdir()

isFirst = True

for gg in gList:
    print(gg)

    dat = pd.read_csv(gg)
    dat.drop('Unnamed: 0', axis = 1, inplace = True)

    # limit time
    dat = dat[(dat['date'] >= '2011-01-01') & (dat['date'] <= '2017-12-31')]

    print(dat)
    
    if isFirst:
        df = dat
        isFirst = False
    else:
        df = pd.merge(df, dat, on = 'date', how = 'outer')


df = df.sort_values(by = 'date')
print(df)

df.to_csv('swfwmd_ufa_wells_GW_merged.csv')