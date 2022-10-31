
"""  
Created on Fri Oct 28 10:39:00 2022

extract - save - plot rainfall data 
for stations and their multiple dbkeys

this is to compare the multiple dbkeys 
for a given station

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



dir_home = "D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\Hazen and Sawyer\\"\
                "MIKE_Modeling_Group - Documents\\BCB\\data\\"\
                            "Rainfall\\bk_nexrad_gage\\gage\\additional"

dir_out = "D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\Hazen and Sawyer\\"\
                "MIKE_Modeling_Group - Documents\\BCB\\data\\"\
                            "Rainfall\\bk_nexrad_gage\\gage\\additional\\extracted"

dir_nex = "E:\\NEXRAD"


os.chdir(dir_home)
dat = pd.read_csv('all_gages.csv')
gage_info = pd.read_csv('all_bcb_gages_information.csv')
print(dat)

stations = dat['station_unq'].unique()
print(stations)

for ss in stations:
    print(ss)

    df = dat[dat['station_unq'] == ss]
    df['datetime'] = pd.to_datetime(df['datetime'])
    print(df)

    os.chdir(dir_out)
    df.to_csv(ss + '.csv')


    # plot all dbkeys
    plt.figure(figsize = (12, 5))
    
    db_unq = df['dbkey'].unique()
    print(db_unq)

    isFirst = True
    for db in db_unq:
        print(db)

        # get recorder type
        rec = gage_info[gage_info['DBKEY'] == db]['RCDR'].values[0]
        print(rec)

        # get nexrad data
        os.chdir(dir_nex)
        pixel = gage_info[gage_info['DBKEY'] == db]['nex_pixel'].values[0]
        nex_dat = pd.read_csv("pix" + str(pixel) + '.csv')
        nex_dat['DateTime'] = pd.to_datetime(nex_dat['DateTime'])
        nex_dat = nex_dat[(nex_dat['DateTime'] >= '2018-01-01 00:00:00') & 
                        (nex_dat['DateTime'] <= '2019-01-01 00:00:00')]

        print(nex_dat)

        new_df = df[df['dbkey'] == db]
        print(new_df)
        
        # add nexrad plot
        plt.plot(nex_dat['DateTime'], nex_dat['RAIN'], 'o', label = pixel, color = 'black', lw = 2)

        if isFirst:
            plt.plot(new_df['datetime'], new_df['value'], 'o', label = str(db) + "_" + rec, color = 'red', lw = 1)
            isFirst = False
        else:
            plt.plot(new_df['datetime'], new_df['value'], label = str(db) + "_" + rec)


    plt.title(ss)
    plt.ylabel('Rainfall Depth (in)')
    plt.legend()
    plt.grid()
    # plt.show()

    
    os.chdir(dir_out)
    plt.savefig(ss + '.jpeg', dpi = 400)


    