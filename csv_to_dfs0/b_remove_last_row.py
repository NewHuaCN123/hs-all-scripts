"""  
Created on Fri Aug 04 20:37:00 2023

remove the last row the data downloaded from DBHYDRO

@author: Michael Getachew Tadesse

"""

import os
import pandas as pd 

dir_in = "R:\\KB_USACE\\Data\\data_from_dbhydro\\SW\\stage_clean"
dir_out = "R:\\KB_USACE\\Data\\data_from_dbhydro\\SW\\stage_clean_v2"



os.chdir(dir_in)

dfList = os.listdir()

# dfList = ['C38BAS.csv']

for pp in dfList:
    os.chdir(dir_in)
    print(pp)

    dat = pd.read_csv(pp)

    # print(dat)

    newDat = dat.head(dat.shape[0] -1)

    os.chdir(dir_out)

    newDat.to_csv(pp)
