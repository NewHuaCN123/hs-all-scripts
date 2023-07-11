from pickle import TRUE
import numpy as np
import pandas as pd
import mikeio
import os 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


dir_obs = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\calibration_validation_stats\\cal_0608_v13\\plots_4_report\\GW_obs_TS'
dir_sim = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\calibration_validation_stats\\cal_0608_v13\\plots_4_report'
dir_table = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\calibration_validation_stats\\cal_0608_v13\\plots_4_report'


# get simulated time series file
os.chdir(dir_sim)
####
# change
####
sim = pd.read_csv('Cal_0608_v13DetailedTS_SZ.csv')
print(sim)

# get station names
os.chdir(dir_table)
dat = pd.read_csv('GW_item_numbers.csv')
stn = dat.station.unique()
print(dat)
print(stn)

# manually add stations
stn = ['Walk-in-Water 2 Surf Aq Monitor']

for ss in stn:
    print(ss)

    # get observed time series
    stnRow = dat[dat['station'] == ss]
    stnFile = stnRow['fileName'].values[0]
    # print(stnFile)
    
    if pd.isnull(stnFile):
        continue

    stnFile = stnFile.split('.dfs0')[0] + ".csv"
    print(stnFile)


    # get item number
    itNum = stnRow['itm_num'].values[0]
    print(itNum)

    os.chdir(dir_obs)
    obs = pd.read_csv(stnFile)
    obs = obs.iloc[:,[0,itNum]]
    obs.columns = ['datetime', 'Obs']
    obs['datetime'] = pd.to_datetime(obs['datetime'])
    print(obs)

    # get simulated time series
    sim_dat = sim.filter(['Time', ss])

    print(sim_dat)

    sim_dat.columns = ['datetime', 'Sim']

    # get year-month-date
    getDate = lambda x: x.split(' ')[0]
    sim_dat['datetime'] = pd.DataFrame(map(getDate, sim_dat['datetime']))
    # print(sim_dat)


    # convert units
    sim_dat['Sim'] = sim_dat['Sim']/0.3048

    sim_dat['datetime'] = pd.to_datetime(sim_dat['datetime'])
    print(sim_dat)

    # # merge time series
    # dat_merged = pd.merge(obs, sim_dat, on = 'datetime', how = 'outer')
    # dat_merged.reset_index(inplace = True)
    # print(dat_merged)


    # subset time frame
    # dat_merged['datetime'] = pd.to_datetime(dat_merged['datetime'])
    # print(dat_merged)
    # dat_merged = dat_merged[(dat_merged['datetime'] >= '2017-09-10') & (dat_merged['datetime'] <= '2017-10-10')]

    # # for calibration period
    # obs = obs[(obs['datetime'] >= '2017-09-10') & (obs['datetime'] <= '2017-10-10')]
    # sim_dat = sim_dat[(sim_dat['datetime'] >= '2017-09-10') & (sim_dat['datetime'] <= '2017-10-10')]

    # for validation period
    ####
    # change
    ####
    obs = obs[(obs['datetime'] >= '2017-09-10') & (obs['datetime'] <= '2017-9-18')]
    sim_dat = sim_dat[(sim_dat['datetime'] >= '2017-09-10') & (sim_dat['datetime'] <= '2017-9-18')]



    plt.figure(figsize = (16,7))
    plt.rcParams.update({'font.size': 16})

    plt.plot(obs['datetime'], obs['Obs'], label = 'Observed', color = 'blue', lw = 2)
    plt.ylim(40, 120)
    plt.plot(sim_dat['datetime'], sim_dat['Sim'], label = 'Simulated', color = 'red', lw = 2)
    plt.title(ss)

    dtFmt = mdates.DateFormatter('%m/%d') # define the formatting
    plt.gca().xaxis.set_major_formatter(dtFmt) # apply the format to the desired axis


    plt.ylabel('Stage NAVD88 [ft]')




    plt.grid(which='both', alpha=0.5)
    plt.legend()

    plt.show()

