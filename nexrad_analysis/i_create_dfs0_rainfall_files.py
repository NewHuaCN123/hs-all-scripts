"""  
Created on Wed Aug 03 17:42:00 2022

create dfs0 files

@author: Michael Getachew Tadesse

"""

import os
from turtle import title
import pandas as pd 
import datetime
import mikeio
from mikeio.eum import ItemInfo, EUMType, EUMUnit
from mikecore.DfsFile import DataValueType

dir_in = "R:\\40715-013 UKFPLOS\\Data\\Rainfall\\0606\\csv\\2017"
dir_out = "R:\\40715-013 UKFPLOS\\Data\\Rainfall\\0606\\csv\\2017"



# # get standard pixel id names
# os.chdir(pix_stand_dir)
# pix_stand = pd.read_csv('pixel_standard_id.csv')



os.chdir(dir_in)
gList = os.listdir()


for pp in gList:
    print(pp)

    df = pd.read_csv(pp, parse_dates=True, 
                index_col='datetime', na_values=-99.99)

    df = df[['value']]

    print(df)

    item = ItemInfo(EUMType.Rainfall, EUMUnit.inch, data_value_type = DataValueType.StepAccumulated)

    da = mikeio.DataArray(df['value'], time = df.index, item = item)

    ds = mikeio.Dataset([da])

    os.chdir(dir_out)

    # # find standard pixel id
    saveName = pp + ".dfs0"

    # print(pp, saveName)

    ds.to_dfs(saveName)