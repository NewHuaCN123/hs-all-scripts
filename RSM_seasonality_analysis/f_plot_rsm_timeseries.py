"""  
Created on Tue OCt 10 09:07:00 2023

plot RSM timeseries

@author: Michael Getachew Tadesse

"""

import os
import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator, FormatStrFormatter 


dir_in = "R:\\40715-021\\Modeling\\Data\\RSM_boundary_data"


os.chdir(dir_in)

ecb = pd.read_csv('rsm_bnd_data_ecb_oct1999.csv')
ecb['datetime'] = pd.to_datetime(ecb['datetime'])
fwoi = pd.read_csv('rsm_bnd_data_fowi_oct1999.csv')
fwoi['datetime'] = pd.to_datetime(fwoi['datetime'])


# print(ecb)
# print(fwoi)


# ii = 0
# while ii < ii + 4:
#     if ii == 16:
#         break
#     else:
#         fig, axs = plt.subplots(4)
#         for ss in ecb.columns[1:]:
#             axs[ii].plot(ecb.iloc[:,0], ecb[ss], label= ss + "_ecb", c = 'blue')
#             axs[ii].plot(fwoi.iloc[:,0], fwoi[ss], label= ss + "_fwoi", c = 'red')
#             axs[ii].legend()
#     ii = ii + 1
#     plt.show()       



# for ss in ecb.columns[1:]:
#     fig, axs = plt.subplots(4)
    
#     if ii < 3:
#         print(ii)

#         print(ss)
#         axs[ii].plot(ecb.iloc[:,0], ecb[ss], label= ss + "_ecb", c = 'blue')
#         axs[ii].plot(fwoi.iloc[:,0], fwoi[ss], label= ss + "_fwoi", c = 'red')
#         axs[ii].legend()
#         ii = ii + 1
#     plt.show()
#     # else:
# #     fig, axs = plt.subplots(4)



    




for ss in ecb.columns[1:]:
    plt.figure(figsize = (14,6))
    plt.plot(ecb.iloc[:,0], ecb[ss], label= ss + "_ecb", c = 'blue')
    plt.plot(fwoi.iloc[:,0], fwoi[ss], label= ss + "_fwoi", c = 'red')

    dtFmt = mdates.DateFormatter('%m/%d') # define the formatting
    plt.gca().xaxis.set_major_formatter(dtFmt) # apply the format to the desired axis
    plt.ylabel("Water Level NGVD29 [ft]")
    plt.legend()
    # plt.show()
    plt.savefig(ss, dpi = 400)