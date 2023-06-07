"""  
Created on Mon Nov 30 15:39:00 2022

plot well timeseries of groundwater stages

@author: Michael Getachew Tadesse

"""

import pandas as pd
import os
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
 


sns.set_context('notebook', font_scale = 1.5)

os.chdir("R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\GW")

dat = pd.read_csv("ufa_wells_2011_transposed.csv")
dat['datetime'] = pd.to_datetime(dat['datetime'])

print(dat)



cols = dat.columns[1:]

# west central
# cols = ['3491', '11424', '25370', 'AO616', '24723', '3543']

# # north east
# cols = ['TO065', '37315', '3545', '3555', '3571', '3575', '11522218']

# # south east 
cols = ['TA837', 'O6378', 'AO644', 'PD409', 'PC156', 'VN339']

# central
# cols = ['JU765', 'PT092', 'TA835', 'WF809', 'O6370', 'PT526']

print(cols)


plt.figure(figsize = (12,5))

for ii in cols:
    plt.plot(dat['datetime'], dat[ii], label = ii)

plt.legend()
plt.show()