

import os
import pandas as pd
from functools import partial, reduce

os.chdir('R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\landuse_for_manning\\landuse_csvs')

print(os.listdir())


allurban = pd.read_csv('allurban_grouped.csv')
lu_41 = pd.read_csv('lu41_grouped.csv')
lu_42 = pd.read_csv('lu42_grouped.csv')
lu_43 = pd.read_csv('lu43_grouped.csv')

print(allurban)
print(lu_41)
print(lu_42)
print(lu_43)

# merge all four land uses
dfs = [allurban, lu_41, lu_42, lu_43]
dat_merged = reduce(lambda left, right: pd.merge(left, right, on = 'id', how = 'outer'), dfs)

print(dat_merged)

dat_merged.to_csv("merged_grouped_lu_dat.csv")