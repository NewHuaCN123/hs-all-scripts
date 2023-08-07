

import os
import pandas as pd
import mikeio
from mikeio1d.res1d import Res1D, QueryDataReach



os.chdir('E:\data_transfer\may-31\BCB_0411\MHydro_0523\BCB_061923-NoHS-FCv6b.mhydro - Result Files')

df = Res1D('HD_BCB_112222.res1d').read()

print(df)
