"""  
Created on Tue Apr 16 2024 11:24:00

Analyze SO_Exhausted

@author: Michael Getachew Tadesse

"""
import os
import datetime
import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


os.chdir("C:\\Users\\mtadesse\\OneDrive - Hazen and Sawyer\\OASIS\\CRTPM\\Data\\FxnFLow_analysis")

dat = pd.read_csv("SO_Exhausted.csv")
dat['datetime'] = pd.to_datetime(dat['datetime'])
dat['year'] = dat['datetime'].dt.year

print(dat)

# filter dataframe with so_exhausted == 1
dat_100 = dat[dat['so_exhausted_100kcfs'] == 1]
dat_120 = dat[dat['so_exhausted_120kcfs'] == 1]
dat_140 = dat[dat['so_exhausted_140kcfs'] == 1]

# pick the first rows of this dataframe
dat_100.reset_index(inplace = True)
dat_120.reset_index(inplace = True)
dat_140.reset_index(inplace = True)

unique_yr = dat_100['year'].unique()
print(unique_yr)
print(dat_100)

# create new dataframe
dat_100_so = pd.DataFrame(columns = ['year', 'so_exhausted', 'day_year'])
dat_120_so = pd.DataFrame(columns = ['year', 'so_exhausted', 'day_year'])
dat_140_so = pd.DataFrame(columns = ['year', 'so_exhausted', 'day_year'])

isFirst = True
for yy in unique_yr:
    new_dat = dat_100[(dat_100['year'] == yy) & dat_100["so_exhausted_100kcfs"] == 1]
    new_dat.reset_index(inplace = True)
    print(new_dat)

    # print(str(pd.Timestamp(str((new_dat.iloc[0,2]))).month) + "-datetime")
    # print(pd.Timestamp(str((new_dat.iloc[0,2]))).timetuple().tm_yday)

    day_year = pd.Timestamp(str((new_dat.iloc[0,2]))).timetuple().tm_yday

    df = pd.DataFrame([yy, 
            str(pd.Timestamp(str((new_dat.iloc[0,2]))).month) + "/"+
                  str(pd.Timestamp(str((new_dat.iloc[0,2]))).day), day_year]).T

    df.columns = ['year', 'so_exhausted', 'day_year']
    

    if isFirst:
        dat_100_so = df
        isFirst = False
    else:
        dat_100_so = pd.concat([dat_100_so, df])

dat_100_so.reset_index(inplace = True)

# 120kcfs
fname = dat_120
isFirst = True
for yy in unique_yr:
    new_dat = fname[(fname['year'] == yy) & fname["so_exhausted_120kcfs"] == 1]
    new_dat.reset_index(inplace = True)
    print(new_dat)

    # print(str(pd.Timestamp(str((new_dat.iloc[0,2]))).month) + "-datetime")
    # print(pd.Timestamp(str((new_dat.iloc[0,2]))).timetuple().tm_yday)

    day_year = pd.Timestamp(str((new_dat.iloc[0,2]))).timetuple().tm_yday

    df = pd.DataFrame([yy, 
            str(pd.Timestamp(str((new_dat.iloc[0,2]))).month) + "/"+
                  str(pd.Timestamp(str((new_dat.iloc[0,2]))).day), day_year]).T

    df.columns = ['year', 'so_exhausted', 'day_year']
    

    if isFirst:
        dat_120_so = df
        isFirst = False
    else:
        dat_120_so = pd.concat([dat_120_so, df])

dat_120_so.reset_index(inplace = True)

# 140kcfs
fname = dat_140
isFirst = True
for yy in unique_yr:
    new_dat = fname[(fname['year'] == yy) & fname["so_exhausted_140kcfs"] == 1]
    new_dat.reset_index(inplace = True)
    # print(new_dat)

    # print(str(pd.Timestamp(str((new_dat.iloc[0,2]))).month) + "-datetime")
    # print(pd.Timestamp(str((new_dat.iloc[0,2]))).timetuple().tm_yday)

    day_year = pd.Timestamp(str((new_dat.iloc[0,2]))).timetuple().tm_yday

    df = pd.DataFrame([yy, 
            str(pd.Timestamp(str((new_dat.iloc[0,2]))).month) + "/"+
                  str(pd.Timestamp(str((new_dat.iloc[0,2]))).day), day_year]).T

    df.columns = ['year', 'so_exhausted', 'day_year']
    

    if isFirst:
        dat_140_so = df
        isFirst = False
    else:
        dat_140_so = pd.concat([dat_140_so, df])

dat_140_so.reset_index(inplace = True)

print(dat_100_so)
print(dat_120_so)
print(dat_140_so)



# # plot
plt.figure(figsize = (18,6))
plt.rcParams.update({'font.size': 12})
plt.grid()

# plt.scatter(dat_100_so['year'], dat_100_so['day_year'], 
#             c = "k", label = "SO_Exhausted = 100kcfs")

sns.regplot(data=dat_100_so, x="year", y="day_year", fit_reg=False, 
            marker="o", color="skyblue", scatter_kws={'s':75}, label = "FxnFlow = 100kcfs")

# add annotations one by one with a loop
for line in range(0,dat_100_so.shape[0]):
     plt.text(dat_100_so.year[line], dat_100_so.day_year[line]+3, 
              dat_100_so.so_exhausted[line], 
                verticalalignment='bottom', size='x-small', color='blue', weight='semibold')

# 120kcfs
sns.regplot(data=dat_120_so, x="year", y="day_year", fit_reg=False, 
            marker="o", color="red", scatter_kws={'s':75}, label = "FxnFlow = 120kcfs")

# add annotations one by one with a loop
for line in range(0,dat_120_so.shape[0]):
     plt.text(dat_120_so.year[line], dat_120_so.day_year[line]-10, 
              dat_120_so.so_exhausted[line], 
                verticalalignment='bottom', size='x-small', color='red', weight='semibold')
# 140kcfs
sns.regplot(data=dat_120_so, x="year", y="day_year", fit_reg=False, 
            marker="x", color="darkslategray", scatter_kws={'s':75}, label = "FxnFlow = 140kcfs")

# add annotations one by one with a loop
for line in range(0,dat_140_so.shape[0]):
     plt.text(dat_140_so.year[line], dat_140_so.day_year[line]-15, 
              dat_140_so.so_exhausted[line], 
                verticalalignment='bottom', size='x-small', color='darkslategray', weight='semibold')



plt.xticks(np.arange(dat_100_so['year'].min(), dat_100_so['year'].max(), 3)) 
plt.ylabel('Day of Year when SO is Exhausted')
plt.title("Functional Flow Sensitivity Analysis")
plt.ylim([150,366])
plt.legend(ncol = 3)
plt.savefig("FxnFlow_Sensitivity_Analysis", dpi = 400)
plt.show()

