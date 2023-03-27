

import os 
import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.metrics import mean_absolute_error

os.chdir('D:\\data_transfer\\mar-07\\sim_obs_comp')

obs = pd.read_csv('c995_obs.csv')
obs['datetime'] = pd.to_datetime(obs['datetime'])

sim = pd.read_csv('c995_sim_l4.csv')
sim['datetime'] = pd.to_datetime(sim['datetime'])
sim['sim'] = (sim['sim']/0.3048) +1.325

# print(obs)
# print(sim)


dat = pd.merge(obs, sim, on = 'datetime', how = "inner")
# print(dat)

# plt.figure()
# plt.plot(dat['datetime'], dat['obs'], c = 'blue')
# plt.plot(dat['datetime'], dat['sim'], c = 'red')
# plt.show()

# calculate stats
dat['diff'] = dat['obs'] - dat['sim']
dat['absDiff'] = dat['diff'].abs() 

print(dat)

me = dat['diff'].mean()
mae = dat['absDiff'].mean()

print("\n\n")

print(me)
print(mae)
# print(mean_absolute_error(dat['obs'], dat['sim']))
