
"""  
Created on Mon Aug 22 16:34:00 2022

plot time series - convert date to month while plotting
*mdates

@author: Michael Getachew Tadesse

"""

import pandas as pd
import os
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates 


sns.set_context('notebook', font_scale = 1.5)

os.chdir("R:\\40715-013 UKFPLOS\\SubC\\DataSent\\regulation_schedule")

dat = pd.read_csv("s57.csv")
dat['Date'] = pd.to_datetime(dat['Date'])
# dat['mmyy'] = pd.to_datetime(dat['Date']).dt.strftime('%b-%y')

print(dat)

# Set the locator
locator = mdates.MonthLocator()  # every month
# Specify the format - %b gives us Jan, Feb...
fmt = mdates.DateFormatter('%b')



plt.figure(figsize = (10,6))

plt.plot(dat['Date'], dat['Stage [ft, NAVD88]'], c = 'b')
plt.scatter(dat['Date'], dat['Stage [ft, NAVD88]'], c ='b')

plt.ylabel('Stage (ft) NAVD88')
plt.title('S57')


X = plt.gca().xaxis
X.set_major_locator(locator)
# Specify formatter
X.set_major_formatter(fmt)


plt.grid()
plt.show()