fn = "C:\\Users\\mtadesse\\Downloads\\DEM_USGS2018_Avg500ft_original.tif"
'C:\\Users\\mtadesse\\Downloads\\DEM_USGS2018_Avg500ft_original.tif'
fi = QFileInfo()
fname = fi.baseName()
rlayer = iface.addRasterLayer(fn, fname)
rlayer = iface.addRasterLayer(fn, fname)