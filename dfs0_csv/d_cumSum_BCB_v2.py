
"""
Created on Tue Jul 11 08:31:00 2023
modified on Mon Jul 24, 2023 09:10:00

To calculate the cumulative flow and plot it
To calculate the difference between observed 
and simulated cumulative flows

Updated: to calculate volume for each timestep by
considering the same flow rate unless it changes in the BK

@author: Michael Getachew Tadesse

"""

import numpy as np
import pandas as pd
import mikeio
import os 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


dir_obs = 'R:\\40715-010\\Data\\calibration_stats\\bcb_stat_summary\\0720\\flow_stats\\sw_obs'
dir_sim = 'R:\\40715-010\\Data\\calibration_stats\\bcb_stat_summary\\0720\\flow_stats'
dir_table = 'R:\\40715-010\\Data\\calibration_stats\\bcb_stat_summary\\0720\\flow_stats'


# get simulated time series file
os.chdir(dir_sim)

####
# change
####
sim = pd.read_csv('BCB_071123_PD_FC9_noQimp_newstnsDetailedTS_M11.csv')
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


stn = ['COCO1_Q']

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
    print(sim_dat)
    

    # # original dates
    obs = obs[(obs['datetime'] >= '2017-07-01') & (obs['datetime'] <= '2020-12-31')]
    sim_dat = sim_dat[(sim_dat['datetime'] >= '2017-07-01') & (sim_dat['datetime'] <= '2020-12-31')]

    # # when looking at a unique date
    # obs = obs[(obs['datetime'] >= '2018-08-18') & (obs['datetime'] <= '2019-07-13')]
    # sim_dat = sim_dat[(sim_dat['datetime'] >= '2018-08-18') & (sim_dat['datetime'] <= '2019-07-13')]

    
    obs.reset_index(inplace = True)
    print(obs)
    # calculate volume for each time step
    obs['time_dff_sec'] = 'nan'
    obs['vol'] = 'nan'
    print(obs)

    isObsFirst = True
    for ii in range(len(obs['index'])):
        # print(ii)

        if isObsFirst:
            obs['time_dff_sec'][ii] = 0
            obs['vol'] = 0
            isObsFirst = False
            continue
        
        obs['time_dff_sec'][ii] = (obs['datetime'][ii] - obs['datetime'][ii-1]) / pd.Timedelta(seconds=1)
        obs['vol'][ii] = obs['Obs'][ii-1] * obs['time_dff_sec'][ii]

    print(obs)
    
    # calculate cumulative sum
    obs['obs_cum_sum'] = obs['vol'].cumsum()
    print(obs)

    obs.to_csv(ss + "_BK_accumulated.csv")


    # calculate volume for each time step
    sim_dat.reset_index(inplace = True)
    sim_dat['time_dff_sec'] = 'nan'
    sim_dat['vol'] = 'nan'
    print(sim_dat)

    isSimFirst = True
    for ii in range(len(sim_dat['index'])):
        # print(ii)

        if isSimFirst:
            sim_dat['time_dff_sec'][ii] = 0
            sim_dat['vol'] = 0
            isSimFirst = False
            continue
        
        sim_dat['time_dff_sec'][ii] = (sim_dat['datetime'][ii] - sim_dat['datetime'][ii-1]) / pd.Timedelta(seconds=1)
        sim_dat['vol'][ii] = sim_dat['Sim'][ii-1] * sim_dat['time_dff_sec'][ii]

    print(sim_dat)


    # calculate cumulative sum
    sim_dat['sim_cum_sum'] = sim_dat['vol'].cumsum()
    print(sim_dat)

    sim_dat.to_csv(ss + "_sim_accumulated.csv")
    

    plt.figure(figsize = (16,7))
    plt.rcParams.update({'font.size': 16})

    plt.plot(obs['datetime'], obs['obs_cum_sum'], label = 'Observed', color = 'blue', lw = 2)
    plt.plot(sim_dat['datetime'], sim_dat['sim_cum_sum'], label = 'Simulated', color = 'red', lw = 2)
    plt.ticklabel_format(axis= 'y', scilimits= (3,4))
    plt.title(ss)

    dtFmt = mdates.DateFormatter('%m/%y') # define the formatting
    plt.gca().xaxis.set_major_formatter(dtFmt) # apply the format to the desired axis



    plt.ylabel('Cumulative Volume [cubic feet]')


    plt.grid(which='both', alpha=0.5)
    plt.legend()

    plt.show()

