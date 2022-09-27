"""  
Created on Wed Aug 10 16:38:00 2022

parse the data to create a dfs0 file


@author: Michael Getachew Tadesse
"""

import os
import datetime
import pandas as pd 


dir_in = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\SWFWMD\\GroundwaterLevelData\\ufa_081222"
os.chdir(dir_in)

gList = os.listdir()



for gg in gList:

    dat = pd.read_csv(gg)
    # print(dat)

    stations = dat['SID'].unique()

    isFirst = True

    for ss in stations:
        print(gg, ss)

        df = dat[dat['SID'] == ss]
        # print(df)

        ## select based on datum
        
        if len(df[df['TimeSeries'] == 'District Manual NAVD 88']) != 0:
            stDf = df[df['TimeSeries'] == 'District Manual NAVD 88']
            datum = 'navd88'
        elif len(df[df['TimeSeries'] == 'District Daily Maximum NAVD 88']) != 0:
            stDf = df[df['TimeSeries'] == 'District Daily Maximum NAVD 88']
            datum = 'navd88'
        elif len(df[df['TimeSeries'] == 'District Manual NGVD 29']) != 0:
            stDf = df[df['TimeSeries'] == 'District Manual NGVD 29']
            datum = 'ngvd29'
        else:
            stDf = df[df['TimeSeries'] == 'District Daily Maximum NGVD 29']
            datum = 'ngvd29'
        
        stDf = stDf[['Timestamp', 'Value']]
        stDf['date'] = pd.to_datetime(stDf['Timestamp']).dt.date
        stDf = stDf[['date', 'Value']]
        stDf.columns = ['date', str(str(ss) + "_"+ datum)]

        print(stDf)

        if isFirst:
            mainDf = stDf
            isFirst = False
        else:
            mainDf = pd.merge(mainDf, stDf, on = 'date', how = 'outer')

        print(mainDf)
    
    mainDf['date'] = pd.to_datetime(mainDf['date'])
    mainDf = mainDf.sort_values(by = 'date')

    mainDf.to_csv(gg.split('.csv')[0] + "_parsed.csv")


