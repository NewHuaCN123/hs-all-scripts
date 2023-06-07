"""
Author: Michael Tadesse
Date:   June 05, 2023 17:20
Purpose: pre-process data for copula application
"""

import os 
import pandas as pd
import matplotlib.pyplot as plt


os.chdir("D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\Hazen and Sawyer\\"\
         "MIKE_Modeling_Group - Documents\\BrowardRes\\"\
                "scenarios_joint_probability\\virginia_key_data")

print(os.listdir())

precip = pd.read_csv("vn239_daily_rainfall.csv")
surge = pd.read_csv("virginia_keys_dmax_surge.csv")
surge['date'] = pd.to_datetime(surge['date'])
surge = surge[(surge['date'] >= "2008-10-01") & (surge['date'] <= "2020-12-31")]
surge.reset_index(inplace = True)

precip = precip[["date", "value"]]
precip['date'] = pd.to_datetime(precip['date'])
precip = precip[(precip['date'] >= "2008-10-01") & (precip['date'] <= "2020-12-31")]
precip.reset_index(inplace = True)

print(precip)
print(surge)

dat_merged = pd.merge(precip, surge, on = 'date', how = 'outer')
dat_merged = dat_merged[['date', 'value', 'max_surge']]
print(dat_merged)


print(dat_merged[dat_merged['max_surge'].isnull()])


# fill in missing data
dat_merged['max_surge'].fillna(dat_merged['max_surge'].mean(numeric_only= True), inplace  = True) 
dat_merged['value'].fillna(dat_merged['value'].mean(numeric_only= True), inplace  = True) 
# print(dat_merged[dat_merged['max_surge'].isnull()])

dat_merged.to_csv("vign_keys_precip_surge.csv")




# plt.figure()
# plt.plot(dat_merged['date'], dat_merged['max_surge'])
# plt.show()