"""  
Created on Thu Feb 01 10:33:00 2023

create dfs0 files
Input files = water level dfs0 files

@author: Michael Getachew Tadesse

"""
import os 
import mikeio
import datetime 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dir_in = 'C:\\Users\\mtadesse\\OneDrive - Hazen and Sawyer\\Broward-Watershed-Plan\\Data'
dir_obs = 'C:\\Users\\mtadesse\\OneDrive - Hazen and Sawyer\\Broward-Watershed-Plan\\Data\\100y_3d'
dir_out = 'C:\\Users\\mtadesse\\OneDrive - Hazen and Sawyer\\Broward-Watershed-Plan\\Data\\100y_5d'


os.chdir(dir_in)

diffFile = pd.read_csv("rain_difference.csv")
# print(diffFile)


print(type(diffFile['HYDROID'][0]))

os.chdir(dir_obs)
nexList = os.listdir()

for nex in nexList:
    print(nex)

    # convert dfs0 to csv

    stnFile = nex

    if pd.isnull(stnFile):
        print("**Null**")
        continue

    os.chdir(dir_obs)

    ds = mikeio.read(stnFile)

    df = ds.to_dataframe()
    df.reset_index(inplace = True)
    df.columns = ['datetime', "rainfall_in"]

    df = df[df['datetime'] >= "2017-09-08 02:15:00"]

    # print(df)


    # generate new empty time series between 09/06 02:00 and 09/08 02:00

    dat = pd.DataFrame(pd.date_range(start="2017-09-06 02:00:00",
                                         end='2017-09-08 02:00:00', freq="15min"), 
                                            columns = ['datetime'])

    # print(dat)


    # assign the difference in rainfall
    nex_id = nex.split('.dfs0')[0]
    print(nex_id)

    diff = diffFile[diffFile['HYDROID'] == int(nex_id)]['Diff_5d_3d'].values[0]

    # print(diff)


    dat['rainfall_in'] = diff/len(dat)

    # print(dat)


    # merge with original data
    dat = pd.concat([dat, df], axis = 0)

    print(dat)
    print(dat['rainfall_in'].sum())


    # # plot figure
    # plt.figure(figsize= (16,7))
    # plt.plot(dat['datetime'], dat['rainfall_in'], color = "blue")
    # plt.show()