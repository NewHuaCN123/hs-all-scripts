
"""
Created on Tue Jul 11 08:31:00 2023
modified on Mon Jul 24, 2023 09:10:00
modified on Mon Sep 11, 2023 15:13:00

To calculate the cumulative flow and plot it
To calculate the difference between observed 
and simulated cumulative flows

Updated: to calculate volume for each timestep by
considering the same flow rate unless it changes in the BK

Updated: to aggregate to daily/weekly/monthly values and then compute cumulative volume

@author: Michael Getachew Tadesse

"""

import numpy as np
import pandas as pd
import mikeio
import os 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

# observed file location can stay the same - avoid copying over everywhere
dir_obs = 'R:\\40715-010\\Data\\calibration_stats\\bcb_stat_summary\\0720\\flow_stats\\sw_obs'
dir_sim = 'R:\\40715-010\\Data\\calibration_stats\\bcb_stat_summary\\0828\\flow_stats'
dir_out = 'R:\\40715-010\\Data\\calibration_stats\\bcb_stat_summary\\0828\\flow_stats\\calculated_flows'
dir_table = 'R:\\40715-010\\Data\\calibration_stats\\bcb_stat_summary\\0810\\flow_stats'


# get simulated time series file
os.chdir(dir_sim)

####
# change
####
sim = pd.read_csv('BCB-MODEL-19DetailedTS_M11.csv')
print(sim)

# get station names
os.chdir(dir_table)
dat = pd.read_csv('SW_storing.csv')
stn = dat.station.unique()
# print(dat)
# print(stn)

# stn = ['GG1_Q', 'GG2_Q', 'GG3_Q',
#             'GG4/GOLDW4_Q','GOLDW5_Q',	
#                 'I75W1_Q',	'HC1_Q (Total)','COCO1_Q',	
#                         'COCO2_Q',	'COCO3_Q',	'FAKA_Q',	
#                             'HENDTAMI_Qtotal',	'CR951S_Q',	
#                                 'MIL3_Q',	'Barron293_Q',	'Imperia1_Q', 'FU-6_Q']


stn = ['COCO2_Q']

for ss in stn:
    print(ss)

    # get observed time series
    stnRow = dat[dat['station'] == ss]
    stnFile = stnRow['fileName'].values[0]

    
    if pd.isnull(stnFile):
        continue

    stnFile = stnFile.split('.dfs0')[0] + ".csv"
    # print(stnFile)

    os.chdir(dir_obs)
    obs = pd.read_csv(stnFile)
    # obs = obs[['datetime', 'value']]
    obs.columns = ['datetime', 'Obs']
    obs['datetime'] = pd.to_datetime(obs['datetime'])
    # print(obs)

    # aggregate sim timeseries
    obs.set_index(obs['datetime'], inplace = True)
    obs_agg = pd.DataFrame(obs.iloc[:,1].resample('W').mean())
    # print(obs_agg)



    # get simulated time series
    sim_dat = sim.filter(['Time', ss])
    # print(sim_dat)


    sim_dat.columns = ['datetime', 'Sim']
    # print(sim_dat)

    # # get year-month-date
    # getDate = lambda x: x.split(' ')[0]
    # sim_dat['datetime'] = pd.DataFrame(map(getDate, sim_dat['datetime']))
    
    # # if units are in cms
    # sim_dat['Sim'] = sim_dat['Sim']*35.314666212661
   
    # if units are in cfs
    sim_dat['Sim'] = sim_dat['Sim']

    sim_dat['datetime'] = pd.to_datetime(sim_dat['datetime'])
    # print(sim_dat)
    
    # aggregate sim timeseries
    sim_dat.set_index(sim_dat['datetime'], inplace = True)
    sim_agg = pd.DataFrame(sim_dat.iloc[:,1].resample('W').mean())
    # print(sim_agg)

    # get the date columns back
    obs_agg.reset_index(inplace = True)
    sim_agg.reset_index(inplace = True)

    # # original dates
    obs = obs[(obs['datetime'] >= '2017-07-01') & (obs['datetime'] <= '2020-12-31')]
    sim_dat = sim_dat[(sim_dat['datetime'] >= '2017-07-01') & (sim_dat['datetime'] <= '2020-12-31')]

    # # # when looking at a unique date
    # obs_agg = obs_agg[(obs_agg['datetime'] >= '2018-08-01') & (obs_agg['datetime'] <= '2020-12-31')]
    # sim_agg = sim_agg[(sim_agg['datetime'] >= '2018-08-01') & (sim_agg['datetime'] <= '2020-12-31')]

    # print(obs_agg)
    # print(sim_agg)


    # calculate volume for each time step
    obs_agg['time_dff_sec'] = 'nan'
    obs_agg['vol'] = 'nan'
    print(obs_agg)

    isObsFirst = True
    for ii in range(len(obs_agg['datetime'])):
        # print(ii)

        if isObsFirst:
            obs_agg['time_dff_sec'][ii] = 0
            obs_agg['vol'] = 0
            isObsFirst = False
            continue
        
        obs_agg['time_dff_sec'][ii] = (obs_agg['datetime'][ii] - obs_agg['datetime'][ii-1]) / pd.Timedelta(seconds=1)
        obs_agg['vol'][ii] = obs_agg['Obs'][ii-1] * obs_agg['time_dff_sec'][ii]

    print(obs_agg)
    
    # calculate cumulative sum
    obs_agg['obs_cum_sum'] = obs_agg['vol'].cumsum()
    print(obs_agg)

    os.chdir(dir_out)
    # obs.to_csv(ss + "_BK_accumulated.csv")


    # calculate volume for each time step
    sim_agg.reset_index(inplace = True)
    sim_agg['time_dff_sec'] = 'nan'
    sim_agg['vol'] = 'nan'
    print(sim_agg)

    isSimFirst = True
    for ii in range(len(sim_agg['index'])):
        # print(ii)

        if isSimFirst:
            sim_agg['time_dff_sec'][ii] = 0
            sim_agg['vol'] = 0
            isSimFirst = False
            continue
        
        sim_agg['time_dff_sec'][ii] = (sim_agg['datetime'][ii] - sim_agg['datetime'][ii-1]) / pd.Timedelta(seconds=1)
        sim_agg['vol'][ii] = sim_agg['Sim'][ii-1] * sim_agg['time_dff_sec'][ii]

    print(sim_agg)


    # calculate cumulative sum
    sim_agg['sim_cum_sum'] = sim_agg['vol'].cumsum()
    print(sim_agg)

    # sim_agg.to_csv(ss + "_sim_accumulated.csv")
    

    plt.figure(figsize = (16,7))
    plt.rcParams.update({'font.size': 16})

    plt.plot(obs_agg['datetime'], obs_agg['obs_cum_sum'], label = 'Observed', color = 'blue', lw = 2)
    plt.plot(sim_agg['datetime'], sim_agg['sim_cum_sum'], label = 'Simulated', color = 'red', lw = 2)
    plt.ticklabel_format(axis= 'y', scilimits= (3,4))
    plt.title(ss)

    dtFmt = mdates.DateFormatter('%m/%y') # define the formatting
    plt.gca().xaxis.set_major_formatter(dtFmt) # apply the format to the desired axis



    plt.ylabel('Cumulative Volume [cubic feet]')


    plt.grid(which='both', alpha=0.5)
    plt.legend()

    plt.show()

