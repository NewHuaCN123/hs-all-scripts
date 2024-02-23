"""  
Created on Mon Oct 09 17:31:00 2023

create 500y rainfall based on the 100y rainfall
apply the conversion factor

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


dir_in = "R:\\40715-021\\Modeling\\Data\\rainfall\\100923\\rain_500yr"
dir_out = "R:\\40715-021\\Modeling\\Data\\rainfall\\100923\\rain_500yr"

os.chdir(dir_in)

# factor data
dat_factor = pd.read_csv("NOAA_rainfall_data.csv")
print(dat_factor)

# 100y rainfall data
dat_100y = pd.read_csv("Rain_100y_extended.csv")
# print(dat_100y)

pixels = dat_100y.columns[1:-1]
# print(pixels)


# pixels = [10057792]

dat_500y = dat_100y.copy()

for pp in pixels:
    print(pp)
    # find the conversion factor
    conv_factor = dat_factor[dat_factor['HYDROID'] == int(pp)]['conversion_factor_100y_to_500y'].values[0]
    print(conv_factor)

    # multiply by conversion factor
    dat_500y[pp] = dat_500y[pp]*conv_factor

dat_500y.to_csv("Rain_500y_extended.csv")