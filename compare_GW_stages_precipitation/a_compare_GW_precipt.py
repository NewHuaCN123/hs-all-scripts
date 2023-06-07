"""  
Created on Thu Dec 12 15:24:00 2022

compare GW stage with precipitation

@author: Michael Getachew Tadesse
"""
import os
import logging
import datetime
import numpy
import glob
import pandas as pd
import seaborn as sns
import matplotlib.colors as mcolors
import matplotlib.dates as mdates
import matplotlib.pyplot as plt


dir_home = "R:\\40715-013 UKFPLOS\\Data\\ufa_sa_differences\\2017"
dir_figures = "R:\\40715-013 UKFPLOS\\Data\\ufa_sa_differences\\2017\\figures"

os.chdir(dir_home)

##################
# plotting options
prp_sas = True
sas_ufa = False
##################


# getting data
nex = pd.read_csv('irma_dailyNEXRAD.LonLat.csv')
gw_dat = pd.read_csv('sas_data_with_nexrad_pixel.csv')
gw_dat = gw_dat.iloc[:, 1:]
gw_dat['HYDROID'] = gw_dat['HYDROID'].astype(int)

ufa_dat = pd.read_csv('ufa_data.csv')
ufa_dat = ufa_dat.iloc[:, 1:]

print(nex)
print(gw_dat)

# get unique well ids

unq_well = gw_dat['well_id'].unique()

unq_well = ['574272']
unq_ufa = ['TP352']

print(unq_well)

for uu in unq_well:

    os.chdir(dir_home)

    print(uu)

    df = gw_dat.iloc[:,1:-1][gw_dat['well_id'] == uu].T
    print(df)
    df.reset_index(inplace = True)
    df.columns = ['datetime', 'stage_ft']
    df['datetime'] = pd.to_datetime(df['datetime'])



    # find the corresponding nexrad pixel
    nex_pix = gw_dat[gw_dat['well_id'] == uu]['HYDROID'].values[0].astype(int)
    # print(nex_pix)


    # get the nexrad timeseries
    nex_dat = nex[nex['pixel'] == nex_pix][['date', 'value']]
    nex_dat['date'] = pd.to_datetime(nex_dat['date'])

    if len(nex_dat) == 0:
        continue

    
        

    # print the two datasets
    fig, ax1 = plt.subplots(figsize = (12,5))

    color = 'tab:red'
    color_ufa = 'black'
    ax1.set_ylabel('Daily GW Stages [ft]', color = color)
    ax1.plot(df['datetime'], df['stage_ft'], label = uu, color = color)
    ax1.tick_params(axis ='y', labelcolor = color)
    ax1.legend(loc="upper left")
    ax1.grid()

    if prp_sas:
        # Adding Twin Axes to plot using dataset_2
        ax2 = ax1.twinx()
        
        color = 'tab:blue'
        ax2.set_ylabel('Daily Precipitation [in]', color = color)
        ax2.plot(nex_dat['date'], nex_dat['value'], label = nex_pix, color = color)
        ax2.tick_params(axis ='y', labelcolor = color)
        ax2.grid()

        ax2.legend(loc="upper right")


    if sas_ufa:

        # get UFA timeseries
        for jj in unq_ufa:

            print(jj)
            
            new_dat = ufa_dat.iloc[:,1:][ufa_dat['well_id'] == jj].T
            print(new_dat)

            new_dat.reset_index(inplace = True)
            new_dat.columns = ['datetime', 'stage_ft']
            print(new_dat)
            new_dat['datetime'] = pd.to_datetime(new_dat['datetime'])

            ax1.plot(new_dat['datetime'], new_dat['stage_ft'], label = jj, color = color_ufa)
            ax1.legend(loc="upper left")


    
    plt.show()

    # os.chdir(dir_figures)
    # fig.savefig(str(uu) + '.jpeg', dpi = 400)

