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
    # 使用 with 关键字系统会[自动调用] f.close() 方法， with 的作用等效于 try/finally 语句是一样的。
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
    以上代码我们对可能发生异常的代码处进行 try 捕获，
    发生异常时执行 except 代码块，finally 代码块是无论什么情况都会执行，所以文件会被关闭，不会因为执行异常而占用资源。
    '''