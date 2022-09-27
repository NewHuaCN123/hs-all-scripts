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

dat = pd.read_csv("all_wmds_UFA_2017_transposed.csv")

print(dat)

col_names = dat.columns[1:]
print(col_names)


df = dat[~dat.isna().any(axis = 1)]

print(df)

print(df['well_id'].tolist())


# df.to_csv('all_wmds_2011_transposed_rmvna.csv')


# for ii in col_names:
#     print(ii)
#     print(dat[ii])

# dat.fillna('no data', inplace = True)
# print(dat)

# dat.to_csv('all_wmds_2011_transposed_fillna.csv')