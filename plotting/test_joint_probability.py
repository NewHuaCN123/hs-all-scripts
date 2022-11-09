
"""  
Created on Wed Nov 09 15:36:00 2022

Test joint probability dunctions 

@author: Michael Getachew Tadesse

"""

import os
import numpy as np
import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates 


n = 1000


x = np.random.randn(n)
y = np.random.randn(n)**2

plt.hist2d(x,y, 30, vmax = 10)
plt.xlabel('x')
plt.ylabel('y')

plt.show()