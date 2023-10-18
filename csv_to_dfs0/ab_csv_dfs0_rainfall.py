"""  
Created on Wed Aug 03 17:42:00 2022
Modified on Fri Aug 04 17:06:00 2023

create dfs0 files
Input files = rainfall csv files

Details on EUM
https://dhi.github.io/mikeio/eum.html

*this script still needs to be modified to include the DataValueType item included

@author: Michael Getachew Tadesse

"""

import os
import pandas as pd 
import datetime
import mikeio
from mikeio.eum import ItemInfo, EUMType, EUMUnit
from mikecore.DfsFile import DataValueType

dir_in = "R:\\40715-021\\Modeling\\Data\\rainfall\\100923\\rain_500yr"
dir_out = "R:\\40715-021\\Modeling\\Data\\rainfall\\100923\\rain_500yr"



os.chdir(dir_in)

pixList = os.listdir()

pixList = ['Rain_500y_extended.csv']

for pp in pixList:
    print(pp)

    os.chdir(dir_in)

    df = pd.read_csv(pp, parse_dates=True, 
                index_col='Time', na_values=-99.99)
    
    # df = df[df.columns[1:]]

    # remove the last row
    # df = df.head(df.shape[0] -1)

    os.chdir(dir_out)

    df.to_dfs0("Rain_500y_extended.dfs0", EUMType.Rainfall, EUMUnit.inch)
    