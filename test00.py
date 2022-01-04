#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test00.py
# 循环

import time

def for01():
    # for循环
    for letter in 'Python':     # 第一个实例
        print('当前字母 :', letter)  # 遍历字符串中每个字符

    fruits = ['banana', 'apple',  'mango', "香蕉", "梨子"]
    for fruit in fruits:        # 第二个实例
        print('当前水果 :', fruit)
    print("Good bye!")

def for02():
    # 通过序列索引迭代
    fruits = ['banana', 'apple',  'mango']
    for index in range(len(fruits)):
        print('当前水果 :', index, fruits[index])

    print("Good bye!")

def for03():
    # 循环使用 else 语句
    for num in range(10,20):  # 迭代 10 到 20 之间的数字
        for i in range(2,num): # 根据因子迭代
            if num%i == 0:      # 确定第一个因子
                j=num/i          # 计算第二个因子
                print('%d 等于 %d * %d' % (num,i,j))
                break            # 跳出当前循环
        else:                  # 循环的 else 部分
            print(num, '是一个质数')

def for04():
    # for 循环嵌套语法：
    i=1
    j=1
    for a in range(i,10):
        print("a:",a)
        for b in range(j,10):
            print("b",b)


def for05():
    # while 循环嵌套语法：
    i = 2
    while(i < 100):
        j = 2
        while(j <= (i/j)):
            if not(i%j): break
            j = j + 1
        if (j > i/j) : print(i, " 是素数")
        i = i + 1
    
    print("Good bye!")


def for06():
    # break 语句
    s="PYTHON"
    for Z in s:
        if Z=="o":
            break
        print("Z",Z)

def for07():
    for letter in 'Python':     # 第一个实例
        if letter == 'h':
            break
        print('当前字母 :', letter)# 只会打印Pyt
  
def for08():
    var = 10                    # 第二个实例
    while var > 0:              
        print('当前变量值 :', var)
        var = var -1
        if var == 5:   # 当变量 var 等于 5 时退出循环
            break
    
    print("done")

def for09():
    # continue 语句
    s="python"
    for z in s:
        if z=="o":
            continue
        print("z",z)

def for010():
    # pass
    # 输出 Python 的每个字母
    for letter in 'Python':
    if letter == 'h':
        pass
        print('这是 pass 块')
    print('当前字母 :', letter)
 
 def for011():
    # 等待
    num=10
    for i in range(0,10):
        time.sleep(1)
        print("等待了",i,"秒")
