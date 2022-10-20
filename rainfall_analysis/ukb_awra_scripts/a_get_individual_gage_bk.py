"""  
Created on Thu Oct 20 14:47:00 2022

get the individual gages rain from the 
csv that contains all gages

also subset the time period 


@author: Michael Getachew Tadesse
"""
import os
import logging
import datetime
import numpy
import pandas as pd
import seaborn as sns
import matplotlib.colors as mcolors
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error


dir_home = "R:\\40715-013 UKFPLOS\\Data\\Rainfall\\"\
    "NEXRAD_Gage_15min_comparison_correction_AWRA\\gage_bk_raw"

dat_2011 = "R:\\40715-013 UKFPLOS\\Data\\Rainfall\\"\
        "NEXRAD_Gage_15min_comparison_correction_AWRA\\gage_bk_raw\\2011"

dat_2017 = "R:\\40715-013 UKFPLOS\\Data\\Rainfall\\"\
    "NEXRAD_Gage_15min_comparison_correction_AWRA\\gage_bk_raw\\2017"

# get gage information
os.chdir(dir_home)

gInfo = pd.read_csv('gage_bk_information.csv')
print(gInfo)


# all gages data
os.chdir(dat_2011)
d2011 = pd.read_csv('all_gages_cr10_2011.csv')
print(d2011)

os.chdir(dat_2017)
d2017 = pd.read_csv('all_gages_cr10_2017.csv')
print(d2017)

for db in gInfo['DBKEY']:
    print(db)
    
    df2011 = d2011[d2011['dbkey'] == db]
    os.chdir(dat_2011)
    df2011.to_csv(db + "_2011.csv")

    df2017 = d2017[d2017['dbkey'] == db]
    os.chdir(dat_2017)
    df2017.to_csv(db + "_2017.csv")

    