"""  
Created on Wed Aug 12 08:27:00 2022

converting date format


@author: Michael Getachew Tadesse
"""

import os
import datetime
import pandas as pd 


dir_in = "R:\\40715-013 UKFPLOS\\Data\\GW\\init_cond_boundary_files\\raw_data"
os.chdir(dir_in)

dat = pd.read_csv("all_wmd_dates.csv")

print(dat)


dat['date'] = pd.to_datetime(dat['date'])
dat['date_id'] = dat['date'].dt.strftime('%m%d%y')

print(dat)

dat.to_csv('all_wmd_dates_abridged.csv')