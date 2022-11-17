"""  
Created on Wed Nov 16 13:23:00 2022

plot surface data - exceedance probability

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

# print(dat)

x = dat['rain_in'] 
y = dat['surge_m']
z = dat['return_period']


def plot3D():
    fig = plt.figure()
    ax = Axes3D(fig)
    surf = ax.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0.1)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    # plt.savefig('teste.pdf')

    ax.set_xlabel('rain_in')
    ax.set_ylabel('surge_m')
    ax.set_zlabel('return period (yrs)')

    plt.show()


# contour plots
# Z = dat.pivot_table(index='rain_in', columns='surge_m', values='return_period').T.values
Z = np.array(dat['return_period']).reshape(12,151)
print(Z)

X_unique = np.sort(dat.rain_in.unique())
# print(X_unique)
Y_unique = np.sort(dat.surge_m.unique())
# print(Y_unique)
X, Y = np.meshgrid(X_unique, Y_unique)
# print(X, Y)

print(X.shape)
print(Y.shape)
print(Z.shape)

print(dat['return_period'])





# Initialize plot objects
rcParams['figure.figsize'] = 5, 5 # sets plot size
fig = plt.figure(figsize = (14,8))
ax = fig.add_subplot(111)

# Define levels in z-axis where we want lines to appear
levels = np.array([10, 25, 50, 100, 200, 300, 400, 500, 
                        600, 700, 800, 900, 1000, 1500, 2000, 2288,
                                2500, 3000, 3500, 4000, 4500, 5000])

# Generate a color mapping of the levels we've specified
import matplotlib.cm as cm # matplotlib's color map library
cpf = ax.contourf(X,Y,Z, len(levels), cmap=cm.Reds)

# Set all level lines to black
line_colors = ['black' for l in cpf.levels]


# Make plot and customize axes
cp = ax.contour(X, Y, Z, levels=levels, colors=line_colors)
ax.clabel(cp, fontsize=10, colors=line_colors)
# plt.xticks([0,0.5,1])
# plt.yticks([0,0.5,1])
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')

plt.show()