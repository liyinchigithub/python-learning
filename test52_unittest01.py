#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 文件名:test52_unittest01.py

import unittest
from  test53_unittest02 import Test_class_02 # 导入模块中的测试类

class Test_class_01(unittest.TestCase):
    @classmethod # 必要修饰器
    def setUpClass(cls):
        print("Test_class_01 所有测试用例执行之前")
        
    @classmethod # 必要修饰器
    def tearDownClass(cls) -> None:
        print("Test_class_01 所有测试用例执行之后")
        
    def setUp(self) -> None:
        print("Test_class_01 每个测试用例执行之前")
        
    def tearDown(self) -> None:
        print("Test_class_01 每个测试用例执行之后")
    
    def test_01_01_sum(self):
        self.assertEqual(1,1)
        self.assertNotEqual(1,"1")
        self.assertTrue(1==1)
        self.assertFalse(1=="1")
        print("test_01_01_sum 测试用例")
        
    # @unittest.skip("跳过用例")    
    def test_01_02_sum(self):
        self.assertEqual(2,2)
        self.assertNotEqual(2,"2")
        self.assertTrue(2==2)
        self.assertFalse(2=="2")
        print("test_01_02_sum 测试用例")
        
    # @unittest.skip("跳过用例")    
    def test_01_03_sum(self):
        self.assertEqual(3,3)
        self.assertNotEqual(3,"3")
        self.assertTrue(3==3)
        self.assertFalse(3=="3")
        print("test_01_03_sum 测试用例")

class Test_class_01_02(unittest.TestCase):
    @classmethod # 必要修饰器
    def setUpClass(cls):
        print("Test_class_01_02 所有测试用例执行之前")
        
    @classmethod # 必要修饰器
    def tearDownClass(cls) -> None:
        print("Test_class_01_02 所有测试用例执行之后")
        
    def setUp(self) -> None:
        print("Test_class_01_02 每个测试用例执行之前")
        
    def tearDown(self) -> None:
        print("Test_class_01_02 每个测试用例执行之后")
    
    def test_01_01_sum(self):
        self.assertEqual(1,1)
        self.assertNotEqual(1,"1")
        self.assertTrue(1==1)
        self.assertFalse(1=="1")
        print("test_01_01_sum 测试用例")
        
    # @unittest.skip("跳过用例")    
    def test_01_02_sum(self):
        self.assertEqual(2,2)
        self.assertNotEqual(2,"2")
        self.assertTrue(2==2)
        self.assertFalse(2=="2")
        print("test_01_02_sum 测试用例")
        
    # @unittest.skip("跳过用例")    
    def test_01_03_sum(self):
        self.assertEqual(3,3)
        self.assertNotEqual(3,"3")
        self.assertTrue(3==3)
        self.assertFalse(3=="3")
        print("test_01_03_sum 测试用例")
                
if __name__ == '__main__':
        suite=unittest.TestSuite();# 测试集
        suite.addTest(Test_class_01_02("test_01_01_sum"))# 添加测试用例到测试集，当前文件自己
        suite.addTest(Test_class_02("test_02_03_sum"))# 添加测试用例到测试集，测试用例 导入另一个测试文件测试类的测试用例
        suite.addTest(Test_class_02("test_02_02_sum"))# 添加测试用例到测试集，测试用例 导入另一个测试文件测试类的测试用例
        suite.addTest(Test_class_02("test_02_01_sum"))# 添加测试用例到测试集，测试用例 导入另一个测试文件测试类的测试用例
        unittest.TextTestRunner().run(suite)# 运行测试集
        
        
'''
    执行测试用例:
    python -m unittest -v test52_unittest01
'''