#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test02.py
# 读写txt文件

'''
 f.read()
'''
def txtRead():
    try:
        f=open("./demo01.txt","r")
        print('''txtRead():'''+f.read())
    finally:
        if f:
            f.close
        else:
            print("出错了");
# 调用方法
txtRead()

'''
 f.read() with
'''
def txtReadWith():
    try:
        with open("./demo01.txt","r") as f:
            print('''txtReadWith():'''+f.read())
    finally:
        if f:
            f.close
        else:
            print("出错了");
# 调用方法
txtReadWith()

'''
 f.readlines()
 一次读取多行另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list
'''
def txtReadWithReadlines():
    try:
        with open("./demo01.txt","r") as f:
            for line in f.readlines():
                print('''txtReadWithReadlines():'''+line.strip()) # 把末尾的'\n'删掉  
    finally:
        if f:
            f.close
        else:
            print("出错了")
# 调用方法
txtReadWithReadlines()


'''
 f.write()
'''
def txtWrite():
    try:
        f = open('./demo02.txt', 'w')
        f.write('Hello, world!')
        f.close()
    finally:
        print("出错了")

txtWrite()