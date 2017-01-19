# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 10:08:25 2016

@author: ryder
"""

# read csv with array
import csv
import numpy as np
with open("data/dhTransactionData.csv") as csvfile:
    book_reader = csv.reader(csvfile, delimiter=",")
    
    # Header contains feature names
    # row = book_reader.next()
    # feature_names = np.array(row)
    feature_names = next(book_reader) # 欄位名稱
    books = []
    for row in book_reader:
        books.append(row)
    books = np.array(books)
    
    
import pandas
df=pandas.read_csv("data/dhTransactionData.csv")
dfnan=df.dropna(how='all')
    