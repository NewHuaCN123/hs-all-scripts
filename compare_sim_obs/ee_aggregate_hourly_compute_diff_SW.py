"""  
Created on Wed Aug 29 10:06:00 2023

compare observed and simulated timeseries
by doing hourly aggregation

@author: Michael Getachew Tadesse

"""

import os
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from scipy.stats import pearsonr 
import matplotlib.pyplot as plt


obs_dir = 'R:\\40715-010\\Data\\calibration_stats\\bcb_stat_summary\\0828'
sim_dir = 'R:\\40715-010\\Data\\calibration_stats\\bcb_stat_summary\\0828'
out_dir = 'R:\\40715-010\\Data\\calibration_stats\\bcb_stat_summary\\0828'


os.chdir(obs_dir)

station = "CUR1-T_39043_BK_NAVD88_GapFilled"
obs = pd.read_csv('{}.csv'.format(station))
# print(obs)
obs['datetime'] = pd.to_datetime(obs['datetime'])

print(obs)

os.chdir(sim_dir)
sim = pd.read_csv('CurryCan_Stages.csv')
print(sim)
sim['datetime'] = pd.to_datetime(sim['datetime'])


# # consider only data past '2017-09-10'
# # but for short period analysis do 09/10 - 09/18
sim = sim[(sim['datetime'] >= '2017-07-01') & (sim['datetime'] <= '2020-12-31')]

sim = sim[['datetime', "CurryCan 106.68 "]]
sim["CurryCan 106.68 "] = sim["CurryCan 106.68 "]/0.3048
print(sim)

# # convert CMS to CFS
# sim[station + "_sim"] = sim[station + "_sim"]
# print(sim)

obs.set_index(obs['datetime'], inplace = True)
obs_agg = pd.DataFrame(obs.iloc[:,1].resample('H').mean())

print(obs_agg)

# aggregate sim timeseries
sim.set_index(sim['datetime'], inplace = True)
sim_agg = pd.DataFrame(sim.iloc[:,1].resample('H').mean())
print(sim_agg)

# merge obs and sim
dat_merged = pd.merge(sim_agg, obs_agg, on = 'datetime', how = 'inner')

dat_merged.reset_index(inplace = True)
dat_merged.dropna(inplace = True)
print(dat_merged)


# # calculate calibration target
# dat_merged.columns = ['datetime', 'sim', 'obs']
# dat_merged['good_criteria'] = (dat_merged['sim'] >= 0.85*dat_merged['obs']) & (dat_merged['sim'] <= 1.15*dat_merged['obs']) 
# dat_merged['acceptable_criteria'] = (dat_merged['sim'] >= 0.70*dat_merged['obs']) & (dat_merged['sim'] <= 1.30*dat_merged['obs']) 


# # count TRUE 
# dat_merged['good_perc'] = len(dat_merged[dat_merged['good_criteria'] == True])/len(dat_merged)
# dat_merged['acc_perc'] = len(dat_merged[dat_merged['acceptable_criteria'] == True])/len(dat_merged)
# print(dat_merged)


# calculate stats
# observation is the second one - first simulated
dat_merged['diff'] = dat_merged.iloc[:,2] - dat_merged.iloc[:,1]

# # os.chdir(out_dir)
# # dat_merged.to_csv(station + ".csv")


# # # # print(dat_merged)

me = dat_merged['diff'].mean()
print("Mean Error = ", me)

mae = mean_absolute_error(dat_merged.iloc[:,2], dat_merged.iloc[:,1])
print("MAE = ", mae)

err_std = dat_merged['diff'].std()
print("STD = " , err_std)

rmse = mean_squared_error(dat_merged.iloc[:,2], dat_merged.iloc[:,1])**0.5
print("RMSE = ", rmse)

corr, _ = pearsonr(dat_merged.iloc[:,2], dat_merged.iloc[:,1])
print("Corr = ", corr)

# nse = he.evaluator(he.nse, dat_merged.iloc[:,2], dat_merged.iloc[:,1])
# print("NSE = ", nse[0])


# plot obs vs sim
plt.figure(figsize = (14,5))
plt.plot(dat_merged['datetime'], dat_merged.iloc[:,1], label = 'Sim', color = 'red')
plt.plot(dat_merged['datetime'], dat_merged.iloc[:,2], label = 'Obs', color = 'blue')
plt.ylabel('Stage in ft')
plt.title(station)
plt.legend()
plt.show()

