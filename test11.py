#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test11.py
# Python 字典
# https://www.runoob.com/python3/python3-dictionary.html



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

