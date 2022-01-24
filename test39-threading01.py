#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# test39-threading.py
# Python 多线程 threading
# https://www.runoob.com/python3/python3-multithreading.html
import pytest
import threading
import time
import datetime

'''
    Python3 线程中常用的两个模块为:_thread、threading(推荐使用)
    [_thread 提供了低级别的、原始的线程以及一个简单的锁，它相比于 threading 模块的功能还是比较有限的]
    threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法:
    
        threading.currentThread(): 返回当前的线程变量。
        threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
        threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
        除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:
        run():用以表示线程活动的方法。
        start():启动线程活动。
        join([time]):等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
        isAlive():返回线程是否活动的。
        getName():返回线程名。
        setName():设置线程名。
'''



'''
    [多线程]
'''
exitFlag = 0
# 封装一个类
class myThread (threading.Thread):
    # 构造函数
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)#  从threading.Thread 继承创建一个新的子类
        self.threadID = threadID
        self.name = name
        self.delay = delay
    # 自定义函数
    def run(self):
        print ("开始线程：" + self.name)
        print_time(self.name, self.delay, 5)# 调用外部定义的一个函数
        print ("退出线程：" + self.name)

# 定义一个函数
def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = myThread(1, "Thread-1", 1) # 构造函数，可以直接不实例化而直接使用类名入参
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join() # 等待至线程中止
thread2.join() # 等待至线程中止
print ("退出主线程")

