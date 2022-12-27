
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

# lateral inflow files
ovl = pd.read_csv('lateral_inflow_she_overland.csv')
ovl_drain = pd.read_csv('lateral_inflow_she_overland_drain.csv')
sz = pd.read_csv('lateral_inflow_she_saturated_zone.csv')
sz_drain = pd.read_csv('lateral_inflow_she_saturated_zone_drain.csv')


print(ind_file)
# print(ovl)

# lma = ['alligator']
lma = ind_file['lma'].unique()
print(lma)

for ll in lma:
    os.chdir(dir_home)

    df = ind_file[ind_file['lma'] == lma[0]]
    # print(df)

    # get branches
    brnch_list = df['branch'].to_list()
    # brnch_list = ['Alligator_Lk']


    # create empty dataframe for the variable
    dat_var = pd.DataFrame(ovl.iloc[:,0])
    dat_var.columns = ['datetime']
    print(dat_var)

    # looping though each variable
    df_var = {"ovl": ovl, 
               "ovl_drain": ovl_drain,
               "sz": sz,
               "sz_drain": sz_drain}

    for jj in df_var.keys():
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

