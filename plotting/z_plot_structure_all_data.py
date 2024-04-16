"""  
Created on Mon Aug 22 16:34:00 2022

plot time series - convert date to month while plotting

plotting joint distributions

@author: Michael Getachew Tadesse

"""

import pandas as pd
import os
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
 


os.chdir("C:\\Users\\mtadesse\\OneDrive - Hazen and Sawyer\\Section216\\Postprocessing")

dat = pd.read_csv("g56_data.csv")
datQ = dat[dat['Type'] == 'Discharge']
datHW = dat[dat['Type'] == 'HW']
datTW = dat[dat['Type'] == 'TW']

print(dat)
print(dat.columns)


plt.figure(figsize = (14, 6))

for q in dat.columns[2:]:
    print(q)

    plt.plot(datQ['RSLC, ft above 1992'], datQ[q])
# ax2 = plt.twinx()
# sns.lineplot(data = dat[''])

ax2 = plt.twinx()

for h in dat.columns[2:]:
    print(h)

    plt.plot(datHW['RSLC, ft above 1992'], datHW[h])


plt.show()