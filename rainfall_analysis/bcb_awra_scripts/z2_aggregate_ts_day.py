
"""  
Created on Fri Oct 31 09:53:00 2022

aggregate timeseries to a day

@author: Michael Getachew Tadesse
"""
import os
import logging
import datetime
import numpy
import pandas as pd
import seaborn as sns
import matplotlib.colors as mcolors
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error



dir_home = "D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\Hazen and Sawyer\\"\
                "MIKE_Modeling_Group - Documents\\BCB\\data\\Rainfall\\"\
                            "bk_nexrad_gage\\gage\\ver2\\gages_extracted"

collier_cnty = "D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\Hazen and Sawyer\\"\
                    "MIKE_Modeling_Group - Documents\\BCB\\data\\Rainfall\\"\
                            "bk_nexrad_gage\\collier_county_gages"

dir_nex = "D:\\MIKE_Modeling_Files\\"\
                "Hazen and Sawyer\\Hazen and Sawyer\\"\
                        "MIKE_Modeling_Group - Documents\\BCB\\data\\NEXRAD\\part3"

os.chdir(dir_home)

dat = pd.read_csv('COLGOV_R.csv')


dat = dat[dat['dbkey'] == 'VM982']
dat = dat[['datetime', 'value']]
dat['datetime'] = pd.to_datetime(dat['datetime'])
print(dat)



# aggregate data every day
dat.set_index('datetime', inplace = True)
print(dat)

# nex_agg_15m = nex_data.groupby(pd.Grouper(freq='15Min')).aggregate(numpy.sum)
dat_agg_daily = dat.resample("24H").sum()
dat_agg_daily.reset_index(inplace = True)
print(dat_agg_daily)


# get collier county data
os.chdir(collier_cnty)
df = pd.read_csv('naples_86078_2017_9_3_2017.csv')
print(df.columns)
df['datetime'] = pd.to_datetime(df['datetime'])
print(df)


# get nexrad data
os.chdir(dir_nex)
dat_nex = pd.read_csv('pix10051067.csv')
dat_nex = dat_nex[(dat_nex['DateTime'] >= '2017-09-03 00:00:00') & (dat_nex['DateTime'] <= '2017-09-19 00:00:00')]
dat_nex = dat_nex[['DateTime', 'RAIN']]
dat_nex['DateTime'] = pd.to_datetime(dat_nex['DateTime'])
dat_nex.set_index('DateTime', inplace = True)


nex_agg_daily = dat_nex.resample("24H").sum()
nex_agg_daily.reset_index(inplace = True)
print(nex_agg_daily)



print(nex_agg_daily)



plt.figure(figsize = (12, 6))
plt.plot(dat_agg_daily['datetime'], dat_agg_daily['value'], label = 'COLGOV_R', color = 'blue')
plt.plot(df['datetime'], df[' precipitation'], label = '86078-FCC', color = 'red')
plt.plot(nex_agg_daily['DateTime'], nex_agg_daily['RAIN'], label = '10050120', color = 'black')
plt.ylabel('Daily Rainfall (in)')
plt.legend()
plt.grid()
plt.show()
