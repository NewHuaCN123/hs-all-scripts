"""  
Created on Wed Aug 10 14:05:00 2022

parse the data to create a dfs0 file
*get unique column names

@author: Michael Getachew Tadesse
"""

import os
import pandas as pd 


dir_in = "R:\\40715-013 UKFPLOS\\Data\\GW\\per_WMDs\\sfwmd"


os.chdir(dir_in)

zshift = pd.read_csv('zshift.csv')

dat = pd.read_csv('sfwmd_wells.csv')

print(dat)
print(dat.columns)

# get columns with name 'Qualifier'

col_names = dat.columns
col_names = [x.strip() for x in col_names]

dat.columns = col_names


qual_col = [x for x in col_names if "Qualifier" in x ]

# drop qualifier columns

dat = dat.drop(qual_col, axis = 1)
# dat.to_csv("sfwmd_no_qualifier.csv")

print(dat)

ii = 2

while ii < len(dat.columns):
    # print(ii)
    # print(dat.iloc[:, ii])

    # find column name

    col_name = str(dat.iloc[0, ii-1]).strip()
    # print(col_name)

    # print(dat.columns[ii], col_name)

    # change column name
    dat = dat.rename(columns = {dat.columns[ii] : col_name})

    ii += 2

# print(dat)

# remove DBKEY columns
new_col_names = dat.columns

# print(new_col_names)

# new_col_names = [str(x).strip() for x in new_col_names]


db_col = [x for x in new_col_names if "DBKEY" in x ]

# drop dbkey columns

dat = dat.drop(db_col, axis = 1)

# print(dat)
print(dat.columns)

# dat.to_csv("sfwmd_no_dbkey.csv")


# get unique names of wells
dat_unq = dat.loc[:,~dat.columns.duplicated()].copy()

print(dat_unq)



# # convert to NAVD88 
# col = dat_unq.columns[1:]

# for cc in col:
#     # get zshift
#     z = zshift[zshift['dbkey'] == cc]['zshift']
#     print(cc, z.values[0])


#     print(dat_unq[cc])
#     print(dat_unq[cc] + z)
#     # dat_unq[cc] = dat_unq[cc] + z


dat_unq.to_csv("sfwmd_GW_cleaned_v2.csv")