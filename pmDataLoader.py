# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 11:03:41 2016

@author: ryder
"""

import csv
import numpy as np
with open("data/ATM00625_20161130170549.csv",encoding='utf8') as csvfile:
    pmData = csv.reader(csvfile, delimiter=",")
    
    # Header contains feature names
    # row = book_reader.next()
    # feature_names = np.array(row)
    feature_names = next(pmData) # 欄位名稱
    pmDataList = []
    for row in pmData:
        pmDataList.append(row)
    pmDataList = np.array(pmDataList)