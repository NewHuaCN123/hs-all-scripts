
"""  
Created on Wed Mar 01 15:12:00 2023

compare sim and obs GW analysis

@author: Michael Getachew Tadesse
"""

import os
import pandas as pd
from sklearn.metrics import mean_absolute_error



dir_home = 'R:\\40715-010\\Data\\gw_simulated_daily_average'
dir_obs = 'R:\\40715-010\\Data\\gw_simulated_daily_average\\obs_TS'
dir_out = 'R:\\40715-010\\Data\\gw_simulated_daily_average\\sim_obs_merged'

os.chdir(dir_home)

dat_layer = pd.read_csv('GW_stations_layer_data.csv')
print(dat_layer)

dat_sim = pd.read_csv('bcb_0301_run_SZ_detailed_TS.csv')
print(dat_sim)

#create empty datafrmae 

stat = pd.DataFrame(columns = ['name', 'mae'])
isFirst = True

for ii in range(len(dat_layer['Name'])):
    print(dat_layer['Name'][ii], dat_layer['byLayer'][ii])

    name = dat_layer['Name'][ii]
    layer = dat_layer['byLayer'][ii].lower()

    # get obs data
    os.chdir(dir_obs)

    dat_obs = pd.read_csv(layer + ".csv")


    if name in dat_obs.columns:
        df_obs = dat_obs[['datetime', name]]
        # convert feet to meter
        df_obs[name] = df_obs[name] * 0.3048
        df_obs.columns = ['datetime', name+"_obs"]
        df_obs['datetime'] = pd.to_datetime(df_obs['datetime'])

        
        # print(df_obs)
    else:
        continue
    
    # get sim data
    if name in dat_sim.columns:
        df_sim = dat_sim[['date', name]]
        df_sim.columns = ['datetime', name+"_sim"]
        df_sim['datetime'] = pd.to_datetime(df_sim['datetime'])
        # print(df_sim)
    else:
        continue


    # merge obs and sim
    dat_merge = pd.merge(df_obs, df_sim, on = 'datetime', how = 'inner')
    # print(dat_merge)

    # delete rows with nans
    nan_index = dat_merge[dat_merge.isna().any(axis=1)].index

    print(nan_index)

    dat_merge_clean = dat_merge.drop(nan_index, axis = 0)

    if len(dat_merge_clean) != 0:
        os.chdir(dir_out)
        # dat_merge_clean.to_csv(name + ".csv")
        # print(dat_merge_clean)
    else:
        continue

    mae = mean_absolute_error(dat_merge_clean.iloc[:,1], dat_merge_clean.iloc[:,2])
    new_df = pd.DataFrame([name, mae]).T
    new_df.columns = ['name', 'mae']

    if isFirst:
        stat = new_df
        isFirst = False 
    else:
        stat = pd.concat([stat, new_df], axis = 0)
    

os.chdir(dir_home)
stat.to_csv('gw_sim_obs_stats.csv')

