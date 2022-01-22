#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test32-module.py
# Python 模块
# https://www.runoob.com/python3/python3-module.html
import sys
import pytest
import support;

'''
  当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。
  搜索路径是一个解释器会先进行搜索的所有目录的列表。
  如想要导入模块 support，需要把命令放在脚本的顶端
'''


@pytest.mark.test
def test_import01():
  support.print_func("Runoob") # support.py Hello :  Runoob


'''
  一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行。

  当我们使用import语句的时候，Python解释器是怎样找到对应的文件的呢？

  这就涉及到Python的搜索路径，搜索路径是由一系列目录名组成的，Python解释器就依次从这些目录中去寻找所引入的模块。

  这看起来很像环境变量，事实上，也可以通过定义环境变量的方式来确定搜索路径。

  搜索路径是在Python编译或安装的时候确定的，安装新的库应该也会修改。搜索路径被存储在sys模块中的path变量，做一个简单的实验，在交互式解释器中，输入以下代码：
'''
@pytest.mark.test
def test_import02():
  print(sys.path)
  
  '''
  sys.path 输出是一个列表，其中第一项是空串''，代表当前目录（若是从一个脚本中打印出来的话，可以更清楚地看出是哪个目录），亦即我们执行python解释器的目录（对于脚本的话就是运行的脚本所在的目录）。

  因此若像我一样在当前目录下存在与要引入模块同名的文件，就会把要引入的模块屏蔽掉。

  了解了搜索路径的概念，就可以在脚本中修改sys.path来引入一些不在搜索路径中的模块。

  现在，在解释器的当前目录或者 sys.path 中的一个目录里面来创建一个fibo.py的文件，代码如下：
  '''
  
  # 斐波那契(fibonacci)数列模块
 
def fib(n):    # 定义到 n 的斐波那契数列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()
 
def fib2(n): # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
  
# 然后进入Python解释器，使用命令import fibo导入这个模块 


'''
  from … import 语句
  Python 的 from 语句让你从模块中[导入一个指定的部分]到当前命名空间中，语法如下：
  from 模块名称 import name1[, name2[, ... nameN]]
  这个声明不会把整个fibo模块导入到当前的命名空间中，它只会将fibo里的fib函数引入进来。
'''

'''
  例如，要导入模块 fibo 的 fib 函数，使用如下语句：
>>> from fibo import fib, fib2
>>> fib(500)
1 1 2 3 5 8 13 21 34 55 89 144 233 377  
'''

'''
  from … import * 语句
  把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
  from 模块名称 import *
  这提供了一个简单的方法来导入一个模块中的所有项目。然而[这种声明不该被过多地使用]。
'''