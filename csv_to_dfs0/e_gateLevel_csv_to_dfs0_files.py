"""  
Created on Wed Aug 03 17:42:00 2022
Modified on Fri Aug 04 17:06:00 2023

create dfs0 files
Input files = gate level csv files
@author: Michael Getachew Tadesse

"""

import os
import pandas as pd 
import datetime
import mikeio
from mikeio.eum import ItemInfo, EUMType, EUMUnit
from mikecore.DfsFile import DataValueType

dir_in = "R:\\KB_USACE\\Data\\data_from_dbhydro\\SW\\gates_clean\\clean_v2"
dir_out = "R:\\KB_USACE\\Data\\data_from_dbhydro\\SW\\gates_clean\\clean_v2"



os.chdir(dir_in)

pixList = os.listdir()

# pixList = ['S57_H.csv']

for pp in pixList:
    print(pp)

    os.chdir(dir_in)

    df = pd.read_csv(pp, parse_dates=True, 
                index_col='datetime', na_values=-99.99)
    df = df[['gateLevel']]
    df = df.head(df.shape[0] -1)

    # print(df)

    item = ItemInfo(EUMType.Gate_Level, EUMUnit.feet, data_value_type = DataValueType.Instantaneous)

    da = mikeio.DataArray(df['gateLevel'], time = df.index, item = item)

    ds = mikeio.Dataset([da])

    os.chdir(dir_out)

    # find standard pixel id
    saveName = pp + ".dfs0"

    # print(pp, saveName)

    ds.to_dfs(saveName)