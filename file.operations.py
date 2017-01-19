# -*- coding: utf-8 -*-
"""
title : python - import/export file
date  : 2016.12.02,09
author: Ming-Chang Lee
email : alan9956@gmail.com
RWEPA : http://rwepa.blogspot.tw/
"""

# read and write text
f = open("foo","w") 	# Open a file for writing
f.write("Hello World")
f.close()

g = open("foo","r") 	# Open a file for reading
data = g.read() 		   # Read data
data

g = open("foo","r")
line = g.readline() 	# Read a single line
line

g = open("foo","r")
lines = g.readlines()  # Read data as a list of lines
lines

# write
for i in range(0,10):
	f.write("2 times %d = %d\n" % (i, 2*i))

for i in range(0,10):
	print("2 times %d = %d\n" % (i, 2*i))

# read text file with print
input_file = "data/booklist.txt"
filereader = open(input_file, "r")
for line in filereader:
    print(line)
    
# read text file with list
with open("data/booklist.txt") as f:
    content1 = f.readlines()
    f.close()

# 刪除斷行符號
content2 = [line.rstrip('\n') for line in open("data/booklist.txt")]
            
content1
content2

# read csv with print
import csv
with open("data/booklist.csv") as f: 
    reader = csv.reader(f) # 如果區隔是冒號, 可加上 delimiter=':'
    for row in reader:
        print(row)
        
# read csv with array
import csv
import numpy as np
with open("data/booklist.csv",encoding='utf8') as csvfile:
    book_reader = csv.reader(csvfile, delimiter=",")
    
    # Header contains feature names
    # row = book_reader.next()
    # feature_names = np.array(row)
    feature_names = next(book_reader) # 欄位名稱
    books = []
    for row in book_reader:
        books.append(row)
    books = np.array(books)
    len(books)

# read excel
import pandas
df = pandas.read_excel("data/booklist.xlsx")

# print the column names
print(df.columns)

# get the values for a given column
values = df["Title"].values

#g et a data frame with selected columns
FORMAT = ["Title", "PublishedDate"]
df_selected = df[FORMAT] # ERROR

# 練習匯入細懸浮微粒資料（PM2.5）
# http://data.gov.tw/node/34827 

# Python 連結 MySQL - MySQLdb
# 下載原始檔 MySQL-python-1.2.4b4.tar.gz

# cd MySQL-python-1.2.4b4
# python setup.py build
# python setup.py install

# 載入 MySQL 模組
import MySQLdb
     
# 連接到 MySQL
db = MySQLdb.connect(host="localhost", user="db_user", passwd="db_pass", db="db_name")
cursor = db.cursor()
     
# 執行 SQL 語句
cursor.execute("SELECT * FROM db_table")
result = cursor.fetchall()
     
# 輸出結果
for record in result:
    print(record[0])

# Python 連結 MySQL - pymysql

# pip install pymysql
import pymysql.cursors
import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='passwd',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# try:
with connection.cursor() as cursor:
    # Create a new record
    sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

with connection.cursor() as cursor:
    # Read a single record
    sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
    cursor.execute(sql, ('webmaster@python.org',))
    result = cursor.fetchone()
    print(result)
# finally:
connection.close()    
# ref: http://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python

# Python 連結 MSSQL - pymssql
import pymssql
conn = pymssql.connect(server='yourserver.database.windows.net', 
                       user='yourusername@yourserver', 
                       password='yourpassword', 
                       database='AdventureWorks')
# ref: https://docs.microsoft.com/zh-tw/azure/sql-database/sql-database-develop-python-simple

# Python 連結 Oracle - cx_Oracle
import cx_Oracle
con = cx_Oracle.connect('pythonhol/welcome@127.0.0.1/orcl')
print(con.version)
con.close()
# ref: http://www.oracle.com/technetwork/articles/dsl/python-091105.html

# pandas module
import numpy as np
import pandas as pd

#Series
obj = pd.Series([4, 7, -5, 3])
obj

obj.values
obj.index

#Series 直接指定 index
obj2 = pd.Series([1, 3, 5, 7], index=['d', 'b', 'a', 'c'])
obj2

#篩選
obj2['a']

#設定值
obj2['d'] = 6

#範圍篩選
obj2[['c', 'a', 'd']]

#array操作
obj2

obj2[obj2 > 5]

obj2 * 2

np.exp(obj2)

'b' in obj2

'e' in obj2

#將 Dict 轉換為 Series
sdata = {'台北市': 35000, '新北市': 71000, '台中市': 16000, '高雄市': 5000}
obj3 = pd.Series(sdata)
obj3

data = {'state': ['台北市', '台北市', '台北市', '新北市', '新北市'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = pd.DataFrame(data)
frame

#修改欄位順序
pd.DataFrame(frame, columns=['year', 'state', 'pop'])

#建立新欄位
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                      index=['one', 'two', 'three', 'four', 'five'])
frame2

frame2.columns

frame2['state']

frame2.state

frame2['pop'] = 3.6

frame2['debt'] = np.arange(5.)

del frame2['debt']
frame2

#排序
obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
obj
obj.sort_index()

#合併
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3]) 

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                    index=[4, 5, 6, 7])


df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                    index=[8, 9, 10, 11])

df = [df1, df2, df3]

result = pd.concat(df)

#merge
frame1 = pd.DataFrame( {'id':['ball','pencil','pen','mug','ashtray'],
                        'price': [12.33,11.44,33.21,13.23,33.62]})

frame2 = pd.DataFrame( {'id':['pencil','pencil','ball','pen'],
                        'color': ['white','red','red','black']})

frame1
frame2

pd.merge(frame1, frame2)

#ref: http://pandas.pydata.org/pandas-docs/stable/merging.html
# end
