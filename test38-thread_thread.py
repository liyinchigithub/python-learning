#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# test38-thread_thread.py
# Python 多线程 _thread
# https://www.runoob.com/python3/python3-multithreading.html
import _thread
import time
import datetime

'''
    Python3 线程中常用的两个模块为:_thread、threading(推荐使用)
    thread 模块已被废弃!
    用户可以使用 threading 模块代替。
    所以，在 Python3 中不能再使用"thread" 模块。
    为了兼容性，Python3 将 thread 重命名为 "_thread"。
    [_thread 提供了低级别的、原始的线程以及一个简单的锁，它相比于 threading 模块的功能还是比较有限的]
    [threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法]
'''

'''
    Python中使用线程有两种方式:函数、用类来包装线程对象。
'''
'''
    [函数式]:调用 _thread 模块中的[start_new_thread()]函数来产生新线程。
    语法如下:_thread.start_new_thread ( function, args[, kwargs] )
    参数说明:
            function - 线程函数。
            args - 传递给线程函数的参数，他必须是个tuple类型。
            kwargs - 可选参数。
'''



'''
    [多线程-定义线程函数]
    
'''

def print_time(thread_name,delay=5):
    count=0
    while count<5:
        time.sleep(delay)
        print ("%s: %s" % ( thread_name, time.ctime(time.time()) ))
        count += 1
'''
    [多线程-启动线程]
    第1个参数:线程调用的函数
    第2个参数:入参，即线程调用函数函数自身的入参
'''      
try:
    _thread.start_new_thread(print_time,("线程1",1)) #  
    _thread.start_new_thread(print_time,("线程2",3))
except TypeError as e:
    print(e)
