# -*- coding: utf-8 -*-
"""
title : 案例演練
date  : 2016.12.02,09
author: Ming-Chang Lee
email : alan9956@gmail.com
RWEPA : http://rwepa.blogspot.tw/
"""

# http://web.ydu.edu.tw/~alan9956/rdata/breakfasts.zip

# using csv package
import csv
import numpy as np
with open('data/dhTransactionData.csv') as csvfile:
    dhTransactionData_reader = csv.reader(csvfile, delimiter=",")
    feature_names = next(dhTransactionData_reader) # 欄位名稱
    dhTransactionData = []
    for row in dhTransactionData_reader:
        dhTransactionData.append(row)
    dhTransactionData = np.array(dhTransactionData)

dhTransactionData[0:5, ]
feature_names

# sing pandas
import numpy as np
import pandas as pd
import sys
print('Python version ' + sys.version)
print('Pandas version: ' + pd.__version__) ## __version__(constructor)

df = pd.read_csv('data/dhTransactionData.csv')

df.shape # 682321*12

df.dtypes

len(df) # 列數

df.columns # 顯示欄位名稱

df.ix?

df.ix[680000,]

df.ix[0:5,]

df.ix[0:5, ['WEEK_END_DATE', 'STORE_NUM', 'SPEND']]

df.head()

df.tail() # 有NaN

df['SPEND'][0:5]
dfSPENDrange = pd.cut(df['SPEND'], 5) # 將連續資料轉換為類別型資料
dfSPENDrange[:5]

pd.value_counts(dfSPENDrange)

pd.value_counts(df['WEEK_END_DATE'])

df['WEEK_END_DATE'].value_counts()

df['WEEK_END_DATE'].unique() # 不重複值

len(df['WEEK_END_DATE'].unique())

# 敘述統計(R: summary)
df.SPEND.describe()

# 群組分析(R: aggregate)
wendsum = df.groupby('WEEK_END_DATE').aggregate(np.sum)
wendsum

# NaN 值處理

#drop all rows that have any NaN in SPEND column
dfnew1 = df[np.isfinite(df['SPEND'])] # 524950*12

#drop all rows that have any NaN values
dfnew2 = df.dropna() # 524742*12

#drop only if ALL columns are NaN
dfnew3 = df.dropna(how='all') # 524950*12

#Drop row if it does not have at least two values that are **not** NaN
dfnew4 = df.dropna(thresh=2) # 524950*12

#notnull
dfnew5 = df[df.SPEND.notnull()] # 524950*12

#isnull
dfnew6 = df[~df.SPEND.isnull()] # 524950*12

dfnew7 = df[~np.isnan(df.SPEND)] # 524950*12

#console --> CTRL + .
#reference: http://pandas.pydata.org/pandas-docs/stable/tutorials.html
#end