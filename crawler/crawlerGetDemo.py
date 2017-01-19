# -*- coding: utf-8 -*-
import requests
res = requests.get("http://mall.pchome.com.tw/prod/QBAH2T-A900609T4")
print(res.text)


from bs4 import BeautifulSoup
html_sample = '''
<html>
<body>

<p>Hello World!</p>

<p>The DOM is very useful.</p>
<p>This example demonstrates the <b>getElementsByTagName</b> method</p>
<p id="demo">python Demo</p>
<a href="#" class="link">This is link1</a>
<a href="# link2" class="link">This is link2</a>
</body>
</html>
'''
#print(html_sample)
soup = BeautifulSoup(html_sample)

#只顯示文字內容
print (soup.text)

#顯示DOC內容(tag + 文字) 放入list中
print (soup.contents)

#DOM selector
print (soup.select('p')[0])
print (soup.select('a'))
print (soup.select('#demo'))
print (soup.select('.link'))

import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame

packageTourList = list()
res = requests.get("http://project.xervice.in:9003/nantou/tickets/listAll?zone=exA")
print(res.text)
soup = BeautifulSoup(res.text)
print (soup.select('.boxin'))
for packageTour in soup.select('.boxin'):
    tmpPackageTour=[]
    tmpPackageTour.append(packageTour.select('h4')[0].text)
    tmpPackageTour.append(packageTour.select('.left')[0].text)
    tmpPackageTour.append(packageTour.select('.right')[0].text)
    packageTourList.append(tmpPackageTour)

print(packageTourList)
df = pd.DataFrame(data = packageTourList, columns=['packageTourName', 'salsePrice','ListPrice'])
print(df)


import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
import json
res = requests.get("http://hinet.xervice.in/app/storeQueryEasyCard?storeId=20&username=wchtstore1@gmail.com&password=cht12345&deviceId=08db0340&lang=zh_TW&os=android&appName=android_store&version=1011&cardNumber=00000636LC59DYP02113")
print(res.text)

result = json.loads(res.text)


    


