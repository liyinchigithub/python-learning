#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test46-test-yield.py
# Python 生成器
# https://www.runoob.com/python3/python3-iterator-generator.html
import sys
import pytest

'''
   yield()
   [生成器]
   只要遇到yield() 函数就会马上暂停并且报错全部已经运行的信息。
   保存完后重新返回yield()的设定值，并且从下一个bext位置继续运行。
   
'''


def my_print(x):
   for i in range(x):
      # print(i)
      yield(i)


for j in my_print(10):
   print("j:{}".format(j))
'''
   输出：
      j:0
      j:1
      j:2
      j:3
      j:4
      j:5
      j:6
      j:7
      j:8
      j:9
'''