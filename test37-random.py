#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test37-random.py
# Python 随机数
# https://www.runoob.com/python3/python3-random-number.html
import sys
import pytest
import random # 导入 random(随机数) 模块

'''
    [生成 0 ~ 9 之间的随机数]
'''
@pytest.mark.test
def test_random01():
    i=random.randint(0,9)
    print("生成 0 ~ 9 之间的随机数:".format(i))


'''
    [固定选项中，随机选择一个]
'''
@pytest.mark.test
def test_random02():
    i=random.choice(['apple', 'pear', 'banana'])
    print("既定选项中，随机选择一个:".format(i))


'''
    [随机小数]
'''
@pytest.mark.test
def test_random03():
    i=random.random()    # random float
    print("随机小数:{}".format(i))# 输出 0.17970987693706186
    
'''
    [随机不重复 X个数]
'''
@pytest.mark.test
def test_random04():
    # 第一个参数：指定范围
    # 第二个参数：随机数个数
    i=random.sample(range(100), 10)   # sampling without replacement
    print("随机不重复:{}".format(i))# 输出 [30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
    
'''
   随机范围整数
'''
@pytest.mark.test
def test_random05():
    i=random.randrange(6)    # random integer chosen from range(6)
    print(i) # 输出 2
