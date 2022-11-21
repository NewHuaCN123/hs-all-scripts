"""  
Created on Wed Nov 17 14:49:00 2022

compute the exceedance probabiity of daily maximum surge

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


#####################################################
dat = pd.read_csv('virginia_keys_dmax_surge.csv')
dat = dat[dat['max_surge'] >= 0]
dat.reset_index(inplace = True)
dat['date'] = pd.to_datetime(dat['date'])
print(dat)
#####################################################

# get rainfall data
#####################################################
df = pd.read_csv('vn239_3d_rainfall.csv')
df['date'] = pd.to_datetime(df['date'])
print(df)
#####################################################




def plotTimeSeries():

    sns.set()
    sns.set_context('notebook', font_scale = 1.75)
    plt.figure(figsize = (12,5))
    plt.plot(df['date'], df['value'], color = 'blue')
    plt.grid()
    plt.ylabel('Daily Rainfall (in)')
    plt.show()

# plotTimeSeries()

def calcExdProb():
    " calculate the exceedance probability"

    # calculate exceedance prob
    dat['exd_prob'] = 'nan'

    for ii in range(len(dat)):
        print(ii)

        df = dat[dat['max_surge'] >= dat['max_surge'][ii]]

        prob = len(df)/len(dat)

        dat['exd_prob'][ii] = prob

    print(df)


    dat_sorted = dat.sort_values(by = 'max_surge')
    dat_sorted['return_period'] = 1/dat_sorted['exd_prob']

    print(dat_sorted)

    sns.set(style="ticks")
    sns.set_context('notebook', font_scale = 1.75)
    plt.figure(figsize = (12,5))
    plt.plot(dat_sorted['max_surge'], dat_sorted['return_period'])
    plt.grid()
    plt.xlabel('Daily Maximum Surge (m)')
    plt.ylabel('Return Period (yrs)')
    plt.show()


calcExdProb()