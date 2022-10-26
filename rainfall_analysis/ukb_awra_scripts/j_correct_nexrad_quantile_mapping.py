
"""  
Created on Fri Oct 26 10:05:00 2022

use quantile mapping to correct nexrad by observed rainfall
in this case the interpolated gage rainfall is used

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
from os.path import exists
from sklearn.metrics import mean_squared_error

###############
# set year here
yr = "2017"
###############

###############
# set date here
start = "2017-09-08 00:00:00"
end = "2017-09-22 00:00:00"
###############

dir_home = "R:\\40715-013 UKFPLOS\\Data\\Rainfall\\"\
        "NEXRAD_Gage_15min_comparison_correction_AWRA\\nexrad_raw\\{}".format(yr)
dir_interp = "R:\\40715-013 UKFPLOS\\Data\\Rainfall\\"\
        "NEXRAD_Gage_15min_comparison_correction_AWRA\\gage_interpolated_pixels\\{}".format(yr)
dir_out = "R:\\40715-013 UKFPLOS\\Data\\Rainfall\\"\
        "NEXRAD_Gage_15min_comparison_correction_AWRA\\"\
                "nexrad_corrected_with_interpolated_gage\\{}".format(yr)

os.chdir(dir_home)

# get list of stations
pList = os.listdir()

for pp in pList:
    
    os.chdir(dir_home)

    print(pp)

    dat = pd.read_csv(pp)

    # replace NaN values with zeros
    dat['value'] = dat['value'].fillna(0)

    dat = dat[(dat['datetime'] >= start) & (dat['datetime'] <= end)]

    # print(dat)


    # get corresponding interpolated pixel value
    os.chdir(dir_interp)

    if exists(pp):
        dat_intp = pd.read_csv(pp)
    else:
        continue
    # print(dat_intp)


    def pdf_cdf_plots():
        # No of Data points
        N = len(dat_intp['value'])
        
        
        # getting data of the histogram
        cIntp, bins_intp = np.histogram(dat_intp['value'], bins=N)
        cNex, bins_nex = np.histogram(dat['value'], bins=N)
        
        # print(bins_nex)

        # finding the PDF of the histogram using count values
        pdf_intp = cIntp / sum(cIntp)
        pdf_nex = cNex / sum(cNex)
        
        # using numpy np.cumsum to calculate the CDF
        # We can also find using the PDF values by looping and adding
        cdf_intp = np.cumsum(pdf_intp)
        cdf_nex = np.cumsum(pdf_nex)

        # get CDF dataframes for gage and nexrad
        intp_cdf_df = pd.DataFrame([bins_intp, cdf_intp]).T
        intp_cdf_df.columns = ['pixel_intp', 'perc']
        nex_cdf_df = pd.DataFrame([bins_nex, cdf_nex]).T
        nex_cdf_df.columns = ['pixel_nex', 'perc']

        # add perturbation to the last CDF
        # this is to assign CDF to the maximum value
        nex_cdf_df['perc'][len(nex_cdf_df) - 1] = 1 - (1e-25)
        intp_cdf_df['perc'][len(intp_cdf_df) - 1] = 1 - (1e-25)


        return intp_cdf_df, nex_cdf_df


    pdf_cdf_plots()


    intp_cdf_df, nex_cdf_df = pdf_cdf_plots()

    dat['nex_perc'] = 'x'
    dat['corrected'] = 'x'

    dat.reset_index(inplace = True)

    for nn in range(len(dat['value'])):
        nex_value = dat['value'][nn]
        intp_value = dat_intp['value'][nn]

        # check if both nexrad and gages are reporting zero rainfall
        # in which case apply no correction

        if ((nex_value == 0) & (intp_value == 0)):
            dat['nex_perc'][nn] = 'zero'
            dat['corrected'][nn] = 0
            continue

        # get the corresponding nexrad percentile (from the CDF)
        nex_perc = nex_cdf_df[nex_cdf_df['pixel_nex'] == nex_value]['perc'].values

        # print(nex_perc)

        # if the nex_perc doesn't exist
        if len(nex_perc ) == 0:
            nex_perc = np.interp(nex_value, nex_cdf_df['pixel_nex'], nex_cdf_df['perc'])
        else:
            nex_perc = nex_perc[0]

        # print(nex_value, nex_perc)
        
        # print(intp_cdf_df)

        new_df = intp_cdf_df[intp_cdf_df['perc'] == nex_perc]


        if (new_df.empty):
            # print("es gibt ein Problem!")

            nex_corrected = np.interp(nex_perc, intp_cdf_df['perc'], intp_cdf_df['pixel_intp'])
            # print(nex_corrected)

            dat['nex_perc'][nn] = nex_perc
            dat['corrected'][nn] = nex_corrected
            
        # if there is a number of gage values with the same percentile
        # take the average of those
        elif (len(new_df['pixel_intp']) >= 1):
            nex_corrected = new_df['pixel_intp'].mean()

            # print(nex_corrected)

            dat['nex_perc'][nn] = nex_perc
            dat['corrected'][nn] = nex_corrected
        
        

    os.chdir(dir_out)

    dat = dat[['datetime', 'value', 'corrected']]

    dat.to_csv(pp.split(".csv")[0] + "_corrected.csv")