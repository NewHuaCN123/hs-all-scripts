"""
Author: Michael Tadesse
Date: June 06, 2023, 10:39
Putpose: Separate DBHYDRO timeseries by station
"""

import os
import pandas as pd


os.chdir("R:\\40715-013 UKFPLOS\\Data\\Rainfall\\0606")

dat = pd.read_csv("ukb_stations_2017_bk_clean.csv")
print(dat)

# unique dbkey
dbk = dat['dbkey'].unique()
print(dbk)

for dd in dbk:
    print(dd)

    df = dat[dat['dbkey'] == dd]
    print(df)

    df = df[['datetime', 'value']]
    df.to_csv(dd + "_2017.csv")


