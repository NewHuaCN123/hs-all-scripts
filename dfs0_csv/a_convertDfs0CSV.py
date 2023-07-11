import numpy as np
import pandas as pd
import mikeio
import os 


dir_obs = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\calibration_validation_stats\\cal_0608_v13\\plots_4_report\\GW_obs_TS'

dir_table = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\calibration_validation_stats\\cal_0608_v13\\plots_4_report'


os.chdir(dir_obs)
fileList = os.listdir()


# os.chdir(dir_table)
# dat = pd.read_csv('SW_storing.csv')
# stn = dat.station.unique()
# print(dat)
# print(stn)

stn = ['swfwmd_wells_GW_navd88.dfs0', 'sfwmd_wells_GW_navd88.dfs0']

for ss in stn:
    print(ss)

    # stnRow = dat[dat['station'] == ss]
    # stnFile = stnRow['fileName'].values[0]
    # print(stnFile)

    stnFile = ss

    if pd.isnull(stnFile):
        print("test")
        continue

    os.chdir(dir_obs)

    ds = mikeio.read(stnFile)

    df = ds.to_dataframe()
    df.reset_index(inplace = True)
    # df.columns = ['datetime', 'value']

    print(df)

    saveName = stnFile.split('.dfs0')[0] + ".csv"

    df.to_csv(saveName)
