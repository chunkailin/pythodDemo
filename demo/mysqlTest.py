# -*- coding: utf-8 -*-


# pip install pymysql
# conda install mysql-connector-python

import pymysql

conn = pymysql.connect(host='139.162.114.102', port=3306, user='haproxy_root', passwd='53434976', db='hinetdb')

cur = conn.cursor()

cur.execute("SELECT username FROM sys_user")

print(cur.description)

print()

for row in cur:
    print(row)

cur.close()
conn.close()