

import os
import pandas as pd

os.chdir('R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\qa_qc')

obs = pd.read_csv('ALL1W2_csv.csv')
obs['date'] = pd.to_datetime(obs['date'])

sim = pd.read_csv('CASTW1_CASTW2_ft.csv')
sim['date'] = pd.to_datetime(sim['date'])

# consider only data past '2017-09-10'
sim = sim[sim['date'] >= '2017-09-10']

print(obs)
print(sim)

obs.set_index(obs['date'], inplace = True)
obs_agg = pd.DataFrame(obs.iloc[:,1].resample('D').mean())

print(obs_agg)

# aggregate sim timeseries
sim.set_index(sim['date'], inplace = True)
sim_agg = pd.DataFrame(sim.iloc[:,1:3].resample('D').mean())

print(sim_agg)

# merge obs and sim
dat_merged = pd.merge(sim_agg, obs_agg, on = 'date', how = 'inner')
print(dat_merged)


# calculate stats
# observation is the first one - then simulated
dat_merged['diff'] = dat_merged['ALL1W2'] - dat_merged['CASTW1_ft']

print(dat_merged)

me = dat_merged['diff'].mean()
print(me)