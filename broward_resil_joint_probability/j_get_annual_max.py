"""  
Created on Mon Nov 21 11:10:00 2022

get annual max values of the 24-hr

@author: Michael Getachew Tadesse

"""

import os
import numpy as np
import pandas as pd
import datetime
import seaborn as sns
from itertools import product
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib import rcParams
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.dates as mdates
import plotly.graph_objects as go
 


sns.set_context('notebook', font_scale = 1.5)

os.chdir("D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\"\
                "Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
                        "BrowardRes\\scenarios_joint_probability\\virginia_key_data")


dat = pd.read_csv('G54_rainfall.csv')

print(dat)

dat['date'] = pd.to_datetime(dat['Daily Date'])
print(dat)
getYear = lambda x: x.split('-')[0]
dat['yr'] = pd.DatetimeIndex(dat['date']).year
print(dat)



years = dat['yr'].unique()
print(years)


df = pd.DataFrame(columns = ['year', 'amax'])

isFirst = True
for y in years:
    print(y)

    y_dat = dat[dat['yr'] == y]

    print(y_dat)

    y_amax = y_dat['Data Value'].max()

    new_df = pd.DataFrame([y, y_amax]).T
    new_df.columns = ['year', 'amax']

    if isFirst:
        df = new_df
        isFirst = False
    else:
        df = pd.concat([df, new_df], axis = 0)
        

print(df)
# df.to_csv('G54_rainfall_amax.csv')

plt.figure(figsize = (12,5))
df['year'] = pd.to_datetime(df['year'])
print(df)
print(dat)
# dat['date'] pd.to_datetime(dat['date'])
# plt.plot(df['year'], df['amax'])
plt.plot(dat['date'], dat['Data Value'])
plt.show()

