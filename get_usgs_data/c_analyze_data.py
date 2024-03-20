"""  
Created on Tue Mar 12 14:14:00 2024

Analyze the dam data

@author: Michael Getachew Tadesse

"""

import requests
import json
import os
import datetime
import pandas as pd
import seaborn as sns
from pprint import pprint 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import urllib.parse
import urllib.request 


os.chdir("C:\\Users\\mtadesse\\OneDrive - Hazen and Sawyer\\"\
            "Documents\\hs-all-scripts\\get_usgs_data")


print(os.listdir())

dat = pd.read_csv('GrandCouleeData.csv')
dat['DateTime'] = pd.to_datetime(dat['DateTime'])
# dat['month'] = pd.to_numeric(dat['datetime'].dt.month)

# qaqc
dat = dat.drop(dat[dat['gcl_fb'] > 20000].index)

print(dat['gcl_q'].describe())



plt.figure(figsize = (16,5))
# plt.plot(dat['DateTime'], dat['gcl_af'], c = 'k')
plt.plot(dat['DateTime'], dat['gcl_q'], c = 'red')
# plt.plot(dat['DateTime'], dat['gcl_q'], c = 'blue')
# plt.plot(dat['DateTime'], dat['gcl_qe'], c = 'green')
plt.show()



# print(dat)

# dat_melt = pd.melt(dat, id_vars= "month", value_vars = "Gage Height (feet)")
# print(dat_melt)

# # plt.figure(figsize = (16,5))
# # sns.boxplot(x="month", y="value", data = dat_melt)

# # plt.show()


# dat_grouped = dat.groupby('month').mean()
# print(dat_grouped)
# dat_grouped.reset_index(inplace = True)

# plt.figure(figsize = (16,5))
# plt.plot(dat_grouped['month'], dat_grouped['Gage Height (feet)'])
# plt.show()