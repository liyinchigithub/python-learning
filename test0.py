#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test0.py
# Python 变量类型


def isBoolean():
   if True:
    print("Answer")
    print("True")
   else:
    print("Answer")
    # 没有严格缩进，在执行时会报错
    print("False")

# isBoolean()

def definitions():
   # 数字
   A = 100
   # 同时对多个变量赋值
   B, C, D = "liyinchi", 12, "泉州" 
   print(A)
   print(B)
   print(C)
   print(D)

# definitions()

def split():
   s='abcdefg'
   print('字符串abcdefg 截取s[1:5] 得到'+s[1:5])# 索引0开始，到5（不包含5） 输出：bcde   

# split()

def listIndex():
   # 字符串
   str = 'Hello World!'
   li=['1','2','3','4','5','6','7'] # 列表
   print(str)           # 输出完整字符串 输出：Hello World!
   print(str[0])        # 输出字符串中的第一个字符 输出H
   print(str[2:5])      # 输出字符串中第三个至第六个(不含第六个)之间的字符串 输出：llo 
   print(str[2:])       # 输出从第三个字符开始的字符串
   print(str*2)      # 输出字符串两次 输出：Hello World!Hello World!
   print(str+"TEST")  # 输出连接的字符串 输出：Hello World!TEST
   print(li[2:5:2])      # 输出字符串中第三个至第六个（不含第六个）之间的字符串,步长为2 输出：['3', '5']

# listIndex()

def listMerge():
   # 列表
   list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
   tinylist = [123, 'john']
   print(list + tinylist)    # 打印组合的列表 输出：[ 'runoob', 786 , 2.23, 'john', 70.2, 123, 'john' ]

# listMerge()

def Tuple():
   # 元组
   tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
   tinytuple = (123, 'john')
   
   print(tuple)               # 输出完整元组 输出：('runoob', 786, 2.23, 'john', 70.2)
   print(tuple[0])            # 输出元组的第一个元素 输出：runoob
   print(tuple[1:3])          # 输出第二个至第四个（不包含）的元素 输出：(786, 2.23)
   print(tuple[2:])           # 输出从第三个开始至列表末尾的所有元素 输出：(2.23, 'john', 70.2)
   print(tinytuple * 2)       # 输出元组两次 输出：(123, 'john', 123, 'john')
   print(tuple + tinytuple)   # 打印组合的元组 输出：('runoob', 786, 2.23, 'john', 70.2, 123, 'john')

# Tuple()

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

def stringToNumber():
   # 数据类型转换
   str="1"
   print(int(str)+1);# 字符串转数值 输出2

# stringToNumber()

def sum():
   # 算数运算符
   a = 21
   b = 10
   c = 0
   
   c = a + b
   print("1 - c 的值为：", c)
   
   c = a - b
   print("2 - c 的值为：", c) 
   
   c = a * b
   print("3 - c 的值为：", c) 
   
   c = a / b
   print("4 - c 的值为：", c)
   
   c = a % b
   print("5 - c 的值为：", c)
   
   # 修改变量 a 、b 、c
   a = 2
   b = 3
   c = a**b 
   print("6 - c 的值为：", c)
   
   a = 10
   b = 5
   c = a//b 
   print("7 - c 的值为：", c)

def compar01():
   # 比较运算符

   a = 21
   b = 10
   c = 0
   
   if  a == b :
      print("1 - a 等于 b")
   else:
      print("1 - a 不等于 b")
   
   if  a != b :
      print("2 - a 不等于 b")
   else:
      print("2 - a 等于 b")

   # python3 已废弃。
   # if  a <> b :
   #    print("3 - a 不等于 b")
   # else:
   #    print("3 - a 等于 b")
   
   if  a < b :
      print("4 - a 小于 b" )
   else:
      print("4 - a 大于等于 b")
   
   if  a > b :
      print("5 - a 大于 b")
   else:
      print("5 - a 小于等于 b")
 
 
   # 修改变量 a 和 b 的值
   a = 5
   b = 20
   if  a <= b :
      print("6 - a 小于等于 b")
   else:
      print("6 - a 大于  b")
   
   if  b >= a :
      print("7 - b 大于等于 a")
   else:
      print("7 - b 小于 a")


def Assignment():
   # 赋值运算符

   a = 21
   b = 10
   c = 0
   
   c = a + b
   print("1 - c 的值为：", c)
   
   c += a
   print("2 - c 的值为：", c) 
   
   c *= a
   print("3 - c 的值为：", c) 
   
   c /= a 
   print("4 - c 的值为：", c) 
   
   c = 2
   c %= a
   print("5 - c 的值为：", c)
   
   c **= a
   print("6 - c 的值为：", c)
   
   c //= a
   print("7 - c 的值为：", c)

def logicOperation():
   # 逻辑运算符

   a = 10
   b = 20
   
   if  a and b :
      print( "1 - 变量 a 和 b 都为 true")
   else:
      print( "1 - 变量 a 和 b 有一个不为 true")
   
   if  a or b :
      print( "2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
   else:
      print( "2 - 变量 a 和 b 都不为 true")
   
   # 修改变量 a 的值
   a = 0
   if  a and b :
      print( "3 - 变量 a 和 b 都为 true")
   else:
      print( "3 - 变量 a 和 b 有一个不为 true")
   
   if  a or b :
      print( "4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
   else:
      print( "4 - 变量 a 和 b 都不为 true")
   
   if not( a and b ):
      print( "5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
   else:
      print( "5 - 变量 a 和 b 都为 true")

def memberOperator():
   # 成员运算符

   a = 10
   b = 20
   list = [1, 2, 3, 4, 5 ]
   if ( a in list ):
      print("1 - 变量 a 在给定的列表中 list 中")
   else:
      print("1 - 变量 a 不在给定的列表中 list 中")
   
   if ( b not in list ):
      print("2 - 变量 b 不在给定的列表中 list 中")
   else:
      print("2 - 变量 b 在给定的列表中 list 中")
   
   # 修改变量 a 的值
   a = 2
   if ( a in list ):
      print("3 - 变量 a 在给定的列表中 list 中")
   else:
      print("3 - 变量 a 不在给定的列表中 list 中")