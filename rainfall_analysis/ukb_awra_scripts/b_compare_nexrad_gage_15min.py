
"""  
Created on Thu Oct 20 15:20:00 2022

comparing 15min gage to NEXRAD rain
creating a merged file of nexrad and gage rainfall

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

###############
# set year here
yr = "2017"
###############


dir_home = "R:\\40715-013 UKFPLOS\\Data\\Rainfall\\"\
    "NEXRAD_Gage_15min_comparison_correction_AWRA\\gage_bk_raw"


nex = "R:\\40715-013 UKFPLOS\\Data\\Rainfall\\"\
        "NEXRAD_Gage_15min_comparison_correction_AWRA\\nexrad_raw\\{}".format(yr)

gages = "R:\\40715-013 UKFPLOS\\Data\\Rainfall\\"\
                "NEXRAD_Gage_15min_comparison_correction_AWRA\\"\
                        "gage_bk_raw\\{}\\gages".format(yr)


merged = "R:\\40715-013 UKFPLOS\\Data\\Rainfall\\"\
            "NEXRAD_Gage_15min_comparison_correction_AWRA\\"\
                    "nexrad_gage_merged\\{}".format(yr)


bk_stats = "R:\\40715-013 UKFPLOS\\Data\\Rainfall\\"\
            "NEXRAD_Gage_15min_comparison_correction_AWRA\\"\
                    "gage_bk_raw\\{}\\agg_15min".format(yr)


# get names of gages
os.chdir(dir_home)
gInfo = pd.read_csv('gage_bk_information.csv')
print(gInfo)

gageUnq = gInfo['DBKEY']

# print(gageUnq)


# nex data dictionary
nex_dict = { "2004" : ["cfij.out", "09/25/2004", "09/27/2004"], 
            "2008" : ["tsfay.out", "08/18/2008", "08/20/2008"], 
            "2011" : ["noname.out", "10/05/2011", "10/21/2011"], 
            "2017" : ["irma.out", "09/08/2017", "09/22/2017"] }


for gg in gageUnq:

    print(gg)
    
    os.chdir(gages)

    # get bk gage data
    dat = pd.read_csv(gg + "_{}.csv".format(yr))
    dat['date'] = pd.to_datetime(dat['date'])
    dat = dat[(dat['date'] >= nex_dict[yr][1]) & (dat['date'] <= nex_dict[yr][2])]


    # aggregate data every 15 min
    dat.set_index('date', inplace = True)
    # gage_agg_15m = dat.groupby(pd.Grouper(freq='15Min')).aggregate(numpy.sum)
    gage_agg_15m = dat.resample('15T', label = 'right',
                                closed = 'right').sum()


    os.chdir(bk_stats)
    # gage_agg_15m.to_csv(gg + "_gage15m.csv")


    gage_agg_15m.reset_index(inplace = True)
    print(gage_agg_15m)

    # # plotting gage data
    # plt.figure(figsize = (10,6))
    # plt.plot(gage_agg_15m['date'], gage_agg_15m['rain[in]'])
    # # plt.savefig(gg + ".jpeg", dpi = 400)
    


    # get corresponding nex pixel
    os.chdir(nex)

    print(gInfo)

    print(gg)
    pixel = gInfo[gInfo['DBKEY'] == gg]['pixel'].values[0]

    nex_data = pd.read_csv(str(pixel) + ".csv")
    nex_data['datetime'] = pd.to_datetime(nex_data['datetime'])
    nex_data = nex_data[(nex_data['datetime'] >= nex_dict[yr][1]) & \
                                    (nex_data['datetime'] <= nex_dict[yr][2])]
    
    # aggregate data every 15 min
    nex_data.set_index('datetime', inplace = True)
    # nex_agg_15m = nex_data.groupby(pd.Grouper(freq='15Min')).aggregate(numpy.sum)
    nex_agg_15m = nex_data.resample('15T', label = 'right',
                        closed = 'right').sum()
    
    nex_data.reset_index(inplace = True)
    nex_data = nex_data[['datetime', 'pixel', 'value']]
    nex_data.columns = ['date', 'pixel', 'value']
    print(nex_data)

    # merge nexrad and gage data
    datMerged = pd.merge(gage_agg_15m, nex_data, on = 'date', how = 'outer')
    datMerged = datMerged[['date', 'rain[in]', 'value']]
    datMerged.columns = ['date', 'gage', 'nexrad']

    print(datMerged)

    # save merged file
    os.chdir(merged)
    datMerged.to_csv(gg + "_" + str(pixel) + ".csv")


    ##########################
    # plotting nexrad and gage 
    plt.figure(figsize = (12,5))
    plt.plot(gage_agg_15m['date'], gage_agg_15m['rain[in]'], label = gg, color = 'blue')
    plt.plot(nex_data['date'], nex_data['value'], label = pixel, color = 'red')
    # plt.show()
    plt.legend()
    plt.savefig(gg + "_" + str(pixel) + ".jpeg", dpi = 400)
    ##########################