"""  
Created on Mon Nov 14 10:00:00 2022

aggregate daily rainfall to 3 day

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


rain = pd.read_csv('vn239_daily_rainfall.csv')
rain = rain[['date', 'value']]
rain['date'] = pd.to_datetime(rain['date'])
print(rain)

# aggregate every 3 day
# rain.set_index('date', inplace = True)
rain['agg_3d'] = rain['value'].rolling(3).sum()

print(rain)

rain.to_csv('vn239_3d_rainfall.csv')
