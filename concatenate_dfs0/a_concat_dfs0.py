"""  
Created on Thu Sep 14 15:42:00 2023

concatenate dfs0 files into one dfs0 file

@author: Michael Getachew Tadesse

"""

import numpy as np
import pandas as pd
import mikeio
import os 
from mikeio import generic


dir_obs = 'C:\\Users\\mtadesse\\Downloads\\rain_10yr_25yr_100yr\\100y'

dir_out = 'C:\\Users\\mtadesse\\Downloads\\rain_10yr_25yr_100yr\\concatenated_rain\\rain_100yr'


os.chdir(dir_obs)

stn = os.listdir()

# stn = ['10054941.dfs0', '10050678.dfs0']

isFirst = True

for ss in stn:
    print(ss)

    # stnRow = dat[dat['station'] == ss]
    # stnFile = stnRow['fileName'].values[0]
    # print(stnFile)

    stnFile = ss

    if pd.isnull(stnFile):
        print("test")
        continue

    os.chdir(dir_obs)

    ds = mikeio.read(stnFile)

    df = ds.to_dataframe()
    df.reset_index(inplace = True)

    # rename the PIXEL
    pixel = df.columns[1]
    print(pixel)

    df.columns = ['datetime', pixel.split(" ")[0]]

    # print(df)


    # start concatenating
    if isFirst:
        combined_file = df
        isFirst = False
    else:
        combined_file = pd.merge(combined_file, df, on = 'datetime', how = 'outer')


os.chdir(dir_out)
saveName = "combined_10yr.csv"

combined_file.to_csv(saveName)
