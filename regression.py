# -*- coding: utf-8 -*-
"""
title : regression model with scikit-learn in Python
date  : 2016.12.02,09
author: Ming-Chang Lee
email : alan9956@gmail.com
RWEPA : http://rwepa.blogspot.tw/
"""

#步驟 1：商業了解
#步驟 2：資料了解
#步驟 3：資料準備 (!)
#步驟 4：模式建立
#步驟 5：評估與測試
#步驟 6：佈署

# 檢視 scikit-learn 版本
import sklearn
print("The scikit-learn version is", format(sklearn.__version__))

# 匯入模組
import numpy as np

from sklearn.datasets import load_boston
boston = load_boston()

print(boston.data.shape) # (506, 13)

# ['CRIM' 'ZN' 'INDUS' 'CHAS' 'NOX' 'RM' 'AGE' 'DIS' 'RAD' 
#  'TAX' 'PTRATIO'  'B' 'LSTAT']
print(boston.feature_names)

print(np.max(boston.target), np.min(boston.target), np.mean(boston.target))

print(boston.DESCR)

print(boston.data[0]) # 顯示第1筆記錄
print(np.max(boston.data), np.min(boston.data), np.mean(boston.data))

from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.25, random_state=33)

# Normalize data
from sklearn.preprocessing import StandardScaler

scalerX = StandardScaler().fit(X_train)
scalery = StandardScaler().fit(y_train) # Warning
scalery = StandardScaler().fit(y_train.reshape(-1,1))

X_train = scalerX.transform(X_train)
y_train = scalery.transform(y_train.reshape(-1,1))
X_test = scalerX.transform(X_test)
y_test = scalery.transform(y_test.reshape(-1,1))

print(np.max(X_train), np.min(X_train), np.mean(X_train), np.max(y_train), np.min(y_train), np.mean(y_train))

# five-fold cross-validation and coefficient of determination
from sklearn.cross_validation import *
def train_and_evaluate(clf, X_train, y_train):
    
    clf.fit(X_train, y_train)
    
    print("Coefficient of determination on training set:", clf.score(X_train, y_train))
    
    # create a k-fold croos validation iterator of k=5 folds
    cv = KFold(X_train.shape[0], 5, shuffle=True, random_state=33)
    scores = cross_val_score(clf, X_train, y_train, cv=cv)
    print("Average coefficient of determination using 5-fold crossvalidation:",np.mean(scores))
    
# linear model
from sklearn import linear_model
clf_sgd = linear_model.SGDRegressor(loss='squared_loss', penalty=None,  random_state=42)

train_and_evaluate(clf_sgd, X_train, y_train)

print(clf_sgd.coef_)

# penalty with L2 norm (the squared sums of the coefficients)
clf_sgd1 = linear_model.SGDRegressor(loss='squared_loss', penalty='l2',  random_state=42)
train_and_evaluate(clf_sgd1,X_train,y_train)
#end