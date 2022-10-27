
"""  
Created on Thu Oct 27 14:25:00 2022

compare and plot timeseries

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



os.chdir("D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\Hazen and Sawyer\\"\
                "MIKE_Modeling_Group - Documents\\BCB\\data\\Rainfall\\"\
                            "bk_nexrad_gage\\lee_county_gages")

start = '2017-09-03 00:00:00'
end = '2017-09-17 00:00:00'


nex = pd.read_csv('pix10057703.csv')
nex['datetime'] = pd.to_datetime(nex['DateTime'])
nex = nex[(nex['datetime'] >= start) & (nex['datetime'] <= end)]
nex = nex[['datetime', 'RAIN']]



gage = pd.read_csv('three_oaks.csv')
gage['datetime'] = pd.to_datetime(gage['DateTime'])
gage = gage[(gage['datetime'] >= start) & (gage['datetime'] <= end)]
gage = gage[['datetime', 'Rainfall']]
print(nex)
print(gage)



dat_merged = pd.merge(gage, nex, on = 'datetime', how = 'inner')

print(dat_merged)

plt.figure(figsize = (12,6))
plt.plot(dat_merged['datetime'], dat_merged['Rainfall'], label = 'Gage', color = 'blue')
plt.plot(dat_merged['datetime'], dat_merged['RAIN'], label = 'NEXRAD', color ='red')
plt.title('three_oaks')
plt.legend()
plt.grid()
plt.show()
