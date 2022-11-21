"""  
Created on Mon Nov 11 15:38:00 2022

plotting rainfall and surge time series

doing correlation analysis for these variables

plotting 3D joint histogram

@author: Michael Getachew Tadesse

"""

import os
import numpy as np
import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_toolkits.mplot3d import Axes3D
 


sns.set_context('notebook', font_scale = 1.5)

os.chdir("D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\"\
                "Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
                        "BrowardRes\\scenarios_joint_probability\\virginia_key_data")

surge = pd.read_csv('virginia_keys_dmax_surge.csv')
surge['date'] = pd.to_datetime(surge['date'])
print(surge)

rain = pd.read_csv('G54_rainfall.csv')
rain['date'] = pd.to_datetime(rain['date'])
print(rain)


# merge rain and surge data
dat_merged = pd.merge(surge, rain, on='date', how='inner')
dat_merged = dat_merged[['date', 'rain_in', 'max_surge']]
dat_merged.columns = ['date', 'rain_in', 'surge_m']
print(dat_merged)

# # plot
# sns.set()
# plt.figure(figsize = (12,6))
# plt.plot(surge['date'], surge['max_surge'], color = 'black')
# plt.ylabel('Daily Maximum Surge [m]')
# plt.grid()
# plt.show()



# # plot
# sns.set()
# plt.figure(figsize = (10,6))
# # plt.scatter(dat_merged['rain_in'], dat_merged['surge_m'])
# plt.xlabel('Daily Rainfall [in]')
# plt.ylabel('Daily Max Surge [m]')
# plt.grid()
# plt.show()

def plot3D():
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        hist, xedges, yedges = np.histogram2d(dat_merged['rain_in'], dat_merged['surge_m'], 
                                                        bins=20, range=[[0, 2], [-1, 1]])
        xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25)
        xpos = xpos.flatten('F')
        ypos = ypos.flatten('F')
        zpos = np.zeros_like(xpos)


        # Construct arrays with the dimensions for the 16 bars.
        dx = 0.5 * np.ones_like(zpos)
        dy = dx.copy()
        dz = hist.flatten()

        ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')
        ax.set_xlabel('Rain[in]')
        ax.set_ylabel('Surge[m]')

        plt.show()

plot3D()


sns.jointplot(dat_merged['rain_in'], dat_merged['surge_m'], 
                kind = 'kde', color = 'red').plot_joint(sns.scatterplot)
plt.show()