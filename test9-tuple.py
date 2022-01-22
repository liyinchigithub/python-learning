#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test9.py
# Python 元组
# https://www.runoob.com/python3/python3-tuple.html



'''
Python的元组与列表类似，不同之处在于“元组的元素不能修改”。
元组使用小括号 ( )，列表使用方括号 [ ]。
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
'''
def Tuple():
   # 元组
   tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
   tinytuple = (123, 'john')
   
   print(tuple)               # 输出完整元组 输出：('runoob', 786, 2.23, 'john', 70.2)
   print(tuple[0])            # 输出元组的第一个元素 输出：runoob
   print(tuple[1:3])          # 输出第二个至第四个（不包含）的元素 输出：(786, 2.23)
   print(tuple[2:])           # 输出从第三个开始至列表末尾的所有元素 输出：(2.23, 'john', 70.2)
   print(tinytuple * 2)       # 输出元组两次 输出：(123, 'john', 123, 'john')
   print(tuple + tinytuple)   # 打印组合的元组 输出：('runoob', 786, 2.23, 'john', 70.2, 123, 'john')

# Tuple()


def updateTuple():
   tup1 = (12, 34.56)
   tup2 = ('abc', 'xyz')
   
   # 以下修改元组元素操作是非法的。
   # tup1[0] = 100
   
   # 创建一个新的元组
   tup3 = tup1 + tup2
   print (tup3)
   
# updateTuple()

def delTuple():
   tup = ('Google', 'Runoob', 1997, 2000)
   print (tup)
   del tup
   print ("删除后的元组 tup : ")
   print (tup)

# delTuple() #以上实例元组被删除后，输出变量会有异常信息

'''
元组运算符
与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。

Python 表达式	                      结果	              描述
len((1, 2, 3))	                    3	                计算元素个数
(1, 2, 3) + (4, 5, 6)	   (1, 2, 3, 4, 5, 6)	      连接
('Hi!',) * 4	      ('Hi!', 'Hi!', 'Hi!', 'Hi!')	    复制
3 in (1, 2, 3)	                   True             	元素是否存在
for x in (1, 2, 3): print (x,)   	1 2 3	            迭代
'''
