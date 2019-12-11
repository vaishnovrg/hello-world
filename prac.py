# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 13:25:34 2019

@author: rgvaish
"""

import pandas as pd
import numpy as np

df = pd.read_csv('training.tsv',sep='\t')
df_test = pd.read_csv('test.tsv',sep='\t')

df.columns = ['userid','date','activity']
group = pd.DataFrame(df.groupby('userid'))
group1 = df.groupby('userid').head()
group1.to_csv('group.csv')

df_train = pd.read_csv('training.tsv',sep='\t')
df_train.columns = ['userid','date','activity']
#df_train = df_train.drop(['userid'],axis=1)
df_train.head()

df_train['Year'] = pd.DatetimeIndex(df_train['date']).year
df_train['Month'] = pd.DatetimeIndex(df_train['date']).month
df_train['Day'] = pd.DatetimeIndex(df_train['date']).day
df_train['dayofweek'] = pd.DatetimeIndex(df_train['date']).dayofweek
df_train['week_num'] = pd.DatetimeIndex(df_train['date']).weekofyear

season=[]
for i,j in zip(df_train['Month'],df_train['Day']):
    month = i
    day = j

    if (month == '3') and (day > 19):
        son = 'spring'
    elif (month == '6') and (day > 20):
        son = 'summer'
    elif (month == '9') and (day > 21):
        son = 'autumn'
    elif (month == '12') and (day > 20):
        son = 'winter'

    season.append(son)

df_train=pd.DataFrame(season,columns=['season'])

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
le.fit_transform(df_train['activity'])

