#' 
#' """  
#' Created on Mon Nov 21 09:23:00 2022
#' 
#' extreme value analysis of daily maximum storm surges
#' 
#' @author: Michael Getachew Tadesse
#' 
#' """

library(extRemes)
library(evd)

setwd('D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\BrowardRes\\scenarios_joint_probability\\virginia_key_data')

dat = read.csv('rain24_surge_amax_std.csv')

dat

plot(dat$year, dat$summed_std, 'l')

# fit a GEV to the maxima and assess fit
gevfit1 <- fevd(x = dat$summed_std, type = "Gumbel")
gevfit1

return.level(gevfit1, do.ci = TRUE)

# 
plot(gevfit1)


CI_delta <- ci(gevfit1, return.period = 78, verbose = T)
CI_delta