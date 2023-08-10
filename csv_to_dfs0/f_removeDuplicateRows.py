"""  
Created on Wed Aug 09 10:05:00 2022

to remove rows that are duplicate

@author: Michael Getachew Tadesse

"""

import os
import pandas as pd 
import datetime
import mikeio
from mikeio.eum import ItemInfo, EUMType, EUMUnit
from mikecore.DfsFile import DataValueType

dir_in = "R:\\KB_USACE\\Data\\data_from_dbhydro\\SW\\gates_clean\\csv"
dir_out = "R:\\KB_USACE\\Data\\data_from_dbhydro\\SW\\gates_clean\\clean_v2"



os.chdir(dir_in)

pixList = os.listdir()

# pixList = ['S57_H.csv']

for pp in pixList:
    os.chdir(dir_in)
    print(pp)

    os.chdir(dir_in)

    df = pd.read_csv(pp)

    print(df)

    df = df[~(df['diff'] == 0)]

    print(df)

    os.chdir(dir_out)

    df.to_csv(pp)