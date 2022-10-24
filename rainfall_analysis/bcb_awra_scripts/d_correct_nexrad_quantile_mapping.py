
"""  
Created on Fri Oct 21 14:33:00 2022

use quantile mapping to correct nexrad by observed rainfall

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


dir_home = "R:\\40715-013 UKFPLOS\\Data\\Rainfall\\"\
        "NEXRAD_Gage_15min_comparison_correction_AWRA\\nexrad_gage_merged\\{}".format(yr)
dir_out = "R:\\40715-013 UKFPLOS\\Data\\Rainfall\\"\
        "NEXRAD_Gage_15min_comparison_correction_AWRA\\corrected_nexrad\\{}".format(yr)

os.chdir(dir_home)

# get list of stations
gageList = glob.glob('./*.csv')
print(gageList)

for gg in gageList:
    
    os.chdir(dir_home)

    print(gg)

    dat = pd.read_csv(gg)

    # replace NaN values with zeros
    dat['nexrad'] = dat['nexrad'].fillna(0)

    print(dat)


    def pdf_cdf_plots():
        # No of Data points
        N = len(dat['gage'])
        
        
        # getting data of the histogram
        cGage, bins_gage = np.histogram(dat['gage'], bins=N)
        cNex, bins_nex = np.histogram(dat['nexrad'], bins=N)
        
        print(bins_nex)

        # finding the PDF of the histogram using count values
        pdf_gage = cGage / sum(cGage)
        pdf_nex = cNex / sum(cNex)
        
        # using numpy np.cumsum to calculate the CDF
        # We can also find using the PDF values by looping and adding
        cdf_gage = np.cumsum(pdf_gage)
        cdf_nex = np.cumsum(pdf_nex)

        # get CDF dataframes for gage and nexrad
        gage_cdf_df = pd.DataFrame([bins_gage, cdf_gage]).T
        gage_cdf_df.columns = ['gage', 'perc']
        nex_cdf_df = pd.DataFrame([bins_nex, cdf_nex]).T
        nex_cdf_df.columns = ['nex', 'perc']

        # add perturbation to the last CDF
        # this is to assign CDF to the maximum value
        nex_cdf_df['perc'][len(nex_cdf_df) - 1] = 1 - (1e-25)
        gage_cdf_df['perc'][len(gage_cdf_df) - 1] = 1 - (1e-25)


        return gage_cdf_df, nex_cdf_df


    pdf_cdf_plots()


    gage_cdf_df, nex_cdf_df = pdf_cdf_plots()

    dat['nex_perc'] = 'x'
    dat['corrected'] = 'x'


    for nn in range(len(dat['nexrad'])):
        nex_value = dat['nexrad'][nn]
        gage_value = dat['gage'][nn]

        # check if both nexrad and gages are reporting zero rainfall
        # in which case apply no correction

        if ((nex_value == 0) & (gage_value == 0)):
            dat['nex_perc'][nn] = 'zero'
            dat['corrected'][nn] = 0
            continue

        # get the corresponding nexrad percentile (from the CDF)
        nex_perc = nex_cdf_df[nex_cdf_df['nex'] == nex_value]['perc'].values


        # if the nex_perc doesn't exist
        if len(nex_perc ) == 0:
            nex_perc = np.interp(nex_value, nex_cdf_df['nex'], nex_cdf_df['perc'])
        else:
            nex_perc = nex_perc[0]

        # print(nex_value, nex_perc)
        

        new_df = gage_cdf_df[gage_cdf_df['perc'] == nex_perc]

        if (new_df.empty):
            # print("es gibt ein Problem!")

            nex_corrected = np.interp(nex_perc, gage_cdf_df['perc'], gage_cdf_df['gage'])
            print(nex_corrected)

            dat['nex_perc'][nn] = nex_perc
            dat['corrected'][nn] = nex_corrected

        # if there is a number of gage values with the same percentile
        # take the average of those
        elif (len(new_df['gage']) >= 1):
            nex_corrected = new_df['gage'].mean()

            print(nex_corrected)

            dat['nex_perc'][nn] = nex_perc
            dat['corrected'][nn] = nex_corrected
        
        

    os.chdir(dir_out)
    dat.to_csv(gg + "_corrected.csv")