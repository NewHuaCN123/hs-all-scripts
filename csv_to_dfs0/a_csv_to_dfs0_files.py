"""  
Created on Wed Aug 03 17:42:00 2022
Modified on Fri Aug 04 17:06:00 2023

create dfs0 files
Modify the variable type and its units accordingly

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

dir_in = "R:\\40715-021\\Modeling\\Data\\OL_tidal_boundary\\Scenario3\\FWOP\\Low"
dir_out = "R:\\40715-021\\Modeling\\Data\\OL_tidal_boundary\\Scenario3\\FWOP\\Low"



os.chdir(dir_in)

pixList = os.listdir()

########################################
pixList = ['Scenario_3_FWOP_low.csv'] 
variable = "Elevation"
unit = "feet"
########################################



for pp in pixList:
    print(pp)

    os.chdir(dir_in)

    df = pd.read_csv(pp, parse_dates=True, 
                index_col='datetime', na_values=-99.99)
    
    # df = df[df.columns[1:]]

    # # remove the last row
    # df = df.head(df.shape[0] -1)

    os.chdir(dir_out)

    df.to_dfs0("{}.dfs0".format(pp), EUMType.Elevation, EUMUnit.feet)
    