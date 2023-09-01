
"""
Created on Mon Jul 24, 2023 09:10:00

"""

import numpy as np
import pandas as pd
import mikeio
import os 
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


os.chdir("R:\\40715-010\\Data\\calibration_stats\\bcb_stat_summary\\0720\\Structure Flows")

stn = "COCO1.txt"

dat = pd.read_csv(stn, delimiter="\t")

print(dat.columns)

print(dat)

dat['total'] = dat.iloc[:,1:4].sum(axis = 1)*35.314666212661


print(dat)

dat = dat[['Date Time  ', 'total']]
dat.columns = ['datetime', 'total']

# # # dat = dat.replace('/', '-', regex = True)

# print(dat['datetime'][0])
# print(pd.to_datetime(dat['datetime'][0]))
# print(datetime.strptime(dat['datetime'][0], "%d-%m-%Y %H:%M:%S"))


dat['datetime_modified'] = 'nan'
print(dat)

dat['datetime_modified'] = pd.to_datetime(dat['datetime'], format = "mixed")
dat.sort_values(by = "datetime_modified", inplace = True)

# convert string to datetime
# for ii in range(len(dat['datetime'])):
#     print(ii)
#     print(dat['datetime'][ii])
#     dat['datetime_modified'][ii] = pd.to_datetime(dat['datetime'][ii])
#     # print(dat)

print(dat)

dat.to_csv("COCO1_summed_v3.csv")