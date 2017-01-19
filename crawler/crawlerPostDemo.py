# -*- coding: utf-8 -*-
import requests
payload={
    'StartStation':'977abb69-413a-4ccf-a109-0272c24fd490',
    'EndStation':'a7a04c89-900b-4798-95a3-c01c455622f4',
    'SearchDate':'2016/12/30',
    'SearchTime':'16:00',
    'SearchWay':'DepartureInMandarin'
}
res = requests.post('https://www.thsrc.com.tw/tw/TimeTable/SearchResult',data=payload)
print (res.text)



import requests
from bs4 import BeautifulSoup

url = "http://www.moneydj.com/InfoSvc/apis/vc"
payload = {"counts":[{"svc":"NV","guid":"a180a15b-9e4f-4575-b28f-927fcb5c63a3"}]} 
head = {'Content-Type':'application/json'}
res = requests.post(url, data=payload, headers = head)
print (res.text)
