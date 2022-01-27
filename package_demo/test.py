#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pytest # 引入单元测试库
from package_demo.module_a import compute1 # 引入自定义包、模块、类、函数、属性变量
from package_demo.module_b import compute2

@pytest.mark.test
def test_package_sum():
    print(compute1.compute(1,2).sum())# 输出 3
    
@pytest.mark.test
def test_package_structure():
    print(compute2.compute(1,2).structure())# 输出 -1
    
    
    
    
    
    
'''
    包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境。
    简单来说，包就是文件夹，但该文件夹下必须存在 __init__.py 文件, 该文件的内容可以为空。
    [__init__.py ]用于标识当前文件夹是一个包
'''


'''
    package_demo/               顶层包
      __init__.py               初始化 package_demo 包
      module_a/                  子包
              __init__.py           初始化 module_a 包
              wavread.py            子包中的模块（每个模块即每个py文件封装对应功能的函数、属性）
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      module_B/                  子包
              __init__.py           初始化 module_a 包
              echo.py               子包中的模块（每个模块即每个py文件封装对应功能的函数、属性）
              surround.py
              reverse.py
              ...
'''