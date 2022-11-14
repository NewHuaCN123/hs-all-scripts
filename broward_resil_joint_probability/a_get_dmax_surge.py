"""  
Created on Mon Nov 11 15:38:00 2022

get the daily maximum surge values

@author: Michael Getachew Tadesse

"""

import os
import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
 


sns.set_context('notebook', font_scale = 1.5)

os.chdir("D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\"\
                "Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
                        "BrowardRes\\scenarios_joint_probability\\virginia_key_data")

surge = pd.read_csv('virginia_key_tide_data_after_ttide.csv')
print(surge)

# get ymd column

getYmd = lambda x: x.split(" ")[0]
surge['ymd'] = pd.DataFrame(list(map(getYmd, surge['date'])))

print(surge)

# create empty dataframe
dat = pd.DataFrame(columns = ['date', 'max_surge'])

# get unique days
dd_unq = surge['ymd'].unique()

# get daily max values
for dd in dd_unq:
    print(dd)

    df = surge[surge['ymd'] == dd]
    # print(df)

    max_surge = df['surge'].max()
    # print(max_surge)

    new_df = pd.DataFrame([dd, max_surge]).T
    new_df.columns = ['date', 'max_surge']

    dat = pd.concat([dat, new_df], axis = 0)


dat.to_csv('virginia_keys_dmax_surge.csv')

print(dat)