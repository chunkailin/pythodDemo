# -*- coding: utf-8 -*-
# pip install pymysql
# conda install mysql-connector-python

import pymysql

conn = pymysql.connect(host='hinet.xervice.in', port=3306, user='itriadmin', passwd='02750963c200', db='hinetdb')

cur = conn.cursor()

cur.execute("SELECT username FROM sys_user")

print(cur.description)

print()

for row in cur:
    print(row)

cur.close()
conn.close()