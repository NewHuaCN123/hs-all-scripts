"""  
Created on Tue Mar 13 15:01:00 2024

Get USGS data from API

@author: Michael Getachew Tadesse

"""

import csv
import pandas as pd
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup

# html = urlopen('https://www.usbr.gov/pn-bin/instant.pl?station=gcl&format=html&year=2023&month=1&day=1&year=2024&month=12&day=31&pcode=af&pcode=fb&pcode=q&pcode=qe')
# bs = BeautifulSoup(html, 'html.parser')
# table = bs.findAll('table', {'class': ''})[0]

# # print(table)

# rows = table.findAll('tr')

# # pprint(rows)

# csvFile = open('GrandCouleeData.csv', 'wt+')
# writer = csv.writer(csvFile)
# try:
#     for row in rows:
#         csvRow = []
#         for cell in row.findAll(['td', 'th']):
#             csvRow.append(cell.get_text())
#         writer.writerow(csvRow)
#         print(csvRow)
# finally:
#     csvFile.close()


dat = pd.read_html('https://www.usbr.gov/pn-bin/instant.pl?station=gcl&format=html&year=1982&month=1&day=1&year=2024&month=3&day=31&pcode=af&pcode=fb&pcode=q&pcode=qe')

# print(dat)
# print(dat[0])

# # dat = pd.DataFrame(dat)

dat[0].to_csv("GrandCouleeData.csv")

