#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test-file.py
# 读写txt文件
# https://www.runoob.com/python3/python3-file-methods.html

'''
 f.read() 不用with
 读取文本文件
'''
import pytest;

@pytest.mark.test
def test_txtRead():
    try:
        f=open("./file/demo01.txt","r")# 打开文件
        print('''txtRead():'''+f.read()) # 读取文件
    except Exception as e:
        print(e)
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
    except Exception as e:
        print(e)


'''
    f.readlines()
    一次读取多行另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list
'''
@pytest.mark.test
def test_txtReadWithReadlines():
    try:
        with open("./file/demo01.txt","r") as f:
            # 判断f.readlines()数据类型 
            print("type(f.readlines())",type(f.readlines()))# <class 'list'>
            # 遍历list
            for line in f.readlines():
                print('''txtReadWithReadlines():'''+line.strip()) # 把末尾的'\n'删掉  
    except Exception as e:
        # 文件操作，出现异常时执行
        print(e)
    finally:
        # 总会执行
        if f:
            print("f.close()") # 用了with可以不用f.close()
        else:
            print("出错了");



'''
 f.write()
 写入文本文件
'''
@pytest.mark.test
def test_txtWrite():
    try:
        with open('./file/demo02.txt', 'w') as f:
            
            f.write('Hello, world!\n')
            
    except FileNotFoundError:
        print("出错了:",FileNotFoundError)
    finally:
        pass
        # f.close() # 使用with as 就不用再执行f.close
'''
    追加的方式打开文件，如果文件存在则在尾部进行追加输入
    a 追加方式
    a+ 读写的模式追加
'''

@pytest.mark.test
def test_textAddpen():
    try:
        with open("./file/text.txt","a+") as fw: # 既要读
            fw.write("测试写入\n")
        with open("./file/text.txt","r+") as fr: # 又要写
            result1=fr.read()
            print(type(result1))# <class 'str'>
            print("内容是",result1)
        with open("./file/text.txt","r+") as fr: # 又要写
            result2=fr.readline()
            print(type(result2))# <class 'str'>
            print("内容是",result2)
        with open("./file/text.txt","r+") as fr: # 又要写
            result3=fr.readlines()
            print(type(result3))# <class 'list'>
            print("内容是",result3)
        # 一个open操作只能打开一个文件，不能同时f.read()和f.readlines()和f.readline()
    except FileNotFoundError:
         print("出错了:",FileNotFoundError)
         
@pytest.mark.test
def test_file_tell():
    try:
        with  open("./file/demo01.txt","r+") as f:  
            print("f.tell()",f.tell())  # 0
    except FileNotFoundError:
            print("出错了:",FileNotFoundError) 
            
'''
    seek() 方法用于移动文件读取指针到指定位置。 
    参数
    offset -- 开始的偏移量，也就是代表需要移动偏移的字节数，如果是负数表示从倒数第几位开始。

    whence：可选，默认值为 0。给 offset 定义一个参数，表示要从哪个位置开始偏移；0 代表从文件开头开始算起，1 代表从当前位置开始算起，2 代表从文件末尾算起。

    返回值
    如果操作成功，则返回新的文件位置，如果操作失败，则函数返回 -1。
'''
@pytest.mark.test
def test_seek():
        pass
        # f.seek(5)      # 移动到文件的第六个字节
        # 5
        # f.read(1)
        # b'5'
        # f.seek(-3, 2)  # 移动到文件倒数第三个字节
        
        
'''
    命令行执行：
    pytest -v -run=test_textAddpen test_file_pytest.py
    
    失败重试：
    pytest test_file_pytest.py --reruns 2
    --reruns x 即失败重试x次
    --reruns-delay 重试间隔时间
'''