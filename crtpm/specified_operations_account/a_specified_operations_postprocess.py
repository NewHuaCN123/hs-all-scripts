"""  
Created on Wed Mar 20 08:49:00 2024

Post-process outputs of Specified Operations
CRTPM

@author: Michael Getachew Tadesse

"""

import os 
import datetime as dt
import numpy as np
import pandas as pd

os.chdir("C:\\Users\\mtadesse\\OneDrive - Hazen and Sawyer"\
            "\\OASIS\\CRTPM\\Data\\specified_account_postprocessing")



# read SO output
# create daily used + daily filled + percent used + percent filled
def get_data(filename):
    dat = pd.read_csv(filename)
    dat['DATE'] = pd.to_datetime(dat['DATE'])
    # print(dat)
    return dat

def add_used_filled(dat):
    dat['daily_used'] = 'nan'
    dat['daily_filled'] = 'nan'
    dat['percent_used'] = 'nan'
    dat['percent_filled'] = 'nan'

    isFirst = True
    for ii in range(len(dat)):
        # print(dat['MAF'][ii])
        if isFirst:
            dat['daily_used'][ii] = SO_account - dat['MAF'][ii]
            dat['daily_filled'][ii] = -(SO_account - dat['MAF'][ii])
            dat['percent_used'][ii] = 100*dat['daily_used'][ii]/ SO_account
            dat['percent_filled'][ii] = 100*dat['daily_filled'][ii]/ SO_account
            isFirst = False

        # when SO account is not being used at all
        elif (dat['MAF'][ii] == SO_account) | (dat['MAF'][ii] == dat['MAF'][ii-1]):
            dat['daily_used'][ii] = 0
            dat['daily_filled'][ii] = 0
            dat['percent_used'][ii] = 100*dat['daily_used'][ii]/ SO_account
            dat['percent_filled'][ii] = 100*dat['daily_filled'][ii]/ SO_account

        # when SO is being used
        elif (dat['MAF'][ii-1] > dat['MAF'][ii]):
            dat['daily_used'][ii] = dat['MAF'][ii-1] - dat['MAF'][ii]
            dat['daily_filled'][ii] = 0
            dat['percent_used'][ii] = 100*dat['daily_used'][ii]/ SO_account
            dat['percent_filled'][ii] = 100*dat['daily_filled'][ii]/ SO_account
        
        # when SO is being refilled
        elif (dat['MAF'][ii-1] < dat['MAF'][ii]):
            dat['daily_used'][ii] = 0
            dat['daily_filled'][ii] = dat['MAF'][ii] - dat['MAF'][ii-1]
            dat['percent_used'][ii] = 100*dat['daily_used'][ii]/ SO_account
            dat['percent_filled'][ii] = 100*dat['daily_filled'][ii]/ SO_account

    print(dat.iloc[1028:1070, :])
    
    return dat

# aggregate monthly
def mon_aggregate(dat):
    dat.set_index("DATE", inplace = True)
    dat_agg = dat.groupby(pd.Grouper(freq = "M"))[['daily_used', 'daily_filled']].sum()
    # [['daily_used', 'daily_filled']].sum()
    dat_agg.reset_index(inplace = True)

    dat_agg.columns = ['DATE', 'monthly_used', 'monthly_filled']

    # add percent used + percent filled
    dat_agg['percent_used'] = 100*dat_agg['monthly_used']/SO_account
    dat_agg['percent_filled'] = 100*dat_agg['monthly_filled']/SO_account

    print(dat_agg.iloc[30:40,:])

## input parameters
SO_account = 1

dat = get_data("data_v1.96_1FF.csv")
dat_used_filled = add_used_filled(dat)
dat_mon_agg = mon_aggregate(dat_used_filled)
