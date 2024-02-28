"""  
Created on Wed Feb 28 12:11:00 2024

analyze financial data

@author: Michael Getachew Tadesse

"""

import os
import datetime
import pandas as pd
import seaborn as sns
from pprint import pprint 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


os.chdir("C:\\Users\\mtadesse\\Downloads")

dat = pd.read_csv("2024-02-28T01_23_21.759Z-transactions.csv")

print(dat)
print(dat.columns)
print(dat.Name.unique())

# group by Name
dat_agg = pd.DataFrame(dat.groupby([pd.Grouper(key='Name')])['Amount'].sum())
dat_agg.reset_index(inplace = True)
dat_agg = dat_agg.sort_values(by="Amount")
pprint(dat_agg)


# var = "FAITH ASSEMBLY FAITHASSEMBLYFL"


# dat = dat[dat['Name'] == var]
# dat['Date'] = pd.to_datetime(dat['Date'])

# # weekly aggregation
# dat_wk = pd.DataFrame(dat.groupby([pd.Grouper(key='Date', freq='W')])\
#                                 ['Amount'].sum())

# dat_wk.reset_index(inplace = True)
# pprint(dat)
# # pprint(dat_publix_wk[['Date', 'Amount', 'Description']])

plt_var = dat_agg.tail(10)

# plot
plt.figure(figsize = (15,6))
plt.plot(plt_var['Name'], plt_var['Amount'], 'k')

plt.ylabel('Total Spent ($)')
plt.grid()
# plt.title(var)
plt.show()