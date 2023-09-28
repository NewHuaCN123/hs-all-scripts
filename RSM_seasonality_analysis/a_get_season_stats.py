"""  
Created on Tue Sep 27 10:52:00 2023

Data analysis - seasonal stats etc 
Originally prepared for RSM boundary data

@author: Michael Getachew Tadesse

"""

import os
import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt  


dir_in = "R:\\40715-021\\Modeling\\Data\\RSM_boundary_data"


os.chdir(dir_in)

dat = pd.read_csv('216Project_ReachA_Broward_4analysis.csv')
dat['datetime'] = pd.to_datetime(dat['datetime'])

# dat['Year'] = dat['datetime'].dt.strftime('%Y')
# dat['Mon'] = dat['datetime'].dt.strftime('%m')


print(dat)

# grouping

# # by year
# dat_by_year = dat.groupby('Year').mean()
# dat_by_year = dat_by_year.iloc[:, :-1]
# dat_by_year.reset_index(inplace = True)
# dat_by_year.drop('datetime', axis = 1, inplace = True)
# print(dat_by_year)


# # by month
# dat_by_mon = dat.groupby('Mon').mean()
# dat_by_mon = dat_by_mon.iloc[:, :-1]
# dat_by_mon.reset_index(inplace = True)
# dat_by_mon.drop('datetime', axis = 1, inplace = True)
# print(dat_by_mon)


# plot it
# sns.set(font_scale=0.80)
plt.figure(figsize = (14,6))
plt.plot(dat.iloc[:,0], dat.iloc[:,1:], label= dat.columns.values[1:])
plt.legend()
# plt.grid()
plt.show()