# _*_ coding: utf-8 _*_
# 程式 9-8 (Python 3 version)

from bs4 import BeautifulSoup
import requests
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas

url = 'http://new.cpc.com.tw/division/mb/oil-more4.aspx'

html = requests.get(url).text
sp = BeautifulSoup(html, 'html.parser')
data = sp.find_all('span', {'id':'Showtd'})
rows = data[0].find_all('tr')

prices = list()
for row in rows:
    cols = row.find_all('td')
    if len(cols[1].text) > 0:
        item = [cols[0].text, cols[1].text, \
                cols[2].text, cols[3].text]
        prices.append(item)

df = pd.DataFrame(data = prices, columns=['Date', '92無鉛','95無鉛','98無鉛'])
df.to_csv('cpcOilPrice.csv',index=False,header=False)

Location = r'C:\pythondata\cpcOilPrice.csv'
df = pd.read_csv(Location, names=['Date', '92無鉛','95無鉛','98無鉛'])

pd.to_datetime(df.index, format='%Y/%m/%d')
df[['92無鉛','95無鉛','98無鉛']] = df[['92無鉛','95無鉛','98無鉛']].astype(float)
df.head()
df.info()
%pylab inline
df.plot(kind='line', y=['92無鉛','95無鉛','98無鉛'])




