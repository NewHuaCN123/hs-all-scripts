"""
Created on Mon May 23 15:15:00 2022
updated in Mon Aug 22 08:50:00 2022

This script selects the highest percentiles 
and plots the scatterplot 

@author: Michael Tadesse
"""


import os 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

os.chdir("D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\MIKE_Modeling_Group -"\
        " Documents\\UKLOS\\Data\\calib_valid_selection\\combinedRefinedData")


df = pd.read_csv("threeDayRollingSumRefined.csv")
id = df.columns[1:]
# print(id)

isFirst = True

for st in id:
    print(st)
    
    # get 99.99 percentile data
    # print(df[st].quantile(0.999))
    dat = df[df[st] >= df[st].quantile(0.999)][['Daily Date', st]]
    # print(dat)
    
    if isFirst:
        newDF = dat
        isFirst = False
    else:
        newDF = pd.merge(newDF, dat, on = "Daily Date", how = "outer")
    
# print(newDF)

newDF['Daily Date'] = pd.to_datetime(newDF['Daily Date'])
newDF = newDF.sort_values(by = "Daily Date")
print(newDF)
# newDF.to_csv("higherPercentilePrecip.csv")

sns.set_context('notebook', font_scale= 1.75)

for st in id:
    plt.plot(newDF['Daily Date'], newDF[st], 'o', label = st)

plt.legend(ncol = 6, fontsize=12)
plt.ylabel('99th percentile of three day \n rolling summed precipitation (in)')
plt.grid()


plt.show()