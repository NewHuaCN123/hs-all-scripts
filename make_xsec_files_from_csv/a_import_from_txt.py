"""  
Created on Wed Feb 22 09:29:00 2023

import cross sections from .csv file
into xns11 importable format

@author: Michael Getachew Tadesse

"""

import os 
import pandas as pd


os.chdir('R:\\40715-010\\GIS\\corkscrew_transects')

dat = pd.read_csv('cross_sections_qced.csv')

# get unique branch names
brn = dat['branch'].unique()

for bb in brn:

    print(bb)

    # select branch
    dat_branch = dat[dat['branch'] == bb]

    # get unique chainage points
    chng = dat_branch['chainage_m'].unique()
    print(chng)

    # create an empty file
    file = open(bb + ".txt", "w")

    for jj in chng:

        # select chainage
        dat_chng = dat_branch[dat_branch['chainage_m'] == jj]
        dat_chng.reset_index(inplace = True)

        print(dat_chng)


        # topoID
        file.write("corks_transect\n")

        # branch
        file.write("EsteroS\n")

        # chainage
        file.write("           " + jj.astype(str) + "\n")

        # boilerplate - don't touch
        file.write("COORDINATES\n")
        file.write("    0\n")
        file.write("FLOW DIRECTION\n")
        file.write("    0\n")
        file.write("PROTECT DATA\n")
        file.write("    0\n")
        file.write("DATUM\n")
        file.write("    0\n")
        file.write("CLOSED SECTION\n")
        file.write("    0\n")
        file.write("RADIUS TYPE\n")
        file.write("    0\n")
        file.write("DIVIDE X-Section\n")
        file.write("    0\n")
        file.write("SECTION ID\n")
        file.write("    Corkscrew_Transect\n")
        file.write("INTERPOLATED\n")
        file.write("    0\n")
        file.write("ANGLE\n")
        file.write("    0.00   0\n")

        file.write("RESISTANCE NUMBERS\n")
        file.write("   2  0     1.000     1.000     1.000    1.000    1.000\n")


        # profile
        # get profile number (number of z points)
        zpoints = len(dat_chng)
        file.write("PROFILE        {}\n".format(zpoints))

        # iterate with s and z
        for ii in range(len(dat_chng)):
            file.write(dat_chng['s'][ii].astype(str) + "   " + dat_chng['z'][ii].astype(str) + "   " + "1.000     <#0>     0     0.000     0\n")



        file.write("LEVEL PARAMS\n")
        file.write("   1  0    0.000  0    0.000  50\n")
        file.write("*******************************\n")


file.close()