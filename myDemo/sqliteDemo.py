# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('C:/Users/A40152/Documents/Sqlite/scores.sqlite')
conn.execute('insert into student values(1,"林駿凱")')
conn.commit()
conn.close()

