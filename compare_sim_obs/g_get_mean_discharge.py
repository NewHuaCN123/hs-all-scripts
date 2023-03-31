
import os
import pandas as pd

os.chdir('R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\calibration_validation_stats\\validation_stats_0329\\obs_flows')


station = "boggy_creek.csv"
dat = pd.read_csv(station)
dat.iloc[:,0] = pd.to_datetime(dat.iloc[:,0])

# print(dat)

# limit time 
df1 = dat[(dat.iloc[:,0] >= "2011-09-21") & (dat.iloc[:,0] <= "2011-11-15")]
# print(df1)
df2 = dat[(dat.iloc[:,0] >= "2011-09-29") & (dat.iloc[:,0] <= "2011-11-15")]
# print(df2)
df3 = dat[(dat.iloc[:,0] >= "2011-10-03") & (dat.iloc[:,0] <= "2011-10-27")]
# print(df3)


# get nonzero values of the dataframes
df1 = df1[df1.iloc[:,1] != 0]
df2 = df2[df2.iloc[:,1] != 0]
df3 = df3[df3.iloc[:,1] != 0]

# get average value
# print("average '0921-1115' = ", df1.iloc[:,1].mean())
# print("average '0929-1115' = ", df2.iloc[:,1].mean())
print("average '1003-1027' = ", df3.iloc[:,1].mean())
