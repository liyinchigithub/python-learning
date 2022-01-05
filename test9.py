#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test9.py
# Python 元组
# https://www.runoob.com/python3/python3-tuple.html



'''
   元组 
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

