import pyhecdss

# Open the DSS file
dss_file = pyhecdss.DSSFile('C:\\CRTPM\\Runs\\Sim\\v2.0_2FF_JustScour_100kcfs\\output.dss')

# Get the catalog of paths
catalog = dss_file.getCatalog()