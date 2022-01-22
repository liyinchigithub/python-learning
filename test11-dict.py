#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test11.py
# Python 字典
# https://www.runoob.com/python3/python3-dictionary.html

'''
字典是另一种可变容器模型，且可存储任意类型对象。

字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,格式如下所示：

d = {key1 : value1, key2 : value2, key3 : value3 }
'''

def dict():
   # 字典
   dict = {}
   dict['one'] = "This is one" # 放入字典中 {'one':"This is one"}
   dict[2] = "This is two" # 放入字典中 {'one':"This is one",2:"This is two"}
   tinydict = {'name': 'runoob','code':6734, 'dept': 'sales'}
   print(dict['one'])          # 输出键为'one' 的值 输出:This is one
   print(dict[2])              # 输出键为 2 的值 输出:"This is two"
   print(tinydict)             # 输出完整的字典 输出：{'name': 'runoob','code':6734, 'dept': 'sales'}
   print(tinydict.keys())      # 输出所有键 输出：dict_keys(['name', 'code', 'dept'])
   print(tinydict.values())    # 输出所有值 输出：dict_values(['runoob', 6734, 'sales'])

# dict()

'''
创建空字典
使用大括号 { } 创建空字典：
'''
def createDict():
   # 使用大括号 {} 来创建空字典
   emptyDict = {}
   
   # 打印字典
   print(emptyDict) # 输出：{}
   
   # 查看字典的数量
   print("Length:", len(emptyDict)) # 输出：Length: 0
   
   # 查看类型
   print(type(emptyDict)) # 输出：<class 'dict'>
   
# createDict()

'''
重建字典
'''
def reCreateDict():
   emptyDict = dict()
   # 打印字典
   print(emptyDict)
   # 查看字典的数量
   print("Length:",len(emptyDict))
   # 查看类型
   print(type(emptyDict))
   
# reCreateDict()

'''
访问字典里的值
把相应的键放入到方括号中
如果用字典里没有的键访问数据，会输出错误
'''
def visitDict():
   tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
   
   print ("tinydict['Name']: ", tinydict['Name'])
   print ("tinydict['Age']: ", tinydict['Age'])
   
# visitDict()


'''
修改字典
向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值
'''

def updateDict():
   tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
   tinydict['Age'] = 8               # 更新 Age
   tinydict['School'] = "菜鸟教程"  # 添加信息
   
   
   print ("tinydict['Age']: ", tinydict['Age']) # 输出：tinydict['Age']:  8
   print ("tinydict['School']: ", tinydict['School']) # 输出：tinydict['School']:  菜鸟教程
# updateDict()

'''
删除字典元素
能删单一的元素也能清空字典，清空只需一项操作。

显示删除一个字典用del命令
'''


def delDict():
   tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
   del tinydict['Name'] # 删除键 'Name'
   
   # tinydict.clear()     # 清空字典
   # del tinydict         # 删除字典
   
   print ("tinydict['Age']: ", tinydict['Age'])
   # print ("tinydict['School']: ", tinydict['School']) # 如果删除一个不存在的字典汇报异常

delDict()
   
'''
字典键的特性
字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。

两个重要的点需要记住：

1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
'''


'''
Python字典包含了以下内置方法：

序号	函数及描述
1	   radiansdict.clear()                  删除字典内所有元素
2	   radiansdict.copy()                     返回一个字典的浅复制
3	   radiansdict.fromkeys()              创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
4	   radiansdict.get(key, default=None)  返回指定键的值，如果键不在字典中返回 default 设置的默认值
5	   key in dict                         如果键在字典dict里返回true，否则返回false
6  	radiansdict.items()              以列表返回一个视图对象
7  	radiansdict.keys()               返回一个视图对象
8  	radiansdict.setdefault(key, default=None)       和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
9  	radiansdict.update(dict2)        把字典dict2的键/值对更新到dict里
10	   radiansdict.values()       返回一个视图对象
11	   pop(key[,default])         删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
12	   popitem()                     随机返回并删除字典中的最后一对键和值。
'''