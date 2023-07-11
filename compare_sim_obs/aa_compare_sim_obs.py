

import os 
import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.metrics import mean_absolute_error

os.chdir('R:\\40715-010\\Data\\qa_qc\\bcb_071223_run_c0492_stages')

obs = pd.read_csv('c0492_obs.csv')
obs['datetime'] = pd.to_datetime(obs['Time'])


sim = pd.read_csv('c0492_sim.csv')
sim['datetime'] = pd.to_datetime(sim['Time'])
# sim['sim'] = (sim['sim']/0.3048) +1.325

obs = obs[obs['datetime'] >= '2017-01-01']
sim = sim[sim['datetime'] >= '2017-01-01']

print(obs)
print(sim)


# dat = pd.merge(obs, sim, on = 'datetime', how = "inner")
# # print(dat)

plt.figure()
plt.plot(obs['datetime'], obs['02317 _C-492_MAX'], c = 'blue', label = "obs")
plt.plot(sim['datetime'], sim['L1_ft'], c = 'red', label = "L1")
plt.plot(sim['datetime'], sim['L2_ft'], c = 'green', label = "L2")
plt.plot(sim['datetime'], sim['L3_ft'], c = 'black', label = "L3")
plt.legend()
plt.show()

# # calculate stats
# dat['diff'] = dat['obs'] - dat['sim']
# dat['absDiff'] = dat['diff'].abs() 

# print(dat)

# me = dat['diff'].mean()
# mae = dat['absDiff'].mean()

# print("\n\n")

# print(me)
# print(mae)
# # print(mean_absolute_error(dat['obs'], dat['sim']))
