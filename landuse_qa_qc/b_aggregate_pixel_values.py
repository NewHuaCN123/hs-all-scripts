import os
import pandas as pd
from functools import partial, reduce

os.chdir('R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\landuse_for_manning\\landuse_csvs')

print(os.listdir())


allurban = pd.read_csv('allurban.csv')
lu_41 = pd.read_csv('lu_41.csv')
lu_42 = pd.read_csv('lu_42.csv')
lu_43 = pd.read_csv('lu_43.csv')



print(allurban)
allurban = allurban.groupby(['id'])[['area_comb', 'perc_comb']].sum().reset_index()
print(allurban)
print(lu_41)
lu_41 = lu_41.groupby(['id'])[['area_41', 'perc_41']].sum().reset_index()
print(lu_41)
print(lu_42)
lu_42 = lu_42.groupby(['id'])[['area_42', 'perc_42']].sum().reset_index()
print(lu_42)
print(lu_43)
lu_43 = lu_43.groupby(['id'])[['area_43', 'perc_43']].sum().reset_index()
print(lu_43)


allurban.to_csv("allurban_grouped.csv")
lu_41.to_csv("lu41_grouped.csv")
lu_42.to_csv("lu42_grouped.csv")
lu_43.to_csv("lu43_grouped.csv")