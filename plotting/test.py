
import pandas as pd
import os
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
 


sns.set_context('notebook', font_scale = 1.5)

os.chdir("R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\SW\\QH_4ModelCalib\\compare_SW_GW")


hw = pd.read_csv('g113hw.csv')
hw['datetime'] = pd.to_datetime(hw['datetime'])
tw = pd.read_csv('g113tw.csv')
tw['datetime'] = pd.to_datetime(tw['datetime'])
gw = pd.read_csv('gw_stages.csv')
gw['datetime'] = pd.to_datetime(gw['datetime'])


print(hw)
print(tw)
print(gw)


plt.figure(figsize = (12,5))
plt.plot(hw['datetime'], hw['g113hw'], label = "g113hw", color = "blue")
plt.plot(tw['datetime'], tw['g113tw'], label = "g113tw", color = "red")
plt.plot(gw['datetime'], gw['VN000'], label = "VN000", color = "black")
plt.plot(gw['datetime'], gw['VN002'], label = "VN002", color = "magenta")
plt.plot(gw['datetime'], gw['VN004'], label = "VN004", color = "green")
plt.plot(gw['datetime'], gw['VM998'], label = "VM998", color = "brown")

plt.legend()
plt.show()