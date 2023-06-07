
import os
import pandas as pd

os.chdir('R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\lateral_inflow_computation')

dat = pd.read_csv('lateral_inflow_she_saturated_zone.txt')

print(dat)