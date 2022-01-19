#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test26-str-strip.py
# Python 删除字符串头尾和尾部指定字符或字符序列
# 
import sys
import pytest;

'''
    
'''
@pytest.mark.test
def test_str_strip():
   str="+-*/ python3 -+/*"
   print(str.strip('+、-、*、/')) #  输出: python3  注意还会包含前后空格
    

'''
    pytest test26-str-strip.py
'''