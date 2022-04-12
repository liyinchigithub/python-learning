#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test25-str-format.py
# Python 格式化输出
# 
import sys
import pytest;

'''
    大括号和format中参数，形成映射关系
'''
@pytest.mark.test
def test_str_format():
    a=1
    b=2
    c=3
    print("a为{} b为{} c为{}".format(a,b,c)) #  输出:a为1 b为2 c为3
    
# 赋值方式
@pytest.mark.test
def test_str_format02():
    print("c为{c} a为{} b为{}".format(1,2,c=3)) # 输出:c为3 a为1 b为2


# 索引映射
@pytest.mark.test
def test_str_format03():
    print("{0}+{1}={2:>2}".format(1,2,1+2));# 输出 1+2= 3 注意：3前面有2个单位的空格
    # :2 表示索引2的值（即1+2的结果）向右对齐2个单位

# f
@pytest.mark.test
def test_f_format():
    a=1000
    print(f"a为{a}") # 输出:a为1000


'''
    pytest test25-str-format.py
'''