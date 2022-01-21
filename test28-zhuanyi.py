#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test28-zhuanyi.py
# Python 转义符
# 
import sys
import pytest;

'''
    \n 换行
'''
@pytest.mark.test
def test_n():
   print("这是一个\n转义符")# 输出：这是一个 换行 转义符
'''
   \r 回车
'''
@pytest.mark.test
def test_r():
   print("这是一个\r转义符") # 输出：这是一个\转义符

'''
   \\ 反斜杠
'''
@pytest.mark.test
def test_():
   print("这是一个\\转义符") # 输出：这是一个\转义符
   
'''
   \b 退格
'''
@pytest.mark.test
def test_b():
   print("这是一个\b转义符") # 输出：这是一个 转义符

'''
   \000 空行
'''
@pytest.mark.test
def test_000():
   print("这是一个\000转义符") # 输出：这是一个转义符
   
'''
   \a
'''
@pytest.mark.test
def test_a():
   print("这是一个\a 转义符") # 输出：这是一个 转义符

'''
   \'
'''
@pytest.mark.test
def test_danyinhao():
   print("这是一个\' 转义符") # 输出：这是一个' 转义符
   
'''
   \"
'''
@pytest.mark.test
def test_shuangyinhao():
   print("这是一个\" 转义符") # 输出：这是一个" 转义符