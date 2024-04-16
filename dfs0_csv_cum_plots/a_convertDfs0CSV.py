"""  
Created on Thu Aug 31 10:33:00 2023

create dfs0 files
Input files = water level dfs0 files

@author: Michael Getachew Tadesse

"""

import numpy as np
import pandas as pd
import mikeio
import os 


dir_obs = 'C:\\Users\\mtadesse\\OneDrive - Hazen and Sawyer\\Section216\\Postprocessing\\M11_scenarios_3_5'

# dir_table = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\calibration_validation_stats\\"\
    # "cal_0608_v13\\plots_4_report'


os.chdir(dir_obs)
fileList = os.listdir()


# stn = ['10044502.dfs0']

stn = fileList.copy()


for ss in stn:
    print(ss)

    # stnRow = dat[dat['station'] == ss]
    # stnFile = stnRow['fileName'].values[0]
    # print(stnFile)

    stnFile = ss

    if pd.isnull(stnFile):
        print("**Null**")
        continue

    os.chdir(dir_obs)

    ds = mikeio.read(stnFile)

    df = ds.to_dataframe()
    df.reset_index(inplace = True)
    # df.columns = ['datetime', 'value']

    # print(df.columns)

    df = df[['index', 'G-56_HW', 'G-56_TW','G-56_Q',
             'S-37B_HW','S-37B_TW','S-37B_Q',
             'S-37A_HW', 'S-37A_TW','S-37A_Q',
             'G-57_HW','G-57_TW', 'G-57_Q',
             'S-36_HW', 'S-36_TW','S-36_Q',
             'S-33_HW', 'S-33_TW', 'S-33_Q',
             'G-54_HW', 'G-54_TW', 'G-54_Q',
             'S-13_Pump_HW', 'S-13_Pump_TW','S-13_Pump&Spillway_Q'
             ]]


    saveName = stnFile.split('.dfs0')[0] + ".csv"

    df.to_csv(saveName)
