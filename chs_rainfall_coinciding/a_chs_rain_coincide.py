"""  
Created on Tue Sep 26 09:55:00 2023

coincide CHS and rainfall peak data

@author: Michael Getachew Tadesse

"""

import os
import mikeio
import datetime
import pandas as pd
import matplotlib.pyplot as plt  
from mikecore.DfsFile import DataValueType
from mikeio.eum import ItemInfo, EUMType, EUMUnit

dir_scenario = "R:\\40715-021\\Modeling\\Data\\CHS_data\\New_BND_Files\\Events_tobe_Simulated"
# dir_out = "C:\\Users\\mtadesse\\Downloads\\rainfall_analysis\\rain_10yr_25yr_100yr\\concatenated_rain\\rain_100yr"

# scenarios
scenario = ['Scenario1', 'Scenario2',
            'Scenario3', 'Scenario4',
            'Scenario5', 'Scenario6',
            'Scenario7']

# CHS save points
savepoint = ['30214', '30450', '30814', '31429']
# datum conversion
datum = {'30214':-1.572, '30450':-1.578, '30814':-1.588, '31429':-1.565}

# rainfall data
rain = {'Scenario1':'5y_extracted.csv', 'Scenario2':'10y_extracted.csv', 
        'Scenario3':'10y_extracted.csv', 'Scenario4':'25y_extracted.csv',
        'Scenario5':'25y_extracted.csv', 'Scenario6':'100y_extracted.csv',
        'Scenario7':'100y_extracted.csv', 'Scenario8':'500y_extracted.csv'}

# horizon years
hoz_yr = ['2035', '2085']



def getCHSData(scenario, savepoint, hoz_yr):
    """
    this function gets the data
    """

    os.chdir(dir_scenario + "\\{}\\{}\\{}".format(scenario,savepoint,hoz_yr))
    # print(os.listdir())

    print(scenario,savepoint, hoz_yr)

    # read each CHS dat under this folder:
    for ii in os.listdir():

        os.chdir(dir_scenario + "\\{}\\{}\\{}".format(scenario,savepoint,hoz_yr))
        
        print(ii)

        dat = pd.read_csv(ii)
        # print(dat)

        # convert to NGVD29
        zshift = datum[savepoint]
        dat['Water level (ft NGVD29)'] = dat['value'] - zshift

        # # plot the data
        # plotIt(dat)

        # print(dat)
        chs_date = getCHSPeak(dat)

        # get corresponding rain delta in hours
        delta, start_time = getRainData(scenario)

        new_chs_date = getCHSRainDiff(chs_date, delta)
        print(new_chs_date)

        new_chs = getNewCHS(dat, new_chs_date)
        new_chs.reset_index(inplace = True)
        new_chs = new_chs.iloc[:,1:]

        # add the timesteps that start with that of rainfall
        new_chs['datetime'] = pd.date_range(start_time, freq='15T', periods=len(new_chs))
        new_chs = new_chs[['datetime', 'Water level (ft NGVD29)']]
        print(new_chs)

        # plotIt(new_chs)

        # save as csv
        os.chdir(dir_scenario + "\\{}\\{}\\{}".format(scenario,savepoint,hoz_yr))
        new_chs.to_csv(ii.split(".csv")[0] + "_SHIFTED.csv")





def getNewCHS(dat, new_chs_date):
    dat = dat[dat.iloc[:,0] >= new_chs_date]
    print(dat)
    return dat



def getRainData(scenario):
    """
    this function gets the rainfall data
    """
    os.chdir(dir_scenario + "\\{}".format(scenario))
    dat = pd.read_csv(rain[scenario])
    dat = dat.iloc[:,1:]

    # print(dat)

    # # plot rain
    # plotIt(dat)

    delta, start_time = getRainPeak(dat)

    return delta, start_time



def getCHSPeak(dat):
    """
    this function gets the peak of the CHS time series
    """
    # print(dat)
    dat.iloc[:,0] = pd.to_datetime(dat.iloc[:,0])
    # print(dat[dat['Water level (ft NGVD29)'] == dat['Water level (ft NGVD29)'].max()])

    return dat[dat['Water level (ft NGVD29)'] == dat['Water level (ft NGVD29)'].max()]['Time'].values[0]



def getRainPeak(dat):
    """
    this function gets the peak of the rain data
    """
    print(dat)
    dat.iloc[:,0] = pd.to_datetime(dat.iloc[:,0])

    start_time = dat.iloc[:,0][0]
    peak_time = dat[dat.iloc[:,1] == dat.iloc[:,1].max()]['index'].values[0]

    # print(start_time)
    # print(peak_time)

    delta_hr = (peak_time - start_time)/ pd.Timedelta(hours=1)

    return delta_hr, start_time


def getCHSRainDiff(chs_date, delta):
    """
    this function returns the time when the CHS timeseries
    should start in order to match the rain peak
    """
    return chs_date - pd.Timedelta(hours = delta)


def plotIt(dat):
    """
    this function plots any given dataframe
    """
    dat.iloc[:,0] = pd.to_datetime(dat.iloc[:,0])
    plt.figure(figsize = (14,6))
    plt.plot(dat.iloc[:,0], dat.iloc[:,1])
    plt.grid()
    plt.show()






#### Execution

for ss in scenario:
    for sv in savepoint:
        for hh in hoz_yr:
            getCHSData(ss, sv, hh)