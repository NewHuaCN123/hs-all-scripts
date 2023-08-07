
import numpy as np
import pandas as pd
import mikeio
import os 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


os.chdir("R:\\40715-010\\Data\\qa_qc")

obs = pd.read_csv("coco1q_obs.csv")
obs['datetime'] = pd.to_datetime(obs['datetime'])

print(obs)

sim = pd.read_csv("coco1q_sim.csv")
sim['datetime'] = pd.to_datetime(sim['datetime'], format = 'mixed')

print(sim)

sim = sim.sort_values(by = "datetime")


print(obs)
print(sim)


plt.figure(figsize = (16,7))
plt.rcParams.update({'font.size': 16})

plt.plot(obs['datetime'], obs['obs'], label = 'Observed', color = 'blue', lw = 2)
plt.plot(sim['datetime'], sim['sim'], label = 'Simulated', color = 'red', lw = 2)
# plt.ticklabel_format(axis= 'y', scilimits= (3,4))
# plt.title(ss)
plt.legend()
plt.show()