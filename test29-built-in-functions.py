#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test298-built-in-functions.py
# Python 内置函数
# 
import sys
import pytest;
'''
    [字符串]
'''
@pytest.mark.test
def test_str():
   str='hello world!'
   print("这是一个\n转义符")# 输出：
   print("第一个字符大写:{}".format(str.capitalize())) # 字符串，是否[ 第一个字符大写]
   print("字符在指定范围内，出现：{}次".format(str.count('l',0,5)))# 统计字符[出现次数]
   print("字符串是否以！结尾：{}".format(str.endswith('!')))# 字符串是否以什么结尾
   print("字符串是否以！结尾：{}".format(str.endswith('!',0,5)))# 指定范围内，字符串是否[以什么结尾]
   print("编码:{}".format(str.encode()))# 编码
   print("解码:{}".format(str.encode().decode()))# 解码
   print("检查'll'是否包含在字符串str中：{}".format(str.find("ll")))# 输出 2
   print("检查是否包含字母和数字:{}".format(str.isalnum()))# 检查是否[同时包含字母和数字]，仅字符串无数字返回False
   print("检查是否由小写字母组成:{}".format(str.islower()))# 是否由[小写字母组成]
   print("检查是否由字母组成:{}".format(str.isalpha()))# 字符串中[是否由字母组成（含大小写）]，仅小写无大写返回False
   print("检查字符串中，是否有数字:{}".format(str.isdigit()))# 字符串中[是否有数字]，无数字返回False
   print("检查字符串中，是否全数字:{}".format(str.isnumeric()))# 字符串中[是否全数字]，非全数字返回False
   print("检查字符串中，是否由空格组成:{}".format(str.isspace()))# 字符串中[是否由空格组成]，非全数字返回False
   print("检查字符串中，是否标题化:{}".format(str.isspace()))# 字符串中[是否标题化（第一个字母大写后面都是小写）]，非标题化返回False
   print("连接符 {}".format(('-').join(('1','2','3','4','5'))))# 输出：连接符 1-2-3-4-5 连接符针对[元组]
   print("连接符 {}".format(('-').join(['1','2','3','4','5'])))# 输出：连接符 1-2-3-4-5 连接符针对[列表]
   print("连接符 {}".format(('-').join('liyinchi')))# 输出：连接符 l-i-y-i-n-c-h-i 连接符针对[字符串]
   print("字符串长度:{}".format(len(str)))# 字符串的长度 12
   print("元组长度:{}".format(len(('1','2','3','4','5'))))# 元组的长度 输出5
   print("列表长度:{}".format(len(['1','2','3','4','5'])))# 列表的长度 输出：5
   print("字符串中最大字母:{}".format(max(str)))# 字符串中最大字母 输出：w
   print("字符串中最小字母:{}".format(min(str)))# 字符串中最小字母
   print("替换字符串中的字符:{}".format(str.replace("w","W")))# 输出：替换字符串中的字符:hello World! 第三个参数可以指定不超过指定次数
   print("查找字符，从右到左:{}".format(str.rfind("w")))# 查找字符，从右到左 返回-1 即没有找到，返回非负数即找到 输出6
   print("查找字符，从右到左，在指定范围内查找:{}".format(str.rfind("w",0,5)))# 查找字符，从右到左，在指定范围内查找 返回-1 即没有找到，返回非负数即找到
   print("去除前后空格:".format(str.strip()))# 去除字符串，前后空格
   print("去除字符串，左边的空格:".format(str.lstrip()))# 去除字符串，左边的空格
   print("去除字符串，右边的空格:".format(str.rstrip()))# 去除字符串，右边的空格
   print("小写转大写，大写转小写:".format(str.swapcase()))# 小写转大写，大写转小写
   print("小写转大写:".format(str.upper()))# 小写转大写