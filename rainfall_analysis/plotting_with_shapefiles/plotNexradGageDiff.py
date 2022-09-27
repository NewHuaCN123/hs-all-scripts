# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 15:09:12 2022
modified on Tue Sep  20 15:45:12 2022

Plot comparison of NEXRAD and Gages

*useful links
http://earthpy.org/tag/cartopy.html
https://stackoverflow.com/questions/67508054/improve-resolution-of-cartopy-map

@author: Michael Getachew Tadesse
"""

import os 
import pandas as pd
import seaborn as sns
import cartopy
import cartopy.crs as ccrs
# from cmocean import cm as cmo
import matplotlib.pyplot as plt
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature

os.chdir("D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
             "Documents\\UKLOS\\Data\\Climate\\kissrain\\shapefile")

fname = 'watersheds_rprj.shp'
shape_feature = ShapelyFeature(Reader(fname).geometries(),
                                ccrs.PlateCarree(), facecolor='none', lw = 0.5)
    
dir_home = "D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
    "Documents\\UKLOS\\Data\\Climate\\kissrain\\analysis\\"\
        "comparison_NEX_Gages\\comparison_stats"
        
os.chdir(dir_home)


datOrignal = pd.read_csv("nexrad_gages_comparison_percDiff_v2.csv")
# datOrignal['date'] = pd.to_datetime(datOrignal['date'])
# print(datOrignal)

dateUnq = datOrignal['event'].unique()


print(dateUnq)


count = 1

# get dates
for dd in dateUnq:
    print(dd)
    
    os.chdir(dir_home)
    
    dat = datOrignal[datOrignal['event'] == dd]
    # print(dat[['date', 'value', 'datID']])
    
    print(dat)
    
    saveName = "Event_" + str(count)
    # saveName = saveName.replace("\\", "_")
    print(saveName)

    sns.set_context('notebook', font_scale= 1.75)
    
    fig = plt.figure(figsize = (10,10))
    ax = fig.add_subplot(1, 1, 1,
                          projection=ccrs.PlateCarree())
    ax.set_extent([-82.3, -80.5, 27.5, 28.75], crs=ccrs.PlateCarree())
    
    ax.add_feature(shape_feature)
    # ax.background_img(name='ETOPO', resolution='high')

    ax.add_feature(cartopy.feature.LAND)
    ax.add_feature(cartopy.feature.OCEAN)
    ax.add_feature(cartopy.feature.COASTLINE)
    ax.add_feature(cartopy.feature.BORDERS, linestyle=':')
    ax.add_feature(cartopy.feature.LAKES, zorder = -1)
    ax.coastlines()

    map = ax.scatter(x = dat["lon"], 
                    y = dat["lat"],
                        c = dat["perc_diff"], cmap='seismic',  marker = 's',#this is the changes
                            edgecolor = 'black', s=100, alpha=1, vmin = -125, vmax = 125)

    # chose 1.5 becuase of the maximum hourly intensity
    
    # ax.add_feature(cartopy.feature.RIVERS)

    # ax.stock_img()


    # ax.set_title("Percent Difference between Daily Accumulated NEXRAD and Gages Rainfall- {} Rainfall Event"
    #                   .format(dd))
    ax.set_title("{} Rainfall Event".format(dd), fontsize = 20)
    
    # fix colorbar
    
    
    plt.colorbar(map, orientation = "horizontal", pad = 0.03)
    
    
    # os.chdir("D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
    #               "Documents\\UKLOS\\Data\\Climate\\kissrain\\plots_15min\\tsfay")
    
    os.chdir(dir_home)
    # fig.savefig(dd, dpi = 400)
    
    # plt.savefig(os.path.join(dir_home, '%s.png' % saveName))
    
    count += 1
plt.show()
