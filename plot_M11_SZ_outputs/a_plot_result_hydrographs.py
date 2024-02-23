"""  
Created on Thu Oct 05 13:23:00 2023

plot stage and flow hydrographs

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


dir_in = "R:\\40715-021\\QAQC\\model_results_comparison\\100623"
dir_out = "R:\\40715-021\\QAQC\\model_results_comparison\\100623\\figures"


variable = "stage"


os.chdir(dir_in)
dat = pd.read_csv("100S100R85i_v3DetailedTS_M11_{}.csv".format(variable))
dat['Time'] = pd.to_datetime(dat['Time'])


print(dat)
print(dat.columns)

stn_flow = ['G-54_Q', 'G-56_Q', 'G-57_Q', 'S-13_Pump&Spillway_Q', 'S-29_Q', 
       'S-33_Q', 'S-34_Q', 'S-36_Q', 'S-37B_Q', 'S-37A_Q', 'S-38_Q', 'S-38A_Q',
       'S-38C_Q', 'S-124_Q', 'S-381_Q', 'G-86N Q', 'G-86S Q',
       'C-9 Impoundment Inflow', 'C-11 Impoundment Inflow',
       'Site-1 Impoundment Inflow', 'Conceptual 1 Q', 'Conceptual 2 Q',        
       'Conceptual 3 Q', 'Conceptual 4 Q', 'Conceptual 5 Q']

stn_stage = ['G-54_HW', 'G-54_TW', 'G-56_HW', 'G-56_TW', 'G-57_HW',
       'G-57_TW', 'G-65_HW', 'G-65_TW', 'S-9_Pump_HW', 'S-9_Pump_TW',
       'S-9XS_HW', 'S-9XS_TW', 'S-13_Pump_HW', 'S-13_Pump_TW', 'S-13A_HW',
       'S-13A_TW', 'S-29_HW', 'S-29_TW', 'S-30_HW', 'S-30_TW', 'S-32_HW',
       'S-33_HW', 'S-33_TW', 'S-34_TW', 'S-36_HW', 'S-36_TW', 'S-37B_HW',
       'S-37B_TW', 'S-37A_HW', 'S-37A_TW', 'S-38_TW', 'S-38A_HW', 'S-38A_TW',
       'S-38C_HW', 'S-38C_TW', 'S-39_HW', 'S-39_TW', 'S-124_HW', 'S-124_TW',
       'S-125_HW', 'S-125_TW', 'S-381_HW', 'S-381_TW', 'G-94A TW', 'G-86N HW',
       'G-86S HW', 'C-9 Impoundment Stage', 'C-11 Impoundment Stage',
       'Site-1 Impoundment Stage', 'Conceptual 1 Stage', 'Conceptual 2 Stage',
       'Conceptual 3 Stage', 'Conceptual 4 Stage', 'Conceptual 5 Stage']

hilsboro = ['Site-1 Impoundment Inflow', 'Conceptual 1 Q', 'Conceptual 2 Q', 'Conceptual 5 Q', 'G-56_Q']
c14 = ['S-38_Q', 'S-38A_Q','S-38C_Q', 'S-37B_Q', 'G-57_Q', 'S-37A_Q']

test1 = ['G-54_Q', 'S-34_Q','S-33_Q', 'S-36_Q']
test2 = ['G-86N Q', 'C-11 Impoundment Inflow','Conceptual 3 Q', 'Conceptual 4 Q', 'S-13_Pump&Spillway_Q']

test3 = ['G-54_HW', 'G-54_TW']

# plotting



def plotByWatershed(dat, watershed):
    plt.figure(figsize = (16,7))
    plt.rcParams.update({'font.size': 16})
    for ss in watershed:
        
        plt.plot(dat['Time'], dat[ss], label = ss, lw = 2)

        plt.title(ss)

        dtFmt = mdates.DateFormatter('%m/%d') # define the formatting
        plt.gca().xaxis.set_major_formatter(dtFmt) # apply the format to the desired axis

        if variable != 'flow':
            plt.ylabel('Stage NGVD29 [ft]')
        else:
            plt.ylabel('Discharge [cfs]')


        plt.grid(which='both', alpha=0.5)
        plt.legend()

    plt.show()


def plotAll(stn, variable, dir_out):
    for ss in stn:
        plt.figure(figsize = (16,7))
        plt.rcParams.update({'font.size': 16})

        plt.plot(dat['Time'], dat[ss], label = ss, lw = 2, c = "blue")

        plt.title(ss)

        dtFmt = mdates.DateFormatter('%m/%d') # define the formatting
        plt.gca().xaxis.set_major_formatter(dtFmt) # apply the format to the desired axis

        if variable != 'flow':
            plt.ylabel('Stage NGVD29 [ft]')
        else:
            plt.ylabel('Discharge [cfs]')


        plt.grid(which='both', alpha=0.5)
        plt.legend()

        # plt.show()

        # save figure
        os.chdir(dir_out + "\\{}".format(variable))
        plt.savefig(ss, dpi = 400)
    



# # plotByWatershed(dat, hilsboro)
# plotAll(stn_stage, variable, dir_out)
plotByWatershed(dat, test3)