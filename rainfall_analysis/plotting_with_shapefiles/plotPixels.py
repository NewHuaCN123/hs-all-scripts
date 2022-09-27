"""
Created on Mon Nov 15 14:19:00 2021

plot NEXRAD pixels  

@author: Michael Getachew Tadesse

"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap



# dat = pd.read_csv("pixel_lon_lat.csv")

# # print(dat["PIXEL_NO"])

# x = dat["CENTROID_X"].to_numpy()
# y = dat["CENTROID_Y"].to_numpy()
# z = dat["PIXEL_NO"].to_numpy()



# xy = dat[["CENTROID_X", "CENTROID_Y"]].to_numpy()
# print(xy)

# plt.pcolormesh(xy)

# # # plt.pcolormesh(dat["CENTROID_X"], dat["CENTROID_Y"], dat["PIXEL_NO"])
# plt.show()