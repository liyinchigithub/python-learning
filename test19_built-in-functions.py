#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名:test57_method.py

from ast import Str
from base64 import decode
from cgi import print_arguments
from unittest import skip
import random
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

        #  f-string 是 python3.6 之后版本添加的，称之为字面量格式化字符串，是新的格式化字符串的语法。
        name = 'Runoob'
        print(f'My name is {name}')# My name is Runoob
        
    # 2.srt()和repr() 数据类型转换为字符串
    @pytest.mark.L2
    def test_02(self) -> None:
        print("str()", str('100'))  # 100
        print("repr()", repr('100'))  # '100' 带单引号

    # 3.strip() 过滤符号、空格、换行符
    @pytest.mark.L2
    def test_03(self) -> None:
        text = " *+_/ hello world *)_+( "
        print("strip()", text.strip("*+_/()")) # hello world 
        print("rstrip()", text.rstrip("*+_/()"))#  从右边开始查找字符串

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
    @pytest.mark.L2
    def test_05_join(self) -> None:
        seq1=("a","b","c","d","e","f") # join元组
        seq2=["1","2","3","4","5","6"] # 这边列表不能使用[1,2,3,4,5,6] 因为python数字和字符串不能直接拼接，需要进行转换。元素类型都需要为字符串或字符
        seq3={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6}# join字典
        seq4={"1","2","3","4","5","6"}  #join集合
        s1="-"
        s2="="
        s3="@"
        print("s1.join(seq1)",s1.join(seq1))# a-b-c-d-e-f
        print("s2.join(seq2)",s2.join(seq1))# a=b=c=d=e=f
        print("s3.join(seq3)",s3.join(seq1))# a@b@c@d@e@f
        print("s1.join(seq2)",s1.join(seq2))# a-b-c-d-e-f
        print("s2.join(seq2)",s2.join(seq2))# a=b=c=d=e=f
        print("s3.join(seq2)",s3.join(seq2))# a@b@c@d@e@f
        print("s1.join(seq3)",s1.join(seq3))# a-b-c-d-e-f 字典是去key进行拼接join符号
        print("s2.join(seq3)",s2.join(seq3))# a=b=c=d=e=f
        print("s3.join(seq3)",s3.join(seq3))# a@b@c@d@e@f
        print("s1.join(seq4)",s1.join(seq4))# a-b-c-d-e-f
        print("s2.join(seq4)",s2.join(seq4))# a=b=c=d=e=f
        print("s2.join(seq4)",s3.join(seq4))# a@b@c@d@e@f
        print(type(s1.join(seq1)))# <class 'str'>

    # 6.replace() 字符串替换
    @pytest.mark.L2
    def test_06_replace(self) -> None:
       str="python3.X"
       print("replace",str.replace("X","7"))# python3.7

    # 7.encode() 字符串编码
    @pytest.mark.L2
    def test_07_encode(self) -> None:
        str="这是编码内容"
        # 对内容进行编码
        print("encode()",str.encode("utf-8"))# b'\xe8\xbf\x99\xe6\x98\xaf\xe7\xbc\x96\xe7\xa0\x81\xe5\x86\x85\xe5\xae\xb9'

    # 8.decode() 字符串解码
    @pytest.mark.L2
    def test_08_decode(self) -> None:
        str=b'\xe8\xbf\x99\xe6\x98\xaf\xe7\xbc\x96\xe7\xa0\x81\xe5\x86\x85\xe5\xae\xb9'
        print("str.decode()",str.decode(encoding='UTF-8',errors='strict'))# 这是解码内容

    # 9.format() 字符串格式化
    @pytest.mark.L2
    def test_09_format(self) -> None:
        print("a={},b={},c={}".format("a","b","c"))
    # 10.isalpha() 字符串是否全部是字母
    @pytest.mark.L2
    def test_10_isalpha(self) -> None:
        str="Python"
        print(str.isalpha())# True
    # 11.isalnum() 字符串是否全部是字母和数字
    def test_11_isalnum(self) -> None:
        str="Python3.0"
        print(str.isalnum())# True
    # 12.isdigit() 字符串是否有数字
    def test_12_isdigit(self) -> None:
        str="3.0"
        print(str.isdigit())# True
        str2="123456"
        print(str2.isnumeric())# 字符串全数字  
    # 13.isspace() 字符串是否全部是空格
    def test_13_isspace(self) -> None:
        str="   "
        print(str.isspace())# True
    # 14.istitle() 字符串是否全部是标题 首字母大写，后面字母小写
    def test_14_istitle(self) -> None:
        str="Python3.0"
        print(str.istitle())
    # 15.isupper() 字符串是否全部是大写
    def test_15_isupper(self) -> None:
        str="PYTHON"
        print(str.isupper())
    # 16.islower() 字符串是否全部是小写
    def test_16_islower(self) -> None:
        str="python"
        print(str.islower())
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
    @pytest.mark.L2
    
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
        # 创建字典 1.使用dict()函数
        d = dict()
        d['a'] = 1
        d['b'] = 2
        d['c'] = 3
        print("字典d为", d)  # {'a': 1, 'b': 2, 'c': 3}
        print("type(d)", type(d))  # 判断类型 <class 'dict'>
        print(d.keys())  # 获取字典所有key  dict_keys(['a', 'b', 'c'])
        print(d.values())  # 获取字典所有value dict_values([1, 2, 3])
        print(d['c'])  # 3 获取某个key的value
        # 创建字典 2.使用dict()函数
        numbers1 = dict({'x': 4, 'y': 5})
        print('numbers1 =',numbers1)
        # 创建字典  3.不使用dict()函数
        numbers2 = {'x': 4, 'y': 5}
        print('numbers2 =',numbers2)
        # 创建字典  4.关键字
        print('传入关键字',dict(a=1, b=2, c=3))  # 传入关键字 {'a': 1, 'b': 2, 'c': 3}
        # 创建字典  5.可迭代对象
        print("可迭代对象方式来构造字典",dict([('a', 1), ('b', 2), ('c', 3)]))  #  可迭代对象方式来构造字典 [('a', 1), ('b', 2), ('c', 3)]
        # 创建字典 6.映射
        print('映射函数方式来构造字典',dict(zip(['a','b','c'],[1,2,3])))# 映射函数方式来构造字典 {'a': 1, 'b': 2, 'c': 3}

    # 40.list() 字符串转列表 创建列表
    @pytest.mark.L2
    def test_40_list(self) -> None:
        str1="a,b,c"
        str2="abc"
        str3="a,b,c"
        print("str.split(',')",str1.split(','))# 
        print("type(str.split(','))",type(str1.split(',')))# <class 'list'>
        print(list(str2))# ['a', 'b', 'c']
        print("type(list(str))",type(list(str2)))# <class 'list'>
        # 注意：逗号也会被当做列表元素
        print(list(str3))# ['a', ',', 'b', ',', 'c']

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

    # 45.eval(str) 字符串转表达式（字符串转对象）
    @pytest.mark.L2
    def test_45_eval(self) -> None:
        str = "{'a':1,'b':2,'c':3}"
        print("str", eval(str))  # {'a': 1, 'b': 2, 'c': 3}
        print("type(str)", type(eval(str)))  # type(eval(str)) <class 'dict'>
        #  eval 入参是一个字符串表达式
        x=7
        print("eval( '3 * x' ):",eval( '3 * x' ))# 21
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
    @pytest.mark.L2
    def test_52_len(self) -> None:
        list=[1,2,3,4,5]
        tup=(1,2,3,4,5)
        dict={'a':1,'b':2,'c':3}
        col={1,2,3,4,5}
        print("list长度",len(list))
        print("tup长度",len(tup))
        print("dict长度",len(dict))
        print("col长度",len(col))
        
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
        
    # 68.count() 计算元素在集合中出现的次数
    @pytest.mark.L2
    def test_68_count(self) -> None:
        str="abcdefgccc"
        print("count()",str.count("d")) # 1
        print("sub",str.count("c",3)) # 从第三个开始计算 sub 3
        print("sub",str.count("c",3,8)) # 从第三个开始计算，到第八个结束 指定范围内出现的次数 sub 1
        
    # 69.find() 查找子字符串的位置
    @pytest.mark.L2
    def test_69_find_rfind(self) -> None:
        str1="abcdefghijklmn"
        str2="fgh"
        str3="xyz"
        print("find()",str1.find(str2)) # 6 子字符串在字符串中的位置
        print("find()",str1.find(str3)) # -1 没有找到
        str4="abcdefghijklmn"
        # 从右边开始查找
        print("rfind()",str4.rfind(str2,3)) # rfind() 5
        
        # index()       str.index(str, beg=0, end=len(string))    返回如果包含子字符串返回开始的索引值，否则抛出异常。
        str1 = "Runoob example....wow!!!"
        str2 = "exam"
        print (str1.index(str2)) # 4
        print (str1.index(str2, 5))# 5
        print (str1.index(str2, 10))# 10
        
    # 70.zfill() 字符串补全
    @pytest.mark.L2
    def test_70_zfill(self) -> None:
        str="pytho"
        print("zfill()",str.zfill(10)) # pytho0000000   
        
    # 71.set() 用set方法删除重复元素
    @pytest.mark.L2
    def test_71_set(self) -> None:
        str="googgle"
        str2=['a','a','b','c']
        print("set(str)",set(str)) # {'o', 'g', 'e', 'l'}
        print("set(str)",set(str2)) # {'b', 'a', 'c'}  注意：是无需的
    '''
        [推导式]
        https://www.runoob.com/python3/python-comprehensions.html
        推导式是一种独特的数据处理方式，可以从一个数据序列构建另一个新的数据序列的结构体。
        
        [表达式 for 变量 in 列表] 
        [out_exp_res for out_exp in input_list]

        或者 

        [表达式 for 变量 in 列表 if 条件]
        [out_exp_res for out_exp in input_list if condition]
        
        out_exp_res：列表生成元素表达式，可以是有返回值的函数。
        for out_exp in input_list：迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中。
        if condition：条件语句，可以过滤列表中不符合条件的值。

    '''
    # 72. 列表推导式    使用中括号
    @pytest.mark.L2
    def test_72_list_comprehension(self) -> None:
        # 过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母：
        name_list = ['Bob','Tom','alice','Jerry','Wendy','Smith']
        new_list=[ name.lower() for name in name_list if len(name)<=3]
        print("[ name.lower() for name in name_list if len(name)<=3]",new_list)# ['bob', 'tom']
        
        # 过滤大于5的
        list=[1,2,3,4,5,6,7,8,9,10]
        new_list=[num for num in list if num>5]
        print("[num for num in list if num>5]",new_list)
        # 仅保留能被3整除
        multiples = [i for i in range(30) if i % 3 == 0]
        print(multiples)# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
        #  仅保留指定字符内容
        new_list='abracadabra'
        print([i for i in new_list if i in 'ab'])# ['a', 'b']
        
    # 73. 元组推导式
    @pytest.mark.L2
    def test_73_tuple_comprehension(self) -> None:
        '''
        元组推导式可以利用 range 区间、元组、列表、字典和集合等数据类型，快速生成一个满足指定需求的元组。
        [改格式]
            (expression for item in Sequence )
            或
            (expression for item in Sequence if conditional )
        '''
        list1 = (x for x in range(1,10))# 返回的是生成器对象
        # 使用 tuple() 函数，可以直接将生成器对象转换成元组
        print(tuple(list1))
 
    
    # 74. 集合推导式       使用大括号
    @pytest.mark.L2
    def test_75_set_comprehension(self) -> None:
        '''
        [格式]
            { expression for item in Sequence }
            或
            { expression for item in Sequence if conditional }
        和字典推导式的区别，在集合没有key只有value
        '''
        # 计算数字 1,2,3 的平方数
        setnew1 = {i**2 for i in (1,2,3,4,5,6,7,8,9,10)}
        setnew2 = {i**2 for i in (1,2,3,4,5,6,7,8,9,10) if i%2==0}
        print(setnew1)# {1, 4, 9, 16, 25, 36, 49, 64, 81, 100}
        print(setnew2)# {4, 16, 36, 64, 100}
        
    # 75. 字典推导式    使用大括号
    @pytest.mark.L2
    def test_76_dict_comprehension(self) -> None:
        '''
        [格式]
            { key_expr: value_expr for value in collection }
            或
            { key_expr: value_expr for value in collection if condition }
        '''
        
        # 把列表元素作为字典key，列表元素长度作为字典value
        list=["python","java","php","c++","c","c#"]
        new_dict={i:len(i) for i in list if len(i)>2}
        print("{i:len(i) for i in list if len(i)>1} 值为 ",new_dict)# {'python': 6, 'java': 4, 'php': 3, 'c++': 3}
        # 提供三个数字，以三个数字为键，三个数字的平方为值来创建字典
        list=[1,2,3]
        new_dict={i:i**2 for i in list}
        print("{i:i**2 for i in list} 值为 ",new_dict)# {1: 1, 2: 4, 3: 9}
        #  仅保留指定字符内容
        list1='abracadabra'
        list2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        print({i for i in list1 if i in 'abzfs'})# 
      
    #  76.random()  随机生成下一个实数，它在[0,1)范围内。
    @pytest.mark.L2
    def test_76_random(self) -> None:
        # 第一个随机数
        print ("random() : ", random.random())# 0.988897
        # 第二个随机数
        print ("random() : ", int(random.random()*100))# 99
        
    #  77.choice()      从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
    @pytest.mark.L2
    def test_77_choice(self) -> None:
        # 注意：choice()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。
        print ("从 range(100) 返回一个随机数 : ",random.choice(range(100)))# 从 range(100) 返回一个随机数 : 84
        print ("从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 : ", random.choice([1, 2, 3, 5, 9]))# 从列表中 [1, 2, 3, 5, 9] 返回一个随机元素 :  5
        print ("从字符串中 'Runoob' 返回一个随机字符 : ", random.choice('Runoob'))# 从字符串中 'Runoob' 返回一个随机字符 : r
        random
    
    #  78.seed()        x -- 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
    @pytest.mark.L2
    def test_78_seed(self) -> None:
        '''
            我们调用 random.random() 生成随机数时，每一次生成的数都是随机的。但是，当我们预先使用 random.seed(x) 设定好种子之后，其中的 x 可以是任意数字，如10，这个时候，先调用它的情况下，使用 random() 生成的随机数将会是同一个。
            注意：seed()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。
        '''
        random.seed()
        print ("使用默认种子生成随机数：", random.random())
        print ("使用默认种子生成随机数：", random.random())

        random.seed(10)
        print ("使用整数 10 种子生成随机数：", random.random())
        random.seed(10)
        print ("使用整数 10 种子生成随机数：", random.random())

        random.seed("hello",2)
        print ("使用字符串种子生成随机数：", random.random())
    
    #  79. randrange()   从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
    @pytest.mark.L2
    def test_79_randrange(self) -> None:
        '''
            random.randrange ([start,] stop [,step])
                start -- 指定范围内的开始值，包含在范围内。
                stop -- 指定范围内的结束值，不包含在范围内。
                step -- 指定递增基数。
                返回值：从给定的范围返回随机项
        '''
        # 从 1-100 中选取一个奇数
        print ("randrange(1,100, 2) : ", random.randrange(1, 100, 2))
        # 从 0-99 选取一个随机数
        print ("randrange(100) : ", random.randrange(100))
        
    # 80. shuffle(lst)  将序列的所有元素随机排序
    
    # 89. uniform(x, y)     随机生成下一个实数，它在[x,y]范围内。   
    
    # 90. 字符串内建函数
    
    
    
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
