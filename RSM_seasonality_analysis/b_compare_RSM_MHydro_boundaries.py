"""  
Created on Tue Sep 28 08:47:00 2023

Data analysis
compare the boundary conditions of what is in
the RP models vs the RSM boundary condition

@author: Michael Getachew Tadesse

"""

import os
import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline  


dir_in = "R:\\40715-021\\Modeling\\Data\\RSM_boundary_data"
dir_out = "R:\\40715-021\\Modeling\\Data\\RSM_boundary_data\\figures\\S40_Sep"

os.chdir(dir_in)

# rsm data
rsm = pd.read_csv('216Project_ReachA_Broward_4analysis.csv')
rsm['datetime'] = pd.to_datetime(rsm['datetime'])
rsm['Year'] = rsm['datetime'].dt.strftime('%Y')
rsm['Mon'] = rsm['datetime'].dt.strftime('%m')
rsm['day'] = rsm['datetime'].dt.strftime('%d')

# print(rsm)

# MHydro data
s39_mhydro = pd.read_csv('S39_MHydro.csv')
s39_mhydro['datetime'] = pd.to_datetime(s39_mhydro['datetime'])
s39_mhydro['Year'] = s39_mhydro['datetime'].dt.strftime('%Y')
s39_mhydro['Mon'] = s39_mhydro['datetime'].dt.strftime('%m')
s39_mhydro['day'] = s39_mhydro['datetime'].dt.strftime('%d')

s40_mhydro = pd.read_csv('S40_MHydro.csv')
s40_mhydro['datetime'] = pd.to_datetime(s40_mhydro['datetime'])
s40_mhydro['Year'] = s40_mhydro['datetime'].dt.strftime('%Y')
s40_mhydro['Mon'] = s40_mhydro['datetime'].dt.strftime('%m')
s40_mhydro['day'] = s40_mhydro['datetime'].dt.strftime('%d')

# print(s39_mhydro)
# print(s40_mhydro)

# # pick data to plot
# year = '1999'
# month = '09'


# # multiple plots
# for yr in range(1965, 2017):
#     print(yr)
#     month = '09'

#     rsm_new = rsm[(rsm['Year'] == str(yr)) & (rsm['Mon'] == month)]
#     s40_mhydro = s40_mhydro[(s40_mhydro['Mon'] == month)]
#     print(s40_mhydro)
#     s40_mhydro_new = s40_mhydro.groupby('day').mean()
#     s40_mhydro_new.reset_index(inplace = True)
#     s40_mhydro_new = s40_mhydro_new[['day', 'value']]

#     print(rsm)
#     print(s40_mhydro)


#     # plot
#     plt.figure(figsize = (14,6))
#     plt.plot(rsm_new['day'], rsm_new['S40_HW_ecb'], label= 'S40_HW_ecb', c = 'blue')
#     plt.plot(rsm_new['day'], rsm_new['S40_HW_fwoi'], label= 'S40_HW_fwoi', c = 'red')
#     plt.plot(s40_mhydro_new['day'], s40_mhydro_new['value'], label= 's40_mhydro', c = 'k')
#     plt.legend()
#     # plt.grid()
#     plt.title(yr)
#     # plt.show()

#     os.chdir(dir_out)
#     plt.savefig("S40_{}.jpeg".format(yr))


# # plotting just one ensemble
# month = '09'
# s40_mhydro = s40_mhydro[(s40_mhydro['Mon'] == month)]

# plt.figure(figsize = (14,6))
# plt.plot(s40_mhydro['day'], s40_mhydro['value'], label= 's40_mhydro', c = 'k')

# # multiple plots
# for yr in range(1965, 2017):
#     print(yr)

#     rsm_new = rsm[(rsm['Year'] == str(yr)) & (rsm['Mon'] == month)]
#     print(rsm)
#     print(s40_mhydro)


#     # plot
#     plt.plot(rsm_new['day'], rsm_new['S40_HW_ecb'])
#     plt.plot(rsm_new['day'], rsm_new['S40_HW_fwoi'])
#     # plt.grid()
#     # plt.title(yr)

#     # os.chdir(dir_out)
#     # plt.savefig("S40_{}.jpeg".format(yr))
# plt.show()
# # plt.legend()


# compiling all the data to get 90th percentile

rsm_ecb = pd.DataFrame()

isFirst = True
for yr in range(1965, 2017):
    print(yr)
    month = '09'

    rsm_ecb_new = rsm[(rsm['Year'] == str(yr)) & (rsm['Mon'] == month)]
    rsm_ecb_new.reset_index(inplace = True)
    rsm_ecb_new = rsm_ecb_new[['day', 'S40_HW_fwoi']]
    rsm_ecb_new.columns = ['day', yr]

    if isFirst:
        rsm_ecb = rsm_ecb_new
        isFirst = False
    else:
        rsm_ecb = pd.concat([rsm_ecb, rsm_ecb_new[yr]], axis = 1)

print(rsm_ecb)

# avg
rsm_ecb['avg'] = rsm_ecb.iloc[:,1:53].mean(axis = 1)
# 90th percentile
rsm_ecb['p_90'] = rsm_ecb.iloc[:,1:53].quantile(0.9, axis = 1)
# 95th percentile
rsm_ecb['p_95'] = rsm_ecb.iloc[:,1:53].quantile(0.95, axis = 1)



print(rsm_ecb)


s40_mhydro = s40_mhydro[(s40_mhydro['Mon'] == '09')]
print(s40_mhydro)
s40_mhydro_new = s40_mhydro.groupby('day').mean()
s40_mhydro_new.reset_index(inplace = True)
s40_mhydro_new = s40_mhydro_new[['day', 'value']]
print(s40_mhydro_new['value'].max())

s39_mhydro = s39_mhydro[(s39_mhydro['Mon'] == '09')]
print(s39_mhydro)
s39_mhydro_new = s39_mhydro.groupby('day').mean()
s39_mhydro_new.reset_index(inplace = True)
s39_mhydro_new = s39_mhydro_new[['day', 'value']]



# # plot
# plt.figure(figsize = (14,6))
# plt.plot(rsm_ecb['day'], rsm_ecb['avg'], label= 'S40_Avg_fwoi', c = 'blue')
# plt.plot(rsm_ecb['day'], rsm_ecb['p_90'], label= 'S40_90th_fwoi', c = 'red')
# plt.plot(rsm_ecb['day'], rsm_ecb['p_95'], label= 'S40_95th_fwoi', c = 'green')
# # plt.plot(rsm.iloc[:,0], rsm['S-39_HW_fwoi'], label= 'S-39_HW_fwoi', c = 'red')
# plt.plot(s40_mhydro_new.iloc[:,0], s40_mhydro_new['value'], label= 's40_mhydro', c = 'k')
# plt.legend()
# # plt.grid()
# plt.show()
