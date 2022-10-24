
"""  
Created on Fri Oct 21 14:53:00 2022

plot corrected NEXRAD time series

@author: Michael Getachew Tadesse
"""
import os
import glob
import distfit
import logging
import datetime
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.colors as mcolors
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from distfit import distfit
from sklearn.metrics import mean_squared_error

###############
# set year here
yr = "2017"
###############

dir_home = "D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\Hazen and Sawyer\\"\
                "MIKE_Modeling_Group - Documents\\BCB\\data\\Rainfall\\"\
                        "bk_nexrad_gage\\corrected_nexrad"
dir_out = "D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\Hazen and Sawyer\\"\
                "MIKE_Modeling_Group - Documents\\BCB\\data\\Rainfall\\"\
                        "bk_nexrad_gage\\corrected_nexrad_figures"


os.chdir(dir_home)

# get list of stations
gageList = glob.glob('./*.csv')
print(gageList)


for gg in gageList:
    
    os.chdir(dir_home)

    print(gg)

    dat = pd.read_csv(gg)

    print(dat)

    # plotting gage data
    plt.figure(figsize = (10,6))

    dat['date'] = pd.to_datetime(dat['date'])
    plt.plot(dat['date'], dat['nexrad'], 'o', color="red", label="NEXRAD-Original", markersize = 5)
    plt.plot(dat['date'], dat['corrected'], color="green", label="NEXRAD-Corrected", markersize = 2)
    plt.plot(dat['date'], dat['gage'], 'o', color="blue", label="Gage", markersize =3.2)
    plt.grid()
    plt.legend()

    # plt.show()
    
    os.chdir(dir_out)
    plt.savefig(gg + ".jpeg", dpi = 400)