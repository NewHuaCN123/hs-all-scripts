
"""  
Created on Tue Nov 01 11:15:00 2022

plot corrected NEXRAD time series

@author: Michael Getachew Tadesse
"""
import os
import glob
import distfit
import logging
import datetime
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.colors as mcolors
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from distfit import distfit
from sklearn.metrics import mean_squared_error


dir_home = "D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\Hazen and Sawyer\\"\
                "MIKE_Modeling_Group - Documents\\BCB\\data\\Rainfall\\"\
                        "bk_nexrad_gage\\bcb_east_of_model_domain_gages"
dir_nex = "E:\\NEXRAD"


os.chdir(dir_home)


dat = pd.read_csv('FKSTRN.csv')
dat['datetime'] = pd.to_datetime(dat['datetime'])


start = '2017-09-03 00:00:00'
end = '2017-09-17 00:00:00'


print(dat)

db_unq = dat['dbkey'].unique()
print(db_unq)


# plot just gages
plt.figure(figsize = (12,6))

isFirst = True
for db in db_unq:
    print(db)

    df = dat[dat['dbkey'] == db]

    print(df)

    # get the nexrad data
    os.chdir(dir_nex)
    nex = df['pixel'].unique()[0]
    

    nex_dat = pd.read_csv(nex)
    nex_dat['DateTime'] = pd.to_datetime(nex_dat['DateTime'])
    nex_dat = nex_dat[(nex_dat['DateTime'] >= start) & (nex_dat['DateTime'] <= end)]

    print(nex_dat)

    if isFirst:
        plt.plot(df['datetime'], df['value'], marker = 'o', 
                label = db, lw = 4, color = 'black')
        isFirst = False
    else:
        plt.plot(df['datetime'], df['value'], marker = 'o', 
                label = db, lw = 2, color = 'red')


plt.plot(nex_dat['DateTime'], nex_dat['RAIN'], label = nex, lw = 1.5, color = 'blue')
plt.legend()
plt.title('FKSTRN')
plt.show()