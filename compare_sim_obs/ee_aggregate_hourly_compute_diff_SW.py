

import os
import pandas as pd
import matplotlib.pyplot as plt


obs_dir = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\calibration_validation_stats\\validation_stats_0329\\obs_flows'
sim_dir = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\calibration_validation_stats\\validation_stats_0329\\sim_flows'
out_dir = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\calibration_validation_stats\\hourly_peak_analysis\\clean_merged_short_period'




os.chdir(obs_dir)

station = "boggy_creek"
obs = pd.read_csv('{}.csv'.format(station))
print(obs)
obs['date'] = pd.to_datetime(obs['date'])

print(obs)

os.chdir(sim_dir)
sim = pd.read_csv('detailedTS_M11.csv')
sim['date'] = pd.to_datetime(sim['date'])

# consider only data past '2017-09-10'
# but for short period analysis do 09/10 - 09/18
sim = sim[(sim['date'] >= '2011-10-03') & (sim['date'] <= '2011-10-27')]
sim = sim[['date', station + "_sim"]]
print(sim)



obs.set_index(obs['date'], inplace = True)
obs_agg = pd.DataFrame(obs.iloc[:,1].resample('H').mean())

print(obs_agg)

# aggregate sim timeseries
sim.set_index(sim['date'], inplace = True)
sim_agg = pd.DataFrame(sim.iloc[:,1].resample('H').mean()*35.314666212661)
print(sim_agg)

# merge obs and sim
dat_merged = pd.merge(sim_agg, obs_agg, on = 'date', how = 'inner')
print(dat_merged)


# calculate stats
# observation is the first one - then simulated
dat_merged['diff'] = dat_merged.iloc[:,1] - dat_merged.iloc[:,0]

os.chdir(out_dir)
dat_merged.to_csv(station + ".csv")


print(dat_merged)

me = dat_merged['diff'].mean()
print("Mean Error = ", me/35.314666212661)

err_std = dat_merged['diff'].std()
print("STD = " , err_std/35.314666212661)

# plot obs vs sim
plt.figure()
plt.plot(dat_merged.iloc[:,0], label = 'sim', color = 'red')
plt.plot(dat_merged.iloc[:,1], label = 'obs', color = 'blue')
plt.legend()
plt.title(station)
plt.show()