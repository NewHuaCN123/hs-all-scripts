"""  
Created on Tue Oct 03 08:02:00 2023

Apply EVA to get return periods


@author: Michael Getachew Tadesse

"""

import os
import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt  


dir_in = "R:\\40715-021\\Modeling\\Data\\RSM_boundary_data"


os.chdir(dir_in)

# horizon year
condition = "ecb"
stn = ["S-39_HW", "S40_HW", "S151_HW",
       "S144_HW", "S-31_HW", "EDEN 13",
       "3B-76", "2A-19", "PB-1661", "S-38 HW",
       "S-34HW", "S-9 TW", "S-31_TW", "S-32_TW"]

stn = ["S-31_TW"]

dat = pd.read_csv('all_rsm_bnd_data_{}.csv'.format(condition))
dat['datetime'] = pd.to_datetime(dat['datetime'])
dat['Year'] = dat['datetime'].dt.strftime('%Y')

print(dat)

# create empty dataframe
dat_max = pd.DataFrame()

isFirst = True
# per year
for ss in stn:
    print(stn)
    for yr in range(1965, 2017):
        print(yr)
        df = dat[dat['Year'] == str(yr)]
        df['Mon'] = df['datetime'].dt.strftime('%m')
        # print(df)

        # get sep-oct-nov data only
        df = df[(df['Mon'] >= "09") & (df['Mon'] <= "11")]
        # print(df)

        # get maximum value
        # print(df[df[stn] == df[stn].max()])
        df_max = df[df[ss] == df[ss].max()][ss].values[0]
        # print(df_max)

        new_dat = pd.DataFrame([yr, ss, df_max]).T
        new_dat.columns = ['year', 'station', 'annual_max_{}'.format(condition)]

        if isFirst:
            dat_max = new_dat
            isFirst = False
        else:
            dat_max = pd.concat([dat_max, new_dat], axis = 0)
            dat_max.columns = ['year', 'station', 'annual_max_{}'.format(condition)]

print(dat_max)

print(dat_max['annual_max_ecb'].quantile(0.8))
print(dat_max['annual_max_ecb'].quantile(0.9))
print(dat_max['annual_max_ecb'].quantile(0.95))
print(dat_max['annual_max_ecb'].quantile(0.99))
# dat_max.to_csv(ss+"_amax.csv")