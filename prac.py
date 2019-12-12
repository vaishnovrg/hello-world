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
#group = pd.DataFrame(df.groupby('userid'))
#group1 = df.groupby('userid').head()
#group1.to_csv('group.csv')

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
son=''
for i in df_train['Month']:
    month = i


    if (3<month<=6):
        son = 'spring'
    elif (6<month<=9):
        son = 'summer'
    elif (9<month<=12):
        son = 'autumn'
    elif (1<month<=3):
        son = 'winter'

    season.append(son)
    

df_train_1=pd.DataFrame(season,columns=['season'])

train = pd.concat([df_train, df_train_1],axis=1)

del train['userid']
del train['date']

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
train['activity'] = le.fit_transform(train['activity'])

train.head()

le1 = LabelEncoder()
train['season'] = le1.fit_transform(train['season'])

X_train = train.loc[:, train.columns != 'activity']

y_train = train['activity']

from sklearn.tree import DecisionTreeClassifier 
clf = DecisionTreeClassifier() 
clf.fit(X_train,y_train)

from sklearn.externals import joblib 
joblib.dump(clf, 'practise.pkl') 
#clf = joblib.load('filename.pkl')  
#clf.predict(X_test) 
#-----------------------------------------test set----------------------------------------------------------------------------------------------

df_test.columns = ['userid','date','activity']
df_test['Year'] = pd.DatetimeIndex(df_test['date']).year
df_test['Month'] = pd.DatetimeIndex(df_test['date']).month
df_test['Day'] = pd.DatetimeIndex(df_test['date']).day
df_test['dayofweek'] = pd.DatetimeIndex(df_test['date']).dayofweek
df_test['week_num'] = pd.DatetimeIndex(df_test['date']).weekofyear

season1=[]
son1=''
for i in df_test['Month']:
    month = i


    if (3<month<=6):
        son1 = 'spring'
    elif (6<month<=9):
        son1 = 'summer'
    elif (9<month<=12):
        son1 = 'autumn'
    elif (1<month<=3):
        son1 = 'winter'

    season1.append(son1)
    

df_test_1=pd.DataFrame(season1,columns=['season'])

test = pd.concat([df_test, df_test_1],axis=1)

del test['userid']
del test['date']

test['activity'] = le.transform(test['activity'])
test['season'] = le1.transform(test['season'])

X_test = test.loc[:, test.columns != 'activity']

y_test = test['activity']

#--------------------------------------------Prediction----------------------------------------------------------------------------------------

y_pred = clf.predict(X_test)
y_pred = y_pred.astype(np.int32)

from sklearn.metrics import accuracy_score
score = accuracy_score(y_pred,y_test)

