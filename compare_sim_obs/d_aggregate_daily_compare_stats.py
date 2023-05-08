

import os
import pandas as pd
import matplotlib.pyplot as plt


os.chdir('R:\\40715-010\\Data\\qa_qc\\GW_Stages_extracted_from_3DSZ\\obs')

obs = pd.read_csv('nv383_obs.csv')
obs['datetime'] = pd.to_datetime(obs['datetime'])

sim = pd.read_csv('nv383_sim.csv')
sim['datetime'] = pd.to_datetime(sim['datetime'])

# consider only data past '2017-07-10'
sim = sim[sim['datetime'] >= '2017-07-01']
obs = obs[obs['datetime'] >= '2017-07-01']

print(obs)
print(sim)

obs.set_index(obs['datetime'], inplace = True)
obs_agg = pd.DataFrame(obs.iloc[:,1].resample('D').mean())

print(obs_agg)

# aggregate sim timeseries
sim.set_index(sim['datetime'], inplace = True)
sim_agg = pd.DataFrame(sim.iloc[:,1:6].resample('D').mean())

print(sim_agg)

# merge obs and sim
dat_merged = pd.merge(sim_agg, obs_agg, on = 'datetime', how = 'inner')
print(dat_merged)
print(dat_merged[dat_merged['value_ft'].notnull()])


# calculate stats
# observation is the first one - then simulated
dat_merged = dat_merged[dat_merged['value_ft'].notnull()]
dat_merged['diff'] = dat_merged['value_ft'] - dat_merged['L4']

print(dat_merged)

me = dat_merged['diff'].mean()
print("\n\n", me)

# plot obs vs sim
plt.figure(figsize = (14,5))
plt.plot(dat_merged.iloc[:,0], label = 'L0', color = 'black')
plt.plot(dat_merged.iloc[:,1], label = 'L1', color = 'magenta')
plt.plot(dat_merged.iloc[:,2], label = 'L2', color = 'green')
plt.plot(dat_merged.iloc[:,3], label = 'L3', color = 'brown')
plt.plot(dat_merged.iloc[:,4], label = 'L4', color = 'pink')
plt.plot(dat_merged.iloc[:,5], label = 'obs', color = 'blue')
plt.ylabel('GW stage in ft')
plt.legend()
plt.show()