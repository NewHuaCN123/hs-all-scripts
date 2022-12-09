"""  
Created on Thu Dec 08 15:29:00 2022

create concatenating text

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
from os import fdopen, remove
from tempfile import mkstemp


dir_home = "D:\\2017_ascii"

os.chdir(dir_home)

conc_template = pd.read_csv('ascii_files_2017.csv')

print(conc_template)


ff = 48
for ii in range(48,60):
    # print(ii)
    
    print("[File_{}]".format(ii-47))
    print("  InputFile = {}".format(conc_template['OutputFileName'][ff]))
    print("  Items = 1")
    print("EndSect  // File_{}".format(ii-47))
    print("\n")

    ff += 1

