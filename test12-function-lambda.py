#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test12-function-lambda.py
# Python 匿名函数
# 
import pytest
'''
    当我们不适用def语句定义函数，可以使用lambda来创建匿名函数
    有点像JavaScript中的箭头函数lambda
'''
sum=lambda arg1,arg2:arg1+arg2
print(sum(1,3)) # 输出:4

'''
    命令行执行: python test12-function-lambda.py
'''

