
import os
import pandas as pd

os.chdir('R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\calibration_validation_stats\\peak_analysis_0328\\csv')


station = "romp_74x.csv"
dat = pd.read_csv(station)

dat.iloc[:,0] = pd.to_datetime(dat.iloc[:,0])


# limit time 
dat = dat[(dat.iloc[:,0] >= "2017-09-10") & (dat.iloc[:,0] <= "2017-10-30")]

# print(dat)


# get maximum value date
print(dat[dat.iloc[:,1] == dat.iloc[:,1].max()])
