
"""  
Created on Fri Oct 21 09:24:00 2022

fit theoretical probability distributions

plot CDFs and NEXRAD and gage timeseries

@author: Michael Getachew Tadesse
"""
import os
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
yr = "2011"
###############


dir_home = "R:\\40715-013 UKFPLOS\\Data\\Rainfall\\"\
        "NEXRAD_Gage_15min_comparison_correction_AWRA\\nexrad_gage_merged\\{}".format(yr)
dir_out = "R:\\40715-013 UKFPLOS\\Data\\Rainfall\\"\
            "NEXRAD_Gage_15min_comparison_correction_AWRA\\to_Delete"

os.chdir(dir_home)

dat = pd.read_csv('IW783_10104658.csv')

# replace NaN values with zeros
dat['nexrad'] = dat['nexrad'].fillna(0)

print(dat)


def plotTimeSeries():
    # plotting gage data
    fig, axs = plt.subplots(2)
    # plt.figure(figsize = (10,6))
    axs[0].hist(dat['gage'], bins = 100, color = 'blue')
    axs[0].set_xlim([0, 0.5])
    axs[1].hist(dat['nexrad'], bins = 100, color = 'red')
    axs[1].set_xlim([0, 0.5])

    plt.show()


def distfitPlot():
    # plot probability distribution

    # initialize distfit
    gage_dist = distfit()

    gage_dist.fit_transform(dat['gage'])
    print(gage_dist.summary)
    gage_dist.plot()
    plt.show()

    nex_dist = distfit()

    nex_dist.fit_transform(dat['nexrad'])
    print(nex_dist.summary)
    nex_dist.plot()
    plt.show()



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
    
    # os.chdir(dir_out)
    # nex_cdf_df.to_csv('nexrad_cdf.csv')

    # print(gage_cdf_df)
    # print(nex_cdf_df)

    # plotting PDF and CDF
    fig, axs = plt.subplots(2, ncols=1)
    # # plt.figure(figsize = (10,6))
    # axs[0].plot(bins_gage[1:], pdf_gage, color="blue", label="Gage-PDF")
    # axs[0].plot(bins_nex[1:], pdf_nex, color="red", label="Nex-PDF")
    # axs[0].grid()
    # axs[0].legend()

    dat['date'] = pd.to_datetime(dat['date'])
    axs[0].plot(dat['date'], dat['gage'], color="blue", label="Gage")
    axs[0].plot(dat['date'], dat['nexrad'], color="red", label="NEXRAD")
    axs[0].grid()
    axs[0].legend()

    axs[1].plot(bins_gage[1:], cdf_gage, label="Gage-CDF", color = "blue")
    axs[1].plot(bins_nex[1:], cdf_nex, label="Nex-CDF", color = "red")
    axs[1].grid()
    axs[1].legend()

    # plt.show()

    return gage_cdf_df, nex_cdf_df


pdf_cdf_plots()


gage_cdf_df, nex_cdf_df = pdf_cdf_plots()

dat['corrected'] = 'x'

# print(np.interp(0.9998, gage_cdf_df['perc'], gage_cdf_df['gage']))


for nn in range(len(dat['nexrad'])):
    nex_value = dat['nexrad'][nn]

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
        print("es gibt ein Problem!")

        nex_corrected = np.interp(nex_perc, gage_cdf_df['perc'], gage_cdf_df['gage'])
        print(nex_corrected)

        dat['corrected'][nn] = nex_corrected

    # if there is a number of gage values with the same percentile
    # take the average of those
    elif (len(new_df['gage']) > 1):
        nex_corrected = new_df['gage'].mean()

        print(nex_corrected)

        dat['corrected'][nn] = nex_corrected
    
    

os.chdir(dir_out)
dat.to_csv("check_correction.csv")