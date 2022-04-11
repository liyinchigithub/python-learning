#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test0.py
# Python 列表
# https://www.runoob.com/python3/python3-list.html

'''
Python3 列表

序列是 Python 中最基本的数据结构。

序列中的每个值都有对应的位置值，称之为索引，第一个索引是 0，第二个索引是 1，依此类推。

Python 有 6 个序列的内置类型，但最常见的是列表和元组。

列表都可以进行的操作包括索引，切片，加，乘，检查成员。

此外，Python 已经内置确定序列的长度以及确定最大和最小的元素的方法。

列表是最常用的 Python 数据类型，它可以作为一个方括号内的逗号分隔值出现。

列表的数据项不需要具有相同的类型

创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：

list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
'''


'''
   [索引下标]
   https://www.runoob.com/python3/python3-list.html
'''
def listIndex():
   # 字符串
   str = 'Hello World!'
   li=['1','2','3','4','5','6','7'] # 列表
   print(str)           # 输出完整字符串 输出：Hello World!
   print(str[0])        # 输出字符串中的第一个字符 输出H
   print(str[2:5])      # 输出字符串中第三个至第六个(不含第六个)之间的字符串 输出：llo 
   print(str[2:])       # 输出从第三个字符开始的字符串到最后一个
   print(str*2)      # 输出字符串两次 输出：Hello World!Hello World!
   print(str+"TEST")  # 输出连接的字符串 输出：Hello World!TEST
   print(li[2:5:2])      # 输出字符串中第三个至第六个（不含第六个）之间的字符串,步长为2 输出：['3', '5']

# listIndex()

'''
[更新列表]
append()
'''
def updateList():
   list = ['Google', 'Runoob', 1997, 2000]
 
   print ("第三个元素为 : ", list[2])#  输出：第三个元素为 :  1997
   list[2] = 2001
   print ("更新后的第三个元素为 : ", list[2])# 输出：更新后的第三个元素为 :  2001
   
   list1 = ['Google', 'Runoob', 'Taobao']
   list1.append('Baidu')
   print ("更新后的列表 : ", list1) # 输出：更新后的列表 :  ['Google', 'Runoob', 'Taobao', 'Baidu']

# updateList()

'''
   删除列表值
   del 
'''
def delList():
   list = ['Google', 'Runoob', 1997, 2000]
   print ("原始列表 : ", list)# 输出：原始列表 :  ['Google', 'Runoob', 1997, 2000]
   del list[2]# 删除第三个元素
   print ("删除第三个元素 : ", list)# 输出：['Google', 'Runoob', 2000]
delList()


'''
   [合并列表值]
   +
   也可以用list1.extend(list2)
'''
def listMerge():
   # 列表
   list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
   tinylist = [123, 'john']
   print(list + tinylist)    # 打印组合的列表 输出：[ 'runoob', 786 , 2.23, 'john', 70.2, 123, 'john' ]

   # 列表去重后再合并
   list1=[1,2,3,4,5,6]
   list2=[3,4,5,6,7,8]
   print(list(set(list1)&set(list2))) # 输出：[3, 4, 5, 6]
# listMerge()


'''
   [列表截取与拼接]
'''
def test_():
   L=['Google', 'Runoob', 'Taobao']
   print(L[2])#  输出第三个元素
   print(L[-2])# 输出倒数第二个元素
   print(L[1:])# 输出从第二个元素开始的所有元素
   print(L[:2])# 输出前两个元素
   
   
'''
   [嵌套列表]
[['a', 'b', 'c'], [1, 2, 3]]

列表函数
序号	函数
1	   len(list)   列表元素个数
2	   max(list)   返回列表元素最大值
3	   min(list)   返回列表元素最小值
4	   list(seq)   将元组转换为列表

序号	方法
1	   list.append(obj)  在列表末尾添加新的对象
2	   list.count(obj)   统计某个元素在列表中出现的次数
3	   list.extend(seq)  在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表） 合并列表？？？ +号可以合并类表，合并列表并去重使用set()将2个列表转成集合在进行交集操作最后转回列表
4	   list.index(obj)   从列表中找出某个值第一个匹配项的索引位置  list1 = ['Google', 'Runoob', 'Taobao']  list1.index('Runoob') 返回1
5	   list.insert(index, obj) 将对象插入列表
6	   list.pop([index=-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	   list.remove(obj)     移除列表中某个值的第一个匹配项
8	   list.reverse()    反向列表中元素       list1 = ['Google', 'Runoob', 'Taobao', 'Baidu'] list1.reverse()   列表反转后:  ['Baidu', 'Taobao', 'Runoob', 'Google']
9	   list.sort( key=None, reverse=False) 对原列表进行排序  list.sort(reverse=True)
10	   list.clear()   清空列表
11	   list.copy()    复制列表
'''


