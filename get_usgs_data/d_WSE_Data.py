import requests
import csv

def download_water_surface_elevation(site_code, start_date, end_date):
    # USGS API base URL
    base_url = 'https://waterservices.usgs.gov/nwis/iv/'

    # Parameters for the request
    params = {
        'format': 'json',
        'site': site_code,
        'startDT': start_date,
        'endDT': end_date,
        'parameterCd': '62620',  # Water Surface Elevation parameter code
    }

    # Making the request
    response = requests.get(base_url, params=params)
    data = response.json()

    # Extracting time series data
    time_series = data['value']['timeSeries'][0]['values'][0]['value']

    # Creating CSV file
    with open(f'{site_code}_water_surface_elevation.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['datetime', 'water_surface_elevation (feet)'])

        for entry in time_series:
            datetime = entry['dateTime']
            elevation = entry['value']
            writer.writerow([datetime, elevation])

    print(f"Data saved as {site_code}_water_surface_elevation.csv")

# Example usage
site_code = 'site_code'  # Replace 'site_code' with the specific site code you want to retrieve data for
start_date = 'YYYY-MM-DD'  # Replace with your desired start date
end_date = 'YYYY-MM-DD'  # Replace with your desired end date

download_water_surface_elevation(site_code, start_date, end_date)
