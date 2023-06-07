"""  
Created on Thu Jan 05 16:20:00 2023

get the peak stage/flow and time

@author: Michael Getachew Tadesse
"""

import os
import glob
import datetime
import pandas as pd 


dir_in = "R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\calibration_validation_stats\\"\
            "calibration_stats_full\\sent_by_RR_010323\\Calibration\\DFS0\\DBK"

os.chdir(dir_in)


all_stations = glob.glob("*.csv")

# print(all_stations)

#################
new_text = 'G113_T'
station = 'G113_T-42035-SW.csv'
################


def filterStations(new_text):

    select_station = [ii for ii in all_stations if ii.startswith(new_text)]

    for ii in select_station:
        print(ii)


filterStations(new_text)



def getMax(dat):
    dat['Date'] = pd.to_datetime(dat['Date'])

    # adjust datetime here
    # this has been changed ot 09/07
    new_dat = dat[(dat['Date'] >= '2017-09-07') & 
                        (dat['Date'] <= '2017-10-30')]

    new_dat.reset_index(inplace = True)
    new_dat = new_dat.iloc[:, 1:]
    print(new_dat, '\n')

    # get row that has max values

    max_dat = new_dat[new_dat.iloc[:,1] == new_dat.iloc[:,1].max()]
    print(max_dat)


def openFile(station):
    dat = pd.read_csv(station)
    # print(dat)
    
    getMax(dat)

openFile(station)







