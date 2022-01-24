#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test20.py
# Python 日期和时间
# https://www.runoob.com/python3/python3-date-time.html 

import time  # 引入time模块
import datetime
import calendar
import pytest


'''
Python 程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能。

Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。

时间间隔是以秒为单位的浮点小数。

每个时间戳都以自从 1970 年 1 月 1 日午夜（历元）经过了多长时间来表示。

Python 的 time 模块下有很多函数可以转换常见日期格式。如函数 time.time() 用于获取当前时间戳
'''


'''
    [时间戳]
'''
@pytest.mark.test
def test_datatime():
    ticks = time.time()
    print ("当前时间戳为:", ticks)  

'''
    [获取年-月-日 时:分:秒]
'''
@pytest.mark.test
def test_get_year_month_day_hours_mi():
    print()


'''
    [获取当前时间]
    从返回浮点数的时间戳方式向时间元组转换，只要将浮点数传递给如localtime之类的函数。
'''

@pytest.mark.test
def test_localtime():
    localtime=time.localtime(time.time())
    print("test_localtime:{}".format(localtime))
    # 输出:time.struct_time(tm_year=2022, tm_mon=1, tm_mday=24, tm_hour=11, tm_min=11, tm_sec=6, tm_wday=0, tm_yday=24, tm_isdst=0)
    print("test_localtime:{}".format(localtime.tm_year))# 获取 年
    print("test_localtime:{}".format(localtime.tm_mon))# 获取 月
    print("test_localtime:{}".format(localtime.tm_mday))# 获取 日
    print("test_localtime:{}".format(localtime.tm_hour))# 获取 时
    print("test_localtime:{}".format(localtime.tm_min))# 获取 分
    print("test_localtime:{}".format(localtime.tm_sec))# 获取 秒
    t="{}-{}-{} {}:{}:{}".format(localtime.tm_year,localtime.tm_mon,localtime.tm_mday,localtime.tm_hour,localtime.tm_min,localtime.tm_sec)
    print("现在是:{}".format(t)) # 输出:现在是:2022-1-24 11:16:15  注意：这边数据类型字符串


'''
    [获取格式化的时间]
    你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():
'''

@pytest.mark.test
def test_format_localtime():
    localtime = time.asctime( time.localtime(time.time()) ) # asctime
    print ("test_format_localtime 本地时间为 :", localtime) 
    # 输出:本地时间为 : Mon Jan 24 11:17:58 2022
    
'''
    [格式化日期]
    我们可以使用 time 模块的 [strftime] 方法来格式化日期
'''

@pytest.mark.test
def test_format_time():
    # 格式化成2016-03-20 11:45:39形式
    print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))# 输出:2022-01-24 11:19:47

    # 格式化成Sat Mar 28 22:24:24 2016形式
    print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))# 输出:Mon Jan 24 11:19:47 2022
    
    # 将格式字符串转换为时间戳
    a = "Sat Mar 28 22:24:24 2016"
    print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))) # 输出:1459175064.0

'''
    python中时间日期格式化符号：
    
        %y 两位数的年份表示（00-99）
        %Y 四位数的年份表示（000-9999）
        %m 月份（01-12）
        %d 月内中的一天（0-31）
        %H 24小时制小时数（0-23）
        %I 12小时制小时数（01-12）
        %M 分钟数（00=59）
        %S 秒（00-59）
        %a 本地简化星期名称
        %A 本地完整星期名称
        %b 本地简化的月份名称
        %B 本地完整的月份名称
        %c 本地相应的日期表示和时间表示
        %j 年内的一天（001-366）
        %p 本地A.M.或P.M.的等价符
        %U 一年中的星期数（00-53）星期天为星期的开始
        %w 星期（0-6），星期天为星期的开始
        %W 一年中的星期数（00-53）星期一为星期的开始
        %x 本地相应的日期表示
        %X 本地相应的时间表示
        %Z 当前时区的名称
        %% %号本身
'''


'''
    [获取某月日历]
'''
@pytest.mark.test
def test_calendar():
    cal = calendar.month(2022, 1)
    print ("以下输出2016年1月份的日历:")
    print ("test_calendar:{}".format(cal))
    
    '''
    以下输出2016年1月份的日历:
    test_calendar:    January 2022
    Mo Tu We Th Fr Sa Su
                    1  2
    3  4  5  6  7  8  9
    10 11 12 13 14 15 16
    17 18 19 20 21 22 23
    24 25 26 27 28 29 30
    31
    '''


if __name__=="__main__":
    pytest.main();