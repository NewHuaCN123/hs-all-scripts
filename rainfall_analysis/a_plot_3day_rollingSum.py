import os
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

dir_in = "D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
                "Documents\\UKLOS\\Data\\"\
                    "calib_valid_selection\\combinedRefinedData"


os.chdir(dir_in)

sns.set_context('notebook', font_scale= 1.25)


dat = pd.read_csv("threeDayRollingSumRefined.csv")
dat['Daily Date'] = pd.to_datetime(dat['Daily Date'])
# dat.set_index('Daily Date', inplace = True)

print(dat)

# plt.figure()

dat.plot(x = 'Daily Date', y = dat.columns[1:])

# sns.lineplot(data = dat)


plt.ylabel('Daily Rainfall (inches)')
plt.xlabel('')

plt.legend(ncol = 4, fontsize = 10)

plt.show()