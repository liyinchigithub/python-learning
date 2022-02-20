#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名:test49_with.py
# https://www.runoob.com/python3/python-with.html

import pytest

'''
Python 中的 with 语句用于异常处理，封装了 try…except…finally 编码范式，提高了易用性。

with 语句使代码更清晰、更具可读性， 它简化了文件流等公共资源的管理。

在处理文件对象时使用 with 关键字是一种很好的做法。
'''
@pytest.mark.test
def test_with():
    with open('./file/test_runoob.txt', 'a+') as file:
        file.write('hello world !\n')
        file.write('hello world !\n')
        
    '''
    如果使用try...except...finally的写法，如下：
        file = open('./test_runoob.txt', 'w')
    try:
        file.write('hello world')
    finally:
        file.close()
    '''