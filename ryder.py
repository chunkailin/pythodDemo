# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 14:11:16 2016

@author: ryder
"""

#number1.py
import numpy as np
def divide(a,b):
    q=a/b
    r=a-q*b
    return q,r
    
def gcd(x,y):
    q=y
    while x > 0:
        q=x        
        x=y%x        
        y=g
        return g