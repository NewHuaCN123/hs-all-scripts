
"""
Created on Tue Jul 11 08:31:00 2023

To calculate the cumulative flow and plot it
To calculate the difference between observed 
and simulated cumulative flows

@author: Michael Getachew Tadesse

"""

import numpy as np
import pandas as pd
import mikeio
import os 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


dir_obs = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\calibration_validation_stats\\cal_0608_v13\\plots_4_report\\SW_obs_TS'
dir_sim = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\calibration_validation_stats\\cal_0608_v13\\plots_4_report'
dir_table = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\calibration_validation_stats\\cal_0608_v13\\plots_4_report'


# get simulated time series file
os.chdir(dir_sim)

####
# change
####
sim = pd.read_csv('Cal_0608_v13DetailedTS_M11_ver2.csv')
print(sim)

# get station names
os.chdir(dir_table)
dat = pd.read_csv('SW_storing_ver2.csv')
stn = dat.station.unique()
print(dat)
print(stn)

stn = ['S57_Flow', 'S59_Flow', 'S61_Flow', 'S62_Flow', 'S63_Flow', 'S63A_Flow', 'S65_Flow', 'S65A_Flow']

for ss in stn:
    print(ss)

    # get observed time series
    stnRow = dat[dat['station'] == ss]
    stnFile = stnRow['fileName'].values[0]

    
    if pd.isnull(stnFile):
        continue

    stnFile = stnFile.split('.dfs0')[0] + ".csv"
    print(stnFile)

    os.chdir(dir_obs)
    obs = pd.read_csv(stnFile)
    obs = obs[['datetime', 'value']]
    obs.columns = ['datetime', 'Obs']
    obs['datetime'] = pd.to_datetime(obs['datetime'])
    print(obs)

    # get simulated time series
    print(sim)
    sim_dat = sim.filter(['Time', ss])

    print(sim_dat)

    sim_dat.columns = ['datetime', 'Sim']

    # # get year-month-date
    # getDate = lambda x: x.split(' ')[0]
    # sim_dat['datetime'] = pd.DataFrame(map(getDate, sim_dat['datetime']))
    

    # check if its flow/stage
    type = ss.split('_')[1]
    print(type)

    if type != 'Flow':
        # # if units are in meters
        # sim_dat['Sim'] = sim_dat['Sim']/0.3048
        # if units are in feet
        sim_dat['Sim'] = sim_dat['Sim']
    else:
        # if units are in cms
        sim_dat['Sim'] = sim_dat['Sim']*35.314666212661
        # # if units are in cfs
        # sim_dat['Sim'] = sim_dat['Sim']

    sim_dat['datetime'] = pd.to_datetime(sim_dat['datetime'])
    print(sim_dat)
    


    obs = obs[(obs['datetime'] >= '2017-09-10') & (obs['datetime'] <= '2017-10-10')]
    sim_dat = sim_dat[(sim_dat['datetime'] >= '2017-09-10') & (sim_dat['datetime'] <= '2017-10-10')]

    # aggregating obs hourly
    obs.set_index('datetime')
    obs = pd.DataFrame(obs.resample('H', on='datetime').Obs.mean())
    obs.reset_index(inplace = True)
    obs['vol'] = obs['Obs']*3600
    print(obs)

    

    # aggregating sim hourly
    sim_dat.set_index('datetime')
    sim_dat = pd.DataFrame(sim_dat.resample('H', on='datetime').Sim.mean())
    sim_dat.reset_index(inplace = True)
    sim_dat['vol'] = sim_dat['Sim']*3600
    print(sim_dat)

    # calculate cumulative sum
    obs['obs_cum_sum'] = obs['vol'].cumsum()
    print(obs)
    
    sim_dat['sim_cum_sum'] = sim_dat['vol'].cumsum()
    print(sim_dat)




    plt.figure(figsize = (16,7))
    plt.rcParams.update({'font.size': 16})

    plt.plot(obs['datetime'], obs['obs_cum_sum'], label = 'Observed', color = 'blue', lw = 2)
    plt.plot(sim_dat['datetime'], sim_dat['sim_cum_sum'], label = 'Simulated', color = 'red', lw = 2)
    plt.ticklabel_format(axis= 'y', scilimits= (3,4))
    plt.title(ss)

    dtFmt = mdates.DateFormatter('%m/%d') # define the formatting
    plt.gca().xaxis.set_major_formatter(dtFmt) # apply the format to the desired axis

    if type != 'Flow':
        plt.ylabel('Cumulative Stage NAVD88 [ft]')
    else:
        plt.ylabel('Cumulative Volume [cubic feet]')


    plt.grid(which='both', alpha=0.5)
    plt.legend()

    plt.show()

