import numpy as np
import pandas as pd
from itertools import chain

df = pd.read_csv('/Users/zoekim/Desktop/g/Flash-U-Map/dataset/dc_crime_add_vars.csv')

def get_loc(x):
  num = str(x)
  if len(num[0:8]) == 8:
    return num[0:8]

def preprocess(df):  
    df = df[['hour', 'XBLOCK', 'YBLOCK']]   
    df['log'] = df.apply(lambda row: get_loc(row['XBLOCK']), axis=1)
    df['lat'] = df.apply(lambda row: get_loc(row['YBLOCK']), axis=1)
    df['result'] = 1
    df = df.drop(['XBLOCK', 'YBLOCK'], axis = 1)
    new_df = create_training_set(df)
    final_df = pd.concat([df, new_df])
    fianl_df = final_df.dropna(how = 'any',axis=0) 
    return final_df


def create_training_set(df):
    groups = pd.pivot_table(df,values='hour',index=['log', 'lat'],aggfunc={'hour': list})
    log_lat_pair = list(groups.index.values)
    hour_list = list(range(0, 23))
    new_df = pd.DataFrame(columns = ['hour', 'log', 'lat', 'result'])
    for i in log_lat_pair:
        hours = list(set(hour_list) - set(unlist(unlist(groups.loc[[i]].values))))
        #print(hours)
        for h in hours:    
            new_df = new_df.append({'hour' : h, 'log' : i[0], 'lat' : i[1], 'result' : 0}, ignore_index = True)

    return new_df

def unlist(li):
  return list(chain(*li))