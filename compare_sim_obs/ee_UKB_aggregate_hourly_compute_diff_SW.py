"""  
Created on Wed Aug 29 10:06:00 2022

Calculate the times when flows are within 20% of observed flows

@author: Michael Getachew Tadesse

"""


import os
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
# from scipy.stats import pearsonr 
# import hydroeval as he
# import matplotlib.pyplot as plt


obs_dir = "R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\calibration_validation_stats\\"\
                    "cal_0608_v13_AugIC_MixCoef\\flow_stats\\obs_flows"
sim_dir = "R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\calibration_validation_stats\\"\
                    "val_0608_MixCoef\\flow_stats\\sim_flows"
out_dir = "R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\calibration_validation_stats\\"\
                    "val_0608_MixCoef\\flow_stats\\merged_flow"


os.chdir(obs_dir)

# list of stations
sList = ['g113','s65A',	'g103',	
         's57',	's58',	's59',	
         's60',	's61',	's62',	
         's63',	's63A',	's65',	
         'shingle_creek','reedy_creek',	
         'boggy_creek',	'kub001']


for station in sList:
    os.chdir(obs_dir)
    # print(station)

    obs = pd.read_csv('{}.csv'.format(station))
    # print(obs)
    obs['datetime'] = pd.to_datetime(obs['datetime'])

    # print(obs)

    os.chdir(sim_dir)
    sim = pd.read_csv('Val_0626_MixCoefDetailedTS_M11.csv')
    sim['datetime'] = pd.to_datetime(sim['datetime'])


    # # consider only data past '2017-09-10'
    # # but for short period analysis do 09/10 - 09/18

    # # Cal - Long Run
    # sim = sim[(sim['datetime'] >= '2017-09-10') & (sim['datetime'] <= '2017-10-10')]

    ## Val - Long Run
    # sim = sim[(sim['datetime'] >= '2011-09-29') & (sim['datetime'] <= '2011-10-27')]

    # Cal - Storm Event Period
    # sim = sim[(sim['datetime'] >= '2017-09-10') & (sim['datetime'] <= '2017-09-18')]

    # ## Val - Storm Event Period
    sim = sim[(sim['datetime'] >= '2011-10-03') & (sim['datetime'] <= '2011-10-27')]

    sim = sim[['datetime', station + "_sim"]]
    # print(sim)

    # # convert CMS to CFS
    # sim[station + "_sim"] = sim[station + "_sim"]*35.314666212661

    # use as is - if the DetailedTS is in feet/cfs
    sim[station + "_sim"] = sim[station + "_sim"]
    # print(sim)

    obs.set_index(obs['datetime'], inplace = True)
    obs_agg = pd.DataFrame(obs.iloc[:,1].resample('H').mean())

    # print(obs_agg)

    # aggregate sim timeseries
    sim.set_index(sim['datetime'], inplace = True)
    sim_agg = pd.DataFrame(sim.iloc[:,1].resample('H').mean())
    # print(sim_agg)

    # merge obs and sim
    dat_merged = pd.merge(sim_agg, obs_agg, on = 'datetime', how = 'inner')

    dat_merged.reset_index(inplace = True)
    dat_merged.dropna(inplace = True)
    # print(dat_merged)


    # check length of dat_merged
    if len(dat_merged) == 0:
        print(station + " - No Data")
        continue

    # calculate calibration target
    dat_merged.columns = ['datetime', 'sim', 'obs']
    dat_merged['good_criteria'] = (dat_merged['sim'] >= 0.80*dat_merged['obs']) & (dat_merged['sim'] <= 1.2*dat_merged['obs']) 


    # count TRUE 
    dat_merged['good_perc'] = len(dat_merged[dat_merged['good_criteria'] == True])/len(dat_merged)
    print(station, "  -  ", dat_merged['good_perc'][0])



# # # calculate stats
# # # observation is the first one - then simulated
# # dat_merged['diff'] = dat_merged.iloc[:,2] - dat_merged.iloc[:,1]

# os.chdir(out_dir)
# dat_merged.to_csv(station + ".csv")


# # # print(dat_merged)

# # me = dat_merged['diff'].mean()
# # print("Mean Error = ", me)

# # mae = mean_absolute_error(dat_merged.iloc[:,2], dat_merged.iloc[:,1])
# # print("MAE = ", mae)

# # err_std = dat_merged['diff'].std()
# # print("STD = " , err_std)

# # rmse = mean_squared_error(dat_merged.iloc[:,2], dat_merged.iloc[:,1])**0.5
# # print("RMSE = ", rmse)

# # corr, _ = pearsonr(dat_merged.iloc[:,2], dat_merged.iloc[:,1])
# # print("Corr = ", corr)

# # nse = he.evaluator(he.nse, dat_merged.iloc[:,2], dat_merged.iloc[:,1])
# # print("NSE = ", nse[0])


# # # plot obs vs sim
# # plt.figure(figsize = (14,5))
# # plt.plot(dat_merged['datetime'], dat_merged.iloc[:,1], label = 'Sim', color = 'red')
# # plt.plot(dat_merged['datetime'], dat_merged.iloc[:,2], label = 'Obs', color = 'blue')
# # plt.ylabel('Flow in CFS - {}'.format(station))
# # plt.legend()
# # plt.show()

