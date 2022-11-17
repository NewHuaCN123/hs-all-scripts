"""  
Created on Wed Nov 16 13:23:00 2022

plot return period curves using plotly

@author: Michael Getachew Tadesse

"""

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
                        "BrowardRes\\scenarios_joint_probability\\virginia_key_data")


#####################################################
dat = pd.read_csv('rain_24h_positive_surge_joint_prob.csv')
dat['return_period'] = dat['return_period'].apply(np.floor)
print(dat)
#####################################################


feature_x = np.unique(dat['rain_in'])
print(len(feature_x))
print(feature_x.shape)



feature_y = np.unique(dat['surge_m'])
print(len(feature_y))

z = np.reshape(dat['return_period'].to_list(), ( 151, 12 )).T
print(z)
print(z[0])
 
# Creating 2-D grid of features
[X, Y] = np.meshgrid(feature_x, feature_y)
 
Z = z

fig = go.Figure(data =
     go.Contour(x = feature_x, y = feature_y, z = Z,


        colorscale='jet',

          contours=dict(
            start=0,
            end=5000,
            size=100,
            showlabels = True,
            labelfont = dict( # label font properties
                size = 12,
                color = 'white',
            )
        ),

    
     ),
     layout = go.Layout(

        xaxis = dict(
            title = 'Rain [in]',
          ),

        yaxis = dict(
            title = 'Surge [m]',
          ),
      ),
     )

  
# #Adjust the number of coutour levels
# fig.update_traces(contours_start= 10, contours_end= 5000, contours_size= 100)

fig.show()