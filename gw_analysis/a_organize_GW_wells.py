"""  
Created on Wed Aug 08 14:50:00 2022

parse GW data into separate csv files
for each well

*the script also cleans up raw DBHYDRO data

@author: Michael Getachew Tadesse
"""

import os
import pandas as pd 


dir_in = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\FromSFWMD\\GW\\all_sfwmd_wells"
out = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\FromSFWMD\\GW\\cleaned_well_data"
dir_meta = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\FromSFWMD\\GW"

os.chdir(dir_meta)

metadata = pd.read_csv("ukb_sf_GW_wells_sites_zshift_v4.csv")

print(metadata)


os.chdir(dir_in)
gwList = os.listdir()

for gg in gwList:
    print(gg)

    dat = pd.read_fwf(gg, header = None)

    # print(dat.head(30))


    start_index = dat[dat.iloc[:,0].str.contains("Daily")].index
    end_index = dat[dat.iloc[:,0].str.contains("Query")].index
    
    newDat = dat.iloc[start_index.values[0] + 1:end_index.values[0], :]
    newDat.reset_index(inplace = True)
    newDat = newDat.drop('index', axis = 1)

    # print(newDat)

    # separate columns
    newDat = newDat.iloc[:, 0].str.split(',', expand = True)

    # number of columns
    col_num = newDat.shape[1]

    # print(newDat)

    # select date, dbkey, and value columns
    i = 1

    while i <= (col_num - 3):
        print(i)

        df = newDat[[0, i, i+1]]
        df.columns = ['date', 'dbkey', 'value']


        df['date'] = df['date'].str.replace('"', '')
        df['dbkey'] = df['dbkey'].str.replace('"', '')
        df['value'] = pd.to_numeric(df['value'].str.replace('"', ''))

        # print(df)

        # get zshift value

        dbk = df['dbkey'].unique()[0]
        print(dbk)

        zshift = metadata[metadata['DBKEY'] == dbk]['zshift1'].unique()
        print(zshift)

        i += 3