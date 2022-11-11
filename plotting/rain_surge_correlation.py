"""  
Created on Mon Nov 11 10:21:00 2022

plot rainfall and surge data for Virginia Keys 

@author: Michael Getachew Tadesse

"""

import pandas as pd
import os
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
 


sns.set_context('notebook', font_scale = 1.5)

os.chdir("D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\Hazen and Sawyer\\"\
                "MIKE_Modeling_Group - Documents\\BrowardRes\\"\
                        "scenarios_joint_probability\\virginia_key_data")


rain = pd.read_csv('vn239_daily_rainfall.csv')
rain['date'] = pd.to_datetime(rain['date'])

surge = pd.read_csv('virginia_key,fl_755a_usa_daily_max.csv')
surge['ymd'] = pd.to_datetime(surge['ymd'])


print(rain)
print(surge)


sns.set()
sns.jointplot(rain['value'],surge['surge'], kind = 'kde', color = 'red').plot_joint(sns.scatterplot)

plt.show()

