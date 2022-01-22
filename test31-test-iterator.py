#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test31-test-iterator.py
# Python 迭代器与生成器
# https://www.runoob.com/python3/python3-iterator-generator.html
import sys
import pytest

'''
    迭代是Python最强大的功能之一，是[访问集合元素的一种方式]。

   迭代器是一个可以记住遍历的位置的对象。

   迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

   迭代器有两个基本的方法:[iter()] 和 [next()]。

   字符串，列表或元组对象都可用于创建迭代器：
'''


@pytest.mark.test
def test_iter01():
    list = [1, 2, 3, 4]
    it = iter(list)    # 创建迭代器对象
    print(next(it))  # 输出迭代器的下一个元素 1
    print(next(it))  # 输出迭代器的下一个元素 2
    print(next(it))  # 输出迭代器的下一个元素 3
    print(next(it))  # 输出迭代器的下一个元素 4

'''
   迭代器对象可以使用常规for语句进行遍历
'''
@pytest.mark.test
def test_iter02():
   list=[1,2,3,4]
   it = iter(list)    # 创建迭代器对象
   for x in it:
      print (x, end=" ") # 1 2 3 4
      
'''
   不使用迭代器
'''
@pytest.mark.test
def test_iter03():
   list=[1,2,3,4]
   for x in list:
      print (x, end=" ") # 1 2 3 4