"""  
Created on Tue Oct 24 09:26:00 2023

plot 3D surface

@author: Michael Getachew Tadesse

"""

import os
import datetime
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
 


sns.set_context('notebook', font_scale = 1.5)

os.chdir("C:\\Users\\mtadesse\\OneDrive - Hazen and Sawyer\\Documents\\UKBFPLOS")

obs = pd.read_csv("S65_obs.csv")
sim = pd.read_csv("S65_simulated.csv")
sim_go = pd.read_csv('S65_simulated_HW_TW_GO.csv')
obs_go = pd.read_csv('s65_combined_hw_tw_go.csv')
obs_go['datetime'] = pd.to_datetime(obs_go['datetime'])

obs_go = obs_go[(obs_go['datetime'] >= '2017-01-01') & (obs_go['datetime'] <= '2017-12-31')]


print(obs)
print(sim)

# # observed - flows
# fig = plt.figure(figsize=(12,12))
# ax = fig.add_subplot(111, projection='3d')
# # # Plot a 3D surface
# ax.scatter(obs['S65_H_ft'], obs['S65_T_ft'], obs['S65_Flow_cfs'], c= "blue")
# ax.set_xlabel('S65_H_ft', labelpad=20)
# ax.set_ylabel('S65_T_ft', labelpad=20)
# ax.set_zlabel('S65_Flow_cfs', labelpad=20)
# ax.set_title('S65 - Observed Stages + Flows')

# plt.show()

# # simulated - flowss
# fig = plt.figure(figsize=(12,12))
# ax = fig.add_subplot(111, projection='3d')
# # # Plot a 3D surface
# ax.scatter(sim['HW_ft'], sim['TW_ft'], sim['flow_cfs'], c= "red")
# ax.set_xlabel('HW_ft', labelpad=20)
# ax.set_ylabel('TW_ft', labelpad=20)
# ax.set_zlabel('flow_cfs', labelpad=20)
# ax.set_title('S65 - Simulated Stages + Flows')

# plt.show()


# simulated - gate opening
fig = plt.figure(figsize=(12,12))
ax = fig.add_subplot(111, projection='3d')
# # Plot a 3D surface
ax.scatter(sim_go['HW_ft'], sim_go['TW_ft'], sim_go['GO_ft'], c= "#458B00")
ax.set_xlabel('HW_ft', labelpad=20)
ax.set_ylabel('TW_ft', labelpad=20)
ax.set_zlabel('GO_ft', labelpad=20)
ax.set_title('S65 - Simulated Stages + Gate Opening')

plt.show()


# simulated - gate opening
fig = plt.figure(figsize=(12,12))
ax = fig.add_subplot(111, projection='3d')
# # Plot a 3D surface
ax.scatter(obs_go['HW_ft'], obs_go['TW_ft'], obs_go['GO_ft'], c= "#6495ED")
ax.set_xlabel('HW_ft', labelpad=20)
ax.set_ylabel('TW_ft', labelpad=20)
ax.set_zlabel('GO_ft', labelpad=20)
ax.set_title('S65 - Observed Stages + Gate Opening')
plt.show()