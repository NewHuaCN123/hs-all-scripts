"""  
Created on Wed Aug 11 18:34:00 2022

QGIS cheet sheet


@author: Michael Getachew Tadesse
"""

## Using conditionals in QGIS
#### modifying attributes

case
	when layer = 'sfwmd_wells_not_in_shp' then DBKEY
	when layer = 'ukb_sf_GW_sites_sa_ufa_zshift_v3' then DBKEY
	when layer = 'ukb_swf_wells_not_in_SHP' then SITE_ID
	when layer = 'ukb_swf_sa_ufa' then SITE_ID
	when layer = 'ukb_sjr_sa_int_ufa' then HYDRO_NO
end 



## Using GDAL raster calculator

<!-- choose band first -->

<!-- to select raster values with OR operator -->
logical_or(A == 41, A == 42, A == 43)


<!-- to replace raster values -->
<!-- replacing 41 with 5, 42 with 15, and 43 with 45 -->
(A == 41)*5 + (A == 42)*15 + (A == 43)*45



## Converting/translating from TIF -> ASCII
Make sure to add the nodata format - 9999

## For Cartopy to work properly you might need to install shapely and pyproj .whl files too


## to label only selected features in QGIS

properties -> rendering -> show label -> edit -> modify using field calculator