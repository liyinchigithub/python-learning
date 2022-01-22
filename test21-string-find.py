#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名：test21.py
# Python 字符串是否包含
# https://www.runoob.com/python3/python3-date-time.html
import string
import pytest
'''
    使用成员能操作符in
'''
@pytest.mark.test
def test_string_include01():
    s='nihao,shijie'
    t='nihao'
    result = t in s
    print(result) #True


'''
    使用string模块的find()/rfind()方法
    第一个参数:被匹配的字符串
    第二个参数:所要查找的字符串
'''
@pytest.mark.test
def test_string_incloud02():
    s='nihao,shijie'
    t='nihao'
    result2 = string.rfind(s,t)!=-1
    print(result2) #True
    result3 = string.rfind(s,t)!=-1
    print(result3) #True


'''
index()/rindex()方法，跟find()/rfind()方法一样，只不过找不到子字符串的时候会报一个ValueError异常。
第一个参数:被匹配的字符串
第二个参数:所要查找的字符串
'''
@pytest.mark.test
def test_string_include03():
    def find_string(s,t):
        try:
            string.index(s,t)
            return True
        except(ValueError): 
            return False
    s='nihao,shijie'
    t='nihao'
    result = find_string(s,t)
    print(result)  #True



if __name__=="__main__":
    pytest.main();