
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
                            "bk_nexrad_gage\\lee_county_gages\\gages")

start = '2017-09-03 00:00:00'
end = '2017-09-17 00:00:00'


# nex = pd.read_csv('pix10057703.csv')
# nex['datetime'] = pd.to_datetime(nex['DateTime'])
# nex = nex[(nex['datetime'] >= start) & (nex['datetime'] <= end)]
# nex = nex[['datetime', 'RAIN']]


gList = os.listdir()


# plot just gages
plt.figure(figsize = (12,6))

for gg in gList:
    print(gg)

    gage = pd.read_csv(gg)
    gage['datetime'] = pd.to_datetime(gage['DateTime'])
    gage = gage[(gage['datetime'] >= start) & (gage['datetime'] <= end)]
    gage = gage[['datetime', 'Rainfall']]
    # print(nex)
    print(gage)

    if gg == "three_oaks.csv":
        plt.plot(gage['datetime'], gage['Rainfall'], marker = 'o', label = gg.split('.csv')[0], lw = 3, color = 'black')
    elif gg == "bonita_springs_utilities.csv":
        plt.plot(gage['datetime'], gage['Rainfall'], marker = 'o', label = gg.split('.csv')[0], lw = 3, color = 'red')
    elif gg == "corkscrew_water_plant.csv":
        plt.plot(gage['datetime'], gage['Rainfall'], marker = 'o', label = gg.split('.csv')[0], lw = 3, color = 'blue')
    else:
        plt.plot(gage['datetime'], gage['Rainfall'], label = gg.split('.csv')[0], lw = 1.5)

    
plt.ylabel('Rainfall Depth (in)')
plt.legend()
plt.grid()
plt.show()



# dat_merged = pd.merge(gage, nex, on = 'datetime', how = 'inner')

# print(dat_merged)

# plt.figure(figsize = (12,6))
# plt.plot(dat_merged['datetime'], dat_merged['Rainfall'], label = 'Gage', color = 'blue')
# plt.plot(dat_merged['datetime'], dat_merged['RAIN'], label = 'NEXRAD', color ='red')
# plt.title('three_oaks')
# plt.legend()
# plt.grid()
# plt.show()
