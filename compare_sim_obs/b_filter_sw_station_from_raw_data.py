

import os 
import pandas as pd


os.chdir('R:\\40715-010\\Data\\calibration_stats\\calibration_target_check')

raw = pd.read_csv('sw_raw_data.csv')
filtered = pd.read_csv('SW_new_stations.csv')

print(raw)
print(filtered)

merged = pd.merge(filtered, raw, on = 'Name', how = 'inner')

print(merged)

merged.to_csv('sw_stations_filtered.csv')