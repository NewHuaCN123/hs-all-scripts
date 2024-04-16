remotes::install_github("mkoohafkan/dssrip2")

options(
  # replace with the install path on your machine
  dss.home = "C:/Program Files/HEC/HEC-DSSVue"
)


exfile = system.file("C:/CRTPM/Runs/Sim/v2.0_2FF_JustScour_100kcfs/output.dss", package = "dssrip2")
# time series
dss_read(exfile, "/SO_EXHAUSTED/")





# Load the rDSS library
library(rDSS)

dss_file <- "C:/CRTPM/Runs/Sim/v2.0_2FF_JustScour_100kcfs/output.dss"


# Open the DSS file
dss_data <- read.dss(dss_file)

# Print the data
print(dss_data)