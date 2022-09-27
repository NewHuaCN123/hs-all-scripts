"""
Created on Wed Sep 13 13:26:00 2022

to get end of day stage and flow values

@author: Michael Getachew Tadesse

"""
import os
import pandas as pd
import matplotlib.pyplot as plt


os.chdir('R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\BackCalcLatQ\\Kiss_Rain_Event_Sep17\\timeseries')


dat = pd.read_csv('s65_2017.csv')

# choose variable
dat = dat[dat['station'] == 'S65-T']


dat['date'] = pd.to_datetime(dat['date'])

dat['date'] = dat['date'].dt.strftime('%Y-%m-%d')


dat = dat[(dat['date'] >= '2017-09-08') & (dat['date'] <= '2017-09-22')]

# print(dat)

# get unique dates
unq_date = dat['date'].unique()
# print(unq_date)


# create empty dataframe
df = pd.DataFrame(columns = ['date', 'value'])

isFirst = True
for uu in unq_date:
    # print(uu)
    df2 = dat[dat['date'] == uu]
    # print(df2)

    # last row of the data
    df3 = pd.DataFrame(df2.iloc[-1, :]).T[['date', 'value']]
    df3.columns = ['date', 'value']
    # print(df3)

    if isFirst:
        df = df3
        isFirst = False
    else:
        df = pd.concat([df, df3])

print(df)

df.to_csv('s65_tw_2017_endday_flow.csv')
