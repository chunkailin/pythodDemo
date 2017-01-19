# -*- coding: utf-8 -*-
"""
title : python - summary and group
date  : 2016.12.02,09
author: Ming-Chang Lee
email : alan9956@gmail.com
RWEPA : http://rwepa.blogspot.tw/
"""

import numpy as np
x = np.arange(10)

#平均值 mean
np.mean(x)

xWithNan = np.hstack( (x, np.nan) ) # append nan
np.mean(xWithNan) # nan

np.nanmean(xWithNan)

#中位數 median
np.median(x)

#眾數 mode
from scipy import stats #stats 統計模組
data = [1, 3, 4, 4, 7, 7, 7, 8]
stats.mode(data)

#全距Range
np.ptp(data)

#標準差 standard deviation
np.std(data)

#6力分析
import pandas as pd
df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],
                [np.nan, np.nan], [0.75, -1.3]],
                index=['a', 'b', 'c', 'd'],
                columns=['one', 'two'])
df

df.sum() # 欄合計

df.sum(axis=1) # 列合計
df.sum(axis=1, skipna=False) # 列合計, NaN excluded

df.mean(axis=1, skipna=False)

df.cumsum()

df.describe()

# 建立隨機樣本
from random import randint
print(randint(0,9))

from random import randrange, uniform, gauss
# randrange gives you an integral value
randrange(0, 10)

# uniform gives you a floating-point value
uniform(0, 10)

gauss(0, 1)


#群組分析
frame1 = pd.DataFrame(np.arange(9).reshape(3,3),
                      index=['white','black','red'],
                      columns=['ball','pen','pencil'])
frame1

#stack (unstack)
frame1.stack()

#長資料轉為寬資料
longframe = pd.DataFrame({ 'color':['white','white','white', 'red','red','red',  'black','black','black'],
                          'item':['ball','pen','mug', 'ball','pen','mug', 'ball','pen','mug'],
                          'value': np.random.rand(9)})
longframe

wideframe = longframe.pivot('color','item')
wideframe
#end