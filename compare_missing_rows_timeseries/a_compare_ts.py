
import pandas as pd
import os

os.chdir('R:\\40715-010\\Data\\qa_qc\\other')

dat_aa = pd.read_csv('gw_stations_aa.csv')
dat_mt = pd.read_csv('gw_stations_mt.csv')

print(dat_aa)
print(dat_mt)


dat_merged = pd.merge(dat_aa, dat_mt, on = 'Name', how = 'outer')

print(dat_merged)

dat_merged.to_csv('aa_mt_merged.csv')