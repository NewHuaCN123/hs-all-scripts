# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 15:49:02 2022

Make sure the data that is plotted and the shapefiles
are in the same projection


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
    
os.chdir("D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
             "Documents\\UKLOS\\Data\\Climate\\kissrain")
    

datOrignal = pd.read_csv("tsfay_dailyNEXRAD.LonLat.csv")
datOrignal['date'] = pd.to_datetime(datOrignal['date'])
# print(datOrignal)

dateUnq = datOrignal['date'].unique()


print(dateUnq)
# get dates
for dd in dateUnq:
    print(dd)
    dat = datOrignal[datOrignal['date'] == dd]
    
    saveName = "Nex_" + dd.astype("str").split("T00:00:00.000000000")[0]
    
    fig = plt.figure(figsize = (10,10))
    ax = fig.add_subplot(1, 1, 1,
                          projection=ccrs.PlateCarree())
    ax.set_extent([-82.3, -80.5, 27.5, 28.75], crs=ccrs.PlateCarree())
    
    ax.add_feature(cartopy.feature.LAKES, alpha=0.5)
    
    map = ax.scatter(x = dat["lon"], 
                    y = dat["lat"],
                        c = dat["value"], cmap='hot_r',  #this is the changes
                            s=20, alpha=1, vmin = 0, vmax = 13)
    
    ax.add_feature(shape_feature)
    ax.stock_img()
    ax.coastlines()


    ax.set_title("Daily Accumulated Rainfall (in) - {}"
                     .format(dd.astype("str").split("T00:00:00.000000000")[0]))
    
    # fix colorbar
    
    
    plt.colorbar(map, orientation = "horizontal", pad = 0.03)
    
    
    os.chdir("D:\\Hazen and Sawyer\\MIKE_Modeling_Group - "\
                  "Documents\\UKLOS\\Data\\Climate\\kissrain\\plots_fixed_limit\\tsfay")
    # fig.savefig(dd, dpi = 400)
    
    plt.savefig(saveName, dpi = 400)
        
    