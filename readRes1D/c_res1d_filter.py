"""  
Created on Thu Feb 08 10:02:00 2024

filter branches from res1d csv
based on: https://github.com/DHI/mikeio1d

@author: Michael Getachew Tadesse

"""

import os
import datetime
import pandas as pd

dir_in = "R:\\40715-021\\Modeling\\Data\\PerformanceMetrics\\PM1\\FWOP"


os.chdir(dir_in)

# read res1D file
fileName = "08-res1d_2S500R85i.csv"
df = pd.read_csv(fileName)

print(df)
# branch name
branch = "Cypress_Creek"

dat = df[df['Water level'].str.startswith(branch)]

{
# # Hillsboro
# dat = dat[~dat['Water level'].str.startswith(
#             ('Hillsboro Tidal', 'Hillsboro_AddlStorage', 'HillsboroInlet'))]

# # C-14
# dat = dat[~dat['Water level'].str.startswith(
#             ('C-14 Tidal'))]

# # C-13
# dat = dat[~dat['Water level'].str.startswith(
#             ('C-13-S2_tr6', 'C-13-S2_tr5', 'C-13-S2_tr4', 
#                 'C-13-S2_tr3', 'C-13-S2_tr2', 'C-13-S2_tr1',
#                     'C-13-S2_AddlStorage', 'C-13-S2', 'C-13-S5', 'C-13_S5', 'C-13_S4',
#                         'C-13_S3', 'C-13_S2', 'C-13_S1', 'C-13_N5_1', 'C-13_N5', 'C-13_N4'
#                         , 'C-13_N3', 'C-13_N2', 'C-13_N1', 'C-13_Canal 9W', 'C-13_Canal 9N',
#                         'C-13-_Canal 9', 'C-13_01', 'C-13 Tidal'))]

# # C-12
# dat = dat[~dat['Water level'].str.startswith(
#             ('C-12-unincorporated', 'C-12Tidal', 'C-12_N2', 'C-12_N1'))]

# # North New River
# dat = dat[~dat['Water level'].str.startswith(
#             ('North New River Tidal'))]

# # SFWMD_C-11
# dat = dat[~dat['Water level'].str.startswith(
#             ('SFWMD_C-11S_AddlStorage', 'SFWMD_C-11S_AddlStorage', 'SFWMD_C-11S'))]


}

# remove duplicates
dat = dat.drop_duplicates()

print(dat)

dat.to_csv(branch + "_" + fileName)