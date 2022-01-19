#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test-file.py
# 读写txt文件
# https://www.runoob.com/python3/python3-file-methods.html

'''
 f.read()
 读取文本文件
'''
import pytest;

@pytest.mark.test
def test_txtRead():
    try:
        f=open("./file/demo01.txt","r")
        print('''txtRead():'''+f.read())
    finally:
        if f:
            f.close # 没有使用with as 则需要执行f.close()来关闭文件
        else:
            print("出错了");

# 调用方法
# txtRead()

'''
 f.read() with
 读取文本文件
'''
@pytest.mark.test
def test_txtReadWith():
    try:
        with open("./file/demo01.txt","r") as f:
            print('''txtReadWith():'''+f.read())
    finally:
        if f:
            f.close
        else:
            print("出错了");# 没有使用with as 则需要执行f.close()来关闭文件


'''
 f.readlines()
 一次读取多行另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list
'''
@pytest.mark.test
def test_txtReadWithReadlines():
    try:
        with open("./file/demo01.txt","r") as f:
            for line in f.readlines():
                print('''txtReadWithReadlines():'''+line.strip()) # 把末尾的'\n'删掉  
    finally:
        if f:
            f.close
        else:
            print("出错了")



'''
 f.write()
 写入文本文件
'''
@pytest.mark.test
def test_txtWrite():
    try:
        with open('./file/demo02.txt', 'w') as f:
            f.write('Hello, world!')
            # f.close() # 使用with as 就不用再执行f.close
    except FileNotFoundError:
        print("出错了:",FileNotFoundError)
'''
    追加的方式打开文件，如果文件存在则在尾部进行追加输入
    a 追加方式
    a+ 读写的模式追加
'''

@pytest.mark.test
def test_textAddpen():
    try:
        with open("./file/text.txt","a+") as fw: # 既要读
            fw.write("测试测试下，");
        with open("./file/text.txt","r+") as fr: # 又要写
            result=fr.read()
            print(type(result))
            print("内容是",result)
    except FileNotFoundError:
         print("出错了:",FileNotFoundError)