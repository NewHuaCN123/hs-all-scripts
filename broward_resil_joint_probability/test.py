import os
import numpy as np
import pandas as pd
import datetime
import seaborn as sns
from itertools import product
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib import rcParams
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.dates as mdates
import plotly.graph_objects as go
 


sns.set_context('notebook', font_scale = 1.5)

os.chdir("D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\"\
                "Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
                        "BrowardRes\\scenarios_joint_probability\\extreme_value_analysis")


dat = pd.read_csv('joint_return_period.csv')
print(dat)

# # dat_merged.to_csv('rain24_surge_amax_std.csv')

plt.figure(figsize = (12,5))
plt.plot(dat_merged['year'], dat_merged['summed_std'])
plt.show()
