
"""
Created on Sat Oct 08 14:00:00 2022


*This script reads NetCDF file and extracts
the requested variables

*adds a county map shapefile

*plots a scatter of the lon/lat values

*needs to be improved to make a surface plot

@author: Michael Getachew Tadesse
"""

import os 
import pandas as pd
from netCDF4 import Dataset
import pandas as pd
import datetime
from datetime import datetime, timedelta
from tkinter import filedialog as fd
import seaborn as sns
import cartopy
import cartopy.crs as ccrs
# from cmocean import cm as cmo
import matplotlib.pyplot as plt
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader


# get shapefiles
os.chdir('D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\BrowardRes\\data_from_PalmBeach_county\\shapefiles')
reader = shpreader.Reader('countyl010g.shp')
counties = list(reader.geometries())
COUNTIES = cfeature.ShapelyFeature(counties, ccrs.PlateCarree())


## reading file
os.chdir('D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\BrowardRes\\data_from_PalmBeach_county\\PBC_Appeal\\ModelResults\\storm-21-rerun')
storm_name = 'storm21'
filename = 'maxele.63_storm21c.nc'

g = Dataset(filename)

print(g.title)

for variable in g.variables.keys():

    if (hasattr(g.variables[variable], 'long_name')):
        print(f"{variable:<25}  {g.variables[variable].long_name}")
    else:
        print(f"{variable:<25}  {variable}")

lon = pd.DataFrame(g.variables['x'][:], columns= ['lon'])
lat = pd.DataFrame(g.variables['y'][:], columns= ['lat'])
date_time = pd.DataFrame(g.variables['time_of_zeta_max'][:], columns = ['datetime'])
zmax = pd.DataFrame(g.variables['zeta_max'][:], columns = ['zeta_max'])

def getDetails():
    print(g['x'])
    print(g['y'])
    print(g['time_of_zeta_max'])
    print(g['zeta_max'])

## getting results
dat = pd.concat([date_time, lon, lat, zmax], axis = 1)
# dat.to_csv('storm21_results.csv')

print(dat)
dat = dat[~dat['datetime'].isna()]
dat.reset_index(inplace = True)
print(dat)


## converting the datetime
getDate = lambda x: datetime(2000, 1, 1) + timedelta(seconds = x)
date = pd.DataFrame(list(map(getDate, dat['datetime'])), columns= ['date'])
dat['date'] = date['date'].dt.strftime('%Y-%m-%d')
print(dat)


date_unique = dat['date'].unique()

storm_date = 1

for dd in date_unique:
    df = dat[dat['date'] == dd]

    ## plotting results
    fig = plt.figure(figsize = (10,10))
    ax = fig.add_subplot(1, 1, 1,
                            projection=ccrs.PlateCarree())
    ax.set_extent([-83, -79, 25, 28], crs=ccrs.PlateCarree())


    ## adding mapping extras
    ax.add_feature(cartopy.feature.LAND)
    ax.add_feature(cartopy.feature.OCEAN)
    ax.add_feature(cartopy.feature.COASTLINE)
    ax.add_feature(cartopy.feature.BORDERS, linestyle=':')
    ax.add_feature(COUNTIES, facecolor='none', edgecolor='gray')
    ax.add_feature(cartopy.feature.LAKES, zorder = -1)
    ax.coastlines()


    map = ax.scatter(x = dat["lon"], 
                    y = dat["lat"],
                        c = dat["zeta_max"], cmap='seismic',  marker = 's',#this is the changes
                            edgecolor = 'black', s=20, alpha=1, vmin = dat["zeta_max"].min(), 
                                        vmax = dat["zeta_max"].max())

    ax.set_title("{} - Day {}".format(storm_name, storm_date), fontsize = 20)
    plt.colorbar(map, orientation = "horizontal", pad = 0.03)

    plt.show()

    storm_date += 1