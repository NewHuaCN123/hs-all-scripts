"""  
Created on Wed Aug 11 17:57:00 2022
modified on Mon Aug 15 09:44:00 2022

combine all WMD wells to prepare for
spatial/surface dataset - interpolated

separate by year (2011, 2017)
separate by aquifer (SA, UFA)
*turn on/off SA and UFA code snippets

@author: Michael Getachew Tadesse
"""

import os
import datetime
import pandas as pd 

# get file with aquifer details
dir_aquifer = "R:\\40715-013 UKFPLOS\\Data\\GW\\per_Aquifer"
os.chdir(dir_aquifer)

dat_aqu = pd.read_csv('wells_by_aquifer.csv')
print(dat_aqu)


dir_in = "R:\\40715-013 UKFPLOS\\Data\\GW\\init_cond_boundary_files\\"\
                "raw_data\\wmd_data"
os.chdir(dir_in)


wmdList = os.listdir()

isFirst = True
for ww in wmdList:
    print(ww)

    dat = pd.read_csv(ww)

    # adjust date
    dat['date'] = pd.to_datetime(dat['date'])
    dat = dat[(dat['date'] >= '2017-09-01') & (dat['date'] <= '2017-10-30')]
    dat.reset_index(inplace = True)
    dat.drop('index', axis = 1, inplace = True)
    # print(dat)

    if isFirst:
        df = dat
        isFirst = False
    else:
        df = pd.merge(df, dat, on = 'date', how = 'outer')
    
print(df)


# ###############
# # SA wells list

# sa_wells = dat_aqu[dat_aqu['well_aquif'] == "SA"]['well_id'].tolist()
# print(len(sa_wells))
# df2 = pd.concat([df['date'], df[sa_wells]], axis = 1)
# print(df2)
# ###############


###############
# UFA wells list

ufa_wells = dat_aqu[dat_aqu['well_aquif'] == "UFA"]['well_id'].tolist()
print(len(ufa_wells))
df2 = pd.concat([df['date'], df[ufa_wells]], axis = 1)
print(df2)
###############



##################################

df2.to_csv('all_wmds_UFA_2017.csv')
##################################

##################################
df3 = df2.T
df3.to_csv('all_wmds_UFA_2017_transposed.csv')
##################################
