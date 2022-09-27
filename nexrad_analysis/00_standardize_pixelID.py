"""  
Created on Wed Aug 04 10:39:00 2022

standardize the pixel ids for sjrwmd and swfwmd 

@author: Michael Getachew Tadesse

"""

import os
import pandas as pd 

dir_in = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\SWFWMD\\rainfall\\"\
                "pixel_rainfall_distributed\\2011"
dir_out = "R:\\40715-013 UKFPLOS\\Received_Data_Models\\SWFWMD\\rainfall\\"\
                "pixel_rainfall_distributed"


pixList = pd.DataFrame(os.listdir(dir_in), columns = ['pixel'])

# remove extention
rmvExt = lambda x: x.split('.csv')[0]
pixList['pixel_clean'] = pd.DataFrame(list(map(rmvExt, pixList['pixel'])))

# check length of pixel id
chkLen = lambda x: len(x)
pixList['len'] = pd.DataFrame(list(map(chkLen, pixList['pixel_clean'])))

pixList['pixel_stand'] = 'nan'

print(pixList)

for pp in range(len(pixList)):
    # print(pp)
    
    if pixList['len'][pp] == 6:
        pixList['pixel_stand'][pp] = '10' + str(pixList['pixel_clean'][pp])
    elif pixList['len'][pp] == 5:
        pixList['pixel_stand'][pp] = '100' + str(pixList['pixel_clean'][pp])

# add extension
addExt = lambda x: x + '.dfs0'
pixList['pixel_final'] = pd.DataFrame(list(map(addExt, pixList['pixel_stand'])))


print(pixList)

os.chdir(dir_out)
pixList.to_csv('pixel_standard_id.csv')
