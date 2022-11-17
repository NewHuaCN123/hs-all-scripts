"""  
Created on Wed Nov 16 10:54:00 2022

generate mesh of dataframes using the product from itertools
compute exceedance probability of rainfall and surge jointly

@author: Michael Getachew Tadesse

"""

import os
import numpy as np
import pandas as pd
import datetime
import seaborn as sns
from itertools import product
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.dates as mdates
 


sns.set_context('notebook', font_scale = 1.5)

os.chdir("D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\"\
                "Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
                        "BrowardRes\\scenarios_joint_probability\\virginia_key_data")


#####################################################
rain = pd.read_csv('vn239_3d_rainfall.csv')
rain['date'] = pd.to_datetime(rain['date'])

surge = pd.read_csv('virginia_keys_dmax_surge.csv')
surge['date'] = pd.to_datetime(surge['date'])
#####################################################


print(rain)
print(surge)

# merge rain and surge data
dat_merged = pd.merge(surge, rain, on='date', how='inner')
dat_merged = dat_merged[['date', 'value', 'max_surge']]
dat_merged.columns = ['date', 'rain_in', 'surge_m']
print(dat_merged)
print(len(dat_merged))

# get only positive surges
dat_merged = dat_merged[dat_merged['surge_m'] >= 0]
dat_merged.reset_index(inplace = True)

dat_merged.to_csv('rain_24h_surge_merged_positive_surges.csv')



# sort based on rain data
df = dat_merged[['rain_in', 'surge_m']]

# df = df.sort_values(by = ['rain_in'])
# df.reset_index(inplace = True)
# df = df[['rain_in', 'surge_m']]
# df['exd_prob'] = 'nan'
print(df.head(107))

# print(dat_merged['rain_in'].min(), dat_merged['rain_in'].max())
# print(dat_merged['surge_m'].min(), dat_merged['surge_m'].max())


# creating a dataframe of rain and surge combination (permutation)
dat_rain = np.arange(0, 15.1, 0.1)
dat_surge = np.arange(0, 1.2, 0.1)
# print(len(dat_rain))
# print(len(dat_surge))

mesh_dat = pd.DataFrame(list(product(dat_rain, dat_surge)))
mesh_dat.columns = ['rain_in', 'surge_m']
mesh_dat['exd_prob'] = 'nan'
mesh_dat['return_period'] = 'nan'

# print(mesh_dat)

# # compute exceedence prob
for ii in range(len(mesh_dat)):
    print(ii)

    print(df['rain_in'][ii], df['surge_m'][ii])
    # find the number of rows that exceed both rain and surge
    # for this row
    new_df = df[(df['rain_in'] >= mesh_dat['rain_in'][ii]) & 
                        (df['surge_m'] >= mesh_dat['surge_m'][ii])]
    print(new_df)

    # check if the dataframe is empty
    if len(new_df) == 0:
        continue
    else:
        prob = len(new_df)/len(df)
        # print(prob)

        # add calculated probability
        mesh_dat['exd_prob'][ii] = prob
        mesh_dat['return_period'][ii] = 1/prob

    # print(df)
mesh_dat.to_csv('rain_24h_positive_surge_joint_prob.csv')
