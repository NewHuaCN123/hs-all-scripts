
library(extRemes)


##Loading data
setwd("R://40715-021//Modeling//Data//RSM_boundary_data")



#load declustered surge time series
dat <- read.csv("S-31_TW_amax.csv")

surge = dat[,c(1,3)]
surge$year = as.Date(surge$year,tryFormats="%Y")
colnames(surge)<-c("Year","Value")

plot(surge$Year, surge$Value)


#filter surge based on a threshold
# surge_thres <- na.omit(surge[surge$Value > 1.4, ])

plot(surge$Year, surge$Value, col = "darkblue")
fit <- fevd(surge$Value, type = "GEV")

names(fit)

fit$type

plot(fit)

return.level(fit, return.period = c(2, 5, 10, 25, 50, 100))



#load declustered rainfall time series
rain_dat <- read.csv("rain_declust.csv")
rain = rain_dat[,c(2,3)]
rain$date = as.Date(rain$date,tryFormats="%m/%d/%Y")
colnames(rain)<-c("Date","Value")

plot(rain$Date, rain$Value)


#filter surge based on a threshold
rain_thres <- na.omit(rain[rain$Value > 1.13, ])
plot(rain_thres$Date, rain_thres$Value, col = "darkblue")
fit <- fevd(rain_thres$Value, type = "GEV")
plot(fit)

return.level(fit, return.period = c(2, 5, 10, 25, 50, 100))


