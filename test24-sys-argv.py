#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test24-sys.py
# Python 命令行参数
# https://note.youdao.com/s/M0A8ft8x
# https://www.runoob.com/python3/python3-command-line-arguments.html
import sys
import pytest;

'''
    Python 提供了4中获取命令行参数的模块，来获取命令行参数。
    （1）
    $ python test.py arg1 arg2 arg3
    
    Python 中也可以使用 sys 的 sys.argv 来获取命令行参数：

    sys.argv 是命令行参数列表。

    len(sys.argv) 是命令行参数个数。

    注：sys.argv[0] 表示脚本名。
'''
@pytest.mark.skip
def test_argv():
    print('文件名为{}，第一个参数{}，第二个参数{}，第三个参数{}'.format(sys.argv[0],sys.argv[1],sys.argv[2],sys.argv[3]))
    print(f"{sys.argv[0]},{sys.argv[1]},{sys.argv[2]},{sys.argv[3]}")
# test_argv()

'''
    命令行执行:python -s test24-sys-argv.py a b c
'''
@pytest.mark.test
def test_ptest_argv(cmdopt):
    print('文件名为{}，第一个参数{}，第二个参数{}，第三个参数{}'.format(cmdopt[0],cmdopt[1],cmdopt[2],cmdopt[3]))

'''
    命令行执行:pytest test24-sys-argv.py a b c  
'''


# pytest 获取命令行参数
# https://www.cnblogs.com/yoyoketang/p/9457473.html






