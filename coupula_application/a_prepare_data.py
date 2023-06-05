"""
Author: Michael Tadesse
Date:   June 05, 2023 17:20
Purpose: pre-process data for copula application
"""

import os 
import pandas as pd
import matplotlib.pyplot as plt


os.chdir("D:\\MIKE_Modeling_Files\\Hazen and Sawyer\\Hazen and Sawyer\\"\
         "MIKE_Modeling_Group - Documents\\BrowardRes\\"\
                "scenarios_joint_probability\\virginia_key_data")

print(os.listdir())

precip = pd.read_csv("vn239_daily_rainfall.csv")
surge = pd.read_csv("virginia_keys_dmax_surge.csv")

precip = precip[["date", "value"]]



print(precip)
print(surge)

