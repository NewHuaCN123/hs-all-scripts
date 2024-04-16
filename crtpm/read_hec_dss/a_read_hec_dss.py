"""  
Created on Tue Apr 16 2024 10:10:00

Read and extract time series from HEC-DSS

@author: Michael Getachew Tadesse

"""


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydsstools.heclib.dss import HecDss
from pyhecdss import DSSFile
import pyhecdss


os.chdir("C:\\CRTPM\\Runs\\Sim\\v2.0_2FF_JustScour_100kcfs")
fname = "output.dss"

from datetime import datetime
from pyhecdss import DSSFile

def read_dss_timeseries(dss_filename, pathname):
    with DSSFile(dss_filename, mode="r") as dss_file:
        dataset = dss_file.read_dataset(pathname)
        if dataset:
            times = dataset.get("times")
            values = dataset.get("values")
            units = dataset.get("units")
            interval = dataset.get("interval")

            start_time = datetime.fromtimestamp(times[0])
            end_time = datetime.fromtimestamp(times[-1])

            print(f"Time series data for pathname: {pathname}")
            print(f"Start Time: {start_time}")
            print(f"End Time: {end_time}")
            print(f"Time Interval: {interval} seconds")
            print(f"Units: {units}")
            print("Time\t\tValue")
            for time, value in zip(times, values):
                timestamp = datetime.fromtimestamp(time)
                print(f"{timestamp}\t{value}")
        else:
            print(f"No data found for pathname: {pathname}")


if __name__ == "__main__":
    dss_filename = "C:\\CRTPM\\Runs\\Sim\\v2.0_2FF_JustScour_100kcfs\\output.dss"
    pathname = "/your/pathname/to/data"
    read_dss_timeseries(dss_filename, pathname)