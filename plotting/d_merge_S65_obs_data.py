"""  
Created on Tue Oct 24 13:36:00 2023

merge observed data

@author: Michael Getachew Tadesse

"""

import os
import datetime
import numpy as np
import pandas as pd
import seaborn as sns
from functools import reduce
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
 


sns.set_context('notebook', font_scale = 1.5)

os.chdir("C:\\Users\\mtadesse\\OneDrive - Hazen and Sawyer\\Documents\\UKBFPLOS")


hw = pd.read_csv('S65_obs_HW.csv')
tw = pd.read_csv('S65_obs_TW.csv')
go = pd.read_csv('S65_obs_GO.csv')



# print(hw)
# print(tw)
# print(go)


dfs = [hw, tw, go]


# # merge all DataFrames into one
# final_df = reduce(lambda  left,right: pd.merge(left,right,on=['datetime'],
#                                             how='inner'), dfs)

dfs2 = pd.merge(hw, tw, on = "datetime", how = "inner")
print(dfs2)

dfs3 = pd.merge(dfs2, go, on = 'datetime', how = 'inner')
print(dfs3)
# print(final_df)

# final_df.to_csv("s65_combined_hw_tw_go.csv")