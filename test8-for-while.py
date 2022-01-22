#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test00.py
# for、while 循环
# https://www.runoob.com/python3/python3-loop.html

import time

    # for循环
def for01():
    # 遍历字符串
    for letter in 'Python':     # 第一个实例
        print('当前字母 :', letter)  # 遍历字符串中每个字符

    # 遍历列表
    fruits = ['banana', 'apple',  'mango', "香蕉", "梨子"]
    for fruit in fruits:        # 第二个实例
        print('当前水果 :', fruit)
    print("Good bye!")# 遍历完成后执行该语句
    
# for01()

def for02():
    # 通过序列索引迭代
    fruits = ['banana', 'apple',  'mango']
    for index in range(len(fruits)):# len(fruits) 列表size
        print('当前水果 :', index, fruits[index])# 列表[索引]获取列表索引值
    print("Good bye!")# 遍历完成后执行该语句
    
# for02()

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
# for03()

def for04():
    # for 循环嵌套语法：
    i=1
    j=1
    for a in range(i,10):# 1至10 外层执行每执行1次
        print("a:",a)
        for b in range(j,10):# 1至10 内层执行10次
            print("b",b)
# for04()

def for05():
    # while 循环嵌套语法：
    i = 2
    while(i < 100):# 2至99 外层执行每执行1次
        j = 2
        while(j <= (i/j)):
            if not(i%j): break #
            j = j + 1
        if (j > i/j) : print(i, " 是素数")
        i = i + 1
    
    print("Good bye!")

# for05()

def for06():
    # break 语句 跳出所有循环，不再继续循环
    s="PYTHON"
    for Z in s:
        if Z=="o":# 区分大小写，因此不会执行到break
            break
        print("Z",Z)

# for06()

def for07():
    for letter in 'Python':     # 第一个实例
        if letter == 'h':
            break
        print('当前字母 :', letter)# 只会打印Pyt
# for07()
  
def for08():
    # break
    var = 10                    # 第二个实例
    while var > 0:              
        print('当前变量值 :', var)
        var = var -1# 自减 var=-1
        if var == 5:   # 当变量 var 等于 5 时退出循环
            break
    print("done")
# for08()

def for09():
    # continue 跳出本次循环，执行下一次循环
    s="python"
    for z in s: # 值得注意的是z并未初始化某个值
        if z=="o":# if 块
            continue# if 块
        print("z",z)# 非if块，但在for内
    print('所有循环执行完毕')# 非if块，在for外
# for09()

def for010():
    # pass
    # 输出 Python 的每个字母
    for letter in 'Python':
        if letter == 'h':   # if 块
            pass            # if 块
            print('这是 pass 块')# if 块
        print('当前字母 :', letter)# 非if块，但在for内
    print('所有循环执行完毕')# 非if块，在for外
# for010()
 
def for011():
    # 等待
    num=10
    for i in range(0,num):
        time.sleep(1) # import time 库
        print("等待了",i,"秒")
# for011()
