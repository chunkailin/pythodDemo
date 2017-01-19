# _*_ coding: utf-8 _*_
# 程式 6-3.py (Python 3.x version)
# 計算單字在文章中出現的頻率
# 只列出出現超過一次以上的單字
import re

fp = open("demo\cklin.txt", "r")
article = fp.read()
new_article = re.sub("[^a-zA-Z\s]", "", article)
words = new_article.split()
word_counts = {}

for i in range(2,7,4):
    print(i)

def pick(x):
    fruits = ['Apple', 'Banana', 'Orange', 'Tomato', 'Pine Apple', 'Berry']
    return fruits[x]

alist = [1, 4, 2, 5, 0, 3, 4, 4, 2]
choices = map(pick, alist)
for choice in choices:
    print(choice)
    
for i in alist:
    print(pick(i))
    
age = input("what is your age?")
if age < 15:
    print("You are too young");
    
while True :
    try:
        age = int(input("What is your age?"))
        break
    except:
        print("Please input a number.")

if age < 15:
    print("You are too young");