#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test18.py
# Python OS 文件/目录方法
# https://www.runoob.com/python3/python3-os-file-methods.html

import os;
import sys;
import stat;
import xlsxwriter;

'''
    os.access() 文件是否存在、可读写、可执行
    使用当前的uid/gid尝试访问路径。大部分操作使用有效的 uid/gid, 因此运行环境可以在 suid/sgid 环境尝试。
'''


def osAccess():
    result = os.access('./chromedriver', os.F_OK)  # 是否存在
    print("os.F_OK:", result)

    result = os.access('./chromedriver', os.R_OK)  # 是否可读
    print("os.R_OK:", result)

    result = os.access('./chromedriver', os.W_OK)  # 是否可写
    print("os.W_OK:", result)

    result = os.access('./chromedriver', os.X_OK)  # 是否可执行
    print("os.X_OK:", result)

# osAccess();


'''
    os.remove() 方法用于删除指定路径的文件。如果指定的路径是一个目录，将抛出OSError。
    在Unix, Windows中有效
'''


def removeFile():
    # 删除文件前，判断是否存在
    if(os.access('aa.txt', os.F_OK)):
        print("文件存在执行删除")
        os.remove("aa.txt")
        # 删除完成，判断是否存在
        if(os.access("aa.txt",os.F_OK)):
            print("文件失败成功");
        else:
            print("文件删除成功");
    else:
        print("文件不存在")
        
# removeFile()

'''
    os.listdir(os.getcwd()) 列出目录
'''
def dirFiles():
    print ("目录为: %s" %os.listdir(os.getcwd()))# 输出：['test19.py', 'favicon.ico', 'test-client-http-request.py', 'requirements.txt', 'test-pytesseract.py', 'test-client-http-urllib.py', 'test17.py', 'test.csv', 'test13.py', 'test-csv.py', 'test1.py', 'test12.py', 'tutorial-env', 'test-mongodb.py', 'test16.py', '.history', 'test2.py', 'test-class-object.py', 'README.md', 'test11.py', 'test-client-http-requests.py', 'test6.py', 'test15.py', 'test.xlsx', '.gitignore', 'test7.py', 'test20.py', 'test14.py', 'test-server-http.py', 'test3.py', 'test10.py', 'test-file.py', 'test8.py', 'chromedriver', '.git', 'test-selenium.py', 'test-server-socket.py', 'test-mysql.py', 'demo01.txt', 'coverage', 'demo02.txt', 'test18-os.py', 'test9.py']

# dirFiles()


'''
    os.rmdir(path) 删除空目录
    方法用于删除指定路径的目录。仅当这文件夹是空的才可以, 否则, 抛出OSError。
'''

def removeEmpty(path):
    try:
        os.rmdir(path); # 目录必须是空的
    except OSError:
        print("出错了，非空目录")
# removeEmpty("chromedriver")

'''
    os.removedirs() 递归删除目录。
    像rmdir(), 如果子文件夹成功删除, removedirs()才尝试它们的父文件夹,直到抛出一个error(它基本上被忽略,因为它一般意味着你文件夹不为空)。
    https://www.runoob.com/python3/python3-os-removedirs.html
'''

def removeDirs(path):
    try:
        os.removedirs(path); # 目录必须是空的
    except OSError:
        print("出错了")
# removeDirs("/a")

'''
    os.unlink() 删除文件
    如果文件是一个目录则返回一个错误。
    https://www.runoob.com/python3/python3-os-unlink.html
'''

def unlink(path):
    try:
        os.unlink(path); # 目录必须是空的
        # 删除后的目录
        print ("删除后的目录为 : %s" %os.listdir(os.getcwd()))
        dir=os.listdir(os.getcwd())
        type(dir)
        if(path in dir):
            print("还存在")
        else:
            print(path+"已经不存在")
        # 创建文件夹
        os.mkdir("aaa.txt")    
    except OSError:
        print("出错了")
# unlink("aaa.txt")


'''
    os.mkdir()用于以数字权限模式创建目录。
    默认的模式为 0777 (八进制)。
    如果目录有多级，则创建最后一级，如果最后一级目录的上级目录有不存在的，则会抛出一个 OSError。
'''

'''
    创建文件
'''
def createFile(fileName):
    
    file1 = open("./a/"+fileName + '.txt','w');# 指定路径下
    file2 = open(fileName + '.txt','w');
    file1.close()
    file2.close()
# createFile('text')

'''
    os.makedirs() 方法用于递归创建目录。
    如果子目录创建失败或者已经存在，会抛出一个 OSError 的异常，Windows上Error 183 即为目录已经存在的异常错误。
    如果第一个参数 path 只有一级，则 mkdir() 函数相同。
    https://www.runoob.com/python3/python3-os-makedirs.html
'''

def mkdir(path):
 
	folder = os.path.exists(path)
	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
		os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
		print("---  new folder...  ---")
		print("---  OK  ---")
	else:
		print("---  There is this folder!  ---")
		
file = "a/test/" # 要创建的文件夹路径
# mkdir(file) 


'''
    在指定文件夹中创建txt文件，并写入内容
'''


def txt(name,text):
    file = os.getcwd()[:-4] + 'new'
    if not os.path.exists(file):     # 判断当前路径是否存在，没有则创建new文件夹
        os.makedirs(file)
        xxoo = file + name + '.txt'    # 在当前py文件所在路径下的new文件中创建txt
        file = open(xxoo,'w')
        file.write(text)        # 写入内容信息
        file.close()
        print ('ok')
# txt('test','hello,python')       #创建名称为test的txt文件，内容为hello,python

'''
    创建Excel
'''
def createExcel():
 
    workbook = xlsxwriter.Workbook('test-1.xlsx')
            #在G盘xxoo文件下创建103的excel
    worksheet = workbook.add_worksheet('s001')
            #103的excel的sheet页名称为s001
    worksheet.write(0,0,123456)
    worksheet.write(2,1,664)
    worksheet.write(1,5,250)
            #写入信息
    workbook.close()
createExcel()

'''
    os.getcwd() 返回当前工作目录。
'''
    
def getDir():
    result=os.getcwd();
    print("os.getcwd():",result);

# getDir()

'''
    os.chmod() 更改文件或目录的权限。
    Unix 系统可用。
    https://www.runoob.com/python3/python3-os-chmod.html
'''

def chmod():
    # 假定 /tmp/foo.txt 文件存在，设置文件可以通过用户组执行
    os.chmod("/tmp/foo.txt", stat.S_IXGRP)
    # 设置文件可以被其他用户写入
    os.chmod("/tmp/foo.txt", stat.S_IWOTH)