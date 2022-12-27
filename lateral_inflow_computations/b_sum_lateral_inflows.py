
"""
Created on Thu Dec 27 14:38:00 2022

sum up lateral inflows per lake management area
*make sure the list of the duplicates is available first
*use the unique function on excel

@author: Michael Getachew Tadesse

"""
import os
import pandas as pd
import matplotlib.pyplot as plt

dir_ind = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\lateral_inflow_computation\\from_res1d'
dir_home = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\lateral_inflow_computation\\data_per_lma'
dir_out = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\lateral_inflow_computation\\sum_lma_lateral_inflow'


os.chdir(dir_ind)
ind_file = pd.read_csv('lma_index.csv')['lma'].unique()

print(ind_file)

os.chdir(dir_home)

var_list = os.listdir()

for ll in ind_file:
    os.chdir(dir_home)
    print(ll)

    lma_list = [x for x in var_list if x.startswith(ll)]
    print(lma_list)

    isFirst = True

    for vv in lma_list:
        if isFirst:
            df = pd.read_csv(vv)
            df.drop('Unnamed: 0', axis = 1, inplace = True)
            print(df)
            isFirst = False
        else:
            new_df = pd.read_csv(vv)
            new_df.drop('Unnamed: 0', axis = 1, inplace = True)
            df = pd.merge(df, new_df, on = 'datetime')

    # print(df.iloc[:, 1:])
    df['sum'] = df.iloc[:, 1:].sum(axis = 1)
    print(df)

    os.chdir(dir_out)
    df.to_csv(ll + "_lateral_inflow.csv")
