"""
Created on Wed Sep 06 15:22:00 2022

compare 2014 and 2017 rain data

@author: Michael Getachew Tadesse

"""
import os
import pandas as pd
import matplotlib.pyplot as plt


os.chdir('R:\\40715-013 UKFPLOS\\Data\\Rainfall')


dat = pd.read_csv('gage_inside_study_area_rain.csv')
dat['Daily Date'] = pd.to_datetime(dat['Daily Date'])

print(dat)

d11 = dat[(dat['Daily Date'] >= '1/1/2011') & (dat['Daily Date'] <= '12/31/2011')]
d14 = dat[(dat['Daily Date'] >= '1/1/2014') & (dat['Daily Date'] <= '12/31/2014')]
d17 = dat[(dat['Daily Date'] >= '1/1/2017') & (dat['Daily Date'] <= '12/31/2017')]


print(d11)
print(d17)
print(d17)

sep_11 = d11[(d11['Daily Date'] >= '09/01/2011') & (d11['Daily Date'] <= '10/30/2011')]
sep_14 = d14[(d14['Daily Date'] >= '09/01/2014') & (d14['Daily Date'] <= '10/30/2014')]
sep_17 = d17[(d17['Daily Date'] >= '09/01/2017') & (d17['Daily Date'] <= '10/30/2017')]


print(sep_11)
print(sep_14)
print(sep_17)

sum_sep_11 = sep_11.iloc[:, 1:].sum().sum()
sum_sep_14 = sep_14.iloc[:, 1:].sum().sum()
sum_sep_17 = sep_17.iloc[:, 1:].sum().sum()

print(sum_sep_11)
print(sum_sep_14)
print(sum_sep_17)


#############################################
# plotting rainfall


fig = plt.figure(figsize = (12, 6))

col_names_17 = d17.columns[1:]
col_names_14 = d14.columns[1:]
col_names_11 = d11.columns[1:]

ax1 = fig.add_subplot(311)

for x in col_names_11:
    # print(dat[x])
    # print(dat['Daily Date'])
    ax1 = plt.plot(d11['Daily Date'], d11[x])

plt.ylabel('Daily Rainfall (in)')
plt.grid()

ax2 = fig.add_subplot(312)

for x in col_names_14:
    # print(dat[x])
    # print(dat['Daily Date'])
    ax2 = plt.plot(d14['Daily Date'], d14[x])

plt.ylabel('Daily Rainfall (in)')
plt.grid()


ax3 = fig.add_subplot(313)

for y in col_names_17:
    # print(dat[x])
    # print(dat['Daily Date'])
    ax3 = plt.plot(d17['Daily Date'], d17[y])

plt.ylabel('Daily Rainfall (in)')
plt.grid()


plt.show()
##############################################