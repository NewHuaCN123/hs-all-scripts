"""  
Created on Thu Feb 21 08:31:00 2024

fill zero in rainfall between dates

@author: Michael Getachew Tadesse

"""
import os 
import mikeio
import datetime 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mikeio.eum import ItemInfo, EUMType, EUMUnit
from mikecore.DfsFile import DataValueType

dir_obs = 'C:\\Users\\mtadesse\\OneDrive - Hazen and Sawyer\\Broward-Watershed-Plan\\AdaptationStrategyRuns\\rainfall_data\\100y_5d_dfs0'
dir_out_csv = 'C:\\Users\\mtadesse\\OneDrive - Hazen and Sawyer\\Broward-Watershed-Plan\\AdaptationStrategyRuns\\rainfall_data\\100y_5d_0901_csv'
dir_out_dfs0 = 'C:\\Users\\mtadesse\\OneDrive - Hazen and Sawyer\\Broward-Watershed-Plan\\AdaptationStrategyRuns\\rainfall_data\\100y_5d_0901_dfs0'




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

    # print(df)
    df = df[df['datetime'] >= "2017-09-06 02:00:00"]
    # print(df)

    # generate new empty time series between 09/06 02:00 and 09/08 02:00
    dat = pd.DataFrame(pd.date_range(start="2017-09-01 00:00:00",
                                         end='2017-09-06 01:45:00', freq="24H"), 
                                            columns = ['datetime'])
    # print(dat)


    # assign zero rainfall
    dat['rainfall_in'] = 0



    # merge with original data
    dat = pd.concat([dat, df], axis = 0)

    # print(dat)
    # print(dat['rainfall_in'].sum())


    # write csv
    os.chdir(dir_out_csv)
    dat.to_csv(nex.split(".dfs0")[0] + ".csv")

    # # # plot figure
    # # plt.figure(figsize= (16,7))
    # # plt.plot(dat['datetime'], dat['rainfall_in'], color = "blue")
    # # plt.show()

    # # write a dfs0
    item = ItemInfo(EUMType.Rainfall, EUMUnit.inch, data_value_type=DataValueType.StepAccumulated)
    da1 = mikeio.DataArray(data=dat['rainfall_in'], time=dat['datetime'], item=item)

    os.chdir(dir_out_dfs0)
    da1.to_dfs(nex)
    
