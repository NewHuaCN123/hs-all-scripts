"""  
Created on Wed Aug 04 11:31:00 2022

select rainfall data from three districts
based on priority

1. SFWMD
2. SWFWMD
3. SJRWMD

@author: Michael Getachew Tadesse

"""
import shutil
import os
import pandas as pd 
import datetime
from os.path import exists


sf = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\FromSFWMD\\"\
            "rainfall_modified_files\\pixel_rainfall_distributed\\2017_dfs0"

sj = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\FromSJRWMD\\"\
            "Rainfall\\modified_files\\pixel_rainfall_distributed\\2017_dfs0"

sw = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\SWFWMD\\"\
            "rainfall\\pixel_rainfall_distributed\\2017_dfs0"


out = "R:\\40715-013 UKFPLOS\\Data\\Rainfall\\NEXRAD_UKB_prioritized\\2017"

# get unique pixel ids across the three districts 
os.chdir(sf)
sf_pix = pd.DataFrame(os.listdir(), columns = ['pixel'])
sf_pix['d1'] = 'sf'

os.chdir(sj)
sj_pix = pd.DataFrame(os.listdir(), columns = ['pixel'])
sj_pix['d2'] = 'sj'

os.chdir(sw)
sw_pix = pd.DataFrame(os.listdir(), columns = ['pixel'])
sw_pix['d3'] = 'sw'


sd_sj = pd.merge(sf_pix, sj_pix, on = 'pixel', how = 'outer')
all_pix = pd.merge(sd_sj, sw_pix, on = 'pixel', how = 'outer')
print(all_pix)


# os.chdir("R:\\40715-013 UKFPLOS\\Data\\Rainfall\\NEXRAD_UKB_prioritized")
# all_pix.to_csv("pixel_priority_from_three_wmds.csv")


# for pp in range(len(all_pix)):

    if all_pix['d1'][pp] == 'sf':
        print(all_pix['pixel'][pp], "sf")

        os.chdir(sf)
        source = os.path.join(os.path.abspath(os.getcwd()), all_pix['pixel'][pp])
        destination = os.path.join(out, all_pix['pixel'][pp])

        shutil.copyfile(source, destination)

    elif all_pix['d3'][pp] == 'sw':
        print(all_pix['pixel'][pp], "sw")

        os.chdir(sw)
        source = os.path.join(os.path.abspath(os.getcwd()), all_pix['pixel'][pp])
        destination = os.path.join(out, all_pix['pixel'][pp])

        shutil.copyfile(source, destination)
    
    elif all_pix['d2'][pp] == 'sj':
        print(all_pix['pixel'][pp], "sj")

        os.chdir(sj)
        source = os.path.join(os.path.abspath(os.getcwd()), all_pix['pixel'][pp])
        destination = os.path.join(out, all_pix['pixel'][pp])

        shutil.copyfile(source, destination)









