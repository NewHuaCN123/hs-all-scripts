"""  
Created on Fri Oct 06 17:08:00 2023

read res1D/xns files
based on: https://github.com/DHI/mikeio1d

@author: Michael Getachew Tadesse

"""

import os
import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy.interpolate import make_interp_spline
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from mikeio1d.res1d import Res1D, QueryDataReach
from mikeio1d import xns11


dir_in = "C:\\Users\\mtadesse\\OneDrive - Hazen and Sawyer\\Section216\\Data"
dir_out = "C:\\Users\\mtadesse\\OneDrive - Hazen and Sawyer\\Section216\\Data"

os.chdir(dir_in)


# # read res1D file
# df = Res1D("100S100R85i.res1d").read()

# # print(df)
# # print(df.columns)

# # dat = pd.DataFrame(df.columns)
# # print(dat)

# # dat.to_csv("res1D_columns_v2.csv")

# query = QueryDataReach("WaterLevel", "C-14", 2743.2)
# df = Res1D.read(query)


# read xns11 file
branch = ['Hillsboro', 'Hillsboro Tidal', 'C-14', 'C-14 Tidal']

special_branch = ['C-13', 'C-13 Tidal','North New River', 'North New River Tidal','C-12', 
                  'Dania Cut-Off Canal', 'SFWMD_C-11', 'SFWMD C-9']

branch = ['C-12Tidal']

for bb in branch:

    q2 = xns11.QueryData('TAYLOR', bb)

    geometry = xns11.read('Broward_ResiliencyPlan_Scenarios.xns11', q2)

    # print(q2)
    # print(geometry.columns)
    # print(geometry)

    dat_xns = pd.DataFrame()

    isFirst = True
    for xx in geometry.columns:
        if xx.startswith("z"):
            # print(xx.split("z TAYLOR ")[1])

            zDat = geometry[xx]
            zDat = zDat[~zDat.isna()]
            # print(zDat)

            zDat_top = pd.DataFrame([xx.split("z TAYLOR ")[1], zDat[0]/0.3048, zDat.iloc[-1]/0.3048]).T
            zDat_top.columns = ['station', 'topLeft', 'topRight']
            # print(zDat_top)

            if isFirst:
                dat_xns = zDat_top
                isFirst = False
            else:
                dat_xns = pd.concat([dat_xns, zDat_top], axis = 0)
                dat_xns.columns = ['station', 'topLeft', 'topRight']

    print(dat_xns)

    dat_xns.to_csv(bb + ".csv")
