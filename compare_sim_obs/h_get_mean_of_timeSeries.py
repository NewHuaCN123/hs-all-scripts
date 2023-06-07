

import os
import pandas as pd

obs_dir = 'R:\\40715-013 UKFPLOS\\Data\\H&H_Data\\kissimmee_gradient_figure\\obs'


os.chdir(obs_dir)

station = "s65_H.csv"

dat = pd.read_csv(station)
dat['datetime'] = pd.to_datetime(dat['datetime'])

dat.set_index(dat['datetime'], inplace = True)
dat_agg = pd.DataFrame(dat.iloc[:,1].resample('D').mean())

print(dat)

print(dat_agg)
dat_agg.reset_index(inplace = True)

print(dat_agg[(dat_agg['datetime'] >= "2011-10-03") & (dat_agg['datetime'] <= "2011-10-27")])