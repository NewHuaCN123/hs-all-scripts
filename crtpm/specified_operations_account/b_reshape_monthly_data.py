"""  
Created on Wed Mar 20 12:29:00 2024

Reshape monthly aggregated output
CRTPM

@author: Michael Getachew Tadesse

"""

import os 
import datetime as dt
import numpy as np
import pandas as pd

os.chdir("C:\\Users\\mtadesse\\OneDrive - Hazen and Sawyer"\
            "\\OASIS\\CRTPM\\Data\\specified_account_postprocessing")

filename = "processed_mon_data_1.96_2FF.csv"



dat = pd.read_csv(filename)
dat = dat.iloc[:, 1:]

# round off to two significant digits
dat['monthly_used'] = dat['monthly_used'].round(decimals=2)
dat['monthly_filled'] = dat['monthly_filled'].round(decimals=2)
dat['percent_used'] = dat['percent_used'].round(decimals=2)
dat['percent_filled'] = dat['percent_used'].round(decimals=2)


# rename date column to "Oct-1938"
dat['DATE'] = pd.to_datetime(dat['DATE'])
dat['year'] = pd.DatetimeIndex(dat['DATE']).year
dat['DATE'] = pd.to_datetime(dat['DATE']).dt.strftime('%b-%Y')
dat['mon'] = pd.to_datetime(dat['DATE']).dt.strftime('%b')
dat_mjjaso = dat[dat['DATE'].str.startswith
                 (tuple(['May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']))]

# print(dat)
print(dat_mjjaso)

# pivot table
pivoted = pd.pivot_table(dat_mjjaso, index = ['year'], columns = 'mon', 
                    values = ['monthly_used', 
                              'monthly_filled', 'percent_used', 'percent_filled'], 
                    sort = False)
print(pivoted)

# print(pivoted.loc[:, ('monthly_used')])
pivoted['total_used'] = pivoted.loc[:, ('monthly_used')].sum(axis = 1)
pivoted['total_filled'] = pivoted.loc[:, ('monthly_filled')].sum(axis = 1)
print(pivoted)

# save data
savename = "final_processed_" + filename.split("processed_mon_data_")[1] + ".xlsx"
print(savename)
pivoted.to_excel(savename)

