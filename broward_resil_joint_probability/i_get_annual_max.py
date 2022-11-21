"""  
Created on Mon Nov 21 09:35:00 2022

get annual max surge

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


dat = pd.read_csv('virginia_keys_dmax_surge.csv')

print(dat)

getYear = lambda x: x.split('/')[2]
dat['yr'] = pd.DataFrame(list(map(getYear, dat['date'])))

print(dat)

years = dat['yr'].unique()
print(years)


df = pd.DataFrame(columns = ['year', 'amax'])

isFirst = True
for y in years:
    print(y)

    y_dat = dat[dat['yr'] == y]

    print(y_dat)

    y_amax = y_dat['max_surge'].max()

    new_df = pd.DataFrame([y, y_amax]).T
    new_df.columns = ['year', 'amax']

    if isFirst:
        df = new_df
        isFirst = False
    else:
        df = pd.concat([df, new_df], axis = 0)
        

print(df)
df.to_csv('virginia_keys_amax_surge.csv')

plt.figure(figsize = (12,5))
plt.plot(df['year'], df['amax'])
plt.show()