# -*- coding: utf-8 -*-
"""
title : python - type, operations
date  : 2016.12.02,09
author: Ming-Chang Lee
email : alan9956@gmail.com
RWEPA : http://rwepa.blogspot.tw/
"""

# NumPy package
import numpy as np
a = np.array([0,1,2,3,4,5])
a
a.ndim   # 1
a.shape  # (6,)

# 建立副本, b之修改會影響a
b = a.reshape((3,2))
b
b.ndim   # 2
b.shape  # (3,2)

b[1][0] = 168
b
a # a物件已經更改, array([  0,   1, 168,   3,   4,   5])

c = a.reshape((3,2)).copy()
c
c[0][0] = -999
c
a # a物件沒有更改

# 向量化處理
a = np.array([0,1,2,3,4,5])

a*2

a**4 # 次方運算

# indexing

a[np.array([1,3,4])]

# 離群值調整
a > 10
a[a > 10]
a[a > 3]
a[a > 10] = 10
a

a.clip(0, 3)

# 處理 non-existing values
x = np.array([1, 2, 3, np.NAN, 4])
x
np.isnan(x)

x[~np.isnan(x)]

np.mean(x[~np.isnan(x)])

np.mean(x) # nan

# 計算時間
import timeit
normal_py_sec = timeit.timeit('sum(x*x for x in range(1000))', number=10000)
naive_np_sec = timeit.timeit('sum(na*na)', setup="import numpy as np; na=np.arange(1000)", number=10000)
good_np_sec = timeit.timeit('na.dot(na)', setup="import numpy as np; na=np.arange(1000)", number=10000)
print("Normal Python: %f sec"%normal_py_sec)
print("Naive NumPy: %f sec"%naive_np_sec)
print("Good NumPy: %f sec"%good_np_sec)

print "Hello World"    # python 2
print("Hello World")   # python 3

#==============================================================================
# Tuples 序列
#==============================================================================
f = (2,3,4,5) 			    # A tuple of integers
# g = (,) 				      # error code
g = ()
h = (2, [3,4], (10,11,12)) 	# A tuple containing mixed objects

# tuple operations
x = f[1] 		# Element access. x = 3
x

y = f[1:3] 	# Slices. y = (3,4)
y

z = h[1][1] 	# Nesting. z = 4
z

xy = (2, 3)
personal = ('Hannah',14,5*12+6)
singleton = ("hello",)

# Tuple Operations
("chapter",8) + ("strings","tuples","lists")

2*(3,"blind","mice")

# single format: tuple[index]
# index : 0  ~  len(tuple)-1
# index: -len(tuple)  ~  -1

f[0]
f[-1]
f[-2]
f[len(f)-1]

# slice format: tuple [start:end ]. Items from start to (end -1)
t=((1,2), (2,"Hi"), (3,"RWEPA"), 2+3j, 6E23)
t[2]
t[:3]
t[3:]
t[-1]
t[-3:]

# Tuple Comparison Operations
# standard comparisons ‘<’, ‘<=’, ‘>’, ‘>=’, ‘==’, ‘!=’, in, not in

#==============================================================================
# Lists 串列
#==============================================================================
#任意物件的串列
a = [2, 3, 4]            # A list of integer
b = [2, 7, 3.5, "Hello"] # A mixed list
c = []	                   # An empty list
d = [2, [a, b]]	          # A list containing a list
d[0]
d[1]
e = a + b			          # Join two lists

#串列的操作
x = a[1] 		   # Get 2nd element (0 is first)
y = b[1:3] 	   # Return a sub-list
z = d[1][0][2] # Nested lists
b[0] = 42 		 # Change an element

#==============================================================================
# Set 集合
#==============================================================================

# https://docs.python.org/3/tutorial/datastructures.html#sets
# 集合與字典相似, 但字典沒有key,只有值
a = set() 			# An empty set
type(a)

b = {"台北市", "新北市", "桃園市", "台中市", "台北市", "新北市", "高雄市"}
b # {'台中市', '台北市', '新北市', '桃園市', '高雄市'}

# 集合運算
x = {1,2,3,4,5}
y = {1,3,5,7}
x & y # {1, 3, 5}
x | y # {1, 2, 3, 4, 5, 7}
x ^ y # {2, 4, 7}

#==============================================================================
# Dictionaries 字典
#==============================================================================
a = {} 			# An empty dictionary
type(a)
b = { 'x': 3, "y": 4 }
c = { "uid": 168,
	   "login": "marvelous",
	   "name" : 'Alan Lee'
	 }

u = c["uid"] 		      # Get an element
c["shell"] = "/bin/sh" 	# Add an element
if c.has_key("directory"): 	# Check for presence of a member 適合 v2.x
	d = c["directory"]
else:
	d = None
 
if "directory" in c:   # v3.x 直接使用 in
    d = c["directory"]
else:
    d = None
    
if "uid" in c:   # v3.x 直接使用 in
    d = c["uid"]
else:
    d = None

d = c.get("directory", None) # Same thing, more compact

#==============================================================================
# 表示式(Expressions) & 變數(Variables) 
#==============================================================================
# expressions
3 + 5
3 + (5 * 4)
3 ** 2
"Hello" + "World"

# Variables
# 位移運算子: << 向左位移
# 位移運算子: >> 向右位移
a = 4 << 3 # 0100 --> 0100000, 64 32 16 8 4 2 0
b = a * 4.5
c = (a+b)/2.5
a = "Hello World"

# Loops
# 參考講義, 輸入 python code
for c in "Hello World":
    print (c)
#==============================================================================
# Functions
#==============================================================================
# Return the remainder of a/b
def remainder(a,b):
	q = a/b
	r = a - q*b
	return r

# Now use it
a = remainder(42,5) 		# a = 2

# Return two values
def divide(a,b):
	q = a/b
	r = a - q*b
	return q,r

x,y = divide(42,5) 		# x = 8, y = 2

#http://wiki.scipy.org/Tentative_NumPy_Tutorial
#end