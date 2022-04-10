#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名:test57_method.py

from ast import Str
from unittest import skip
import numpy as np
import pytest
import logging
# 日志级别、时间格式配置
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)  # 实例化


def setup_function() -> None:
        print("不在类中，每个测试用例执行之前")


def teardown_function() -> None:
        print("不在类中， 每个测试用例执行之后")


@pytest.mark.test
@pytest.mark.L1
def test_not_class_function():
    print("test_not_class_function 不在类中，测试用例")


class Test():
    # # 整个类之前
    # def setup_class(self) -> None:
    #     logger.debug("setup_class 整个类之前")
    # # 整个类之后
    # def teardown_class(self) -> None:
    #     print("teardown_class 整个类之后")
    # # 每个测试用例执行之前
    # def setup_method(self) -> None:
    #     print("Test_class_01 类中每个测试用例执行之前")
    # # 类中每个测试用例执行之后
    # def teardown_method(self) -> None:
    #     print("Test_class_01 类中每个测试用例执行之后")
    # # 每个测试用例执行之前
    # def setUp(self) -> None:
    #     print("setUp 每个测试用例执行之前")
    # # 每个测试用例执行之后
    # def tearDown(self) -> None:
    #     print("tearDown 每个测试用例执行之后")

    # 1.字符串格式化
    @pytest.mark.L1
    def test_01_format(self) -> None:
        str = "{} {} {}"
        str = str.format("a", "b", "c")
        print("字符串格式化'{} {} {}'.format('a','b','c')=", str)

    # 2.srt()和repr() 数据类型转换为字符串
    @pytest.mark.L2
    def test_02(self) -> None:
        print("str()", str('100'))  # 100
        print("repr()", repr('100'))  # '100' 带单引号

    # 3.strip() 过滤空格、符号、换行符
    @pytest.mark.L2
    def test_03(self) -> None:
        text = "*+_/ hello world *)_+("
        print("strip()", text.strip("*+_/()"))

    # 4.split() 字符串分割
    @pytest.mark.L2
    def test_04(self) -> None:
        str = "a,b,c,d,e,f"
        print("str.split(',')", str.split(','))
        print("type(str.split(','))", type(str.split(',')))  # <class 'list'>))
        if type(str.split(',')) == list:
            print("str.split(',')是一个列表")
        else:
            print("str.split(',')不是一个列表")

    # 5.join() 字符串连接
    # @pytest.mark.L2
    # def test_05_join(self) -> None:
    #     str="a","b","c","d","e","f"
    #     print("str.join('-')",str.join('-'))
    #     print(type(str.join('-'))) # <class 'str'>

    # 6.replace() 字符串替换
    @pytest.mark.L2
    def test_06_replace(self) -> None:
       print("")

    # 7.encode() 字符串编码
    @pytest.mark.L2
    def test_07_encode(self) -> None:
        print("")

    # 8.decode() 字符串解码
    @pytest.mark.L2
    def test_08_decode(self) -> None:
        print("")

    # 9.format() 字符串格式化
    @pytest.mark.L2
    def test_09_format(self) -> None:
        print("")
    # 10.isalpha() 字符串是否全部是字母

    # 11.isalnum() 字符串是否全部是字母和数字

    # 12.isdigit() 字符串是否全部是数字

    # 13.isspace() 字符串是否全部是空格

    # 14.istitle() 字符串是否全部是标题

    # 15.isupper() 字符串是否全部是大写

    # 16.islower() 字符串是否全部是小写

    # 17.isascii() 字符串是否全部是ASCII字符

    # 18.isdecimal() 字符串是否全部是十进制数字

    # 19.isnumeric() 字符串是否全部是数字

    # 20.isidentifier() 字符串是否是合法的标识符

    # 21.isprintable() 字符串是否全部是可打印的字符

    # 22.input() 仅接受字符串输入  字符串转数值
    @pytest.mark.L2
    def test_22_input(self) -> None:
        str = input("请输入一个字符串：")
        print("输入的字符串是：", str)
        print("type(str)", type(int(str)))

    # 23.input() 仅接受字符串输入 字符串转数值
    # @pytest.mark.L2
    # def test_23_input(self) -> None:
    #     str=input()
    #     print("输入的字符串是：",str)
    #     print("type(str)",type(int(str)))
    # 24.upper() 字符串转大写

    # 25.lower() 字符串转小写

    # 26.capitalize() 字符串首字母大写

    # 27.title() 字符串首字母大写

    # 28.swapcase() 字符串大小写互换

    # 29.center() 字符串居中

    # 30.ljust() 字符串左对齐

    # 31.rjust() 字符串右对齐

    # 32.zfill() 字符串左对齐

    # 33.format() 字符串格式化

    # 34.format_map() 字符串格式化

    # 35.flatten() 字符串展平

    # 36.float() 字符串转浮点数

    # 37.int() 字符串转整数
    @pytest.mark.L2
    def test_37_int(self) -> None:
        print("int('123')", int('123'))  # 123
        print("type(int('123'))", type(int('123')))  # <class 'int'>

    # 38.str() 字符串转字符串
    @pytest.mark.L2
    def test_38_str(self) -> None:
        print("int(123)", str(123))  # 123
        print("type(int(123))", type(str(123)))  # <class 'str'>

    # 39.dict() 字符串转字典 创建字典
    @pytest.mark.L2
    def test_39_dict(self) -> None:
        d = dict()
        d['a'] = 1
        d['b'] = 2
        d['c'] = 3
        print("字典d为", d)  # {'a': 1, 'b': 2, 'c': 3}
        print("type(d)", type(d))  # <class 'dict'>
        print(d.keys())  # dict_keys(['a', 'b', 'c'])
        print(d.values())  # dict_values([1, 2, 3])
        print(d['c'])  # 3

    # 40.list() 字符串转列表 创建列表
    # @pytest.mark.L2
    # def test_40_list(self) -> None:
    #     str="'a','b','c'"
    #     print(list(str))

    # 41.tuple() 字符串转元组 创建元组
    @pytest.mark.L2
    def test_41_tuple(self) -> None:
        t1 = (1, 2, 3)
        t2 = (4, 5, 6)
        t3 = ('7', '8', '9')
        print("元组t1为", t1)  # (1, 2, 3)
        print("t1的类型为", type(t1))  # <class 'tuple'>
        print(t1[2])  # 3
        print(t1[0:])  # (1, 2, 3)
        print(t1[0:2])  # (1, 2)
        print(t1+t2+t3)  # (1, 2, 3, 4, 5, 6, 7, 8, 9)

    # 42.chr() 字符串转字符

    # 43.complex() 字符串转复数

    # 44.set() 字符串转集合 创建集合 {}
    @pytest.mark.L2
    def test_44_set(self) -> None:
        s = set()
        s.add(1)
        s.add(1)  # 集合会自动去重
        s.add(2)
        s.add('3')  # 元素加入集合中
        print(s)  # {1, 2, '3'}

    # 45.eval(str) 字符串转表达式 字符串转对象
    @pytest.mark.L2
    def test_45_eval(self) -> None:
        str = "{'a':1,'b':2,'c':3}"
        print("str", eval(str))  # {'a': 1, 'b': 2, 'c': 3}
        print("type(str)", type(eval(str)))  # type(eval(str)) <class 'dict'>

    # 46.r = re.compile(pattern, flags=0) 字符串转正则表达式

    # 47.r 停止转义
    @pytest.mark.L2
    def test_47_r(self) -> None:
        str_r = r'hello \n world'
        print("停止转义str_r", str_r)  # hello \n world
        str = "hello \n world"
        print("进行转义str", str)  # hello \n world

    # 48.in 判断是否成员属性
    @pytest.mark.L2
    def test_48_in(self) -> None:
        str = {'a', 'b', 'c', 1, 2, 3}
        if 0 in str:
            print("0在集合中")
        else:
            print("0不在集合中")
    # 50.isinstance() 判断是否是某种类型

    # 51.issubclass() 判断是否是某种类型的子类

    # 52.len() 字符串长度

    # 53.max() 字符串最大值

    # 54.min() 字符串最小值

    # 55.ord() 字符串转整数

    # 56.repr() 字符串转字符串

    # 57.round() 字符串四舍五入

    # 58.sorted() 字符串排序

    # 59.sum() 字符串求和

    # 60.type() 字符串类型

    # 61.zip() 字符串转字典
    @pytest.mark.L2
    def testing_61_zip(self) -> None:
        # 定义一个字符串，内容是字典格式
        str = "{'a':1,'b':2,'c':3}"
        # 将字符串转换成字典
        print(zip(str))
        # 判断是否是字典类型
        print(type(zip(str)))

    '''
        列表、元素、字符串，需要先转成结合，才能进行差集、并集、交集等操作
        字典可以直接进行差集、并集、交集等操作，无需转换成集合。 a.items() a.keys() a.values()
    '''
    # 62.差集 -     a-b a有的b没有 b-a b有的a没有（a没有的b有）
    @pytest.mark.L2
    def test_62_difference(self) -> None:
        # 列表之间差集
        a1 = [1, 2, 3, 4, 5]
        b1 = [2, 3, 4, 5, 6]
        print("列表之间差集 a1-b1为{}", list(set(a1)-set(b1)))  # [1]
        print("列表之间差集 a1-b1为{}", list(set(b1)-set(a1)))  # [6]

        # 元组之间差集
        a2 = (1, 2, 3, 4, 5)
        b2 = (2, 3, 4, 5, 6)
        print("元组之间差集 a2-b2为", tuple(set(a2)-set(b2)))  # (1, 5)
        print("元组之间差集 a2-b2为", tuple(set(b2)-set(a2)))  # (6,)

        # 字典之间差集
        a3 = dict(a=1, b=2, c=3)
        b3 = dict(b=2, c=3, d=4)
        print('key和value的差集:', a3.items() - b3.items()) # key和value的交集:{('a', 1)}
        print('key和value的差集:', b3.items() - a3.items()) # key和value的交集: {'b': 2, 'c': 3}

        # 字符串之间差集
        a5 = set("abcdefg")
        b5 = set("bcdefgh")
        print("字符串之间差集 a5-b5为", a5-b5)  # {'a'}
        print("字符串之间差集 b5-a5为", b5-a5)  # {'h'}

    # 63.并集 |     a所有和b所有元素并在一起
    @pytest.mark.L2
    def test_63_(self) -> None:

            # 列表之间并集
            a1 = [1, 2, 3, 4, 5]
            b1 = [2, 3, 4, 5, 6]
            # 第一种方法
            print("列表之间并集 a1|b1为", list(set(a1).union(set(b1))))
            # 第二种方法（推荐）
            ret2 = list(set(a1) | set(b1))  # 先将列表转成集合，做并集后再转成列表
            print("列表之间并集 a1|b1为", ret2)

            # 元组之间并集
            a2 = (1, 2, 3, 4, 5)
            b2 = (2, 3, 4, 5, 6)
            #           第一种方法
            print("元组之间并集 a1|b1为", tuple(set(a2).union(set(b2))))  # 元组不能直接进行并集操作
            #           第二种方法（推荐）
            ret2 = tuple(set(a2) | set(b2))  # 先将元组转成集合，做并集后再转成元组
            print("元组之间并集 a1|b1为", ret2)

            # 字典之间并集
            a3 = {'a': 1, 'b': 2, 'c': 3}
            b3 = {'b': 2, 'c': 3, 'd': 4}
            # 并集的键: {'c', 'a', 'd', 'b'}
            print('交集相同的键:', a3.keys() | b3.keys())
            print('key和value的并集:', a3.items() | b3.items()) # {'g', 'b', 'e', 'c', 'd', 'f'}
            print('key和value的并集:', b3.items() | a3.items()) # {'g', 'b', 'e', 'c', 'd', 'f'}
            # 字符串之间并集
            a5 = set("abcdefg")
            b5 = set("bcdefgh")
            # {'f', 'b', 'a', 'g', 'c', 'h', 'd', 'e'}  集合是无序的！
            print("字符串之间并集 a5|b5为", a5 | b5)
            # {'f', 'b', 'a', 'g', 'c', 'h', 'd', 'e'}  集合是无序的！
            print("字符串之间并集 b5|a5为", b5 | a5)

    # 64.交集 &  a和b相同的元素
    @pytest.mark.L2
    def test_64_(self) -> None:
            # 列表之间并集
            a1 = [1, 2, 3, 4, 5]
            b1 = [2, 3, 4, 5, 6]
            # 第一种方法
            print("列表之间并集 a1&b1为", list(set(a1).intersection(set(b1))))
            # 第二种方法（推荐）
            ret2 = list(set(a1) & set(b1))  # 先将列表转成集合，做并集后再转成列表
            print("列表之间并集 a1&b1为", ret2)

            # 元组之间交集
            a2 = (1, 2, 3, 4, 5)
            b2 = (2, 3, 4, 5, 6)
            print("元组之间交集 a2&b2为",tuple(set( a2 )& set(b2)))  #  (2, 3, 4, 5)元组不能直接进行交集操作
            print("元组之间交集 a2&b2为",tuple(set( b2 )& set(a2)))  # (2, 3, 4, 5)
            
            # 字典之间交集
            a3={'a':1,'b':2,'c':3}
            b3={'b':2,'c':3,'d':4}
            print('key和value的交集:', a3.items() & b3.items()) # key和value的交集: {'b': 2, 'c': 3}
            print('key和value的交集:', b3.items() & a3.items()) # key和value的交集: 
            
            # 集合之间交集
            a4 = set("1, 2, 3, 4, 5")
            b4 = set("2, 3, 4, 5, 6")
            print("集合之间交集 a4&b4为", a4 & b4)  # {2, 3, 4, 5}
            print("集合之间交集 b4&a4为", b4 & a4)  # {2, 3, 4, 5}
            
            # 字符串之间交集
            a5 = set("abcdefg")
            b5 = set("bcdefgh")
            print("字符串之间交集 a5&b5为", a5 & b5) # {'f', 'b', 'c', 'g', 'd', 'e'}  集合是无序的！
            print("字符串之间交集 b5&a5为", b5 & a5)  # {'f', 'b', 'c', 'g', 'd', 'e'}  集合是无序的！

    # 65.不同时存在的元素 ^ a有的b没有，b有的a没有
    @pytest.mark.L2
    def test_65_(self) -> None:
            # 列表之间不同时存在的元素
            a1 = [1, 2, 3, 4, 5]
            b1 = [2, 3, 4, 5, 6]
            ret2 = list(set(a1) ^ set(b1))  # 先将列表转成集合，做不存在元素集后再转成列表
            print("列表之间不同时存在的元素 a1^b1为", ret2)  # [1, 6]

            # 元组之间不同时存在的元素
            a2 = (1, 2, 3, 4, 5)
            b2 = (2, 3, 4, 5, 6)
            print("元组之间不同时存在的元素 a2^b2为", tuple(set(a2) ^ set(b2)))  # (1, 6)
            print("元组之间不同时存在的元素 a2^b2为", tuple(set(b2) ^ set(a2)))  # (1, 6)

           # 字典之间不同时存在的元素   a3有b3没有 b3有a3没有
            a3 = dict(a=1, b=2, c=3)
            b3 = dict(b=2, c=3, d=4)
            print('key和value的不同时存在的元素:', a3.items() ^ b3.items()) # {('a', 1), ('d', 4)}
            print('key和value的不同时存在的元素:', b3.items() ^ a3.items()) # {('a', 1), ('d', 4)}

           
            # 集合之间不同时存在的元素
            a4 = set("1, 2, 3, 4, 5")
            b4 = set("2, 3, 4, 5, 6")
            print("集合之间不同时存在的元素 a4^b4为",a4^b4)#{'6', '1'}  集合是无序的！
            print("集合之间不同时存在的元素 b4^a4为",b4^a4) #{'6', '1'}  集合是无序的！
            # 字符串之间不同时存在的元素
            a5 = set("abcdefg")
            b5 = set("bcdefgh")
            print("字符串之间不同时存在的元素 a5^b5为",a5^b5)#{'h', 'a'}
            print("字符串之间不同时存在的元素 b5^a5为",b5^a5)# {'a', 'h'}
        
    # 66.difference() a和b的差集 a有b没有，b有a没有
    @pytest.mark.L2
    def test_66_difference(self) -> None:
        a = [1,2,5,7]
        b = [2,5,9]
        print("difference()",list(set(a).difference(set(b)))) # a中有而b中没有的  #[1, 7]
        print("difference()",list(set(b).difference(set(a)))) # a中有而b中没有的  #[9]
        
    # 67.intersection() a和b的交集 a和b都有
    @pytest.mark.L2
    def test_67_intersection(self) -> None:
        a = [1,2,5,7]
        b = [2,5,9]
        print("intersection()",list(set(a).intersection(set(b)))) # a和b中都有的  #[2, 5]
        print("intersection()",list(set(b).intersection(set(a)))) # a和b中都有的  #[2, 5]
    
if __name__ == '__main__':
    pytest.main(["-s", "test56_pytest.py",
                "--html=./reports/report.html"])  # 运行指定文件

'''
    运行脚本：
    pytest -v test57_method.py
'''

'''
    注意事项：
    1.文件名（模块）：必须以test_ 或者 _test开头
    2.测试类：必须以Test开头
    3.测试方法：必须以test_
    4.断言：assert
    5.执行结果：.表示成功 F表示失败 E表示发生错误
    6.测试固件：setup_module/teardown_module、setup_function/teardown_function、setup_class/teardown_class、setup_method/teardown_method、setup/teardown
'''
