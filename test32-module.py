#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test33-import.py
# Python 导入模块
# https://www.runoob.com/python3/python3-module.html
import sys
import pytest

'''
  [模块]
  是一个包含所有你定义的函数和变量的文件，其后缀名是.py 一个python文件就是一个模块。
  模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。
  下面是一个使用 python 标准库中模块的例子。
'''


@pytest.mark.test
@pytest.mark.parametrize("argv",["参数1","参数2","参数3"])
def test_module01(argv):
# 文件名: using_sys.py
   print('命令行参数如下:')
   print(argv)
   print('\n\nPython 路径为：', sys.path, '\n')

'''
   1、import sys 引入 python 标准库中的 sys.py 模块；这是[引入某一模块]的方法。
   2、sys.argv 是一个包含[命令行参数的列表]。
   3、sys.path 包含了一个 Python 解释器自动查找[所需模块的路径的列表]。
'''