
"""
Created on Thu Dec 22 16:13:00 2022

to get end of day stage and flow values


@author: Michael Getachew Tadesse

"""
import os
import pandas as pd
import matplotlib.pyplot as plt


dir_home = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\lateral_inflow_computation\\from_res1d'
dir_out = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\lateral_inflow_computation\\data_per_lma'


os.chdir(dir_home)

ind_file = pd.read_csv('lma_index.csv')

# duplicated stations
dup_stn = ['Armstrong_Slough 6489.86.1',	'br_5 11458.5.1',	'br_6 12014.1.1',	'br_6 24000.1',	'br_8 8525.61.1',	'BullCrkSW 2693.76.1',	'BullCrkSW 4059.46.1',	'BullCrkSW 4797.43.1',	'BullCrkSW 7238.15.1',	'BullCrkSW 12075.1.1',	'BullCrkSW 12471.1',	'BullCrkSW 13376.1.1',	'BullCrkSW 13844.5.1',	'BullCrkSW 14608.2.1',	'BullCrkSW 15128.6.1',	'C-29A 2800.1',	'C-38 824.375.1',	'C-38 3242.1',	'C-38 3492.3.1',	'C-38 5460.94.1',	'C-38 6855.8.1',	'C-38 7392.05.1',	'C-38 8674.4.1',	'C-38 9648.1',	'C-38 14721.2.1',	'C-38 15079.6.1',	'C-38 16736.8.1',	'C-38 17215.5.1',	'C-38 17916.2.1',	'C-38 19111.6.1',	'C-38 22870.3.1',	'Coon_Lk 360.1',	'CrabgrassCrk 3157.05.1',	'CrabgrassCrk 5686.23.1',	'CrabgrassCrk 5753.62.1',	'Cypress_Lk 681.747.1',	'Cypress_Lk 3823.85.1',	'East_Lk_Hatchineha 848.918.1',	'East_Lk_Hatchineha 4029.27.1',	'EconlockRiver 7703.58.1',	'EconlockRiver 8818.9.1',	'EconlockRiver 9361.25.1',	'EconlockRiver 9791.15.1',	'EconlockRiver 11282.9.1',	'EconlockRiver 14664.8.1',	'EconlockRiver 15015.3.1',	'EconlockRiver 15863.2.1',	'EconlockRiver 17554.1.1',	'EconlockRiver 19456.4.1',	'EconlockRiver 20374.3.1',	'EconlockRiver 23320.1.1',	'Ice_Cream_Slough 3951.5.1',	'Ice_Cream_Slough 10745.7.1',	'Jackson_Canal 2766.5.1',	'JimCreek 5533.84.1',	'KISSIMMEE 2017.9.1',	'KISSIMMEE 4122.02.1',	'KISSIMMEE 17003.5.1',	'Lake_Marian 11277.6.1',	'Lake_Rosalie 1524.1',	'LittleEconRiver 1812.59.1',	'LittleEconRiver 2444.62.1',	'LittleEconRiver 3649.71.1',	'LittleEconRiver 3788.59.1',	'LittleEconRiver 6970.35.1',	'LittleEconRiver 7623.72.1',	'Lk_Gentry 1059.24.1',	'Lk_Marion_Creek 11207.2.1',	'Lk-Hart 1363.41.1',	'LOWER-E-TOHO 7230.32.1',	'Meander2 1607.58.1',	'Meander4 1701.48.1',	'NorthForkTaylorCrk 2702.91.1',	'PeaceCreekCanal Reach:Main2 2048.13.1',	'PeaceCreekCanal Reach:Main3 9262.74.1',	'Pine_Island_Slough 6589.86.1',	'Pine_Island_Slough_US 2211.88.1',	'Pine_Island_Trib1 3057.71.1',	'Reedy-Creek 19614.1.1',	'S65A_Oxbow 203.922.1',	'S65A_West 1677.53.1',	'SecondCrk 1882.7.1',	'TaylorCrk 2347.44.1',	'TaylorCrk 4656.09.1',	'TaylorCrk 5566.23.1',	'TaylorCrk 8492.37.1',	'Tick_Island_Slough2 8446.52.1',	'Toho-main 3962.4.1',	'Toho-main 7464.41.1',	'TurkeyCrkNW 2341.75.1',	'TysonCrk 1629.26.1',	'TysonCrk 2809.83.1',	'TysonCrk 3328.24.1',	'West_Lk_Hatchineha 5348.76.1',	'WestBrchCrabgrassCrk 1832.22.1']
print(dup_stn)

# lateral inflow files
ovl = pd.read_csv('lateral_inflow_she_overland.csv')
ovl.drop(dup_stn, axis = 1, inplace = True)
# print(ovl)

ovl_drain = pd.read_csv('lateral_inflow_she_overland_drain.csv')
ovl_drain.drop(dup_stn, axis = 1, inplace = True)

sz = pd.read_csv('lateral_inflow_she_saturated_zone.csv')
sz.drop(dup_stn, axis = 1, inplace = True)

sz_drain = pd.read_csv('lateral_inflow_she_saturated_zone_drain.csv')
sz_drain.drop(dup_stn, axis = 1, inplace = True)



print(ind_file)
# print(ovl)

# lma = ['alligator']
lma = ind_file['lma'].unique()
print(lma)

for ll in lma:
    os.chdir(dir_home)

    df = ind_file[ind_file['lma'] == ll]
    print(df)

    # get branches
    brnch_list = df['branch'].to_list()
    # brnch_list = ['Alligator_Lk']

    print(brnch_list)

    # looping though each variable
    df_var = {"ovl": ovl, 
               "ovl_drain": ovl_drain,
               "sz": sz,
               "sz_drain": sz_drain}

    for jj in df_var.keys():

        # create empty dataframe for the variable
        dat_var = pd.DataFrame(ovl.iloc[:,0])
        dat_var.columns = ['datetime']
        print(dat_var)


        print(jj)

        os.chdir(dir_home)

        for br in brnch_list:
            print(ll, "-", jj, "-", br)

            chn_dat = df[df['branch'] == br]

            # chn_start = br + " " + str(chn_dat['start'].values[0])
            # chn_end = br + " " + str(chn_dat['end'].values[0])

            chn_start = chn_dat['start'].values[0]
            chn_end = chn_dat['end'].values[0]

            print(chn_start, chn_end)

            # get the variable data
            cols = df_var[jj].columns[1:]
            # print(pd.DataFrame(cols).head(50))


            with_s = [x for x in cols if x.startswith(br)]
            print(with_s)


            # print(with_s)

            br_subset = [x for x in with_s if (pd.to_numeric(x.split(" ")[1]) >= chn_start) and 
                                                    (pd.to_numeric(x.split(" ")[1]) <= chn_end)]
            # print(br_subset, "\n")

            # print(df_var[jj][br_subset])
            new_dat_var = df_var[jj][br_subset]

            # concatenate with variable dataframe
            dat_var = pd.concat([dat_var, new_dat_var], axis = 1)

        # save variable parameter
        os.chdir(dir_out)
        dat_var.to_csv(ll + "_" + jj + ".csv")

