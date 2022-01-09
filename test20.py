#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test20.py
# Python 日期和时间
# https://www.runoob.com/python3/python3-date-time.html

'''
Python 程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能。

Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。

时间间隔是以秒为单位的浮点小数。

每个时间戳都以自从 1970 年 1 月 1 日午夜（历元）经过了多长时间来表示。

Python 的 time 模块下有很多函数可以转换常见日期格式。如函数 time.time() 用于获取当前时间戳
'''


#!/usr/bin/python3

import time  # 引入time模块
import datetime

ticks = time.time()
print ("当前时间戳为:", ticks)
