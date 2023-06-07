"""  
Created on Thu Dec 08 15:29:00 2022

replace input file name

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


dir_home = "R:\\40715-013 UKFPLOS\\Data\\GW\\init_cond_boundary_files\\updated_intp_rasters\\2017\\sas\\ascii"
template_dir = "R:\\40715-013 UKFPLOS\\Data\\GW\\init_cond_boundary_files\\updated_intp_rasters\\2017\\sas\\ascii_templates"


os.chdir(dir_home)

ascii_files = pd.DataFrame(glob.glob('*.asc'))
ascii_info = pd.read_csv("ascii_files_2017.csv")



print(ascii_files) 
print(ascii_info) 


# looping through the file

# file counting
j = 1 

for ff in ascii_info['files']:
    print(ff)
    
    os.chdir(template_dir)
    file = open("mzt_template.mzt", "r")
    replaced_content = ""

    line_number = 13

    i = 1
    for line in file:

        # stripping line break

        line = line.strip()

        if i == 13:
            replace_name = ascii_info[ascii_info['files'] == ff]['InputFileName'].values[0]
            # print(replace_name)


            replace_name_2 = "InputFileName = " + replace_name
            new_line = line.replace("InputFileName =", replace_name_2)
            # replaced_content = replaced_content + new_line + "\n"
        elif i == 15:
            replace_name3 = ascii_info[ascii_info['files'] == ff]['OutputFileName'].values[0]
            # print(replace_name)

            replace_name_4 = "OutputFileName = " + replace_name3
            new_line = line.replace("OutputFileName =", replace_name_4)
            # replaced_content = replaced_content + new_line + "\n"
        else:
            new_line = line
        
        replaced_content = replaced_content + new_line + "\n"

        print(replaced_content)

        i += 1

        # file.close()

        #Open file in write mode
        write_file = open("mzt_" + str(j) + ".mzt", "w")
        #overwriting the old file contents with the new/replaced content
        write_file.write(replaced_content)
        #close the file
        write_file.close()    


    j += 1