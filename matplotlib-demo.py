# -*- coding: utf-8 -*-
"""
title : python matplotlib
date  : 2016.12.02,09
author: Ming-Chang Lee
email : alan9956@gmail.com
RWEPA : http://rwepa.blogspot.tw/
"""

#pandas
import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randn(10, 4).cumsum(0),
               columns=['A', 'B', 'C', 'D'],
               index=np.arange(0, 100, 10))
df.plot()

import pandas
data = pandas.read_csv('data/brain_size.csv', sep=';', na_values=".")
data

from pandas.tools import plotting
#scatter plot matrix
plotting.scatter_matrix(data[['Weight', 'Height', 'MRI_Count']])  

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()

#matplotlib
import matplotlib.pyplot as plt
import numpy as np

# example 1
plt.plot([1,2,3,4])   # x 軸: 0,1,2,3
plt.ylabel("Quality")
plt.show()

# example 2
plt.plot([1,2,3,4], [1,4,9,16], 'ro')  # ro: red, circle marker
plt.axis([0, 6, 0, 20])
plt.show()

# example 3
# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

# example 4
plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.plot([1, 2, 3])
plt.subplot(212)             # the second subplot in the first figure
plt.plot([4, 5, 6])

plt.figure(2)                # a second figure
plt.plot([4, 5, 6])          # creates a subplot(111) by default

plt.figure(1)                # figure 1 current; subplot(212) still current
plt.subplot(211)             # make subplot(211) in figure1 current
plt.title('Easy as 1, 2, 3') # subplot 211 title

# example 5
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()

# example 6 (直方圖, histogram plot)
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

plt.xlabel("Smarts")
plt.ylabel("Probability")
plt.title("Histogram of IQ")
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

# example 7
fig = plt.figure()
# subplot:設定圖形位置(列,行,編號)
fig.add_subplot(221)   #top left
fig.add_subplot(222)   #top right
fig.add_subplot(223)   #bottom left
fig.add_subplot(224)   #bottom right 
plt.show()

# example 8
import os
os.getcwd()
os.chdir("C:/pythondata")

import scipy as sp
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\mingliu.ttc", size=12)

myData = sp.genfromtxt("data/web_traffic.csv")
myData = sp.genfromtxt("data/web_traffic.csv", delimiter="\t")
print(myData[:6])
myData.ndim
myData.shape # same as print(myData.shape)

x = myData[:,0]
y = myData[:,1]
x.shape

#check invalid data
sp.sum(sp.isnan(y))
print("Number of invalid entries:", sp.sum(sp.isnan(y)))

#取出非NaN
x = x[~sp.isnan(y)] # 735
y = y[~sp.isnan(y)]

#plot the (x,y) points with dots of size 10
plt.scatter(x, y, s=10)
plt.title(u"網路流量-2015年8月每小時", fontproperties=font) # 中文顯示
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)], ['week %i' % w for w in range(10)])
plt.autoscale(tight=True)

#draw a slightly opaque, dashed grid
plt.grid(True, linestyle='-', color='0.75')

#output png file
plt.savefig(u"網路流量-2015年8月每小時.png", dpi=300, format="png")
plt.show()

#plt.subplot()
#subplot(232) # 2列, 3行, 圖2位置
#圖1 , 圖2 , 圖3
#圖4 , 圖5 , 圖6
#plot.plot(x2,y2)

#plt.xticks() 來設定x軸刻度, e.g. plt.xticks([10,20,30,40,50])
#plt.yticks()來設定y軸刻度

# color
"""
b: blue
g: green
r: red
c: cyan
m: magenta
y: yellow
k: black
w: white
"""

# line style or marker
"""
'-'	  solid line style
'--'	dashed line style
'-.'	dash-dot line style
':'	  dotted line style
'.'	  point marker
','	  pixel marker
'o'	  circle marker
'v'	  triangle_down marker
'^'	  triangle_up marker
'<'	  triangle_left marker
'>'	  triangle_right marker
'1'	  tri_down marker
'2'	  tri_up marker
'3'	  tri_left marker
'4'	  tri_right marker
's'	  square marker
'p'	  pentagon marker
'*'	  star marker
'h'	  hexagon1 marker
'H'	  hexagon2 marker
'+'	  plus marker
'x'	  x marker
'D'	  diamond marker
'd'	  thin_diamond marker
'|'	  vline marker
'_'	  hline marker
"""
# http://matplotlib.org/users/pyplot_tutorial.html

#t檢定
import numpy as np
import pandas as pd
data = {'Category': ['cat2','cat1','cat2','cat1','cat2','cat1','cat2','cat1','cat1','cat1','cat2'],
        'values': [1,2,3,1,2,3,1,2,3,5,1]}
my_data = pd.DataFrame(data)
my_data
my_data.groupby('Category').mean()

from scipy.stats import ttest_ind

cat1 = my_data[my_data['Category']=='cat1']
cat2 = my_data[my_data['Category']=='cat2']

ttest_ind(cat1['values'], cat2['values'])
