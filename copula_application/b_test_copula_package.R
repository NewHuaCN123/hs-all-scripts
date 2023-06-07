
# Author: Michael Tadesse
# Date: June 07, 2023 16:14
# Purpose: prepare data for coupula application + apply copula model on dataset

library(MultiHazard)

setwd('C:\\Users\\mtadesse\\Documents\\test_data')

dat <- read.csv('vign_keys_precip_surge.csv')

p <- dat[, c('date', 'value')]
s <- dat[, c('date', 'max_surge')]

# declustering
p_dec <- Decluster(p$value, u = 0.95, SepCrit = 3, mu = 365.25)
s_dec <- Decluster(s$max_surge, u = 0.95, SepCrit = 3, mu = 365.25)

p$dec <- p_dec$Declustered
s$dec <- s_dec$Declustered

# plotting
plot(as.Date(p$date),p$value,col="Grey",pch=16,
     cex=0.25,xlab="Date",ylab="Daily Precipitation")
abline(h=p_dec$Threshold,col="Dark Green")
points(as.Date(p$date[p_dec$EventsMax]),
       p_dec$Declustered[p_dec$EventsMax],
       col="Red",pch=16,cex=0.5)



plot(as.Date(s$date),s$max_surge,col="Grey",pch=16,
     cex=0.25,xlab="Date",ylab="Daily Maximum Surge")
abline(h=s_dec$Threshold,col="Dark Green")
points(as.Date(s$date[s_dec$EventsMax]),
       s_dec$Declustered[s_dec$EventsMax],
       col="Red",pch=16,cex=0.5)


# kendall's correlation
d <- dat[,c('date','value', 'max_surge')]
Kendall_Lag(Data=d,GAP=0.2)


# Bivariate analysis
Copula_Threshold_2D(Data_Detrend=d[, c('value', 'max_surge')],
                    Data_Declust=d[, c('value', 'max_surge')],
                    y_lim_min=-0.075, y_lim_max =0.25,
                    Upper=c(2,9), Lower=c(2,10),GAP=0.15)

dat_bivariate <- Design_Event_2D(Data = d[, c('value', 'max_surge')], Data_Con1 = d$value, Data_Con2 = d$max_surge, u1 = d$value)



