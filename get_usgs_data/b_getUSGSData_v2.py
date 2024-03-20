"""  
Created on Tue Mar 12 10:45:00 2024

Get USGS data from API - Gage Height

@author: ChatGPT

"""


import requests
import csv
from pprint import pprint
import pandas as pd
import datetime
import matplotlib.pyplot as plt


def download_gage_height_data(site_id, start_date, end_date):
    url = f"https://waterdata.usgs.gov/nwis/dv?cb_00065=on&format=rdb&site_no={site_id}&referred_module=sw&period=&begin_date={start_date}&end_date={end_date}"

    response = requests.get(url)
    if response.status_code == 200:
        lines = response.text.split('\n')
        data_lines = [line.split('\t') for line in lines if line.startswith('USGS')]
        # pprint(data_lines)
        return data_lines
    else:
        print("Failed to retrieve data.")
        return None

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Date', 'Gage Height (feet)'])
        # print(writer)
        for row in data:
            writer.writerow([row[2], row[3]])

def plot_hydrograh(filename):
    plt.figure(figsize = (16,5))
    dat = pd.read_csv(filename)
    dat['Date'] = pd.to_datetime(dat['Date'])
    plt.plot(dat['Date'], dat['Gage Height (feet)'], c = "red")
    plt.ylabel('Gage Height (feet)')
    plt.title(site_id)
    plt.grid(which='both', linestyle='--', alpha=0.5)  # Add grid lines
    # plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()

if __name__ == "__main__":
    site_id = input("Enter USGS site ID: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    filename = input("Enter filename to save CSV: ")

    data = download_gage_height_data(site_id, start_date, end_date)
    if data:
        save_to_csv(data, filename)
        plot_hydrograh(filename)
        print("Data saved and plotted successfully.")
