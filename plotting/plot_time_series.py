"""  
Created on Mon Aug 22 16:34:00 2022

plot time series - convert date to month while plotting

plotting joint distributions

@author: Michael Getachew Tadesse

"""

import pandas as pd
import os
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
 


sns.set_context('notebook', font_scale = 1.5)

os.chdir("D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\"\
                "Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
                        "BrowardRes\\scenarios_joint_probability\\virginia_key_data")

everg = pd.read_csv('South_Port_Everglades.csv')[['Date Time', ' Water Level']]
everg['Date Time'] = pd.to_datetime(everg['Date Time'])
everg.columns = ['date', 'waterLevel[ft]']
everg = everg[everg['date'] <= '2022-10-31']
everg['waterLevel[ft]'] = pd.to_numeric(everg['waterLevel[ft]'])


virginia = pd.read_csv("Virginia_Key.csv")[['Date Time', ' Water Level']]
virginia['Date Time'] = pd.to_datetime(virginia['Date Time'])
virginia.columns = ['date', 'waterLevel[ft]']
virginia = virginia[virginia['date'] <= '2022-10-31']
virginia['waterLevel[ft]'] = pd.to_numeric(virginia['waterLevel[ft]'])

print(everg)
print(virginia)




# dat['Date'] = pd.to_datetime(dat['Date'])
# # dat['mmyy'] = pd.to_datetime(dat['Date']).dt.strftime('%b-%y')

# print(dat)

# # Set the locator
# locator = mdates.MonthLocator()  # every month
# # Specify the format - %b gives us Jan, Feb...
# fmt = mdates.DateFormatter('%b')

# merge the two gages data
dat_merged = pd.merge(everg, virginia, on='date', how='inner')

dat_merged['diff'] = dat_merged['waterLevel[ft]_x'] - dat_merged['waterLevel[ft]_y']
dat_merged.columns = ['date', 'south_port_everglades', 'virginia', 'diff']

# print(dat_merged)
# plt.hist2d(dat_merged['south_port_everglades'],dat_merged['virginia'])
# # plt.show()

sns.set()
# sns.jointplot(dat_merged['south_port_everglades'],
#                         dat_merged['virginia'], color = [0.8, 0.3, 0.9]).plot_joint(sns.kdeplot)
sns.jointplot(dat_merged['south_port_everglades'],
                        dat_merged['virginia'], kind = 'kde', color = 'red').plot_joint(sns.scatterplot)

plt.show()


# # plotting
# plt.figure(figsize = (14,6))

# plt.plot(everg['date'], everg['waterLevel[ft]'], label = 'South Port Everglades', color = 'red')
# plt.plot(virginia['date'], virginia['waterLevel[ft]'], label='Virginia Keys', color = 'black')
# plt.plot(dat_merged['date'], dat_merged['diff'], label='Difference [ft]', color = 'yellow', lw = '0.1')

# plt.ylabel('Water Level (ft) NAVD88')
# # plt.title('S57')


# # X = plt.gca().xaxis
# # X.set_major_locator(locator)
# # # Specify formatter
# # X.set_major_formatter(fmt)

# plt.legend()

# plt.grid()
# plt.show()