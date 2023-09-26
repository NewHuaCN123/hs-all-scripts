"""  
Created on Tue Sep 26 12:33:00 2023

convert csv to dfs0

@author: Michael Getachew Tadesse

"""

import os
import pathlib
import mikeio
import datetime
import pandas as pd
import matplotlib.pyplot as plt  
from mikecore.DfsFile import DataValueType
from mikeio.eum import ItemInfo, EUMType, EUMUnit

dir_scenario = "R:\\40715-021\\Modeling\\Data\\CHS_data\\New_BND_Files\\Events_tobe_Simulated"
# dir_out = "C:\\Users\\mtadesse\\Downloads\\rainfall_analysis\\rain_10yr_25yr_100yr\\concatenated_rain\\rain_100yr"

# scenarios
scenario = ['Scenario1', 'Scenario2',
            'Scenario3', 'Scenario4',
            'Scenario5', 'Scenario6',
            'Scenario7']

# CHS save points
savepoint = ['30214', '30450', '30814', '31429']

# horizon years
hoz_yr = ['2035', '2085']




def convert2DFS0(scenario, savepoint, hoz_yr):
    """
    this function converts csv to dfs0
    """

    os.chdir(dir_scenario + "\\{}\\{}\\{}".format(scenario,savepoint,hoz_yr))
    
    # df = list(pathlib.Path(dir_scenario + "\\{}\\{}\\{}".format(scenario,savepoint,hoz_yr)).glob('*_SHIFTED.csv'))

    # convert to dfs0
    for ii in os.listdir():
        if ii.endswith("_SHIFTED.csv"):
            print(ii)

            dat = pd.read_csv(ii, parse_dates=True, 
                        index_col='datetime', na_values=-99.99)
            
            dat = dat[dat.columns[1:]]

            # # remove the last row
            # df = df.head(df.shape[0] -1)

            # os.chdir(dir_out)

            dat.to_dfs0("{}.dfs0".format(ii.split(".csv")[0]), EUMType.Water_Level, EUMUnit.feet)


#### Execution

for ss in scenario:
    for sv in savepoint:
        for hh in hoz_yr:
            convert2DFS0(ss, sv, hh)