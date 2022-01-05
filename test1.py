#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test0.py
# Python3 基本数据类型
# https://www.runoob.com/python3/python3-data-type.html



'''
Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。

在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。

等号（=）用来给变量赋值。

等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：
'''
def dataType():
   counter = 100          # 整型变量
   miles   = 1000.0       # 浮点型变量
   name    = "runoob"     # 字符串

   print (counter)
   print (miles)
   print (name)

# dataType()

'''
[多个变量赋值]
Python允许你同时为多个变量赋值。例如：

a = b = c = 1
以上实例，创建一个整型对象，值为 1，从后向前赋值，三个变量被赋予相同的数值。

您也可以为多个对象指定多个变量。例如：

a, b, c = 1, 2, "runoob"
以上实例，两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c。
'''

def definitions():
   A = 100
   # 同时对多个变量赋值
   B, C, D = "liyinchi", 12, "泉州" 
   print(A)
   print(B)
   print(C)
   print(D)

# definitions()

def split():
   s='abcdefg'
   print('字符串abcdefg 截取s[1:5] 得到'+s[1:5])# 索引0开始，到5（不包含5） 输出：bcde   
# split()

def stringToNumber():
   # 数据类型转换
   str="1"
   print(int(str)+1);# 字符串转数值 输出2
# stringToNumber()

'''
[Python3 中有六个标准的数据类型]

Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
Python3 的六个标准数据类型中：

不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
'''



