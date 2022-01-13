
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test-unitest.py
# unitest
# https://docs.python.org/zh-cn/3/library/unittest.html



'''
unittest 单元测试框架是受到 JUnit 的启发，与其他语言中的主流单元测试框架有着相似的风格。
其支持测试自动化，配置共享和关机代码测试。支持将测试样例聚合到测试集中，并将测试与报告框架独立。
为了实现这些，unittest 通过面向对象的方式支持了一些重要的概念。

1.[测试脚手架 test fixture ]
表示为了开展一项或多项测试所需要进行的准备工作，以及所有相关的清理操作。举个例子，这可能包含创建临时或代理的数据库、目录，再或者启动一个服务器进程。
2.[测试用例 testcase]
一个测试用例是一个独立的测试单元。它检查输入特定的数据时的响应。 unittest 提供一个基类： TestCase ，用于新建测试用例。
3.[测试套件 test suite] 
是一系列的测试用例，或测试套件，或两者皆有。它用于归档需要一起执行的测试。
4.[测试运行器 test runner]
test runner 是一个用于执行和输出测试结果的组件。
这个运行器可能使用图形接口、文本接口，或返回一个特定的值表示运行测试的结果。
'''

import unittest

class TestStringMethods(unittest.TestCase):# 派生类继承基类

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')# 字符串转大写断言
        self.assertEqual('FOO'.lower(), 'foo')# 字符串转小写断言

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())# 判断是否大写
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
    
'''
继承 unittest.TestCase 就创建了一个测试样例。
上述三个独立的测试是三个类的方法，这些方法的命名都以 test 开头。
这个命名约定告诉测试运行者类的哪些方法表示测试。
'''

'''
每个测试的关键是：调用 assertEqual() 来检查预期的输出;
调用 assertTrue() 或 assertFalse() 来验证一个条件;
调用 assertRaises() 来验证抛出了一个特定的异常。
使用这些方法而不是 assert 语句是为了让测试运行者能聚合所有的测试结果并产生结果报告。
'''

'''
通过 setUp() 和 tearDown() 方法，可以设置测试开始前与完成后需要执行的指令,在组织你的测试代码中，对此有更为详细的描述。
'''

'''
最后的代码块中，演示了运行测试的一个简单的方法。 
unittest.main() 提供了一个测试脚本的命令行接口。
'''

'''
    python test_unitest.py
'''