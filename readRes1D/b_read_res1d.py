"""  
Created on Thu Feb 08 08:58:00 2024

read res1D files
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


dir_in = "C:\\Users\\mtadesse\\OneDrive - Hazen and Sawyer\\Documents"
dir_out = "C:\\Users\\mtadesse\\OneDrive - Hazen and Sawyer\\Documents"

os.chdir(dir_in)


# read res1D file
df = Res1D("100S100R85i.res1d").read()

print(df)
print(df.columns)

# # dat = pd.DataFrame(df.columns)
# # print(dat)

# # dat.to_csv("res1D_columns_v2.csv")

query = QueryDataReach("WaterLevel", "1L2W", 3000)
df = Res1D.read(query)

print(df)