# !pip3 install pandas
# !pip3 install numpy
import pandas as pd
import numpy as np
# Fuction
def combine_predictions(zone):

    temp = pd.read_csv(f'raw_data/{zone}.csv')

    temp['pred_temp'] = np.nan
    temp['pred_pm25'] = np.nan
    temp['pred_pm10'] = np.nan
    temp['pred_smog'] = np.nan

    temp1 = pd.read_csv(f'prediction/{zone}.csv')
    temp1.columns = ['date','zone','longitude','latitude','pred_temp','pred_pm25','pred_pm10','pred_smog']

    temp1['temperature'] = np.nan
    temp1['pm2_5']=np.nan
    temp1['pm10']=np.nan
    temp1['smog']=np.nan

    temp1=temp1[['date','zone','longitude','latitude','temperature','pm2_5','pm10','smog','pred_temp','pred_pm25','pred_pm10','pred_smog']]

    return(pd.concat([temp,temp1]))

# check if final_data.csv exists
import os.path
from os import path
if path.exists("final_data.csv"):
    print("final_data.csv exists")
else:
    # Writing back to files
    df = combine_predictions(1)
    df.to_csv('final_data.csv', index=False)

    for i in range(2,249):
        combine_predictions(i).to_csv('final_data.csv', mode='a', header=False, index=False)
        print(f"{i} done")