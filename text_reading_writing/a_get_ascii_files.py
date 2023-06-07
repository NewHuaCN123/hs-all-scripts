"""  
Created on Thu Dec 08 15:29:00 2022

get all ascii files

@author: Michael Getachew Tadesse
"""
import os
import logging
import datetime
import numpy
import glob
import pandas as pd
import seaborn as sns
import matplotlib.colors as mcolors
import matplotlib.dates as mdates
import matplotlib.pyplot as plt


dir_home = "R:\\40715-013 UKFPLOS\\Data\\GW\\init_cond_boundary_files\\updated_intp_rasters\\2017\\sas\\just_ascii"

os.chdir(dir_home)

ascii_files = pd.DataFrame(glob.glob('*.asc'))

print(ascii_files)

ascii_files.to_csv('ascii_files_2017.csv')