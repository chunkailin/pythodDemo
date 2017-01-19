# -*- coding: utf-8 -*-
"""
title : python.sklearn installation
date  : 2016.12.02,09
author: Ming-Chang Lee
email : alan9956@gmail.com
RWEPA : http://rwepa.blogspot.tw/
"""

# 更新 conda and Spyder
# conda install spyder

# 檔案位置 c:/pythondata
# python.sklearn.讀我.py , 檔案說明
# Day 1
# type.operations.py     , 資料操作 
# file.operations.py     , 資料庫連結 
# 案例演練(一)
# 演練目標： 
# (1).熟悉資料匯入 
# (2).資料處理
# http://web.ydu.edu.tw/~alan9956/rdata/breakfasts.zip

# Day 2
# summary_group.py       , 資料摘要與群組分析
# matplotlib-demo.py     , 統計繪圖
# regression.py          , 迴歸分析 regression analysis, 線性模型 linear model
# logistic-regression.py , logistic regression-分類
# decision-tree.py       , 決策樹 decision tree
# decision-tree.py       , 隨機森林法 random forest
# decision-tree-codes.py , 決策樹 Python codes
# 案例演練(二)
# 演練目標： 
# (1).熟悉統計應用: 檢定不同地區平均銷售量是否有所差異 
# (2).建立預測模型: 建立銷售金額預測模型

# Python 2-32位元繪製決策樹
"""
# 安裝32位元-Anaconda
1 Download and install "Anaconda-2.0.1-Windows-x86.exe"
  刪除 C:\Anaconda\Lib\site-packages\sklearn\utils\sparsefuncs.pyd

# 安裝32位元-scikit-learn(如果在上一個步驟已安裝Anaconda則省略)
2 Download and install "scikit-learn-0.15.2.win32-py2.7.exe"

3 Graphviz - http://www.graphviz.org/
  安裝 graphviz-2.38.msi
  加入 PATH: C:\Program Files (x86)\Graphviz2.38\bin

4 pyparsing - http://sourceforge.net/projects/pyparsing/
  https://sourceforge.net/projects/pyparsing/files/pyparsing/pyparsing-2.1.8/
  安裝 pyparsing-2.1.8.win32-py2.6.exe

5 安裝 pydot
  此連結有問題  https://github.com/nlhepler/pydot

  開啟 dot_patser.py
  第28行 刪除 "_noncomma"

  第30行 新增以下程式碼
  _noncomma = "".join( [ c for c in printables if c != "," ] )

  安裝 pydot 模組並切換至 pydot 目錄
  python setup.py install
"""
# end
