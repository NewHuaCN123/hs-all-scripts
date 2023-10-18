"""  
Created on Wed Oct 18 17:33:00 2023

extend csv time series
convert to dfs0 file

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

dir_in = "C:\\Users\\mtadesse\\OneDrive - Hazen and Sawyer\\Documents\\Section216_Models\\M11_Scenarios"
# dir_out = "C:\\Users\\mtadesse\\OneDrive - Hazen and Sawyer\\Documents\\Section216_Models\\M11_Scenarios"


# read the SHIFTED file

# generate empty dataframe from 09/06 - 10/01

# merge these with the original time series

# fill in the missing data

# convert to dfs0