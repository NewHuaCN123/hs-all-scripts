
import os
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score



os.chdir("C:\\Users\\mtadesse\\Documents\\toDelete")
dat = pd.read_csv("testDat.csv")

print(dat)

r = np.corrcoef(dat['g103_sim'], dat['g113_sim'])
print(r)


r2 = r2_score(dat['g103_sim'], dat['g113_sim'])
print(r2)