#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test31-test-iterator.py
# Python 迭代器与生成器
# https://www.runoob.com/python3/python3-iterator-generator.html
import sys
import pytest

'''
    迭代是Python最强大的功能之一，是[访问集合元素的一种方式]。

      迭代器是一个可以[记住遍历的位置]的对象。
      迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
      迭代器只能往前不会后退。
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
      
# for输出的是同行，而next输出的是同列      
      
      
'''
   不使用迭代器
'''
@pytest.mark.test
def test_iter03():
   list=[1,2,3,4]
   # for 遍历
   for x in list:
      print (x, end=" ") # 1 2 3 4
      
      
'''
   结束迭代器
'''
@pytest.mark.test
def test_stop_iter():
   l=[1,2,3,4,5] # 迭代器可迭代 元组、数组、字符串
   try:
      while True:
         it=iter(l)
         print(next(it))
   except IndentationError:
      sys.exit()
      
# 对类使用迭代器

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    x = self.a
    self.a += 1
    return x
'''
   把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
   如果你已经了解的面向对象编程，就知道类都有一个构造函数，Python 的构造函数为 __init__(), 它会在对象初始化的时候执行。
   
   __iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
   __next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。
'''

     
@pytest.mark.test
def test_class_iter():
# 创建一个返回数字的迭代器，初始值为 1，逐步递增 1：
   myclass = MyNumbers()
   myiter = iter(myclass)
   print(next(myiter))
   print(next(myiter))
   print(next(myiter))
   print(next(myiter))
   print(next(myiter))
   
'''
StopIteration
StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
'''

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
 
@pytest.mark.test
def test_stop_iter():
   myclass = MyNumbers()# 类实例化
   myiter = iter(myclass)# 对类进行迭代器
   
   for x in myiter:
      print(x)