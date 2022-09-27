"""  
Created on Wed Aug 03 17:42:00 2022

create dfs0 files

@author: Michael Getachew Tadesse

"""

import os
import pandas as pd 
import datetime
import mikeio
from mikeio.eum import ItemInfo, EUMType, EUMUnit
from mikecore.DfsFile import DataValueType

dir_in = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\FromSJRWMD\\Rainfall\\"\
                "modified_files\\pixel_rainfall_distributed\\2017"
dir_out = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\FromSJRWMD\\Rainfall\\"\
                "modified_files\\pixel_rainfall_distributed\\2017_dfs0"

pix_stand_dir = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\FromSJRWMD\\Rainfall\\"\
                "modified_files\\pixel_rainfall_distributed"

# get standard pixel id names
os.chdir(pix_stand_dir)
pix_stand = pd.read_csv('pixel_standard_id.csv')



os.chdir(dir_in)

pixList = os.listdir()

for pp in pixList:
    print(pp)

    os.chdir(dir_in)

    df = pd.read_csv(pp, parse_dates=True, 
                index_col='datetime', na_values=-99.99)
    df = df[['distributed_rain']]

    item = ItemInfo(EUMType.Rainfall, EUMUnit.inch, data_value_type = DataValueType.StepAccumulated)

    da = mikeio.DataArray(df['distributed_rain'], time = df.index, item = item)

    ds = mikeio.Dataset([da])

    os.chdir(dir_out)

    # find standard pixel id
    saveName = pix_stand[pix_stand['pixel'] == pp]['pixel_final'].values[0]

    print(pp, saveName)

    ds.to_dfs(saveName)