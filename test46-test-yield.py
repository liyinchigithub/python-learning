#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test46-test-yield.py
# Python 生成器
# https://www.runoob.com/python3/python3-iterator-generator.html
import sys
import pytest

'''
   [生成器]
         只要遇到yield() 函数就会马上暂停并且报错全部已经运行的信息。
         保存完后重新返回yield()的设定值，并且从下一个bext位置继续运行。
         
         跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
         在调用生成器运行的过程中，每次遇到 yield 时函数会[暂停并保存当前所有的运行信息]，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
         调用一个生成器函数，返回的是一个迭代器对象。
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

# 使用 yield 实现斐波那契数列
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()