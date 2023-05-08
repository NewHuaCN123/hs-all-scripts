

import os
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from scipy.stats import pearsonr 
import hydroeval as he
import matplotlib.pyplot as plt



obs_dir = 'D:\\data_transfer\\may-08\\combined_flows_data'
out_dir = 'D:\\data_transfer\\may-08\\combined_flows_data\\summed'


station = "i75w1"

weir = "{}_w.csv".format(station)
spillway = "{}_s.csv".format(station)


os.chdir(obs_dir)
dWeir = pd.read_csv(weir)
dWeir['datetime'] = pd.to_datetime(dWeir['datetime'])

dSpilw = pd.read_csv(spillway)
# print(dSpilw)
dSpilw['datetime'] = pd.to_datetime(dSpilw['datetime'])

# print(dWeir)


# aggregate hourly
dWeir.set_index(dWeir['datetime'], inplace = True)
weir_agg = pd.DataFrame(dWeir.iloc[:,1].resample('H').mean())
# print(weir_agg)

dSpilw.set_index(dSpilw['datetime'], inplace = True)
spilw_agg = pd.DataFrame(dSpilw.iloc[:,1].resample('H').mean())
# print(spilw_agg)


# merge obs and sim
dMerged = pd.merge(weir_agg, spilw_agg, on = 'datetime', how = 'inner')
# print(dMerged)


dMerged.reset_index(inplace = True)
dMerged.dropna(inplace = True)

# sum weir and spillway
dMerged['summed'] = dMerged['value_w'] + dMerged['value_s']
print(dMerged)

os.chdir(out_dir)
dMerged.to_csv(station + ".csv")