

import os
import pandas as pd
import matplotlib.pyplot as plt


obs_dir = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\calibration_validation_stats\\hourly_peak_analysis\\observed'
sim_dir = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\calibration_validation_stats\\hourly_peak_analysis'
out_dir = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\calibration_validation_stats\\hourly_peak_analysis\\clean_merged_short_period'

os.chdir(obs_dir)

station = "boggy"
obs = pd.read_csv('{}_obs.csv'.format(station))
print(obs)
obs['date'] = pd.to_datetime(obs['date'])

os.chdir(sim_dir)
sim = pd.read_csv('{}_Flow_sim.csv'.format(station))
sim['date'] = pd.to_datetime(sim['date'])

# consider only data past '2017-09-10'
# but for short period analysis do 09/10 - 09/18
sim = sim[(sim['date'] >= '2017-09-10') & (sim['date'] <= '2017-09-18')]

print(obs)
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
print("Mean Error = ", me)

err_std = dat_merged['diff'].std()
print("STD = " , err_std)

# plot obs vs sim
plt.figure()
plt.plot(dat_merged.iloc[:,0], label = 'sim', color = 'red')
plt.plot(dat_merged.iloc[:,1], label = 'obs', color = 'blue')
plt.legend()
plt.title(station)
plt.show()