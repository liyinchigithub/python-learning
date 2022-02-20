#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名:test50_assert.py
# https://www.runoob.com/python3/python3-assert.html

import pytest
import sys
'''
Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
断言可以在条件不满足程序运行的情况下直接返回错误，而不必等待程序运行后出现崩溃的情况，例如：
我们的代码只能在 Linux 系统下运行，可以先判断当前系统是否符合条件。

语法格式如下：
    assert expression

等价于：
if not expression:
    raise AssertionError
    
assert 后面也可以紧跟参数:
assert expression [, arguments]

等价于：
if not expression:
    raise AssertionError(arguments)
'''
@pytest.mark.test
def test_assert():
    # 断言当前运行平台
    assert ('darwin' in sys.platform), "该代码只能在 Mac 下执行（Linux、Windows）"