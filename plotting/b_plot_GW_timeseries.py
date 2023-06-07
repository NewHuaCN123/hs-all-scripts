"""  
Created on Mon Apr 24 13:56:00 2023

plot GW time series

@author: Michael Getachew Tadesse

"""

import pandas as pd
import os
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
 


os.chdir('R:\\40715-010\\Data\\GW\\4ModelBC\\0424')

dat = pd.read_csv('GW_layer3_obs.csv')
dat['datetime'] = pd.to_datetime(dat['datetime'])
dat = dat[dat['datetime'] >= '2017-01-01']
cols = dat.columns[1:]

print(dat)
print(cols)


plt.figure(figsize = (12,5))


for ii in range(1, 15):
    print(cols[ii-1])
    print(dat)
    plt.plot(dat.iloc[:,0], dat.iloc[:, ii], label = cols[ii-1])
    
    plt.title(cols[ii-1])
    
    plt.show()


    
