"""
Created on Wed Sep 13 13:26:00 2022

to get daily avg flows

@author: Michael Getachew Tadesse

"""
import os
import datetime
import pandas as pd
import matplotlib.pyplot as plt


os.chdir('R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\BackCalcLatQ\\Kiss_Rain_Event_Sep17\\timeseries')


dat = pd.read_csv('s65_2017.csv')

# choose variable
dat = dat[dat['station'] == 'S65_F']

print(dat)

# getDay = lambda x: x.split(' ')[0]
# dat['date'] = pd.DataFrame(list(map(getDay, dat['date'])))
dat['date'] = pd.to_datetime(dat['date'])
print(dat)

dat['date'] = dat['date'].dt.strftime('%Y-%m-%d')

print(dat)

dat = dat[(dat['date'] >= '2017-09-08') & (dat['date'] <= '2017-09-22')]


# get unique dates
unq_date = dat['date'].unique()
# print(unq_date)


# create empty dataframe
df = pd.DataFrame(columns = ['date', 'value'])

isFirst = True
for uu in unq_date:
    # print(uu)
    df2 = dat[dat['date'] == uu]
    print(df2)
    
    print(df2['value'].mean())
    # daily average
    df3 = pd.DataFrame([uu, df2['value'].mean()]).T

    print(df3)

    df3.columns = ['date', 'dailyavg']
    print(df3)

    if isFirst:
        df = df3
        isFirst = False
    else:
        df = pd.concat([df, df3])

print(df)

df.to_csv('s65_2017_dailyavg_flow.csv')
