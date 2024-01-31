"""  
Created on Wed 31 January 15:40:00 20224

read and write MIKE SHE files 

@author: Michael Getachew Tadesse

"""

import pandas as pd
import os
import numpy as np
import datetime


os.chdir("C:\\Users\\mtadesse\\OneDrive - Hazen and Sawyer\\Broward-Watershed-Plan\\Model_Files")

print(os.listdir())

# read original SHE file
dat = open("Broward_VA1.she", 'r+')

lines = dat.readlines()

# write new lines to a new SHE file
with open('test.she', 'w', encoding='utf-8') as file:  
    for txt in lines:
        print(txt)
            
        if "Meteorologic\\10y\\1" in txt:
            # print(txt)
            txt = txt.replace('Meteorologic\\10y\\1', 'Meteorologic\\25y\\1')
            # print(txt)
            
        file.writelines(txt)
    
file.close()

dat.close()