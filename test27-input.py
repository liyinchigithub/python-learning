#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test27-input.py
# Python 提供的输入函数
# 
import sys
import pytest;

'''
    
'''
@pytest.mark.test
def test_input():
   value=input("请输入内容")
   print("你输入的内容是:{}".format(value))
   print("输入的内容数据类型是:",type(value))
'''
    
'''
@pytest.mark.skip
def test_raw_input():
   value=input("请输入内容") # Python3将raw_input和input进行整合成了input....去除了raw_input()函数
   print("你输入的内容是:{}".format(int(value)))
   print("输入的内容数据类型是:",type(value))
'''
    pytest test27-input.py
'''