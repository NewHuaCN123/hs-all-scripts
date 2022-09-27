# -*- coding: utf-8 -*-
"""
Created on Fri Jun  06 11:54:02 2022

plot 15 min NEXRAD rainfall


@author: MTadesse
"""
import os 
import pandas as pd
import cartopy
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature


os.chdir("D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
             "Documents\\UKLOS\\Data\\Climate\\kissrain\\shapefile")

fname = 'watersheds_rprj.shp'
shape_feature = ShapelyFeature(Reader(fname).geometries(),
                                ccrs.PlateCarree(), facecolor='none', lw = 0.5)
    
dir_home = "D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
             "Documents\\UKLOS\\Data\\Climate\\kissrain\\plots_15min\\tsfay"
os.chdir(dir_home)


datOrignal = pd.read_csv("tsfay_selected_15min.csv")
# datOrignal['date'] = pd.to_datetime(datOrignal['date'])
# print(datOrignal)

dateUnq = datOrignal['datID'].unique()


print(dateUnq)


count = 1

# get dates
for dd in dateUnq:
    print(dd)
    
    os.chdir(dir_home)
    
    dat = datOrignal[datOrignal['datID'] == dd]
    # print(dat[['date', 'value', 'datID']])
    
    saveName = "Nex_" + str(count)
    # saveName = saveName.replace("\\", "_")
    print(saveName)
    
    fig = plt.figure(figsize = (10,10))
    ax = fig.add_subplot(1, 1, 1,
                          projection=ccrs.PlateCarree())
    ax.set_extent([-82.3, -80.5, 27.5, 28.75], crs=ccrs.PlateCarree())
    
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    
    map = ax.scatter(x = dat["lon"], 
                    y = dat["lat"],
                        c = dat["value"], cmap='hot_r',  #this is the changes
                            s=20, alpha=1, vmin = 0, vmax = 1.5)
    # chose 1.5 becuase of the maximum hourly intensity
    
    ax.add_feature(shape_feature)
    ax.stock_img()
    ax.coastlines()


    ax.set_title("15min Accumulated Rainfall(in) - {}"
                      .format(dd))
    
    # fix colorbar
    
    
    plt.colorbar(map, orientation = "horizontal", pad = 0.03)
    
    
    # os.chdir("D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
    #               "Documents\\UKLOS\\Data\\Climate\\kissrain\\plots_15min\\tsfay")
    
    os.chdir(dir_home)
    # fig.savefig(dd, dpi = 400)
    
    plt.savefig(os.path.join(dir_home, '%s.png' % saveName))
    
    count += 1


    