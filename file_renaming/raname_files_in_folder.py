"""  
Created on Fri Dec 09 12:51:00 2022

rename files in a folder

@author: Michael Getachew Tadesse
"""
import os
   
dir_home = "R:\\40715-013 UKFPLOS\\Data\\ufa_sa_differences\\2017\\ufa"

os.chdir(dir_home)


for filename in os.listdir():
    print(filename)

    if filename.endswith(".tif"):
        os.rename(filename, filename.split(".tif")[0] + "_ufa.tif")

