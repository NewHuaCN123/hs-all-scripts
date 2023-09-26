"""  
Created on Tue Sep 26 13:52:00 2023

plot new CHS data and rain together

@author: Michael Getachew Tadesse

"""

import os
import pathlib
import mikeio
import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt  
from mikecore.DfsFile import DataValueType
from mikeio.eum import ItemInfo, EUMType, EUMUnit

dir_scenario = "R:\\40715-021\\Modeling\\Data\\CHS_data\\New_BND_Files\\Events_tobe_Simulated_SHIFTED_v2"
dir_out = "R:\\40715-021\\Modeling\\Data\\CHS_data\\New_BND_Files\\Events_tobe_Simulated_SHIFTED_v2\\Figures"

# scenarios
scenario = ['Scenario1', 'Scenario2',
            'Scenario3', 'Scenario4',
            'Scenario5', 'Scenario6',
            'Scenario7']

# CHS save points
savepoint = ['30214', '30450', '30814', '31429']

# rainfall data
rain = {'Scenario1':'5y_extracted.csv', 'Scenario2':'10y_extracted.csv', 
        'Scenario3':'10y_extracted.csv', 'Scenario4':'25y_extracted.csv',
        'Scenario5':'25y_extracted.csv', 'Scenario6':'100y_extracted.csv',
        'Scenario7':'100y_extracted.csv', 'Scenario8':'500y_extracted.csv'}


# horizon years
hoz_yr = ['2035', '2085']

for ss in scenario:
    os.chdir(dir_scenario + "\\{}".format(ss))
    rain_dat = pd.read_csv(rain[ss])
    rain_dat = rain_dat.iloc[:,1:3]
    rain_dat.iloc[:,0] = pd.to_datetime(rain_dat.iloc[:,0])
    # print(rain_dat)

    for sv in savepoint:
        for hh in hoz_yr:
            os.chdir(dir_scenario + "\\{}\\{}\\{}".format(ss,sv,hh))

            for ii in os.listdir():

                os.chdir(dir_scenario + "\\{}\\{}\\{}".format(ss,sv,hh))

                if ii.endswith("_SHIFTED.csv"):
                    print(ii)
                    chs_dat = pd.read_csv(ii)
                    chs_dat = chs_dat.iloc[:,1:3]
                    print(chs_dat)

                    chs_dat.iloc[:,0] = pd.to_datetime(chs_dat.iloc[:,0])

                    sns.set(font_scale=1.5)

                    fig, ax1 = plt.subplots(figsize=(16,9))
                    ax2 = ax1.twinx()

                    sns.lineplot(x = rain_dat.iloc[:,0], y= rain_dat.iloc[:,1], color="red", ax=ax2)
                    ax2.set_ylabel("Rainfall [in]")
                    ax2.invert_yaxis()

                    
                    sns.lineplot(x = chs_dat.iloc[:,0], y= chs_dat.iloc[:,1], color="blue", ax=ax1)
                    ax1.set_ylabel("Water level (ft NGVD29)")


                    # plt.plot(chs_dat.iloc[:,0], chs_dat.iloc[:,1], label = "CHS", c = "k")
                    # plt.plot(rain_dat.iloc[:,0], rain_dat.iloc[:,1], label = "Rain", c = 'red')
                    plt.title(ii.split(".csv")[0] + "  -  " + rain[ss].split(".csv")[0])
                    plt.grid()

                    os.chdir(dir_out)
                    plt.savefig(ii+ "_"+rain[ss]+".jpeg", dpi = 400)

                    # plt.show()
                    