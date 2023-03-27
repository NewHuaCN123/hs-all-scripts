
import os
import pandas as pd
import matplotlib.pyplot as plt


os.chdir('R:\\40715-010\\Data\\calibration_stats\\calibration_target_check')

obs = pd.read_csv('obs_D28_T.csv')
obs['datetime'] = pd.to_datetime(obs['datetime'])

sim = pd.read_csv('D28_TW_res1d_extraction.csv')
sim['datetime'] = pd.to_datetime(sim['datetime'])

print(obs)
print(sim)

# sim = pd.DataFrame(sim.groupby('datetime')['sim_ft'].mean())
# print(sim)

# sim.reset_index(inplace = True)
# print(sim)

# merged = pd.merge(obs, sim, on = 'datetime', how = 'inner')

# print(merged)

# # get data after 2017
# merged_clean = merged[merged['datetime'] > '2017-12-31']
# merged_clean.reset_index(inplace = True)
# print(merged_clean)


# # calculate stats
# merged_clean['diff'] = merged_clean['obs'] - merged_clean['sim_ft']
# merged_clean['absDiff'] = merged_clean['diff'].abs() 

# print(merged_clean)

# me = merged_clean['diff'].mean()
# mae = merged_clean['absDiff'].mean()

# print(me)
# print(mae)

# plt.figure()
# plt.plot(merged_clean['datetime'], merged_clean['obs'], c = 'blue')
# plt.plot(merged_clean['datetime'], merged_clean['sim_ft'], c = 'red')
# plt.show()