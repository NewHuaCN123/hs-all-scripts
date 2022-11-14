"""  
Created on Mon Nov 11 10:21:00 2022

plot rainfall and surge data for Virginia Keys 

@author: Michael Getachew Tadesse

"""

import pandas as pd
import os
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
 


sns.set_context('notebook', font_scale = 1.5)

os.chdir("D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\Hazen and Sawyer\\"\
                "MIKE_Modeling_Group - Documents\\BrowardRes\\"\
                        "scenarios_joint_probability\\virginia_key_data")


rain = pd.read_csv('vn239_3d_rainfall.csv')
rain['date'] = pd.to_datetime(rain['date'])

surge = pd.read_csv('virginia_keys_dmax_surge.csv')
surge['date'] = pd.to_datetime(surge['date'])

print(rain)
print(surge)

# merge rain and surge data
dat_merged = pd.merge(rain, surge, on='date', how='inner')
dat_merged = dat_merged[['date', 'value', 'agg_3d', 'max_surge']]
dat_merged.columns = ['date', 'rain_in', 'rain_agg_3d', 'surge_m']
# dat_merged = dat_merged[~dat_merged['rain_agg_3d'].isna()]
print(dat_merged)


sns.set()
sns.jointplot(dat_merged['rain_agg_3d'], dat_merged['surge_m'], kind = 'kde', color = 'red').plot_joint(sns.scatterplot)
plt.show()

sns.jointplot(dat_merged['rain_in'], dat_merged['surge_m'], kind = 'kde', color = 'red').plot_joint(sns.scatterplot)
plt.show()

def plotIt():
    plt.figure(figsize = (12,5))
    plt.scatter(dat_merged['rain_agg_3d'],dat_merged['surge_m'], color = 'k')
    plt.xlabel('Three Day Accumulated Rainfall (in)')
    plt.ylabel('Daily Maximum Surge (m)')
    plt.grid()
    plt.show()


# plotIt()

# get stats
print(len(dat_merged[((dat_merged['rain_agg_3d']) > 0 & (dat_merged['rain_agg_3d'] <= 2.5)) &
                        ((dat_merged['surge_m'] > 0)  & (dat_merged['surge_m'] <= 0.5))]))

print(len(dat_merged[(dat_merged['rain_agg_3d'] > 2.5) & (dat_merged['rain_agg_3d'] <= 5.0) & 
                        (dat_merged['surge_m'] > 0)  & (dat_merged['surge_m'] <= 0.5)]))

print(len(dat_merged[(dat_merged['rain_agg_3d'] > 0) & (dat_merged['rain_agg_3d'] <= 2.5) & 
                        (dat_merged['surge_m'] > 0.5)  & (dat_merged['surge_m'] <= 1)]))

print(len(dat_merged[(dat_merged['rain_agg_3d'] > 2.5) & (dat_merged['rain_agg_3d'] <= 5) & 
                        (dat_merged['surge_m'] > 0.5)  & (dat_merged['surge_m'] <= 1)]))

print(len(dat_merged[(dat_merged['rain_agg_3d'] > 5.0) & (dat_merged['surge_m'] > 0)]))

