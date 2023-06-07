import os 
import pandas as pd


os.chdir('R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\SW\\solfa_codes')


dat = pd.read_csv('solfa_codes.csv')

print(dat)

solfas = dat['Name'].unique()

print(solfas)

df = pd.DataFrame(columns = ['name', 'code'])

isFirst = True
for ii in solfas:
    
    code = dat[dat['Name'] == ii]['drain_code'].values[0]
    new_df = pd.DataFrame([ii, code]).T
    new_df.columns = ['name', 'code']

    if isFirst:
        df = new_df 
        isFirst = False 
    else:
        df = pd.concat([df, new_df], axis = 0)
print(df)

df.to_csv('solfa_codes_unique.csv')